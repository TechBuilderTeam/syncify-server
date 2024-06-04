from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from io import BytesIO
from django.http import HttpResponse
from .models import WorkSpace, Member, Timeline, Task, TaskComment, Scrum

def generate_workspace_pdf(workspace_id):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    workspace = WorkSpace.objects.get(id=workspace_id)

    # Add header
    def draw_header(canvas):
        canvas.setFont("Helvetica-Bold", 18)
        canvas.drawCentredString(width / 2, height - 30, "Project Syncify")
        canvas.line(30, height - 40, width - 30, height - 40)

    # Add footer
    def draw_footer(canvas):
        y = 40
        canvas.line(30, y + 20, width - 30, y + 20)
        canvas.setFont("Helvetica-Bold", 12)
        canvas.drawCentredString(width / 2, y + 5, "Thanks For Working With Project Syncify")
        canvas.line(30, y, width - 30, y)

    # Draw header only on the first page
    draw_header(p)

    # Title
    p.setFont("Helvetica-Bold", 24)
    p.drawCentredString(width / 2, height - 70, f"Workspace: {workspace.name}")

    # Workspace Manager
    p.setFont("Helvetica-Bold", 12)
    p.drawCentredString(width / 2, height - 100, f"Manager: {workspace.workSpace_manager}")

    # Members table
    member_data = [["Workspace Name", "Role", "User Name"]]
    for member in Member.objects.filter(workspace_Name=workspace):
        member_data.append([workspace.name, member.role, member.user.first_name])
    draw_table(p, member_data, width, height - 150, "Members:")

    # Timelines table
    timeline_data = [["Name", "Details", "Assign", "Start Date", "End Date", "Remaining Time", "Duration", "Status"]]
    for timeline in Timeline.objects.filter(workspace_Name=workspace):
        assign_name = timeline.assign.user.first_name if timeline.assign else "Not Assigned"
        timeline_data.append([
            timeline.name, 
            timeline.details, 
            assign_name, 
            timeline.start_Date, 
            timeline.end_Date, 
            timeline.remaining_time, 
            timeline.duration, 
            timeline.status
        ])
    draw_table(p, timeline_data, width, p._curr_y - 50, "Timelines:")

    # Loop for Scrums and Tasks within each timeline
    for timeline in Timeline.objects.filter(workspace_Name=workspace):
        scrums = Scrum.objects.filter(timeline_Name=timeline)
        for scrum in scrums:
            scrum_data = [["Scrum Name", "Details"]]
            scrum_data.append([scrum.name, scrum.details])
            draw_table(p, scrum_data, width, p._curr_y - 50, "Scrums:")

            tasks = Task.objects.filter(scrum_Name=scrum)
            task_data = [["Scrum Name", "Name", "Details", "Assign", "Status", "Priority", "Type", "Task Value"]]
            for task in tasks:
                assign_name = task.assign.user.first_name if task.assign else "Not Assigned"
                task_data.append([
                    scrum.name, 
                    task.name, 
                    task.details, 
                    assign_name, 
                    task.status, 
                    task.priority, 
                    task.which_Type, 
                    task.task_Value
                ])
            draw_table(p, task_data, width, p._curr_y - 50, "Tasks:")

    # Move to the next page for task comments
    p.showPage()

    # Task comments on the second page
    for timeline in Timeline.objects.filter(workspace_Name=workspace):
        scrums = Scrum.objects.filter(timeline_Name=timeline)
        for scrum in scrums:
            tasks = Task.objects.filter(scrum_Name=scrum)
            for task in tasks:
                comments = TaskComment.objects.filter(task_Name=task)
                comment_data = [["Task Name", "Comment", "Created", "Commenter Name"]]
                for comment in comments:
                    comment_data.append([task.name, comment.comment, comment.created, comment.commenter.user.first_name])
                draw_table(p, comment_data, width, height - 50, "Task Comments:")

    # Draw footer on the second page
    draw_footer(p)

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    return pdf

def draw_table(canvas, data, page_width, y, title):
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Calculate the width of the table and center it
    table_width, table_height = table.wrap(0, 0)
    x = (page_width - table_width) / 2

    # Draw the title
    canvas.setFont("Helvetica-Bold", 16)
    canvas.drawCentredString(page_width / 2, y, title)

    # Draw the table
    table.drawOn(canvas, x, y - table_height - 20)
    canvas._curr_y = y - table_height - 40  # Update current y position for next drawing

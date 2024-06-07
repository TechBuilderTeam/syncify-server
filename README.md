                     
<h1 align="center" style="font-weight: bold;">ProjectSyncify 💻</h1>

<p align="center">
<a href="#tech">Technologies</a>
<a href="#started">Getting Started</a>
<a href="#routes">API Endpoints</a>
<a href="#colab">Collaborators</a>
<a href="#contribute">Contribute</a> 
</p>


<p align="center">ProjectSyncify is a Project Management Application.</p>


<p align="center">
<a href="https://github.com/TechBuilderTeam/project-syncify-server/">📱 Visit this Project</a>
</p>
 
<h2 id="technologies">💻 Technologies</h2>

list of all technologies we used
- Django
- Django REST Framework
- PyJWT
- Google Auth
- Django Channels
- PostgreSQL
- Redis
 
<h2 id="started">🚀 Getting started</h2>

Skip for now
 
<h3>Prerequisites</h3>

```bash
pip install -r requirements.txt
```

Run this command to install all prerequisites. Or have a look on 'requirements.txt'.


 
<h3>Cloning</h3>


```bash
git clone https://github.com/TechBuilderTeam/project-syncify-server.git
```

Run this command to clone this project.
 
<h3>Config .env variables</h2>

Use the `.env` as reference to create your configuration file `.env` with your 
Google, GitHub Credentials

```yaml
EMAIL= ''
EMAIL_PASSWORD='' 
GOOGLE_CLIENT_ID={your google client id}
GOOGLE_CLIENT_SECRET={your google client secret}
GITHUB_CLIENT_ID={your github client id}
GITHUB_CLIENT_SECRET={your github client secret}
SOCIAL_AUTH_PASSWORD=''
```
 
<h3>Starting</h3>

How to start this project

```bash
python manage.py runserver
```
 
<h2 id="routes">📍 API Endpoints</h2>

Here you can list the main routes of your API, and what are their expected request bodies.
​
| route               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>POST /api/v1/auth/register/</kbd>     | Register a new user [details](#get-auth-register-details)
| <kbd>POST /api/v1/auth/login/</kbd>     | Login User [request details](#post-auth-detail)
| <kbd>POST /api/v1/auth/verify-email/</kbd>     | Verify a user
| <kbd>POST /api/v1/auth/password-reset/</kbd>     | Password Reset
| <kbd>GET /api/v1/auth/password-reset-confirm/<uidb64>/<token>/</kbd>    | Password Reset Confirm
| <kbd>PATCH /api/v1/auth/set-new-password/ </kbd>     | Set New Password
| <kbd>POST  /api/v1/auth/logout/ </kbd>     | Logout 
| <kbd>POST /api/v1/auth/token/refresh/</kbd>     | Token Refresh 
| <kbd>POST /api/v1/auth/google/</kbd>     | Google Auth
| <kbd>POST /api/v1/auth/password-reset/</kbd>     | Password Reset
| <kbd>GET /api/v1/user/verified/</kbd>              | Get All Verified Users        |
| <kbd>GET /api/v1/user/verified/{id}</kbd>          | Get Verified User by ID       |
| <kbd>GET /api/v1/user/unverified/</kbd>            | Get All Unverified Users      |
| <kbd>GET /api/v1/user/details/{id}</kbd>           | Get User Details by ID        |
| <kbd>GET /api/v1/user/details/{email}</kbd>        | Get User Details by Email     |
| <kbd>POST /api/v2/workspace/members/add/</kbd>        | Add a member to a workspace        
| <kbd>GET /api/v1/profile/designation/</kbd>            | Get user designation       |
| <kbd>POST /api/v1/profile/designation/</kbd>           | Create or update user designation |
| <kbd>GET /api/v1/profile/contact/</kbd>                | Get user contact information |
| <kbd>POST /api/v1/profile/contact/</kbd>               | Create or update user contact |
| <kbd>GET /api/v1/profile/about/</kbd>                  | Get user about information |
| <kbd>POST /api/v1/profile/about/</kbd>                 | Create or update user about |
| <kbd>GET /api/v1/profile/portfolio/</kbd>             | Get user portfolio information |
| <kbd>POST /api/v1/profile/portfolio/</kbd>            | Create or update user portfolio |
| <kbd>POST /api/v1/profile/education/create/</kbd>     | Add user education |
| <kbd>PUT /api/v1/profile/education/edit/{educationid}/</kbd> | Edit user education |
| <kbd>DELETE /api/v1/profile/education/delete/{educationid}/</kbd> | Delete user education |
| <kbd>GET /api/v1/profile/education/{userid}/</kbd>     | Get all education of a user |
| <kbd>POST /api/v1/profile/work/create/</kbd>           | Add user work experience |
| <kbd>PUT /api/v1/profile/work/edit/{workid}/</kbd>     | Edit user work experience |
| <kbd>DELETE /api/v1/profile/work/delete/{workid}/</kbd> | Delete user work experience |
| <kbd>GET /api/v1/profile/work/{userid}/</kbd>          | Get all work experience of a user |
| <kbd>POST /api/v1/profile/skills/add/</kbd>           | Add user skills |
| <kbd>POST /workspace/scrum/create/</kbd>     | Create Scrum
| <kbd>GET /workspace/scrum/{scrum_id}/</kbd>     | Get Single Scrum
| <kbd>PUT /workspace/scrum/update/{scrum_id}/</kbd>     | Update Scrum
| <kbd>DELETE /workspace/scrum/delete/{scrum_id}/</kbd>     | Delete Scrum
| <kbd>GET /workspace/timeline/scrum/{timeline_id}/</kbd>     | Get All Scrums in Timeline
| <kbd>GET /workspace/user/{user_id}/workspace/{workspace_id}/scrums/</kbd>     | Get All Scrums for User
| <kbd>POST /workspace/tasks/create/</kbd>     | Create Task
| <kbd>GET /workspace/tasks/{task_id}/</kbd>     | Get Single Task
| <kbd>PUT /workspace/tasks/update/{task_id}/</kbd>     | Update Task
| <kbd>DELETE /workspace/tasks/delete/{task_id}/</kbd>     | Delete Task
| <kbd>GET /workspace/scrum/tasks/list/{scrum_id}/</kbd>     | Get All Tasks in Single Scrum
| <kbd>PUT /workspace/task/update/priority/{task_id}/</kbd>     | Change Task Priority
| <kbd>PUT /workspace/task/update/status/{task_id}/</kbd>     | Change Task Status
| <kbd>PUT /workspace/task/update/assign/{task_id}/</kbd>     | Change Task Assign Member
| <kbd>PUT /api/v2/workspace/task/update-status/</kbd>     | Update Task Status
| <kbd>GET /workspace/user/{user_id}/workspace/{workspace_id}/tasks/</kbd>     | Get All Tasks for User
| <kbd>POST /workspace/comments/create/</kbd>     | Create Comment
| <kbd>GET /workspace/comments/{comments_id}/</kbd>     | Get Single Comment
| <kbd>PUT /workspace/comments/update/{comments_id}/</kbd>     | Update Comment
| <kbd>DELETE /workspace/comments/delete/{comments_id}/</kbd>     | Delete Comment
| <kbd>GET /workspace/workspace/singletask/comments/list/{task_id}/</kbd>     | Get All Comments in Single Task
| <kbd>GET /workspace/counts/</kbd>     | Get All Counts for Website
| <kbd>GET /workspace/dashbordinfo/{workspace_id}/</kbd>     | Get Dashboard Info
| <kbd>GET /workspace/pdf/{workspace_id}/</kbd>     | Export Whole Project
more endpoints comming soon...

<h3 id="get-auth-register-details">POST /api/v1/auth/register/</h3>

**POST**
```json
{
  "email": "najmulislamru@gmai.com",
  "first_name": "Najmul",
  "last_name": "Islam"
  "password":"*******"
  "password2":"*******"
}
```

<!--<h3 id="post-auth-detail">POST /authenticate</h3>-->

<!--**REQUEST**-->
<!--```json-->
<!--{-->
<!--  "username": "fernandakipper",-->
<!--  "password": "4444444"-->
<!--}-->
<!--```-->

<!--**RESPONSE**-->
<!--```json-->
<!--{-->
<!--  "token": "OwoMRHsaQwyAgVoc3OXmL1JhMVUYXGGBbCTK0GBgiYitwQwjf0gVoBmkbuyy0pSi"-->
<!--}-->
<!--```-->
 
<h2 id="colab">🤝 Collaborators</h2>

<p>Special thank you for all people that contributed for this project.</p>
<table>
<tr>

<td align="center">
<a href="https://github.com/najmulislamnajim">
<img src="https://i.pinimg.com/736x/90/e7/37/90e7370bc6c22359dc07c5f8b057a5ce.jpg" width="100px;" alt="Najmul Islam Profile Picture"/><br>
<sub>
<b>Najmul Islam</b>
</sub>
</a>
</td>

<td align="center">
<a href="https://github.com/Sifathislam">
<img src="https://avatars.githubusercontent.com/u/105329974?v=4" width="100px;" alt="sifat isalm Profile Picture"/><br>
<sub>
<b>Sifat Islam</b>
</sub>
</a>
</td>



</tr>
</table>
 
<h2 id="contribute">📫 Contribute</h2>



1. `git clone https://github.com/TechBuilderTeam/project-syncify-server.git`
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made, if exists, append screenshot of visual modifications and wait for the review!
 
<h3>Documentations that might help</h3>

[📝 How to create a Pull Request](#)
```bash
git pull
```
[💾 Commit pattern](#)
```bash
git add .
git commit -m"your commit title"
git push
```

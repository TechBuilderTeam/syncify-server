                     
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
| <kbd>POST /api/v2/workspace/members/add/</kbd>        | Add a member to a workspace                                |
|                                                       | **Body:**<br>{<br> "workspace_Name": "id",<br> "role": "Associate Manager/Team Leader/Member",<br> "email": "example@mail.com"<br>}<br>**Response:**<br>201 with data, message -> success<br>400 with error -> user does not exist with this email, user is the manager of this workspace, and the user already exists |
| <kbd>DELETE /api/v2/workspace/members/remove/</kbd>   | Remove a member from a workspace                           |
|                                                       | **Body:**<br>{<br> "workspace_id": "4",<br> "user_id": "7"<br>}<br>**Response:**<br>200 with message -> success<br>404 with message -> member not found<br>400 with error -> workspace_id, user_id not provided |
| <kbd>PUT/PATCH /api/v2/workspace/members/change-role/</kbd> | Change the role of a workspace member                       |
|                                                       | **Body:**<br>{<br> "workspace_id": "4",<br> "new_role": "Associate Manager",<br> "user_id": "4"<br>}<br>**Response:**<br>200 with data -> success<br>404 with error -> member not found<br>400 with error -> all fields required |
| <kbd>GET /api/v2/workspace/id/members/</kbd>          | Get a list of all members in a single workspace             |
|                                                       | **Response:**<br>Each member's data: user_id, user_name, user_email, role |
| <kbd>GET /api/v1/chat/groupname/</kbd>         | Get message history of a specific group|
| <kbd>wss://projectsyncifyapi.onrender.com/ws/v1/chat/gp/</kbd> | WebSocket connection for chat      |
| <kbd>GET /api/v2/workspace/insights/{id}/</kbd>  | Get insights for a specific workspace (replace {id} with your workspace ID) |
| <kbd>GET /api/v1/insights/</kbd>  | Get website insights         |
| <kbd>GET /api/v1/profile/designation/</kbd>                  | Get user designation                                    |
|                                                              | **Body:**<br>{ "user": "user_id" }<br>**Response:**<br>200 ok, get designation<br>404 if user does not exist or designation is not created |
| <kbd>POST /api/v1/profile/designation/</kbd>                 | Create or update user designation                       |
|                                                              | **Body:**<br>{ "designation": "Backend Developer", "user": "user_id" }<br>**Response:**<br>200 ok, get designation<br>404 if user does not exist |
| <kbd>GET /api/v1/profile/contact/</kbd>                      | Get user contact information                            |
|                                                              | **Body:**<br>{ "user": "user_id" }<br>**Response:**<br>200 ok, get contact information<br>404 if user does not exist or contact is not created |
| <kbd>POST /api/v1/profile/contact/</kbd>                     | Create or update user contact information               |
|                                                              | **Body:**<br>{ "phone": "01767500160", "email": "najmulislamru@gmail.com", "user": "user_id" }<br>**Response:**<br>200 ok, get contact information<br>404 if user does not exist |
| <kbd>GET /api/v1/profile/about/</kbd>                        | Get user about information                              |
|                                                              | **Body:**<br>{ "user": "user_id" }<br>**Response:**<br>200 ok, get about information<br>404 if user does not exist or about is not created |
| <kbd>POST /api/v1/profile/about/</kbd>                       | Create or update user about information                 |
|                                                              | **Body:**<br>{ "about": "this is my about", "user": "user_id" }<br>**Response:**<br>200 ok, get about information<br>404 if user does not exist |
| <kbd>GET /api/v1/profile/portfolio/</kbd>                    | Get user portfolio information                          |
|                                                              | **Body:**<br>{ "user": "user_id" }<br>**Response:**<br>200 ok, get portfolio information<br>404 if user does not exist or portfolio is not created |
| <kbd>POST /api/v1/profile/portfolio/</kbd>                   | Create or update user portfolio information             |
|                                                              | **Body:**<br>{ "github": "github link", "linkedin": "LinkedIn link", "portfolio": "portfolio link", "twitter": "twitter link", "user": "user_id" }<br>**Response:**<br>200 ok, get portfolio information<br>404 if user does not exist |
| <kbd>POST /api/v1/profile/education/create/</kbd>            | Add user education                                      |
|                                                              | **Body:**<br>{ "user": null, "institution": "", "degree": "", "start_date": null, "end_date": null, "description": "", "currently_studying": false } |
| <kbd>PUT /api/v1/profile/education/edit/{educationid}/</kbd> | Edit user education                                     |
|                                                              | **Body:**<br>{ "user": null, "institution": "", "degree": "", "start_date": null, "end_date": null, "description": "", "currently_studying": false }<br>**Response:**<br>Update |
| <kbd>DELETE /api/v1/profile/education/delete/{educationid}/</kbd>| Delete user education                                   |
|                                                              | **Response:**<br>Delete a specific education |
| <kbd>GET /api/v1/profile/education/{userid}/</kbd>           | Get all education of a user                             |
|                                                              | **Response:**<br>Get a user all education list |
| <kbd>POST /api/v1/profile/work/create/</kbd>                 | Add user work experience                                |
|                                                              | **Body:**<br>{ "user": null, "company": "", "position": "", "start_date": null, "end_date": null, "description": "", "currently_working": false } |
| <kbd>PUT /api/v1/profile/work/edit/{workid}/</kbd>           | Edit user work experience                               |
|                                                              | **Body:**<br>{ "user": null, "company": "", "position": "", "start_date": null, "end_date": null, "description": "", "currently_working": false } |
| <kbd>DELETE /api/v1/profile/work/delete/{workid}/</kbd>      | Delete user work experience                             |
|                                                              | **Response:**<br>Delete a specific work |
| <kbd>GET /api/v1/profile/work/{userid}/</kbd>                | Get all work experience of a user                       |
|                                                              | **Response:**<br>Get a user all work list |
| <kbd>POST /api/v1/profile/skills/add/</kbd>                  | Add user skills |

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

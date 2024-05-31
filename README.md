                     
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
- SQLite
 
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

[💾 Commit pattern](#)

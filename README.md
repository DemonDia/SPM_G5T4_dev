# Learning Journey Portal

<a name="readme-top"></a>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
LJP system to have a personal learning journey tracker that could guide them on the courses they could take either from the LMS or in physical classes to prepare them for the next position or in a different area within the organisation.
The system would allow staff to set their learning goal by setting on a position that they are working towards. The system will then list out the skills required for those positions and the courses (internal/external) that correspond to those skills. They are then able to view the details of those courses. They are then able to register for those courses. Upon completion of the courses, HR would be able to update the skillset of the staff. The Learning Journey of the staff would also then reflect so.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Vue][Vue.js]][Vue-url] [![FastAPI][FastAPI]][FastAPI-url]


## Frontend

#### Folder structure
```bash 
frontend
|   
├── public
|   ├── index.html
|   
├── src
|   ├── assets
|   | 
|   ├── components
|   |   ├── <component_name>Component.vue
|   | 
|   ├── plugins
|   | 
|   ├── router
|   |   ├── index.js
|   | 
|   ├── router
|   |   ├── index.js
|   |   ├── auth.js
|   |   ├── subscriber.js
|   | 
|   ├── views
|   |   ├── Dashboard
|   |   |   ├── Layout
|   |   |   |   ├── DashboardLayout.vue
|   |   |   ├── Dashboard.vue
|   |   ├── <feature_name>.vue
|   |
|   ├── App.vue
|   |
|   ├── main.js
|
├── .gitignore
|
├── babel.config.js
|
├── package-lock.json
|
├── App.vue

```
### Frontend Prerequisites:
* Node.JS installed on your computer


### Running frontend (for testing):
To run the frontend UI, type the following in your terminal:
```
npm i 
npm run serve
```
Note: 
- Make sure you are in the Frontend folder before you do any of the above in the CLI
- npm i installs all the required dependencies 

## Backend
### IMPORTANT: 
1. For entity column names, use underscore case (eg: column_name) 
2. For variable names, use camel case (eg: variableName)
3. For primary keys of entities with ONLY 1 primary key, that column should be 'id'

#### Folder structure

```bash 
Backend
├── Routes (the various routes are stored; relevant functions from ApiFunctions are imported)
|   ├── <api_name>Routes.py
|
├── Models (Entity models are found here; this is solely for table creation for SQL)
|   ├── <model_name>.py
|
├── Tests (This is where you test the individual APIs)
|   ├── TestScripts (this is where the test cases of each entity is at)
|   |   ├── <api_name>Test.py
|   |
|   ├── HelperFunctionForTest.py (they provide helper functions for the test cases)
|   ├── MainTest.py (they run all the unit tests together)
|
├── Schema (This is to facilitate CRUD operations in FastAPI especially for SQL)
|   ├── <api_name>Schema.py
|
├── HelperFunctions.py (For helper functions that are usable for the API)
|
├── .gitignore (this lists the type of files that will NOT be tracked by GitHub)
|
├── TableInfo.py (this stores the information of the columns of each entity)
|
├── config.py (all the setup will happen there; SQLAlchemy and App initialisation)
|
├── main.py (where you actually run the code; you import the routes from the Routes folder)
|
├── database.py (this is where the database tables are created)
|
├── ErrorHandler.py (this is where the custom error handlers are at)
|
├── requirments.txt (this lists the dependencies required to run the project)
```

**NOTE: the naming convention of <model_name> and <api_name> should be consistent.**

Eg: If your model name is 'Entity', your naming convention should be like:
- Routes: EntityRoutes.py
- ApiFunctions: EntityFunctions.py
- Models: Entity.py
- Tests: EntityTest.py

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Backend Prerequisites 
Python 3.7+

FastAPI stands on the shoulders of giants:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> for the web parts.
* <a href="https://pydantic-docs.helpmanual.io/" class="external-link" target="_blank">Pydantic</a> for the data parts.

### Setup (for testing):
1. Clone this repo
2. Open the project in VSC 
3. In your terminal, type this in CLI: 
```
pip install pipreqs
pipreqs Backend
pip install -r requirements.txt
```

NOTE: 
- pip install pipreqs installs the 'pipreqs' library, which allows you to get the dependencies from ONLY this project.
- this downloads the dependencies stated in the requirements.txt


### Running backend (for testing):
To run the main API, type the following in your terminal:
```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

<details markdown="1">
<summary>About the command <code>uvicorn main:app --reload</code>...</summary>

The command `uvicorn main:app` refers to:

* `main`: the file `main.py` (the Python "module").
* `app`: the object created inside of `main.py` with the line `app = FastAPI()`.
* `--reload`: make the server restart after code changes. Only do this for development.

</details>

To run the test cases, type the following in your terminal:
```
cd Tests
python MainTest.py
```
Note: 
- Make sure you are inside the Backend folder before running the backend API and its test scripts
- cd Tests: you go to the path of the Tests folder
- IMPORTANT: before you run your test file inside the 'Tests' folder, ensure your main.py is running


<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
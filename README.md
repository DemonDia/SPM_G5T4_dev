# Learning Journey Portal
## Frontend

#### Folder structure
```bash 

```
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
```
uvicorn main:app --reload    
```

To run the test cases, type the following in your terminal:
```
cd Tests
python MainTest.py
```
Note: 
- Make sure you are inside the Backend folder before running the backend API and its test scripts
- cd Tests: you go to the path of the Tests folder
- IMPORTANT: before you run your test file inside the 'Tests' folder, ensure your main.py is running


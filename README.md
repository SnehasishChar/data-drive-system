# wapos-wapos-api

## Setup project in PyCharm to run through Docker

Install Docker in system.

Step 1: Connect Docker with pycharm professional:

File -> Setting -> Build, Execution, Deployment -> Docker -> Select docker demon based on the system -> OK

Step 2: Configure Docker tool:

File -> Setting -> Build, Execution, Deployment -> Docker -> Tool -> Select Docker executable file ->
Select Docker Compose the executable file -> OK

Step 3: Configure Docker tool:

File -> Setting -> Project -> Python Interpreter -> Click on the Setting icon -> Add -> Docker Compose -> Select sever
created at the time of DockerDemon -> Select the docker-compose files -> Select Service as web from the dropdown -> OK

Step 4: Add configuration for running the project:

Run -> Edit Configuration -> Click on the plus button -> Select Django Server -> Add name -> Select Python Interpreter
created above -> OK

Step 5: Click on the Debug button to run the project.
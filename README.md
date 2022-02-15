# ProjectManagementWebsite
A minimal project management website for CMSC495 built using the Django stack.

# Group
- Team Lead: @MeyerWilliam
- Front End: @mosiris
- Back End: @Justin444
<a href="https://github.com/Justin444/ProjectManagementWebsite/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Justin444/ProjectManagementWebsite" />
</a>

# User Guide
- Browser and access
  - Access the website through a modern web browser like Google Chrome or Mozilla Firefox by entering the website url.

- Account Creation
  - The user will be directed to a login page with a button to create a new account. New users will need to create an account to access website functions.
Password complexity is a must on account creation. The user will need to create a username and the password must be longer than 8 characters with an upper case, lowercase, number, and symbol for optimal security.

- User Dashboard
  - Upon logging in, the user will be prompted to their dashboard. From here, the user can select an existing project or create a new project to build upon.

- Creating a New Project
  - When creating a new project, the user will be prompted to fill several fields to include Project Name, Type, and expected Completion Date. Each field must have an entry and can be edited by the user after creation. The user will then select “Create” project.

- Project view
  - Once in a project, the user will have four standard columns detailed “Tasks to Do”, “Tasks in Progress”, “Tasks on Hold”, and “Completed Tasks”. The user can elect to create new containers in each column to start building their tasks and workflow by selecting “Add Task” at the bottom of each column.

- New Task Creation
  - The user can select which column to push the container to, the title of that task or objective, and any additional details they would like to include. Once done, the user will then select “Create” in the bottom right corner.

- Column Management
  - Besides the 4 columns that are standard on the project view, the user can include additional columns if their project requires it. Select the “Add List” button next to the current columns. “Add List” has similar parameters to “Add Task” but also includes where it will fall in the list of columns. Lastly, the User can also edit each column by selecting the ellipses on that specific column, selecting edit, and editing the title and position of the column.

- Task Management
  - Like the columns, tasks can also be managed by dragging and dropping where they fall in a column. Additionally, there is a delete option for the task, upon selection the user will be prompted to confirm they would like to delete the task.

- Returning to Dashboard
  - The user can return to the dashboard from any project at any time by selecting “Projects” in the top left.

- Managing Projects
  - The user can manage their project view in the dashboard by selecting edit on the project. From here, the user can select if the project is “In Progress” or “Completed” which will also change the color of the project. From the edit view, the user can also delete the project and will be prompted in the same manner as Task Management.

- Logging Out
  - At any time, the user can logout in the top right corner with the “Logout” button. The user will be prompted to ensure they would like to logout. After logging out, the user will be sent back to the original login page.

# Running the site
- You must first have these packages installed:
  - Django 4.02

To run the website navigate to the upper level "ProjectManagementWebsite" directory and run the command via cmd or pycharm terminal: python manage.py runserver Then you should see a local host link that you enter into your browser to use the website.

![Wedding Planner logo](weddingplanner/docs/heart.ico)

# Wedding Planner

### This is the website for a Wedding Planner Application. It is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential users.

[View the live project here.](https://ci-ms3-weddingplanner.herokuapp.com/)

#

### A screenshot of the responsive website:
![A screenshot of the responsive website](weddingplanner/docs/responsive.png)

#

## Project Scope

    To build a website for users to plan their wedding. They can add their wedding with a unique wedding name (e.g. 'Diana & Nigel'), add tasks for the wedding (e.g. 'Book Licensed Venue') and add suppliers for those tasks (e.g. 'The Lion Inn'). 
    
    All this information should be viewable in a clear format not only for the users wedding but all the other weddings added to the website, hence the comunity aspect.
    
    Weddings, tasks and suppliers should be editable and can be deleted if required. Futhermore, a set of default tasks can be added to a wedding to assit the user in their planning and suppliers from other wedding tasks can be copied to the users wedding task as they see fit.

#

## Future Enhancements

    1. Provide a log in screen so that users can only edit and delete their own wedding, tasks and suppliers.

    2. Provide a priority task list to see what needs to be arranged/completed next.

#

## User Experience (UX)

-    ### User stories

    -   First Time Visitor Goals:
        1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        2. As a First Time Visitor, I want to be able to easily view existing weddings, tasks and suppliers
           in a clear presentation that is responsive on different devices.
        3. As a First Time Visitor, I want to be able to easily search weddings based on the wedding name,
           wedding country and/or wedding town.
        4. As a First Time Visitor, I want to be able to easily add a wedding, a task(s) for a wedding,
           a supplier(s) for those tasks and view all this information in clear presentation that is 
           responsive on different devices.
        5. As a First Time Visitor, I want to be able to easily edit or delete a wedding, task or supplier.
        6. As a First Time Visitor, I want to be able to add a default set of tasks for thier wedding to 
           assist in the set up and planning of their wedding.
        7. As a First Time Visitor, I want to be able to copy a supplier from a selected wedding and task
           to their own wedding and task.
        
    -   Returning & Frequent Visitor Goals:
        1. As a Returning Visitor, I want to quickly access the site and view the status of my wedding tasks
           and task suppliers in a clear presentation that is responsive on different devices.
        2. As a Returning Visitor, I want to be able to update the status of my wedding by adding, editing or
           deleting a wedding, wedding tasks and task suppliers.

-   ### UX Design

    -   #### Frontend Framework
        To create a modern responsive site Google's Material Design Materialize CSS framework is used. The responsive
        behavior is based on the standard 12-column grid system using containers, rows, and columns.

    -   #### Colour Scheme
        To create a modern look and feel in a wedding theme that is clear to new users and familiar to a returning user.
        One of the benefits of using Google's Material Design is that there are 200 custom color classes that can be used
        use for backgrounds and text.

    -   #### Typography
        Roboto 2.0 is the font used on the site. It is the standard font of Materialize and features friendly and open
        curves making a more natural reading rhythm.

    -   #### Imagery
        Imagery is important but has been kept to a minimum to improve the sites upload time.

    -   #### Screenshots of the visual design elements used on the site:
        - ##### Weddings page
        ![A screenshot of the visual design elements for the weddings page](weddingplanner/docs/ux-design-weddings.png)
        - ##### Wedding tasks page
        ![A screenshot of the visual design elements for the tasks page](weddingplanner/docs/ux-design-wedding-tasks.png)
        - ##### Task suppliers page
        ![A screenshot of the visual design elements for the suppliers page](weddingplanner/docs/ux-design-task-suppliers.png)
        - ##### Search weddings form
        ![A screenshot of the visual design elements for the search weddings form](weddingplanner/docs/ux-design-wedding-search.png)
        - ##### Add wedding form
        ![A screenshot of the visual design elements for the add wedding form](weddingplanner/docs/ux-design-add-wedding.png)
        - ##### Add tasks dialog
        ![A screenshot of the visual design elements for the add tasks dialog](weddingplanner/docs/ux-design-add-tasks-dialog.png)
        - ##### Add task form
        ![A screenshot of the visual design elements for the add task form](weddingplanner/docs/ux-design-add-task.png)
        - ##### Add supplier form
        ![A screenshot of the visual design elements for the add supplier form](weddingplanner/docs/ux-design-add-supplier.png)

-   ### Wireframes

    -   #### The wireframes for a standard computer screen:
        ![View of the standard wireframe for the weddings page](weddingplanner/docs/wireframe-weddings.png)

    -   #### The wireframes for a mobile device:
        ![View of the mobile wireframe for the weddings page](weddingplanner/docs/wireframe-weddings-mobile.png)

-   ### Backend/Database Design

    -   The backend will be a Postgres relational database accessed via Python using Flask, the SLQAlchemy ORM.

    -   #### Database schema:
        ![View of the database schema for the weddingplanner application](weddingplanner/docs/weddingplanner-db-schema.png)

-   ### Initial Coding

    -   The site was coded in Gitpod and based on the Relational Database Management System mini-project,
        a task manager application. Therefore the Wedding Planner application takes many of the features
        and setup from from this resource.

-   ### Responsiveness

    -   The site was initially checked with Google Chrome's Dev Tools using the Device Toolbar to 
        check different device sizes, [screenshots below in test section.](#TestResp)

    -   The site was then run on a Nokia 3.1 mobile phone running Andriod version 10 with good results

#

## Features

-   Responsive on all device sizes
-   Interactive elements
-   Interactive front-end that responds to the users' actions, allowing users to actively engage with 
    data, alter the way the site displays the information to achieve their preferred goals.

#

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [W3 Schools:](https://www.w3schools.com/)
    - W3 Schools was used as a HTML and CSS reference.
2. [Code Institute](https://learn.codeinstitute.net/ci_program/diplomainwebappdevelopment)
    - The "Love Maths" project was used as the basis of the Four in a Line website.
3. [Stack Overflow](https://stackoverflow.com/)
    - Stack Overflow was used to search for solutions to specific requirements.
4. [Paint]
    - Paint for Windows was used to crop and resize the images/icons where required.
5. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Raleway' font into the style.css file which is used in the project.
6. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
7. [GitHub:](https://github.com/)
    - GitHub is used to store the project code after being pushed from Git.
8. [Figma:](https://figma.com/)
    - Figma was used to create the [wireframes](https://github.com/) during the design process.
9. [Material Design:](https://material.io/resources/color/)
    - Material Design was used to create and test the colour scheme for the website.
10. [Font Awesome](https://fontawesome.com/)
    - Font Awesome was used on the website to add icons for aesthetic and UX purposes.
11. [Lucidchart](https://www.lucidchart.com)
    - Lucidchart was used to design the database schema for the application.
12. [PostgreSQL](https://www.postgresql.org/)
    - A Postgres relational database will be used to store the application data for the site.
13. [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
    - The Postgres relational database accessed via Python using Flask, the SLQAlchemy ORM.
14. [ElephantSQL](https://www.elephantsql.com/)
    - The Postgres relational database will be hosted on ElephantSQL.
15. [Heroku](https://www.heroku.com)
    - The site will be deployed on the Heroku Cloud Application Platform.
16. [Google Chrome]
    - The Device Toolbar in Dev Tools was used to check the responsiveness of the site.

## Testing

### HTML and CSS Validation

    The W3C Markup Validator and W3C CSS Validator services were used to validate every page of the project to ensure there were no syntax errors
    in the project. There were no errors found in the Markup but the in the CSS there was 1 error and 482 warnings in the Materialize framwork.

-   [W3C Markup Validator](https://validator.w3.org/) - [View results](weddingplanner/docs/html-validation-results.png)

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - [View results](weddingplanner/docs/css-validation-results.png)

### <a id="TestResp"></a>Responsiveness
    
    The site was initially checked with Google Chrome's Dev Tools using the Device Toolbar to check different device sizes, screenshots below:

-   [View a screenshot of the weddings page on a standard computer](weddingplanner/docs/gc-resp-standard-weddings.png)
-   [View a screenshot of the add wedding form on a standard computer](weddingplanner/docs/gc-resp-standard-add-wedding.png)
-   [View a screenshot of the tasks page on a standard computer](weddingplanner/docs/gc-resp-standard-tasks.png)
-   [View a screenshot of the add task form on a standard computer](weddingplanner/docs/gc-resp-standard-add-task.png)
-   [View a screenshot of the tasks page on a standard computer](weddingplanner/docs/gc-resp-standard-suppliers.png)
-   [View a screenshot of the add task form on a standard computer](weddingplanner/docs/gc-resp-standard-add-supplier.png)

-   [View a screenshot of the weddings page on a iPhone SE](weddingplanner/docs/gc-resp-iphonese-weddings.png)
-   [View a screenshot of the add wedding form on a iPhone SE](weddingplanner/docs/gc-resp-iphonese-add-wedding.png)
-   [View a screenshot of the tasks page on a iPhone SE](weddingplanner/docs/gc-resp-iphonese-tasks.png)
-   [View a screenshot of the add task form on a iPhone SE](weddingplanner/docs/gc-resp-iphonese-add-task.png)
-   [View a screenshot of the tasks page on a iPhone SE](weddingplanner/docs/gc-resp-iphonese-suppliers.png)
-   [View a screenshot of the add task form on a iPhone SE](weddingplanner/docs/gc-resp-iphonese-add-supplier.png)

### Testing User Stories from User Experience (UX) Section
        
-   #### First Time Visitor Goals
  
    1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        1. Upon entering the site, users can easily see what the purpose of the site is.
        2. The heading a logo clearly communicate what the site is about.

    2. As a First Time Visitor, I want to be able to easily view existing weddings, tasks and suppliers
       in a clear presentation that is responsive on different devices.
        1. The site has been designed to be easy to use and allow the user to easily view existing weddings,
           tasks and suppliers using different devices such as a standard computer, laptop, tablet or mobile phone.
        2. The tasks for a wedding can be viewed by clicking on the "VIEW TASKS" button on a Weddings card.
        3. The suppliers for a task can be viewed by clicking on the "VIEW SUPPLIERS" button on a Task collapsibles body.
    
    3. As a First Time Visitor, I want to be able to easily search weddings based on the wedding name, wedding
       country and/or wedding town.
        1. The search form can be opened by clicking on the "SEARCH WEDDINGS" button on the weddings page.
        2. The user can then select a specific wedding in a dropdown or select a country and/or town in the dropdowns
           and click the "SEARCH" button to make the search.

    4. As a First Time Visitor, I want to be able to easily add a wedding, a task(s) for a wedding, a supplier(s) for
       those tasks and view all this information in clear presentation that is responsive on different devices.
        1. The user can easily add a wedding using the "ADD WEDDING" button on the weddings page. The add wedding form
           will display allowing the user to enter the required fields. If a field is missed or the wedding name already
           exists the user is prompted on the form after clicking the "ADD WEDDING" button.
        2. The user can easily add a task using the "ADD TASK" button on the tasks page. The add task form will display
           allowing the user to enter the required fields. If a field is missed the user is prompted on the form after
           clicking the "ADD TASK" button.
        3. The user can easily add a task using the "ADD SUPPLIER" button on the suppliers page. The add supplier form
           will display allowing the user to enter the required fields. If a field is missed the user is prompted on the
           form after clicking the "ADD SUPPLIER" button.

    5. As a First Time Visitor, I want to be able to easily edit or delete a wedding, task or supplier.
        1. The user can easily edit a wedding using the "EDIT" button on a specific wedding card on the weddings page.
           The edit task form will display allowing the user to edit the fields. Changes are saved by clicking the 
           "SAVE CHANGES" button.
        2. The user can easily delete a wedding using the "DELETE" button on a specific wedding card on the weddings page.
           A dialog is displayed prompting the user to check they do want to delete the wedding and all of it's
           associated tasks and their associated suppliers.
        3. The user can easily edit a task using the "EDIT" button after clicking a specific task collapsible on the
           tasks page. Changes are saved by clicking the "SAVE CHANGES" button.
        4. The user can easily delete a task using the "DELETE" button after clicking a specific task collapsible on the
           tasks page. A dialog is displayed prompting the user to check they do want to delete the task and all of it's
           associated suppliers.
        5. The user can easily edit a supplier using the "EDIT" button after clicking a specific supplier collapsible on
           the suppliers page. Changes are saved by clicking the "SAVE CHANGES" button.
        6. The user can easily delete a supplier using the "DELETE" button after clicking a specific supplier collapsible
           on the suppliers page. A dialog is displayed prompting the user to check they do want to delete the supplier.

    6. As a First Time Visitor, I want to be able to add a default set of tasks for thier wedding to assist in the set up
       and planning of their wedding.
        1. The user can easily add a default set of wedding tasks using the "ADD TASKS" button on a specific wedding card
           on the weddings page. A dialog is displayed prompting the user to check they do want to add a default set of
           tasks to the wedding.

    7. As a First Time Visitor, I want to be able to copy a supplier from a selected wedding and task to their own wedding
       and task.
        1. The user can easily copy a supplier using the "COPY" button after clicking a specific supplier collapsible
           on the suppliers page. The copy supplier form is displayed allowing the user to select a specific wedding task
           they want to copy the supplier too.

-   #### Returning & Frequent Visitor Goals

    1. As a Returning Visitor, I want to quickly access the site and view the status of my wedding tasks and task suppliers
       in a clear presentation that is responsive on different devices.
        1. The site has been designed to be easy to use and allow the user to easily view existing weddings,
           tasks and suppliers using different devices such as a standard computer, laptop, tablet or mobile phone.
        2. The tasks for a wedding can be viewed by clicking on the "VIEW TASKS" button on a Weddings card.
        3. The suppliers for a task can be viewed by clicking on the "VIEW SUPPLIERS" button on a Task collapsibles body.
    2. As a Returning Visitor, I want to be able to update the status of my wedding by adding, editing or deleting a wedding,
       wedding tasks and task suppliers.
        1. The user can easily edit a wedding using the "EDIT" button on a specific wedding card on the weddings page.
           The edit task form will display allowing the user to edit the fields. Changes are saved by clicking the 
           "SAVE CHANGES" button.
        2. The user can easily delete a wedding using the "DELETE" button on a specific wedding card on the weddings page.
           A dialog is displayed prompting the user to check they do want to delete the wedding and all of it's
           associated tasks and their associated suppliers.
        3. The user can easily edit a task using the "EDIT" button after clicking a specific task collapsible on the
           tasks page. Changes are saved by clicking the "SAVE CHANGES" button.
        4. The user can easily delete a task using the "DELETE" button after clicking a specific task collapsible on the
           tasks page. A dialog is displayed prompting the user to check they do want to delete the task and all of it's
           associated suppliers.
        5. The user can easily edit a supplier using the "EDIT" button after clicking a specific supplier collapsible on
           the suppliers page. Changes are saved by clicking the "SAVE CHANGES" button.
        6. The user can easily delete a supplier using the "DELETE" button after clicking a specific supplier collapsible
           on the suppliers page. A dialog is displayed prompting the user to check they do want to delete the supplier.

### Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Opera browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 6 and various Window phones.
-   Friends and family members were asked to review the site on as many devices as they had available and to point out any
    bugs and/or user experience issues.

### Known Bugs

-   No known bugs at this time!

#

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "Pages" Section on the left hand side of the screen.
4. Under "Source", click the dropdown and select "Deploy from a branch".
5. Under "Branch", click the first dropdown and select "main", "/ (root)" on the next dropdown, then "Save".
5. The page will automatically refresh.
6. Scroll back to the top of the page to locate the now published site next to "Your site is live at".

#

## Credits

### Code

-   The project was initailly coded alongside the "Love Maths" project and therefore takes some of the 
    features and source code from this resource.

### Content

-   All the site content was written by the developer.

### Media

-   

### Acknowledgements

-   Pasquale for his help and encouragement.

-   My Mentor for support and helpful feedback.

-   Slack group members for their help.
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Welcome Code Institute Assessor,

[Final Deployment Available Here](https://project-4-django-app-dee496c0d081.herokuapp.com/)

---

# Gameworld

Welcome to Gamesworld, a dynamic platform that combines the essence of a news aggregator and a discussion forum, catering specifically to the vibrant and ever-evolving world of video games. Much like popular platforms such as Reddit, Gamesworld is designed to be a hub for gaming enthusiasts to stay informed about the latest industry news and engage in meaningful discussions.

# Key Features
## News Aggregation and Sorting
Gamesworld focuses on four leading gaming platforms: PlayStation, Xbox, Nintendo, and PC gaming. Users can easily navigate through these categories, sorting and choosing topics of interest directly from the home page. The admin panel offers flexibility, allowing administrators to introduce new discussion categories and broaden the spectrum of topics.

## User Profiles and Social Connectivity
Users can create personalized profiles, adding a bio, profile picture, and links to their other social media accounts. This information is prominently displayed under each user's posts, fostering connections not only within the Gamesworld community but also across other social media platforms.

## Content Creation and Management
Gamesworld empowers users with CRUD (Create, Read, Update, Delete) functionality. Users can effortlessly create new posts, incorporating body text, titles, and optional header images. The ability to edit and delete posts provides users with complete control over their contributions to the site.

## Agile Development Approach

This video game blog project embraced Agile principles to achieve a flexible and collaborative development process. Divided into three iterations, each represented by a Github Kanban board, the project utilized Github tools for streamlined communication and progress tracking. Custom workflows involving Milestones for Epics and Issues for User Stories provided a structured approach to project organization.

### Dynamic Adaptability and Continuous Improvement

Agile's dynamic prioritization categorized User Stories into 'must do,' 'could do,' and 'should do,' allowing for adaptable planning to accommodate changing project requirements. Despite challenges in pre-planning content due to time constraints, the Agile approach encouraged continuous improvement. The Kanban board visually represented progress, while reflections on completed iterations facilitated insights for refining subsequent cycles, ensuring the successful and flexible development of the video game blog.

---

## Epics and User Stories?

...

## WireFrames? (how do I do these)

...

## Deployment (hell on earth)

## Deployment

### Local Deployment:

1. **Set up Virtual Environment:**
   - Create a virtual environment using virtualenv to isolate the project dependencies.
   - Install required packages such as Django, Gunicorn, and Cloudinary within the virtual environment.

2. **Project Initialization:**
   - Create the project by running `django-admin startproject project_name` inside the virtual environment.
   - Similarly, create the app by running `python3 manage.py startapp app_name`. For this project, two separate apps were created: 'myblog' for handling the Gamesworld blog and 'members' for managing membership and registration.

3. **Database Configuration:**
   - Utilize a database for storing migrations. In this project, Elephant SQL was used under a free tiny turtle plan. Import the database configuration into the project through the `env.py` file.

### Heroku Deployment:

1. **Create Heroku App:**
   - Create a new Heroku app and link it to the Git repository for the project.

2. **Heroku Configurations:**
   - Set up Heroku Config Vars to account for necessary variables such as Cloudinary and the Database.

3. **Cloudinary and Database:**
   - Ensure Cloudinary configurations are set up correctly to handle media files.
   - The database used in this project (Elephant SQL) should be configured in Heroku.

4. **Deployment:**
   - Deploy the project to Heroku by pushing the code to the Heroku remote repository.
   - The project should now be accessible through the provided Heroku app URL.

This deployment process ensures a smooth transition from local development to a live Heroku environment, providing a scalable and accessible platform for users.

---


## Features (Pictures of stuff site can do)

### Navbar Customization
The site's navigation bar dynamically changes based on user authentication status, providing an intuitive and personalized experience.

### Post and Comment Functionality
Users can seamlessly create, edit, and delete posts, fostering a dynamic and engaging community-driven content creation environment.

---

## Credits

- Codemy.com's YouTube channel, without whom's extensive tutorials surround Django and Python I never would've completed this project. [Codemy.com on YouTube](https://www.youtube.com/@Codemycom)
- Pexels for the placeholder images.
- Slack, my classmates, Muinteor Alan B, Tutor Support, and my Discord friends who actually know how to code for finally getting me over the line.

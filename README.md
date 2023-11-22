![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/77da9c4f-318b-4099-b220-f7f5f59f5e9a)![Code Institute Logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Welcome Code Institute Assessor, to Gamesworld!

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/73f34736-f5a6-4db4-b860-5c8a7c93d435)


[Final Deployment Available Here](https://project-4-django-app-dee496c0d081.herokuapp.com/)

---

# Gamesworld

Welcome to Gamesworld, a dynamic platform that seamlessly blends the functions of a news aggregator and a discussion forum. Tailored for the ever-evolving world of video games, Gamesworld serves as a hub where gaming enthusiasts can stay updated on the latest industry news and engage in meaningful discussions.

## Key Features

### News Aggregation and Sorting
Gamesworld focuses on four major gaming platforms: PlayStation, Xbox, Nintendo, and PC gaming. Users can easily navigate these categories, sorting and selecting topics of interest directly from the home page. The admin panel provides flexibility, enabling administrators to introduce new discussion categories and expand the range of topics.

### User Profiles and Social Connectivity
Users can create personalized profiles, adding a bio, profile picture, and links to their other social media accounts. This information is prominently displayed under each user's posts, fostering connections not only within the Gamesworld community but also across other social media platforms.

### Content Creation and Management
Gamesworld empowers users with CRUD (Create, Read, Update, Delete) functionality. Users can effortlessly create new posts, incorporating body text, titles, and optional header images. The ability to edit and delete posts provides users with complete control over their contributions to the site.

### Colour Palette  

I used coolors.com to generate a colour palette which I then applied to my page. While I maintained a minimalist approach to the website's design and kept the colours sparse, opting to use a plain white background, it was helpful to have a colour scheme in place that I could consult when styling the page.

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/782d5635-8d83-432b-865d-d41615233aab)


## Agile Development Approach

Gamesworld follows Agile principles for a flexible and collaborative development process. Divided into three iterations, each represented by a Github Kanban board, the project utilized Github tools for streamlined communication and progress tracking. Custom workflows involving Milestones for Epics and Issues for User Stories provided a structured approach to project organization.

### Dynamic Adaptability and Continuous Improvement

It may seem odd that my issues are not hosted on this repository itself, though this is merely because they were initially created for an earlier iteration of this project which had to be defunct due to several unfixable errors which required me to begin the project again. However rather than recreate the user stories I transferred the project containing the issues to this repository as they were equally applicable to this project and I used them as the basis for my work in recreating the groundwork for the rebuild.

Agile's dynamic prioritization categorized User Stories into 'must do,' 'could do,' and 'should do,' allowing adaptable planning to accommodate changing project requirements. Despite challenges in pre-planning content due to time constraints, the Agile approach encouraged continuous improvement. The Kanban board visually represented progress, while reflections on completed iterations facilitated insights for refining subsequent cycles, ensuring the successful and flexible development of the video game blog.

## Deployment

This project was initialiased using the [Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

### Local Deployment:

1. **Set up Virtual Environment:**
   - Create a virtual environment using virtualenv to isolate the project dependencies.
   - Install required packages such as Django, Gunicorn, and Cloudinary within the virtual environment.

2. **Project Initialization:**
   - Create the project by running `django-admin startproject project_name` inside the virtual environment.
   - Similarly, create the app by running `python3 manage.py startapp app_name`. For this project, two separate apps were created: 'myblog' for handling the Gamesworld blog and 'members' for managing membership and registration.

3. **Database Configuration:**
   - Utilize a database for storing migrations. In this project, Elephant SQL was used under a free tiny turtle plan. Import the database configuration into the project through the `env.py` file.
   - Ensure the connection is operational by pushing migrations to the database and ensuring they have migrated correctly.
  
4. **Cloudinary:**
   - Cloudinary is utilized in this project in this project as online storage for static files such as images users may use as their profile pictures, or as header images for their posts.
   - Set up a free Cloudinary account and add the CLOUDINARY_URL as an environment variable in the env.py file.
   - Hook up Cloudinary in settings.py by configuring STATICFILES_STORAGE, STATICFILES_DIRS, STATIC_ROOT, MEDIA_URL, DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage',

5. **Deployment:**
   -In the ROOT directory create a Procfile containing "web: gunicorn myblog.wsgi"
   -Run pip3 freeze to get the requirements and copy them into a requirements.txt file.
### Heroku Deployment:

1. **Create Heroku App:**
   - Create a new Heroku app and link it to the Git repository for the project.

2. **Heroku Configurations:**
   - Set up Heroku Config Vars to account for necessary variables such as Cloudinary URL, the Database URL and the Secret Key. Also, add DISABLE_COLLECTSTATIC with a value of 1 until final deployment.

3. **Cloudinary and Database:**
   - Ensure Cloudinary configurations are set up correctly to handle media files.
   - The database used in this project (Elephant SQL) should be configured in Heroku.

4. **Deployment:**
   - Deploy the project to Heroku by pushing the code to the Heroku remote repository, setting Debug=True to Debug=False before final deployment.
   - The project should now be accessible through the provided Heroku app URL.

This deployment process ensures a smooth transition from local development to a live Heroku environment, providing a scalable and accessible platform for users.

---

## Features

### Navbar Customization
The site's navigation bar dynamically changes based on user authentication status, providing an intuitive and personalized experience.

### Post and Comment Functionality
Users can seamlessly create, edit, and delete posts, fostering a dynamic and engaging community-driven content creation environment. They are also able to comment and interact with other users posts, with future potential CRUD capabilities for these comments.

### User Profiles
Users can display their own personal flair by creating their own profile page which will display to other users beneath any of their posts. Users can upload their own profile picture, write their own bio and include links to their own personal websites or social media platforms, encouraging users to engagement with one another across their digital footprint.

---

## Testing

### Lighthouse

Testing was done manually via continuous and determined experimentation of functionality on both Desktop and Mobile Phone.

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/a056e283-1b25-4c5b-8bea-894efa47f150)

Lighthouse Testing provided important feedback for Gamesworld, such as a lack of a meta-description or links not having high enough contrast against the site's plain white background. These were swiftly remedied. The only outstanding issue was the SEO's middling score, attributed to various links not having "descriptive text". This seems an unavoidable issue on a user-driven site where the content and discussion and shaped by the users, as they have the freedom to title their posts whatever they please. Thus this issue was noted, but deemed inherent to the site's design and set aside. This was not an issue on the site's individual blog-post pages as they lacked the cascade of various links which affected the homepage's score.

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/d7f70b09-1d29-487e-934f-9a8bdd63b036)

### Responsivity

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/73f34736-f5a6-4db4-b860-5c8a7c93d435)

As the base web-page themselves are relatively simple, Bootstrap's built-in responsivity was more than capable of handling my needs. An issue arouse, that I had built my site locally in Visual Code Studio and Heroku blocked all attempts to use Responsivity Websites which made it difficult to test responsivity via my usual methods. Thankfully the Google Chrome Extension [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb) is made for developers in my position and allowed me to view my site from a catalogue of different view ranges.

---

## Credits

- Codemy.com's YouTube channel, whose extensive tutorials on Django and Python were instrumental in completing this project. [Codemy.com on YouTube](https://www.youtube.com/@Codemycom)
- The creators of [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?pli=1)
- Pexels for the Placeholder images. Google Image Search for the Images used in my test posts.
- Microsoft Bing Image Creator for the image of Crash Bandicoot fighting Sonic the Hedgehog.
- The endless threads on Stackoverflow
- Slack, my classmates, Muinteor Alan B, Tutor Support, and my Discord friends who actually know how to code for finally getting me over the line.

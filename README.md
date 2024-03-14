![Code Institute Logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Welcome Code Institute Assessor, to Gamesworld!

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/91f8e38d-add0-4b50-9392-b22a2f139be3)


[Final Deployment Available Here](https://project-4-django-app-dee496c0d081.herokuapp.com/)

---

### Table of Contents

1. [Gamesworld](#gamesworld)
   - [Key Features](#key-features)
      - [News Aggregation and Sorting](#news-aggregation-and-sorting)
      - [User Profiles and Social Connectivity](#user-profiles-and-social-connectivity)
      - [Post Categorization](#post-categorisation)
      - [Content Creation and Management](#content-creation-and-management)
      - [Colour Palette](#colour-palette)
   - [Agile Development Approach](#agile-development-approach)
      - [Dynamic Adaptability and Continuous Improvement](#dynamic-adaptability-and-continuous-improvement)
   - [Deployment](#deployment)
      - [Local Deployment](#local-deployment)
      - [Heroku Deployment](#heroku-deployment)
   - [Features](#features)
      - [Navbar Customization](#navbar-customization)
      - [Post and Comment Functionality](#post-and-comment-functionality)
      - [Post Likes](#post-likes)
      - [User Profiles](#user-profiles)
      - [If-Else Authentication](#if-else-authentication)
   - [Testing](#testing)
      - [W3C Validator](#w3c-validator)
      - [Lighthouse](#lighthouse)
      - [Manual Testing](#manual-testing)
      - [Responsivity](#responsivity)
   - [Future Features](#future-features)
   - [Bugs](#bugs)
   - [Credits](#credits)

# Gamesworld

Welcome to Gamesworld, a dynamic platform that seamlessly blends the functions of a news aggregator and a discussion forum. Tailored for the ever-evolving world of video games, Gamesworld serves as a hub where gaming enthusiasts can stay updated on the latest industry news and engage in meaningful discussions. The long-term goal of this site is to foster a community of gamers by offering them a place to discuss news, upcoming releases and their own opinions. As an ever-expanding and evolving medium, gaming is a constant cycle of online discussion, and by offering a board specifically tailored to those interested in this field we can build and engaged and active user base and then begin to sell ad space on the gutters and banners of the various pages.

## Key Features

### News Aggregation and Sorting
Gamesworld focuses on four major gaming platforms: PlayStation, Xbox, Nintendo, and PC gaming. Users can easily navigate these categories, sorting and selecting topics of interest directly from the home page. The admin panel provides flexibility, enabling administrators to introduce new discussion categories and expand the range of topics.

### User Profiles and Social Connectivity
Users can create personalized profiles, adding a bio, profile picture, and links to their other social media accounts. This information is prominently displayed under each user's posts, fostering connections not only within the Gamesworld community but also across other social media platforms.

### Post Categorisation 
The ability to both categorise posts and search through others' posts via their category lets the user customise their viewing experience and filter what posts they wish to see and engage with.

### Content Creation and Management
Gamesworld empowers users with CRUD (Create, Read, Update, Delete) functionality. Users can effortlessly create new posts, incorporating body text, titles, and optional header images. The ability to edit and delete posts provides users with complete control over their contributions to the site.

### Colour Palette  

I used coolors.com to generate a colour palette which I then applied to my page. While I maintained a minimalist approach to the website's design and kept the colours sparse, opting to use a plain white background, it was helpful to have a colour scheme in place that I could consult when styling the page.

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/782d5635-8d83-432b-865d-d41615233aab)

### Wireframe

Wireframes for the Gamesworld site were created using Wireframe.cc to visualise how the final deployment of the website would appear. They were intentionally designed to be minimalistic and sleek with sparse to none visual clutter as to focus the attention of the User onto the content of the blogs themselves, thus funnelling them into engaging with the blogs via the comment section.

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/e1a8048b-1f0c-46f4-a754-5f3ab64bae56)

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/82385f74-0c0f-4476-9211-f09a9f002164)


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
Users can seamlessly create, edit, and delete posts, fostering a dynamic and engaging community-driven content creation environment. They are also able to comment and interact with other users posts, with future potential CRUD capabilities for these comments. Posts are also displayed in order of their creation dates, which are displayed on the post's title card displayed on the home-page, giving the Users immediate access to the most up-to-date posts.

### Post Likes
Authenticated users can like and unlike posts which they find interesting or engaging, and these number of likes are tallied allowing users to quickly see at a glance whether the post is of a quality that they would be interested in engaging with should it be particularly lengthy.

### User Profiles
Users can display their own personal flair by creating their own profile page which will display to other users beneath any of their posts. Users can upload their own profile picture, write their own bio and include links to their own personal websites or social media platforms, encouraging users to engagement with one another across their digital footprint.

### If-Else Authentication
A multitude of If-Else statements are employed based on the user's authentification state and whether their user id matches those of various posts. These are used to prevent users editing or deleting posts which are not those, and also display messages to the users should they somehow find themselves on web-pages they were never intended to access via attempting to brute-force the site using html pathing.

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/2da27344-4a9f-4ee8-8103-0ce6f27e4fae)

---

## Testing

Testing was accomplished both manually via continuous and determined experimentation of functionality on both Desktop and Mobile Phone, and automated through various online validators and tests.

### W3C Validator 

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/70ace919-fd90-4901-ab69-53ce083791a5)

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/b6c23565-6b93-4ec4-b928-ccc92c390d7e)


Multiple iterations of the site deployed on Heroku were run through the W3C Validator to ensure the HTML was error-free. This was invaluable as my CSS styling is included in the HTML files and I had misplaced it in several instances. For the curious, they were placed directly in the HTML as opposed to a CSS style sheet as I encountered several errors involving file-pathing to the style sheets, and rather decided to simplify the process for myself via direct insertion of the styling into the html files. Likewise the W3C CSS Validator returned with no errors.

### Python 

The site's Python code was verified using https://pep8ci.herokuapp.com/. It verified that there were no severe instances of code-breaking script, and the errors it returned related to line-length and white space indentation surrounding the lines. Happily, none of these errors affected the practical application of the code itself. 

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/c9062d10-441c-4b90-88ec-e8d0a6dcb0b9)

### Javascript

The site's few instances of Javascript were tested using https://jshint.com/ and manually tested by verifying their functionality in the console logs. All script on the site is functional and fit for purpose.

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/32c87c36-daa1-4119-9b52-0dcc7277dca7)

### Manual Testing

The site was tested through using various web browsers including Google Chrome, Edge, and Firefox. Likewise, the site was viewed on various devices such as desktops, laptops, smartphones and tablets.
In order to confirm the successful implementation of the User Stories manual testing was accomplished.

### User Stories Testing

i) As a site user I can view a paginated list of posts so that I can select which post I want to view
   * Confirmed via visiting the homepage on various screens and browsers, after making posts as an admin and ensuring they are displayed correctly.

ii) As a Site User I can view a list of posts so that I can select one to read
   * Confirmed by loading the homepage as a generic user and verifying the posts are easily viewable on various screen resolutions and platforms.

iii) As a Site User I can click on a post so that I can read the full text
   * Confirmed by clicking on various posts to ensure links are operational and bring the user to the correct post view page.

iv) As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral
   * Confirmed by viewing individual post views and observing that likes are operational.

v) As a Site User / Admin I can view comments on an individual post so that I can read the conversation
   *  Confirmed by going to individual posts while logged in and viewing the comments that have been left beneath the post by other users.

vi) As a Site User I can register an account so that I can comment and like
   * Confirmed by registering for a new user account using a dummy email.

vii) As a Site User I can leave comments on a post so that I can be involved in the conversation
   * Confirmed by going to individual posts while logged in and leaving comments, and verifying they appear.

viii) As a Site User I can like or unlike a post so that I can interact with the content
   * Confirmed by using an account to like and unlike comments on individual page views.

ix) As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
   * Confirmed by using the site admin account to create posts from the create post page only accessible to staff accounts, then editing that post and ensuring it updates appropriately, and then deleting said post and verifying that it is no longer viewable on the website. 

x) As a Site Admin I can create draft posts so that I can finish writing the content later
   * Confirmed by saving a draft page of a post and then revisiting the draft to continue writing it at a later point in the admin panel.
   
xi) As a user I can edit my posts so that I can fix typos or clarify what I was speaking about.
   * Confirmed by using a generic user profile to ensure they are capable of editing their own comments, and that the comments appear in their edited states after being confirmed.

xii) As a User I can Change my Password so that I can alter my credentials in the event of an information leak to prevent people accessing my account.
   * Confirmed by navigating to the Edit Profile Settings page via the navbar while logged in, and following the steps to reset the user's password.

xii) As a User I can Personalise my profile page with information such as my own personal biography, a profile picture, and various personal links so that I can display my own personal flair while also providing important context and information about me as a user
   * Confirmed by navigating to the Edit Profile page by way of the navbar and verifying all the information updates accordingly depending on what the user enters.

xiv) As a User I can view the various blog post categories so that I can quickly find posts and information relevant to my interests, while filtering out the posts I don't care about
   * Confirmed by using the Categories dropdown in the navbar and ensuring that when clicked that the displayed posts correctly align with the category selected.

xv) As an Admin I can prevent users from editing and deleting other users posts so that there is a sense of security upon the site.
   * Confirmed utilising a variety of verification and authentication tests both built into django and custom made for the site, and ensuring they prevent users from brute-forcing their way to pages via directly typing url addresses and trying to bypass security.

### Lighthouse

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/a056e283-1b25-4c5b-8bea-894efa47f150)

Lighthouse Testing provided important feedback for Gamesworld, such as a lack of a meta-description or links not having high enough contrast against the site's plain white background. These were swiftly remedied. The only outstanding issue was the SEO's middling score, attributed to various links not having "descriptive text". This seems an unavoidable issue on a user-driven site where the content and discussion and shaped by the users, as they have the freedom to title their posts whatever they please. Thus this issue was noted, but deemed inherent to the site's design and set aside. This was not an issue on the site's individual blog-post pages as they lacked the cascade of various links which affected the homepage's score.

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/d7f70b09-1d29-487e-934f-9a8bdd63b036)

### Responsivity

![image](https://github.com/BrandonPCollins/my-project-4/assets/131177569/9345f2a2-dfb4-44b1-b1af-43bc5597220b)

As the base web-page themselves are relatively simple, Bootstrap's built-in responsivity was more than capable of handling my needs. An issue arouse, that I had built my site locally in Visual Code Studio and Heroku blocked all attempts to use Responsivity Websites which made it difficult to test responsivity via my usual methods. Thankfully the Google Chrome Extension [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb) is made for developers in my position and allowed me to view my site from a catalogue of different view ranges.

---

## Future Features

* Full CRUD Functionality for user comments, allowing users to edit and delete their comments. Further improvements to the comment system include tracking the user's comment history on their profile page, allowing users to reply to specific comments.
* A user reporting system. For the moment I decided to eschew the need to approve comments and posts as the site is rather small, but in the future, a community sourced moderation system wherein users can report posts and comments for breaking community guidelines would be an essential feature as the site continues to grow.
* The implementation of a private message system, allowing users to interact with one another directly rather than being restricted to the comment section of their posts.
* Advanced Search Functionality to allow users to filter posts based on keywords or user profiles, rather than just the categories as on the current site.
* Incorporate the number of likes into a page for sorting posts, creating a "Hot" or "Trending" page, where rather than filtering posts by their most recent upload, instead the most recent post with the highest proportion of likes are given pride of place atop the page. 
* A dark mode for late-night browsing.

---

## Bugs

* The project initially had a Rich Text Editor for blog posts, with the ckeditor package both installed locally and featured in the requirements.txt. However at some point during development, it disappeared. I'm not at all sure how this happened, and couldn't manage to bring it back either. Rather where it should have been was merely a blank space. I have a feeling it has to do with the requirements.txt somehow but can neither prove this nor did my fiddling with that file return the text editor. Rather I commented out the field for the moment and restored the standard TextField in my models.py. 

---

## Credits

- Codemy.com's YouTube channel, whose extensive tutorials on Django and Python were instrumental in completing this project. [Codemy.com on YouTube](https://www.youtube.com/@Codemycom) and their [tutorial on building a Django blog](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi).
- The creators of [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?pli=1)
- Pexels for the Placeholder images. Google Image Search for the Images used in my test posts.
- Microsoft Bing Image Creator for the image of Crash Bandicoot fighting Sonic the Hedgehog.
- The endless threads on Stackoverflow
- Slack, my classmates, Muinteor Alan B, Tutor Support, and my Discord friends who actually know how to code for finally getting me over the line.

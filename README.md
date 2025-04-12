# [ReelRatings](https://fork-and-flavours-72f7a7edee0f.herokuapp.com/)

Fork & Flavour is a recipe manager website that allows authorised users to create, view, edit, and delete recipes. It features a clean, modern, and playful design, offering a seamless user experience with easy navigation and an interactive recipe management system.

![Fork & Flavours Responsiveness](docs/fork-and-flavours-responsiveness.png)

[View live website here](https://fork-and-flavours-72f7a7edee0f.herokuapp.com/)

## Table of Contents

- [User Experience (UX)](#user-experience-ux)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
  - [Design](#design)
  - [Wireframes](#wireframes)
- [Features](#features)
- [Database Schema](#database-schema)
  - [Tables](#tables)
  - [Relationships](#relationships)
- [Manual Testing](#manual-testing)
  - [Features Testing](#features-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Responsiveness Testing](#responsiveness-testing)
  - [Code Validation](#code-validation)
  - [Bugs](#bugs)
  - [Lighthouse Testing](#lighthouse-testing)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Tools](#frameworks-libraries--tools)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Content](#content)

# User Experience (UX)

## Project Goals

- **Intuitive Navigation:** Ensure that users can easily navigate through the site with a clear, simple, and consistent menu and navigation options.
- **Mobile-Friendly Layout:** Provide a responsive design that works seamlessly across all devices, with a mobile-first approach.
- **Minimalist Aesthetic:** Keep the design clean, modern, and visually appealing by incorporating ample white space and an easy-to-read font pairing.
- **User-Centric Functionality:** Design the site with user goals in mind, ensuring that users can easily create, view, edit, and delete recipes without confusion or unnecessary steps.
- **Accessible Design:** Ensure that the website is fully accessible, with considerations for colour contrast, font readability, and screen reader compatibility.
- **Engaging and Interactive Elements:** Implement interactive features like hover effects and checklist functionality for a more dynamic user experience.

## User Stories

- As a new user, I can create an account so that I can access the recipe management features of the website.
- As a registered user, I can log into my account so that I can access my personalised recipe dashboard.
- As a user, I can view the details of a recipe so that I can learn how to make the dish.
- As a logged-in user, I can create a new recipe so that I can share my cooking creations with others.
- As a logged-in user, I can edit my own recipes so that I can update any mistakes or improve the recipe.
- As a logged-in user, I can delete my recipes so that I can remove any outdated or unwanted recipes from my collection.
- As a user, I can browse a list of all available recipes so that I can discover new dishes to try.

These user stories are also tracked on my [Kanban board](https://github.com/users/desireealexia/projects/7) for ongoing project management and development.

## Design

### Colour Scheme

The colour scheme for Fork & Flavour reflects a modern, minimalist, and vibrant aesthetic. The colours are:

- Cal Poly Green (#1F4F31): A deep, rich green used for the main accents and headings.
- Engineering Orange (#B13F26): A warm, vibrant orange used for buttons and interactive elements.
- Chocolate Cosmos (#5B122A): A deep burgundy, used to complement the green and orange accents.
- Buff (#E49E6B): A soft, warm tone used for secondary accents.
- Seashell (#FBF1EE): A light, neutral background colour that provides a clean, airy feel.
- Jet (#333333): A dark grey used for text, providing high contrast and readability.

![Fork & Flavours Colour Palette](docs/fork-and-flavours-palette.png)

### Typography

For a clean and modern user interface, the following fonts have been chosen:

- Heading Font: Montserrat — A bold, modern sans-serif font for headings and titles.
- Body Font: Open Sans — A clean, sans-serif font for body text, offering readability and balance

### Imagery

- Use of high-quality images to showcase recipes with a playful and vibrant aesthetic.
- Interactive elements and hover effects to engage users.

You can view the logo [here](static/images/fork_and_flavour_logo.png)

### Wireframes

Homepage: The homepage features a clean layout with easy navigation to key areas, such as featured recipes and recipe categories.
My Recipes Page: Users can view all their saved recipes.
Search Results Page: Users are able to view their search results and filter the results based on their categories.

- [Home Page Wireframe - View](docs/home_wireframe.png)
- [Recipe Page Wireframe - View](docs/recipe_page_wireframe.png)
- [Search Results Page Wireframe - View](docs/search_results_wireframe.png)

Profile Page (Scrapped): Originally intended for user profile details, this page was discarded during development because it closely mirrored the functionality of the My Recipes page.

- [Profile Wireframe - View](docs/profile_wireframe.png)

# Features

- **User Authentication**  
  Fork & Flavour provides secure user authentication, allowing users to register for an account, log in, and log out safely. This ensures that users can access and manage their own recipe collections with ease.

| Sign Up Page                 | Login Page                | Sign Out Page                  |
| ---------------------------- | ------------------------- | ------------------------------ |
| ![Sign up](docs/sign-up.png) | ![Login](docs/log-in.png) | ![Sign Out](docs/sign-out.png) |

- **Recipe Creation**  
  Users can create new recipes by filling in details such as the recipe title, a list of ingredients, detailed preparation steps, and the option to upload images. This allows users to share their favourite dishes and cooking tips with the community.

![Recipe Creation](docs/create-recipe.png)

- **Edit & Delete Recipes**  
  Users have full control over their recipes. They can edit any part of their recipe - from ingredients to cooking instructions - and delete their recipes if needed. This flexibility ensures that the content stays relevant and up-to-date.

![Edit & Delete Recipes](docs/edit-and-delete-btns.png)

- **Browse Recipes**  
  Users can browse a wide variety of recipes submitted by others. The browsing experience is intuitive and simple, allowing for effortless discovery of new meals to try.

- **Search & Filter**  
  The search functionality allows users to find recipes by name or by ingredient. The filtering options let users narrow down results based on categories like Breakfast, Dessert, Snack, and more, making it easy to find the perfect recipe for any occasion.

![Search](docs/search.png)
![Filter](docs/filter-search.png)

- **Categories**  
  Recipes are categorised into common meal types such as Breakfast, Lunch, Dinner,etc, allowing users to quickly explore recipes based on their desired meal type.

- **Social Media Sharing**  
  Recipes can be shared directly on popular social media platforms such as Facebook and Twitter. This makes it easy for users to share their favourite recipes with friends and family or discover new recipes from others.

![Social Media Sharing](docs/share-recipes.png)

- **Responsive Design**  
  The website is fully responsive, ensuring an optimal viewing experience on any device, whether it’s a desktop, tablet, or smartphone. Users can access their recipes and browse the site without any loss of functionality.

- **Admin Dashboard**  
  Administrators have access to a powerful dashboard that allows them to manage user accounts, moderate recipes, and oversee the overall content of the site. This helps maintain a safe and organised environment for all users.

![Admin Dashboard](docs/admin-dashboard.png)

## Future Features

While the website already includes a solid set of features, we are planning to add even more functionality to improve the user experience:

- **User Comments & Ratings:**Users will soon be able to leave comments and rate recipes they’ve tried. This feature will help foster a sense of community, allowing users to share their experiences and offer feedback on different dishes.

- **Weekly Featured Recipes:** Every week, a selection of standout recipes will be featured on the homepage. These recipes will be hand picked for their creativity, popularity, or seasonal relevance, giving users fresh inspiration each week.

- **Shopping List Generator:** Users will be able to generate a shopping list based on the ingredients of a selected recipe. This feature will help streamline the cooking process by allowing users to easily gather all the necessary ingredients for their chosen dishes.

- **Optional Ingredients:** A new feature will allow users to mark certain ingredients as optional, making it easier to adjust recipes based on dietary preferences or ingredient availability.

- **Favourite Recipes:** Users will be able to save their favourite recipes to a personal collection for easy access. This feature will help users quickly find and revisit the recipes they love most.

# Database Schema

Fork & Flavour uses a relational database to store user accounts, recipes, ingredients, and categories. Below is the **Entity-Relationship Diagram (ERD)** representing the database structure:

![ERD Diagram](docs/fork-and-flavours-erd.png)

## Tables

### **User**

Stores user account details.

| Column      | Data Type | Constraints                |
| ----------- | --------- | -------------------------- |
| id          | integer   | Primary Key                |
| username    | varchar   | Unique, Not Null           |
| email       | varchar   | Unique, Not Null           |
| password    | varchar   | Not Null                   |
| date_joined | timestamp | Default: current timestamp |

### **Recipe**

Stores recipe details, including the user who created it, its category, and instructions.

| Column       | Data Type | Constraints                        |
| ------------ | --------- | ---------------------------------- |
| id           | integer   | Primary Key                        |
| title        | varchar   | Not Null                           |
| slug         | slug      | Unique, Not Null                   |
| user         | integer   | Foreign Key → user.id              |
| category     | varchar   | Foreign Key → category.id          |
| description  | text      | Nullable                           |
| instructions | text      | Not Null                           |
| image        | image     | Nullable                           |
| status       | integer   | Default: 0 (e.g., Published/Draft) |
| created_at   | timestamp | Default: current timestamp         |
| updated_at   | timestamp | Default: current timestamp         |

### **Ingredient**

Stores ingredient details for recipes.

| Column | Data Type | Constraints |
| ------ | --------- | ----------- |
| id     | integer   | Primary Key |
| name   | varchar   | Not Null    |

### **RecipeIngredient**

Links recipes to their ingredients, with quantities and measurement units.

| Column      | Data Type | Constraints                 |
| ----------- | --------- | --------------------------- |
| id          | integer   | Primary Key                 |
| recipe      | integer   | Foreign Key → recipe.id     |
| ingredient  | integer   | Foreign Key → ingredient.id |
| quantity    | decimal   | Not Null                    |
| unit        | varchar   | Nullable                    |
| is_optional | boolean   | Default: false              |

**NOTE:** is_optional was originally intended to mark ingredients as optional, feature has been removed.

### **Category**

Stores recipe categories (e.g., "Breakfast", "Dessert").

| Column | Data Type | Constraints      |
| ------ | --------- | ---------------- |
| id     | integer   | Primary Key      |
| name   | varchar   | Unique, Not Null |

## Relationships

- **Users & Recipes:** One-to-Many → A user can create multiple recipes, but each recipe belongs to one user.
- **Recipes & RecipeIngredients:** One-to-Many → A recipe can have multiple ingredients, and each ingredient is associated with one recipe.
- **Ingredients & RecipeIngredients:** One-to-Many → An ingredient can be used in multiple recipes.
- **Recipes & Categories:** Many-to-One → Each recipe belongs to one category, but a category can have multiple recipes.

This database structure ensures efficient data management for storing, retrieving, and updating recipes, ingredients, and user-related data in the Fork & Flavour platform.

# Accessibility

Fork & Flavour is designed with accessibility in mind to ensure a positive user experience for everyone, including people with disabilities. Below are some of the key accessibility features implemented in the project:

### **Semantic HTML**

- The website uses semantic HTML elements to provide a meaningful structure for screen readers. Elements like `<header>`, `<main>`, `<footer>` and `<nav>` are used to improve navigation for assistive technologies.

### **Keyboard Navigation**

- All interactive elements, such as links, buttons, and form fields, are fully navigable using the keyboard. This ensures that users who cannot use a mouse can still navigate and interact with the site efficiently.

### **Alt Text for Images**

- All images, including recipe images, are provided with descriptive **alt text** to ensure that visually impaired users can understand the content of the images.

### **Colour Contrast**

- The colour scheme adheres to WCAG (Web Content Accessibility Guidelines) standards, with sufficient contrast between text and background colours to improve readability for users with visual impairments. Specifically, the primary colour palette of **cal poly green**, **engineering orange**, and **chocolate cosmos** ensures strong contrast across the site.
- The **Accessible Color Palette Builder** tool was used to ensure that the colour choices meet WCAG guidelines for contrast, making the site more accessible to users with colour blindness or low vision.

![Accessible Colour Combinations for Fork & Flavours](docs/accessible_colour_palette.png)

### **Form Labels and Fieldset**

- All form fields, including input fields for creating and editing recipes, are properly labelled with clear instructions. Fieldset elements are used to group related fields together, and `<label>` elements are associated with input fields to make forms accessible.

### **Focus States**

- Focus states are clearly visible on all interactive elements, making it easier for users navigating with the keyboard or other assistive technologies to identify which element is currently active.

### **Responsive Design**

- The website is fully responsive and adapts to various screen sizes, making it accessible to users on desktop, tablet, and mobile devices. The layout adjusts to fit the screen size and orientation, ensuring a seamless experience for all users.

### **Error Handling and Feedback**

- Form validation is implemented with clear error messages, providing users with helpful feedback when something goes wrong. These messages are announced to users with assistive technologies, ensuring that everyone can address any issues.

### **Text Alternatives for Interactive Elements**

- Interactive elements such as buttons and links are clearly described with text labels, making them accessible for screen reader users and those with limited vision.

### **ARIA (Accessible Rich Internet Applications)**

- ARIA roles and properties are used where necessary to enhance the accessibility of dynamic content (e.g., recipe creation forms) and complex user interactions (e.g., modal pop-ups or dropdowns).

By implementing these features, Fork & Flavour strives to provide an inclusive and accessible experience for all users, regardless of their abilities or disabilities.

# Manual Testing

## Features Testing

|                        Feature                         |                           Test case                            |                                                     Outcome                                                      |
| :----------------------------------------------------: | :------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------: |
|            Sign up with valid/invalid data             |       Submit sign-up form with valid and invalid inputs        |                       Account is created with valid data; errors shown for invalid inputs                        |
|                   Log in and log out                   |       Log in with valid/invalid credentials and log out        |             Redirect to home page on success; show error on failure; log out redirects to home page              |
|         Hero section content changes on login          |     Log in as a user and check the home page hero section      |           Heading changes to Welcome to Fork & Flavour, <user>! and displays the logged-in user's name           |
|              Hero buttons change on login              |            Log in and view the hero section buttons            |        "Get Started" and "Login" buttons are replaced by "View My Recipes" button linking to recipe list         |
|            Users can’t edit others’ recipes            |          Try to access another user's recipe edit URL          |                                                  Access denied                                                   |
|      Create a new recipe with all required fields      |        Fill and submit the recipe form with valid data         |                                      Recipe is saved and shown on the site                                       |
|                  Upload invalid image                  |           Try uploading a non-image file (e.g. .txt)           |                                            Validation prevents upload                                            |
|                    Form validations                    |            Submit form with missing/invalid fields             |                                       Shows validation errors on the form                                        |
|            Save recipe with status 'draft'             |        User creates a recipe and sets status to 'draft'        |                         Recipe is saved but only visible on the user’s "My Recipes" page                         |
|          Save recipe with status 'published'           |      User creates a recipe and sets status to 'published'      |                       Recipe appears on the public recipe list and is visible to all users                       |
|            Draft recipes hidden from public            |      Log in as a different user or view while logged out       |                Draft recipes from other users are not visible on the public list or detail pages                 |
|            Published recipes visible to all            | View published recipes while logged out or as a different user |             Published recipes are accessible and displayed on the main recipe list and detail pages              |
|                Status badge visibility                 |                 Log in and go to "My Recipes"                  |                   Each recipe displays a "Draft" or "Published" badge depending on its status                    |
|               No badges on public pages                |                   View recipes on home page                    |                                            No status badges are shown                                            |
|                     Edit a recipe                      |            Update title, ingredients, etc, and save            |                                    Changes are reflected in the recipe detail                                    |
|                    Delete a recipe                     |                    Click delete and confirm                    |                                   Recipe is removed from the list and database                                   |
|                View a recipe in detail                 |                  Click a recipe from the list                  |                               Navigates to recipe detail page displaying all info                                |
|                Checkbox on ingredients                 |     Click checkboxes beside each ingredient while cooking      |                                          Checkbox gets marked/unmarked                                           |
|                 Back button link logic                 |           Click each variation and observe behaviour           |      Each back button correctly navigates to its intended destination with proper query/state if applicable      |
|  Back button: viewing someone else’s recipe directly   |     Log in, view another user’s recipe via homepage or URL     |                   Back button text is "Back to Main Page" and clicking it returns to homepage                    |
|        Back button: viewing own recipe directly        |          Log in, go to "My Recipes" and click on one           |             Back button text is "Back to Your Recipes" and clicking it returns to "My Recipes" page              |
| Back button: viewing someone else’s recipe from search |     Search for a recipe and click on someone else’s result     | Back button text is "Back to Search Results" and clicking it returns to search page with query and filter intact |
|      Back button: viewing own recipe from search       |        Search for a recipe and click on your own result        |           Back button text is "Back to Your Recipes" and clicking it returns to the "My Recipes" page            |
|           List all recipes on the home page            |                        Visit home page                         |                                All recipes are listed with titles and thumbnails                                 |
|             Search for a recipe by keyword             |           Enter a search term like "egg" and submit            |                             Recipes with "egg" in the name or ingredients are shown                              |
|               Filter search by category                |       Select a category (e.g., "Dinner") while searching       |                     Only recipes in the "Dinner" category matching the search term are shown                     |
|            Search with no matching results             |        Enter a search term that doesn’t match anything         |                                  A message like "No recipes found" is displayed                                  |
|               View a user’s own recipes                |                       Go to “My Recipes”                       |                               Only recipes created by the logged-in user are shown                               |
| Buttons, links, and forms are clickable and functional |                     Click all UI elements                      |                                  All expected actions happen with no dead links                                  |
|                       Pagination                       |               View more than one page of recipes               |                                  Recipes are split across pages with navigation                                  |
|                   SEO-friendly URLs                    |                    View recipe detail page                     |                            URL includes readable slug (e.g., /recipes/chocolate-cake)                            |
|                     Share recipes                      |        Click share button (copy link, share to social)         |                                Share options open and links copy/share correctly                                 |
|                   Responsive design                    |            Resize browser window or open on mobile             |                                    Layout adjusts and content is still usable                                    |
|                  Accessibility basics                  |             Navigate with keyboard / screen reader             |                                All buttons/links can be accessed without a mouse                                 |

## Browser Compatibility

| Browser Tested | Intended Appearance | Intended Responsiveness |
| :------------: | :-----------------: | :---------------------: |
|     Chrome     |        Good         |          Good           |
|     Safari     |        Good         |          Good           |
| Microsoft Edge |        Good         |          Good           |

## Responsiveness Testing

|    Device Tested    | Site responsive >= 700px | Site responsive < 699px> | Renders as expected |
| :-----------------: | :----------------------: | :----------------------: | :-----------------: |
|  iPhone 14 Pro Max  |           N/A            |           Good           |        Good         |
| Samsung Galaxy S8 + |           N/A            |           Good           |        Good         |
|      iPad Air       |           Good           |           N/A            |        Good         |
|   MacBook Air 13"   |           Good           |           N/A            |        Good         |
|     23" monitor     |           Good           |           N/A            |        Good         |

## Code Validation

### HTML Validator

To ensure the correctness of the HTML code, I used the W3C HTML Validator. The validation process revealed no errors in the HTML code across all pages of the website. This confirms that the HTML is properly structured and adheres to web standards.

![HTML Validator](docs/%20html_validator.png)

### CSS Validator

For CSS validation, I utilised the W3C CSS Validator. The CSS code was thoroughly checked, and no errors were found. This indicates that the CSS is correctly formatted and conforms to the established CSS standards.

![CSS Validator](docs/%20css_validator.png)

## Bugs

### Ingredients Section in Recipe Admin Form Not Positioned Correctly
In the admin panel, when adding or editing a recipe, the ingredients section appears after the instructions, which is not the desired layout for recipes. Typically, ingredients should come before instructions for a more logical flow. This misplacement of the ingredients section affects the user experience by making the form less intuitive and harder to navigate. Admin users would have to scroll past the instructions to manage the ingredients, which goes against standard recipe form structures. To fix the issue, I customised the RecipeAdmin class by using the fieldsets attribute to reorder the fields. I created a new section for ingredients and ensured it appeared before the instructions. Additionally, I used RecipeIngredientInline to manage the ingredients directly within the recipe form. The issue was resolved, and the ingredients section now appears before the instructions in the recipe admin form, improving the form's organisation and user experience.

### Displaying Quantities in Decimal Instead of Readable Form
Quantities for certain ingredients, such as "half a teaspoon of salt" or "2 slices of bread," were displayed in a decimal format, for example, "0.5 teaspoon" or "2.0 slices," making the display less readable and less intuitive. This issue affected the user experience on the site by showing ingredient quantities in an unnatural or awkward format, which could confuse users or make the recipe appear less user-friendly. Instead of seeing familiar measurements like "1/2 teaspoon" or "2 slices," users saw numeric values such as "0.5" or "2.0," making it harder to understand at a glance. The issue was addressed by implementing a format_quantity() method in the RecipeIngredient model. This method converts decimal quantities to fractions when appropriate (e.g., 0.5 to 1/2) and formats whole numbers correctly. It ensures the quantities are displayed in a more readable form, such as "1/2 teaspoon" or "2 slices." The bug was resolved, and ingredient quantities are now displayed in a more readable and familiar format, improving the overall user experience on the site.

### Issue with Media Files Not Loading on Heroku
Media files uploaded through the Django app were not loading correctly after deploying to Heroku, resulting in 404 errors for images. The bug affected the site by preventing images from displaying, causing user-uploaded recipe images to fail loading when viewed in the browser. Since Heroku's file system is ephemeral, the media files were not accessible after the app was redeployed. To resolve the issue, I integrated Cloudinary for media storage. This involved installing the django-cloudinary-storage package, configuring Cloudinary settings in settings.py, and updating the ImageField in the model to use Cloudinary’s cloud storage. I also removed local media file handling for production. After deploying the changes, images were successfully uploaded and served through Cloudinary, solving the issue and ensuring the media files load correctly on Heroku.

### Inconsistent Instruction Formatting for Existing Recipes
Existing recipes with instructions entered as plain text were not being displayed as ordered lists. When users previously created recipes, the instructions were entered as plain text with steps on separate lines. These instructions were displayed as plain text on the recipe detail page, leading to a disorganized appearance. New recipes, however, were formatted correctly using an ordered list, resulting in inconsistent presentation across the site. A data migration was created to process all existing recipe instructions, check if they were in plain text, and then convert them into an ordered list (<ol>). The migration split the instructions based on common delimiters (like numbers or line breaks), formatted them as list items (<li>), and saved the updated instructions to the database. The migration was successfully applied, and all previously created recipes now display their instructions as properly formatted ordered lists, ensuring consistency across the site.

### Ingredients and Instructions Not Auto-Populating in Recipe Update Form
When updating a recipe, the ingredients and instructions fields do not auto-populate with the existing data. This prevents users from seeing and editing their previously added ingredients and instructions. The issue affects the recipe update page where users are unable to modify the ingredients and instructions after they’ve been saved. Instead, the fields appear empty, forcing users to re-enter all the information manually, even if it has already been provided. This leads to a poor user experience. The solution involved updating the RecipeUpdateView to pass the existing ingredients and instructions to the template. A get_context_data() method was added to fetch the related RecipeIngredient data, and the raw instructions were extracted for use in the text area. The ingredients were dynamically rendered in the form, and old ingredients were cleared before saving the new ones in form_valid(). The issue was successfully resolved. Ingredients and instructions now auto-populate in the update form, allowing users to easily modify existing recipes without re-entering all information. This improved the overall user experience on the site.

### Mixed Content Error on the Site
The site was experiencing a mixed content issue, where some resources (images, stylesheets, scripts) were being loaded over an insecure HTTP connection, despite the page being loaded over HTTPS. This caused security warnings and prevented certain resources from being loaded properly in browsers.  This issue affects the site by causing browsers to block or restrict the loading of HTTP resources, leading to incomplete page rendering and security vulnerabilities. Users may also see mixed content warnings in their browsers. To resolve this, a <meta> tag with the Content-Security-Policy header was added to the <head> section of the HTML template. The tag used the upgrade-insecure-requests directive to automatically upgrade all insecure HTTP requests to HTTPS. The issue was resolved successfully. All previously insecure HTTP requests are now automatically upgraded to HTTPS, ensuring that the site’s content loads securely without mixed content errors. This also eliminates the security warnings displayed in browsers.

### JavaScript Not Loading Due to Path Condition in base.html
The JavaScript file (script.js) was not loading on the recipe form page due to a conditional check on the URL path in base.html. The script was only included if the path contained the string 'recipe_form', which caused the script to be missing on the page, preventing certain interactive elements, like the "Add Ingredient" button, from functioning. This bug prevented the JavaScript required to dynamically add and remove ingredient rows from being loaded, causing the "Add Ingredient" button to not work. As a result, users were unable to interact with the ingredients table on the recipe creation/edit form. I removed the conditional check that limited the script loading to pages containing 'recipe_form'. This ensured that the JavaScript file is now loaded on all pages, regardless of the URL. After removing the conditional, the JavaScript file was loaded properly, and the issue was resolved. The "Add Ingredient" button is now functioning as expected, allowing users to dynamically add ingredient rows.

## Lighthouse Testing

I used Lighthouse to audit the performance and quality of this website on desktop and mobile.

### Home Page

![Lighthouse Testing - Home Page (Desktop) ](docs/lighthouse-home-desktop.png)
![Lighthouse Testing - Home Page (Mobile) ](docs/lighthouse-home-mobile.png)

### Recipe Page

![Lighthouse Testing - Recipe Page (Desktop) ](docs/lighthouse-recipe-desktop.png)
![Lighthouse Testing - Recipe Page (Mobile) ](docs/lighthouse-recipe-mobile.png)

### Search Page

![Lighthouse Testing - Search Page (Desktop) ](docs/lighthouse-search-desktop.png)
![Lighthouse Testing - Search Page (Mobile) ](docs/lighthouse-search-mobile.png)

### Create Recipe Page

![Lighthouse Testing - Create Recipe Page (Desktop) ](docs/lighthouse-create-desktop.png)
![Lighthouse Testing - Create Recipe Page (Mobile) ](docs/lighthouse-create-mobile.png)

### My Recipes Page

![Lighthouse Testing - My Recipes Page (Desktop) ](docs/lighthouse-my_recipe-desktop.png)
![Lighthouse Testing - My Recipes Page (Mobile) ](docs/lighthouse-my_recipe-mobile.png)

# Technologies Used

### Languages Used

- HTML/CSS
- JavaScript
- Python
- SQL

### Frameworks, Libraries & Tools

- Django with Django Allauth, SummerNote and Crispy Forms
- PostgreSQL Database
- Bootstrap
- Font Awesome
- Git/GitHub
- Heroku (deployment)
- Cloudinary
- Figma
- Canva

# Credits

## Code

- [Create a Recipe App in Django (CRUD functionality)](https://dev.to/domvacchiano/create-a-recipe-app-in-django-tutorial-5hh)
- [Django User Profile Guide](https://www.devhandbook.com/django/user-profile/)
- [Django Allauth User Profiles](https://www.codu.co/articles/easily-create-user-profiles-with-django-allauth-nsbnigtx)
- [Handle Unchecked Checkboxes in Forms](https://stackoverflow.com/questions/1809494/post-unchecked-html-checkboxes)
- [Django Search Tutorial](https://learndjango.com/tutorials/django-search-tutorial)
- [Fixing Mixed Content Issues](https://web.dev/articles/fixing-mixed-content?hl=en)

## Content

- Recipes created using ChatGPT

## Media

All photos used on the site are sourced from [Pexels](https://www.pexels.com/) and are free for commercial use with attribution where applicable:

- Photo by [Lisa](https://www.pexels.com/photo/person-holding-sandwich-1321942/) — Avocado toast
- Photo by [Diego Romero](https://www.pexels.com/photo/salad-with-bread-19087691/) — Chicken caesar salad
- Photo by [Jose Prada](https://www.pexels.com/photo/chocolate-fondant-with-ice-creams-20522414/) — Chocolate lava cake
- Photo by [Polina Tankilevitch](https://www.pexels.com/photo/fresh-sliced-vegetables-served-with-sauce-in-black-bowl-on-tray-3872351/) — Hummus and veggie sticks
- Photo by [ROMAN ODINTSOV](https://www.pexels.com/photo/close-up-of-ice-cream-with-a-mango-5060371/) — Mango sorbet
- Photo by [Alberta Studios](https://www.pexels.com/photo/meat-stout-with-lemon-9738981/) — Butter chicken
- Photo by [Karina Ustiuzhanina](https://www.pexels.com/photo/cooked-food-on-blue-ceramic-plate-13778610/) — Falafel wrap
- Photo by [Dana Tentis](https://www.pexels.com/photo/round-frying-pan-with-eggs-691077/) — Shakshuka
- Photo by [Angele J](https://www.pexels.com/photo/cooked-pasta-with-sliced-tomatoes-and-green-leafy-128408/) — Spaghetti bolognese
- Photo by [solod_sha](https://www.pexels.com/photo/pancakes-on-ceramic-plate-8605856/) — Classic pancakes

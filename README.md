# [ReelRatings](https://fork-and-flavours-72f7a7edee0f.herokuapp.com/)

![Fork & Flavours Responsiveness](docs\fork-and-flavours-responsiveness.png)

Fork & Flavour is a recipe manager website that allows authorised users to create, view, edit, and delete recipes. It features a clean, modern, and playful design, offering a seamless user experience with easy navigation and an interactive recipe management system.

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
  - [Accessibility Testing](#accessibility-testing)
  - [Code Validation](#code-validation)
  - [Bugs](#bugs)
  - [Lighthouse Testing](#lighthouse-testing)
- [Deployment](#deployment)
  - [Deployment (Heroku)](#deployment-heroku)
  - [Local Deployment](#local-deployment)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Design & Development Tools](#design--development-tools)
- [Credits](#credits)
  - [Code](#code)
  - [Research and Resources](#research-and-resources)
  - [Media](#media)
  - [Content](#content)


# User Experience (UX)

## Project Goals

- **Intuitive Navigation:** Ensure that users can easily navigate through the site with a clear, simple, and consistent menu and navigation options.
- **Mobile-Friendly Layout:** Provide a responsive design that works seamlessly across all devices, with a mobile-first approach.
- **Minimalist Aesthetic:** Keep the design clean, modern, and visually appealing by incorporating ample white space and an easy-to-read font pairing.
- **User-Centric Functionality:** Design the site with user goals in mind, ensuring that users can easily create, view, edit, and delete recipes without confusion or unnecessary steps.
- **Accessible Design:** Ensure that the website is fully accessible, with considerations for colour contrast, font readability, and screen reader compatibility.
**Engaging and Interactive Elements:** Implement interactive features like hover effects and checklist functionality for a more dynamic user experience.

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

![Fork & Flavours Colour Palette](docs\fork-and-flavours-palette.png)

### Typography

For a clean and modern user interface, the following fonts have been chosen:

- Heading Font: Montserrat — A bold, modern sans-serif font for headings and titles.
- Body Font: Open Sans — A clean, sans-serif font for body text, offering readability and balance

### Imagery
- Use of high-quality images to showcase recipes with a playful and vibrant aesthetic.
- Interactive elements and hover effects to engage users.

You can view the logo below:

![Fork & Flavours Logo](static\images\fork_and_flavour_logo.png)

### Wireframes

Homepage: The homepage features a clean layout with easy navigation to key areas, such as featured recipes and recipe categories.
Add Recipe Page: A form-based page where logged-in users can add new recipes, complete with ingredient checklists and preparation steps.
My Recipes Page: A page where users can view, edit, and delete their saved recipes.
Profile Page (Scrapped): Originally intended for user profile details, this page was discarded during development because it closely mirrored the functionality of the My Recipes page.

- [Home Page Wireframe - View](#)
- [Mobile Wireframe - View](#)
- [Recipe Creation Page Wireframe - View](#)

# Features
- Responsive design, optimized for all device sizes.
- Interactive recipe listings and details.
- Secure login and account management for registered users.
- Dynamic recipe creation with ingredient checklists and preparation steps.

# Database Schema

Fork & Flavour uses a relational database to store user accounts, recipes, ingredients, and categories. Below is the **Entity-Relationship Diagram (ERD)** representing the database structure:

![ERD Diagram](docs\fork-and-flavours-erd.png)

## Tables

### **User**
Stores user account details.

| Column       | Data Type  | Constraints           |
|--------------|------------|-----------------------|
| id           | integer    | Primary Key           |
| username     | varchar    | Unique, Not Null      |
| email        | varchar    | Unique, Not Null      |
| password     | varchar    | Not Null              |
| date_joined  | timestamp  | Default: current timestamp |

### **Recipe**
Stores recipe details, including the user who created it, its category, and instructions.

| Column        | Data Type  | Constraints                         |
|---------------|------------|-------------------------------------|
| id            | integer    | Primary Key                         |
| title         | varchar    | Not Null                            |
| slug          | slug       | Unique, Not Null                    |
| user          | integer    | Foreign Key → user.id               |
| category      | varchar    | Foreign Key → category.id           |
| description   | text       | Nullable                            |
| instructions  | text       | Not Null                            |
| image         | image      | Nullable                            |
| status        | integer    | Default: 1 (e.g., Published/Active) |
| created_at    | timestamp  | Default: current timestamp          |
| updated_at    | timestamp  | Default: current timestamp          |

### **Ingredient**
Stores ingredient details for recipes.

| Column        | Data Type  | Constraints           |
|---------------|------------|-----------------------|
| id            | integer    | Primary Key           |
| name          | varchar    | Not Null              |

### **RecipeIngredient**
Links recipes to their ingredients, with quantities and measurement units.

| Column         | Data Type  | Constraints                              |
|----------------|------------|------------------------------------------|
| id             | integer    | Primary Key                              |
| recipe         | integer    | Foreign Key → recipe.id                  |
| ingredient     | integer    | Foreign Key → ingredient.id              |
| quantity       | decimal    | Not Null                                 |
| unit           | varchar    | Nullable                                 |
| is_optional    | boolean    | Default: false                           |

### **Category**
Stores recipe categories (e.g., "Appetizer", "Dessert").

| Column        | Data Type  | Constraints           |
|---------------|------------|-----------------------|
| id            | integer    | Primary Key           |
| name          | varchar    | Unique, Not Null      |

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
- The color scheme adheres to WCAG (Web Content Accessibility Guidelines) standards, with sufficient contrast between text and background colors to improve readability for users with visual impairments. Specifically, the primary color palette of **cal poly green**, **engineering orange**, and **chocolate cosmos** ensures strong contrast across the site.
- The **Accessible Color Palette Builder** tool was used to ensure that the color choices meet WCAG guidelines for contrast, making the site more accessible to users with color blindness or low vision.

![Accessible Colour Combinations for Fork & Flavours](#)

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

###  **ARIA (Accessible Rich Internet Applications)**
- ARIA roles and properties are used where necessary to enhance the accessibility of dynamic content (e.g., recipe creation forms) and complex user interactions (e.g., modal pop-ups or dropdowns).

By implementing these features, Fork & Flavour strives to provide an inclusive and accessible experience for all users, regardless of their abilities or disabilities.

# Manual Testing

## Features Testing



## User Stories Testing



## Browser Compatibility



## Responsiveness Testing



## Accessibility Testing



## Code Validation


## Bugs


## Lighthouse Testing


# Deployment

## Deployment (Heroku)

1. Clone this repository.
2. Run `pip install -r requirements.txt` to install dependencies.
3. Set up the necessary environment variables (e.g., secret key, database URL).
4. Deploy the project on [Heroku](https://www.heroku.com/).

## Local Deployment

1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the database: `python manage.py migrate`
4. Run the development server: `python manage.py runserver`

Visit `http://127.0.0.1:8000` in your browser to view the project locally.

# Technologies Used

### Languages Used
- HTML
- CSS
- JavaScript
- Python
- SQL

### Frameworks, Libraries & Tools
- **Django**: Backend framework to manage data and user authentication.
- **Django Allauth**: User authentication for login and account management.
- **Open Food Facts API**: To fill the ingredient model with nutritional and ingredient data.
- **Bootstrap 4**: For responsive grid layout and components.
- **Font Awesome**: For icons and aesthetic elements.
- **jQuery**: For smooth scroll and other interactive features.
- **Git**: Version control for project management.
- **GitHub**: To store the project's code and manage versions.
- Heroku

## Credits

### Code

### Content

### Media

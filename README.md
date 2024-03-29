![Apex Estates Logo](docs/logo/logo-no-background.png)

# Apex Estates

![Site Image](docs/screenshots/site-image.png)

Apex Estates is tailored for those in pursuit of luxury living in London, providing a curated selection of homes with personalized features for an unparalleled experience.

Live site: [Apex Estates](https://apex-estates-49762cd93db3.herokuapp.com/)

## Contents

[Planning](#planning)

- [The Strategy Plane](#the-strategy-plane)

- [The Scope Plane](#the-scope-plane)

- [The Structure Plane](#the-structure-plane)

- [The Skeleton Plane](#the-skeleton-plane)

- [The Surface Plane](#the-surface-plane)

[Features](#features)

- [Current Features](#current-features)

- [Future Features](#future-features)

[Languages](#languages)

[Frameworks and Libraries](#frameworks-and-libraries)

[Tools Used](#tools-used)

[Testing](#testing)

[Bugs & Fixes](#bugs--fixes)

[Deployment, Cloning and Forking](#deployment-cloning-and-forking)

[Credits](#credits)


## Planning

### The Strategy Plane

#### Product Description:

- Apex Estates is a distinguished online platform serving as an extension of a premier estate agency specializing in luxury housing in London.

- The website acts as an upscale estate agent platform, presenting a curated collection of high-end residences for potential buyers.

- Users can seamlessly explore luxury property listings, save preferred listings, request validations, and engage in a sophisticated online experience tailored for property transactions.

#### Target Audence:

- The primary audience for Apex Estates consists of individuals interested in buying luxury properties in London.

- The platform caters to a diverse clientele, including professionals, young families, and those seeking upscale residences with the dedicated support of a reputable estate agency.

#### Problem Statement:

In the competitive landscape of the London luxury real estate market, potential property buyers and renters face challenges in finding a platform that offers a diverse selection of upscale residences while maintaining a personalized and inclusive approach. Existing options may lack inclusivity and may not adequately cater to the varying preferences and budgets of individuals seeking luxury living spaces. Additionally, there is a need for a trustworthy estate agency platform that provides expert guidance and validation services to instill confidence in the legitimacy of listed properties.

#### Project Aim:

The primary aim of the Apex Estates project is to address the challenges in the London luxury real estate market by creating an online estate agency platform focused on facilitating the purchase of high-end residences. The platform will provide an inclusive and welcoming experience for a diverse range of clients, including professionals, young families, and individuals seeking to buy upscale living spaces. By curating a varied selection of premium properties and offering personalized consultations, the project aims to become the preferred destination for those looking to purchase luxury homes. Through this, Apex Estates seeks to redefine the standards of service in the upscale property market, fostering trust and satisfaction among clients seeking to make a significant investment in the London real estate scene.

### The Scope Plane

When crafting our site, we meticulously detail user stories and prioritize the development of essential components using the MoSCoW method. Guided by this approach, we carefully design every aspect with users in mind, ensuring that each feature serves a distinct purpose and enriches the overall user experience. Our focus on must-have and should-have requirements forms the foundation of our development strategy, allowing us to align seamlessly with the vision of Apex Estates. Through organized sprints and thoughtfully crafted epics, we are dedicated to creating a dynamic and user-centric online environment that sets the standard for luxury real estate exploration in London.

#### Sprint 1: Foundational Functionality
<details>
<summary>Epic 1: User Authentication</summary>

| User Story # | Title                   | Story (Content)                                                    | MoSCoW     | Story Points |
|--------------|-------------------------|--------------------------------------------------------------------|------------|--------------|
| 2            | User Registration       | As a New User I can Register an Account so that I can Login to the site | Must Have | 3            |
| 3            | User Login              | As a Registered User I can Login using my email and password so that access the site securely using my account | Must Have | 2            |
| 4            | User Logout             | As a Logged In User I can Logout so that I can keep my account secure. | Must Have | 1            |
</details>

<details>
<summary>Epic 2: User Navigation</summary>

| User Story # | Title                   | Story (Content)                                                    | MoSCoW     | Story Points |
|--------------|-------------------------|--------------------------------------------------------------------|------------|--------------|
| 26           | Navbar                  | As a Site User I can expect a navbar so that I can easily and intuitively navigate round the site | Must Have | 3            |
| 27           | Footer                  | As a User I can expect a footer so that I can access important information and links regardless of my position on the webpage. | Must Have | 2            |

</details>

#### Sprint 2: Property App
<details>
<summary>Epic 3: Property Management</summary>

| User Story # | Title                   | Story (Content)                                                    | MoSCoW     | Story Points |
|--------------|-------------------------|--------------------------------------------------------------------|------------|--------------|
| 5            | Agent Status            | As a Sales Agent I can have the agent status so that I have full CRUD access over properties and can view/delete messages and valuations | Must Have | 5            |
| 6            | Create Properties       | As a Sales Agent I can Create property listings so that we can display current property listings | Must Have | 8            |
| 7            | Update Properties       | As a Sales Agent I can Update property listings so that I can change / keep listings up to date | Must Have | 5            |
| 8            | Remove Properties       | As a Sales Agent I can Remove/Delete properties so that I can keep the site up to date with current sales. | Must Have | 3            |
</details>

<details>
<summary>Epic 4: Property Display</summary>

| User Story # | Title                   | Story (Content)                                                    | MoSCoW     | Story Points |
|--------------|-------------------------|--------------------------------------------------------------------|------------|--------------|
| 1            | View Paginated Property Lists | As a User I can see a paginated list of properties for sale so that I can select which one I would like to look at. | Must Have | 3            |
| 9            | Read Property Listings  | As a Site User I can Read property listings so that I can explore current property listings | Must Have | 2            |

</details>

#### Sprint 3: User Experience
<details>
<summary>Epic 5: User Experience</summary>

| User Story # | Title                   | Story (Content)                                                    | MoSCoW     | Story Points |
|--------------|-------------------------|--------------------------------------------------------------------|------------|--------------|
| 18           | Landing Page            | As a Site User I can access the landing/home page so that I can navigate to other parts of the site | Must Have | 3            |
| 16           | About Us Page           | As a Site User I can access an about us page so that I can learn more about the company | Must Have | 2            |
| 17           | Contact Us Page         | As a Site User I can Access a Contact us page so that I can find out ways to get in contact, send a message or find the location of the office | Must Have | 2            |
| 10           | Favourite Properties    | As a User I can favourite properties so that I can easily return to my favourite property listings | Should Have | 3            |
| 11           | User Dashboard          | As a Signed-In User I can Display my personal dashboard so that I can display my favourite properties | Should Have | 5            |

</details>

#### Sprint 4: Additional Functionality & Product Refinement
<details>
<summary>Epic 6: Additional User Functionality</summary>

| User Story # | Title                   | Story (Content)                                                    | MoSCoW     | Story Points |
|--------------|-------------------------|--------------------------------------------------------------------|------------|--------------|
| 25           | Agent Admin Dashboard   | As a Agent I can Display a admin dashboard so that I can read through user messages and valuation request and delete them once actioned | Should Have | 5            |
| 13           | Valuation Request       | As a Potential Seller I can Request a Valuation so that I can have my property valued | Should Have | 3            |
| 19           | Apply to Newsletter     | As a Site User I can Apply to the newsletter so that I can keep up to date with Apex Estates latest news | Could Have | 2          |
| 22           | User Messages           | As a Site User I can send agents a message so that I can receive personalised assistance with my enquiries | Could Have | 3          |

</details>

#### Not Included in This Release


For further details regarding this section, please refer to the [Future Features](#future-features) section for additional information and insights.

<details>
<summary>Not Included User Stories</summary>

| User Story # | Title                   | Story (Content)                                                    | 
|--------------|-------------------------|--------------------------------------------------------------------|
| 12           | Password Reset          | As a User I can Reset my password so that I can access my account if I have forgotten it or my password is no longer secure |
| 14           | Property Search         | As a Site User I can Search Properties so that find what I am looking for. |
| 15           | Property Filter         | As a Site User I can filter property listings so that a number of different properties based on my filters |
| 20           | Write Newsletter        | As a Agent I can Write a newsletter so that I can keep subscribed users up-to-date with the latest news |
| 21           | Live Text Chat          | As a Signed In User I can have a live chat so that I can talk to an agent via text chat live |
| 23           | Interactive Property Listing Map | As a User I can use an interactive map so that I can better understand the location of properties and search by using a map |
| 24           | Image Gallery for property listings | As a User I can navigate through a selection of images so that I can better understand the property im looking at |
| 28           | Change Email            | As a Authenticated User I can change my email so that I can keep my account information up-to-date. |
| 29           | For Sale, Sold, Unpublished Listings | As a Agent I can set the state of a listing so that I can users informed about the availability and status of properties. |
</details>


<br>

By following this approach, we ensure that our development efforts are organized, focused, and aligned with the core objectives of Apex Estates. Each sprint builds upon the previous one, incrementally enhancing the platform's functionality and delivering tangible value to our users.

### The Structure Plane

#### Site Map

This diagram provides a structured overview of our platform's architecture and user navigation. Created using [Lucidchart](https://www.lucidchart.com/), it serves as a clear visualization of the pathways and interactions within the system.

Each element within the diagram is positioned to depict the flow of information and user movement.

![Apex Estates Site Map Diagram](docs/diagrams/lucid-chart-site-diagram.png)

---
#### Database Plan

This diagram offers a comprehensive overview of our database structure, crafted using [DrawSQL](https://drawsql.app/). It provides a visual representation of the relationships between various entities and the flow of data within our system.

We've opted for PostgreSQL as our database solution due to its robust features, reliability, and cost-effectiveness as an open-source relational database system. To facilitate our hosting needs, we've selected ElephantSQL, a trusted platform known for its seamless PostgreSQL hosting services. This strategic choice ensures that our database management is efficient, secure, and scalable, aligning perfectly with our business objectives.

![Apex Estates Database Diagram](docs/diagrams/database-diagram.png)

### The Skeleton Plane

#### Wireframes

We created wireframes for desktop, tablet, and mobile views to provide a visual representation of our website's layout and design across different devices. Wireframes serve as a blueprint for our site's structure, illustrating the placement of elements, navigation flow, and overall user interface design. By creating wireframes, we can effectively communicate our design concepts and collaborate with stakeholders to gather feedback and make informed decisions before moving into the development phase.

We utilized [Uizard](https://uizard.io/), an innovative wireframing tool, to streamline the wireframing process and accelerate our design iteration cycles. [Uizard's](https://uizard.io/) intuitive interface enable us to quickly translate our ideas into tangible wireframes, saving time and effort in the design phase. With [Uizard](https://uizard.io/), we can easily experiment with different layouts, iterate on design variations, and visualize how our website will look and function across various devices.



Landing / Home Page

<details>
<summary>
Desktop
</summary>

![Desktop Landing Page Wireframes](docs/wireframes/desktop/landing-page.png)
</details>
<details>
<summary>
Tablet
</summary>
 
![Tablet Landing Page Wireframes](docs/wireframes/tablet/landing-page-tablet.png)
</details>
<details>
<summary>
Mobile
</summary>

![Mobile Landing Page Wireframes](docs/wireframes/mobile/landing-page-mobile.png)
</details>

<br>

Property Listings Page

<details>
<summary>
Desktop
</summary>

![Desktop Property Lisitings Wireframes](docs/wireframes/desktop/property-listings-page.png)
</details>
<details>
<summary>
Tablet
</summary>
 
![Tablet Property Lisitings Wireframes](docs/wireframes/tablet/property-listings-page-tablet.png)
</details>
<details>
<summary>
Mobile
</summary>

![Mobile Property Lisitings Wireframes](docs/wireframes/mobile/property-listings-page-mobile.png)
</details>

<br>

Property Detail Page

<details>
<summary>
Desktop
</summary>

![Desktop Property Detail Wireframes](docs/wireframes/desktop/property-detail.png)
</details>
<details>
<summary>
Tablet
</summary>
 
![Tablet Landing Page Wireframes](docs/wireframes/tablet/property-detail-page-tablet.png)
</details>
<details>
<summary>
Mobile
</summary>

![Mobile Landing Page Wireframes](docs/wireframes/mobile/property-detail-mobile.png)
</details>

<br>

About Us Page

<details>
<summary>
Desktop
</summary>

![Desktop About Us Page Wireframes](docs/wireframes/desktop/about-us-page.png)
</details>
<details>
<summary>
Tablet
</summary>

![Tablet About Us Page Wireframes](docs/wireframes/tablet/about-us-page-tablet.png)
</details>
<details>
<summary>
Mobile
</summary>

![Mobile About Us Page Wireframes](docs/wireframes/mobile/about-us-page-mobile.png)
</details>

<br>
Contact Us Page

<details>
<summary>
Desktop
</summary>

![Desktop Contact Us Page Wireframes](docs/wireframes/desktop/contact-us-page.png)
</details>
<details>
<summary>
Tablet
</summary>

![Tablet Contact Us Page Wireframes](docs/wireframes/tablet/contact-us-page-tablet.png)
</details>
<details>
<summary>
Mobile
</summary>

![Mobile Contact Us Page Wireframes](docs/wireframes/mobile/request-valutaion-page-mobile.png)
</details>

<br>
Request Valuation Page

<details>
<summary>
Desktop
</summary>

![Desktop Request Valuation Page Wireframes](docs/wireframes/desktop/request-valuation-page.png)
</details>
<details>
<summary>
Tablet
</summary>

![Tablet Request Valuation Page Wireframes](docs/wireframes/tablet/request-valuation-page-tablet.png)
</details>
<details>
<summary>
Mobile
</summary>

![Mobile Request Valuation Page Wireframes](docs/wireframes/mobile/request-valutaion-page-mobile.png)
</details>

<br>
Login Page

<details>
<summary>
Desktop
</summary>

![Desktop Login Page Wireframes](docs/wireframes/desktop/log-in-page.png)
</details>
<details>
<summary>
Tablet
</summary>

![Tablet Login Page Wireframes](docs/wireframes/tablet/log-in-page-tablet.png)
</details>
<details>
<summary>
Mobile
</summary>

![Mobile Login Page Wireframes](docs/wireframes/mobile/log-in-page-mobile.png)
</details>

<br>
Register Page

<details>
<summary>
Desktop
</summary>

![Desktop Register Page Wireframes](docs/wireframes/desktop/register-page.png)
</details>
<details>
<summary>
Tablet
</summary>

![Tablet Register Page Wireframes](docs/wireframes/tablet/register-page-tablet.png)
</details>
<details>
<summary>
Mobile
</summary>

![Mobile Register Page Wireframes](docs/wireframes/mobile/register-page-mobile.png)
</details>

<br>
Dashboard Page

<details>
<summary>
Desktop
</summary>

![Desktop Dashboard Page Wireframes](docs/wireframes/desktop/dashboard.png)
</details>
<details>
<summary>
Tablet
</summary>

![Tablet Dashboard Page Wireframes](docs/wireframes/tablet/dashboard-tablet.png)
</details>
<details>
<summary>
Mobile
</summary>

![Mobile Dashboard Page Wireframes](docs/wireframes/mobile/dashboard-mobile.png)
</details>

<br>
Admin Dashboard

<details>
<summary>
Desktop
</summary>

![Desktop Admin Dashboard Page Wireframes](docs/wireframes/desktop/admin-dashboard.png)
</details>


### The Surface Plane

**Colour Scheme**

In the color scheme section of our skeleton plane, we've carefully selected a palette that reflects our design goals and enhances the overall user experience. We've opted for a clean and minimalist approach, with a main background color of white (#ffffff) to provide a spacious and uncluttered feel to our website. To ensure readability and contrast, we're using black (#000000) for text elements, providing a sharp and easily distinguishable appearance against the white background.

For navigation and footer elements, we've chosen a dark gray shade (#282928) to create a subtle yet distinct separation from the main content area. This color adds depth and visual hierarchy to our design, guiding users' attention to important navigation links and footer information.

To draw attention to key actions and encourage user engagement, we're incorporating an eye-catching orange hue (#F5793A) for call-to-action items. This vibrant color adds warmth and energy to our design, effectively highlighting important buttons and prompts throughout the website.

Finally, to introduce subtle variation and soften the overall look, we're introducing an off-white shade (#E0E0DB) as a contrast to the pure white background. This color adds depth and dimension to our design, creating visual interest without overwhelming the user interface.

![Colormind.io Screenshot](docs/colour-scheme/colormind-screenshot.png)

Overall, our carefully curated color scheme aims to create a harmonious and visually appealing experience for our users, balancing contrast, readability, and engagement throughout the website.


In order to ensure that our chosen color scheme meets accessibility standards and provides optimal readability for all users, we employed a contrast grid from [eightshapes](https://contrast-grid.eightshapes.com/) to evaluate the contrast ratios between text and background colors. This grid allows us to assess the color combinations used throughout the website and verify that they adhere to accessibility guidelines.

![Contrast Grid Screenshot](docs/colour-scheme/contrast-grid-screenshot.png)

The contrast grid provides a systematic approach to evaluating color combinations, helping us to create a design that is inclusive and accessible to all users, including those with visual impairments or disabilities.

**Typography**


In crafting our website's visual identity, we've carefully curated typography to ensure optimal readability and aesthetic appeal. Our choice of Montserrat for headings exudes a sense of modernity and sophistication, with its sleek lines and bold presence commanding attention. This typeface adds a touch of elegance to our headers, making them stand out while maintaining readability across different devices and screen sizes.

Complementing Montserrat, we've selected Lato for body text, known for its versatility and legibility. Lato's clean and rounded letterforms provide a comfortable reading experience, enhancing comprehension and engagement with our content. Whether users are browsing lengthy descriptions or informative articles, Lato ensures clarity and ease of reading, contributing to a seamless user experience.

[Return to contents](#contents)

## Features

### Current Features

#### Navbar

Our navigation bar is meticulously crafted to enhance user experience at every turn. It gracefully combines aesthetic appeal with practical functionality, featuring transparency on the homepage for a captivating touch against the hero image, while adopting a sleek dark grey color scheme on other pages to maintain consistency. Catering to different user roles, it offers tailored navigation options, ensuring seamless access to relevant features and information based on individual needs and preferences.

<details>
<summary>Navbar Screenshots</summary>

##### Navbar Homepage

![Nav Bar Homepage](docs/screenshots/navbar/nav-bar-home.png)

##### Navbar Homepage User Logged In

![Nav Bar Homepage User Logged In](docs/screenshots/navbar/nav-bar-home-user.png)

##### Navbar Homepage Admin Logged In

![Nav Bar Homepage Admin Logged In](docs/screenshots/navbar/nav-bar-home-admin.png)

##### Navbar all other pages User Logged In

![Nav Bar All Pages other than Homepage](docs/screenshots/navbar/nav-bar-grey.png)

##### Navbar Collapsed

![Nav Bar Collapsed](docs/screenshots/navbar/nav-bar-collapsed.png)

##### Navbar Offcanvas

![Nav Bar Offcanvas](docs/screenshots/navbar/nav-bar-offcanvas.png)

##### Navbar Offcanvas User Logged In

![Nav Bar Offcanvas User Logged In](docs/screenshots/navbar/nav-bar-offcanvas-user.png)

##### Navbar Offcanvas Admin Logged In

![Nav Bar Offcanvas Admin Logged In](docs/screenshots/navbar/nav-bar-offcanvas-admin.png)

</details>

---

#### Footer

Our footer is a comprehensive hub of essential information and connectivity, featuring:

Features:

- **Contact section:** Providing our address, email, and phone number.

- **Opening hours:** Offering clarity on our service availability.

- **Links section:** Curated resources for seamless navigation.

- **Social media links:** Allowing user to connect with us across different sites.

- **Copyright and educational disclaimer.**

<details>
<summary>Footer Screenshots</summary>

##### Footer Desktop

![Footer Desktop](docs/screenshots/footer/footer-desktop.png)

##### Footer Tablet

![Footer Tablet](docs/screenshots/footer/footer-tablet.png)

##### Footer Mobile

![Footer Mobile](docs/screenshots/footer/footer-mobile.png)

</details>

---

#### Landing Page

The landing page serves as the initial point of entry for users visiting our site. It features several design elements that reflect the premium nature of our platform. Our hero image, showcasing an orange sunset over the London skyline, was selected for its incorporation of our site's colors, which are echoed in our call-to-action buttons throughout the site.

As users scroll down the page, they encounter the 'Latest Properties' section, displaying the four most recently listed properties. Users can click on these cards to access more details or even add them to their favorites if they're logged in. Below this, we present another call-to-action prompting users to explore our listings page, as this is the primary function of our site.

We also encourage users who own properties to consider requesting a free valuation through our platform. Additionally, we feature a review of our company, followed by a signup form for our newsletter, providing users with the opportunity to stay updated on the latest developments and offerings.

Features:

- **Premium design elements:** Hero image featuring an orange sunset over the London skyline, echoing site colors.

- **Latest Properties section:** Displaying four newest listings with clickable cards for easy access.

- **Call-to-action for Listings page:** Directing users to explore our primary site function.

- **Free valuation prompt:** Encouraging property owners to request a valuation through our platform.

- **Company review:** Providing users with insight into our company's reputation and credibility.

- **Newsletter signup form:** Allowing users to stay updated on the latest developments and offerings.

<details>
<summary>Landing Page Screenshots</summary>

##### Landing Page Desktop

![Landing Page Desktop](docs/screenshots/landing-page/landing-page.png)

##### Landing Page Tablet

![Landing Page Tablet](docs/screenshots/landing-page/landing-page-tablet.png)

##### Landing Page Mobile

![Landing Page Mobile](docs/screenshots/landing-page/landing-page-mobile.png)

</details>

---

#### Property Listings

The Property Listings page stands as the cornerstone of our platform, fulfilling our core mission of providing users with an extensive array of properties available for sale. With a user-centric design featuring eight listings per page, our interface ensures clarity and ease of navigation. Pagination buttons are intelligently integrated to appear only when needed, streamlining the browsing experience. For logged-in users, the option to favorite properties directly from the listings page enhances interaction and facilitates efficient organization of preferences. Additionally, agents and administrators can seamlessly add new property listings, ensuring our database remains up-to-date with the latest offerings.

Features:

- **Comprehensive Listings:** Each page presents users with eight meticulously curated property listings or cards, offering a rich selection while maintaining clarity and ease of navigation.

- **Pagination:** Navigation is optimized through an intuitive pagination system. Pagination buttons dynamically appear only when necessary, ensuring a fluid browsing experience without unnecessary clutter.

- **User Interaction:** Logged-in users benefit from seamless interaction by favoriting properties directly from the listings page. This feature simplifies the process of saving and organizing preferred properties for future reference.

- **Agent/Admin Privileges:** Agents and administrators enjoy the convenience of adding new property listings directly from this centralized hub. This capability ensures our listings remain up-to-date and reflective of the latest offerings in the market.

<details>
<summary>Property Listings Screenshots</summary>

##### Property Listings Desktop

![Property Listings Page Desktop](docs/screenshots/property-listings/property-listings-page.png)

##### Property Listings Desktop User Logged In

![Property Listings Page Desktop User Logged In](docs/screenshots/property-listings/property-listings-page-user.png)

##### Property Listings Desktop Admin Logged In

![Property Listings Page Desktop Admin Logged In](docs/screenshots/property-listings/property-listings-page-admin.png)

##### Property Listings Desktop Admin Logged In

![Property Listings Page Tablet](docs/screenshots/property-listings/property-listings-page-tablet.png)

##### Property Listings Desktop Admin Logged In

![Property Listings Page Mobile](docs/screenshots/property-listings/property-listings-page-mobile.png)

</details>

---

#### Property Details

The Property Detail Page offers users a deeper exploration of their selected property, accessed by interacting with any property card across the site. Upon arrival, users are greeted with a comprehensive overview, including a larger feature image capturing the essence of the property, along with essential details such as price, listed date, and property type. Additionally, users can conveniently favorite the property for future reference. A concise summary provides key information, including the property's type, number of bedrooms and bathrooms, and whether it offers parking or a garage. Further details are provided in the description section, styled using Summernote, offering a rich and engaging narrative that paints a vivid picture of the property's unique features and attributes. If the user is an admin or an agent, they are able to edit or delete the relevant property listing. If the agent or admin selects delete, it will prompt for confirmation to ensure they are sure they want to delete the property.

**Features:**

- **Detailed Overview:** Presents users with a comprehensive look at their chosen property, featuring a larger feature image, price, listed date, and property type.
  
- **Convenient Interaction:** Users can easily favorite the property directly from the page for future reference.
  
- **Concise Summary:** Highlights essential information including property type, bedroom and bathroom count, and parking/garage availability.
  
- **Styled Description:** Utilizes Summernote to present a richly styled description, enhancing the narrative and showcasing the property's unique features and attributes.
  
- **Admin/Agent Functionality:** Provides admins and agents with convenient access to edit and delete property listings directly from this page, ensuring efficient management and updates.

<details>
<summary>Property Details Screenshots</summary>

##### Property Details Page Desktop

![Property Details Page Desktop](docs/screenshots/property-details/property-details.png)

##### Property Details Page Desktop User Logged In

![Property Details Page Desktop User Logged In](docs/screenshots/property-details/property-details-user.png)

##### Property Details Page Desktop Admin Logged In

![Property Details Page Desktop Admin Logged In](docs/screenshots/property-details/property-details-admin.png)

##### Property Details Page Desktop Deletion Example

![Property Details Page Desktop Deletion Example](docs/screenshots/property-details/property-details-deletion.png)

##### Property Details Page Tablet

![Property Details Page Tablet](docs/screenshots/property-details/property-details-tablet.png)

##### Property Details Page Mobile

![Property Details Page Mobile](docs/screenshots/property-details/property-details-mobile.png)

</details>

---

#### Create Property Listing Page

The Create Property page is accessible only to admins and agents. This feature allows these users to create a listing in the database directly from the front end. Once the listing is created and submitted, the information is immediately uploaded to the database. Consequently, the new listing becomes visible on the user's listings page, ensuring that the property is available for viewing by potential buyers without delay.

- **Exclusive Access:** Limited to admins and agents, providing them with the ability to create property listings.

- **Seamless Integration:** Enables users to input property details directly on the front end, with immediate upload to the database upon submission.

- **Image Upload:** Integration with Cloudinary allows users to upload property images easily, enhancing listing visual appeal and attractiveness.

- **Rich Description:** Utilizes Summernote for the property description field, enabling users to format and style descriptions with ease.

<details>
<summary>Create Property Listings Screenshots</summary>

##### Create Property Listing Desktop

![Create Property Listing Desktop](docs/screenshots/create-property/create-property-listing.png)

##### Create Property Listing Tablet

![Create Property Listing Tablet](docs/screenshots/create-property/create-property-listing-tablet.png)

##### Create Property Listing Mobile

![Create Property Listing Mobile](docs/screenshots/create-property/create-property-listing-mobile.png)

</details>

---

#### Edit Property Listing Page

The Edit Property Listing feature empowers admins and agents with exclusive access to efficiently manage property listings directly from the front end. Leveraging this functionality, users can seamlessly modify property details, ensuring accuracy and relevance in real-time. With the convenience of front-end editing, updates to property information are promptly reflected in the database, guaranteeing consistency across all platforms. Integrated with Cloudinary, users can effortlessly change the featured image, enhancing the visual appeal of listings. Additionally, the use of Summernote for description editing facilitates the creation of rich, formatted property descriptions, enabling agents to showcase the unique features and attributes of each listing effectively.

Features:

- **Admin/Agent Privilege:** Reserved for admins and agents, granting them exclusive access to edit property listings.

- **Front-End Editing:** Allows users to modify property details directly on the front end, facilitating convenient updates.

- **Seamless Database Integration:** Changes made to property listings are immediately reflected in the database upon submission.

- **Enhanced Functionality:** Provides flexibility for admins and agents to manage property listings efficiently, ensuring accuracy and relevance.

<details>
<summary>Edit Property Listings Screenshots</summary>

##### Edit Property Listing Desktop

![Edit Property Listing Desktop](docs/screenshots/edit-property/edit-property.png)

##### Edit Property Listing Tablet

![Edit Property Listing Tablet](docs/screenshots/edit-property/edit-property-tablet.png)

##### Edit Property Listing Mobile

![Edit Property Listing Mobile](docs/screenshots/edit-property/edit-property-mobile.png)

</details>

---

#### About Us

The About Us page provides insight into Apex Estates and its dedicated team of professionals. Here, visitors can learn about our company's mission, values, and commitment to excellence in the real estate industry.

<details>
<summary>About Us Page Screenshots</summary>

##### About Us Page Desktop

![About Us Page Desktop](docs/screenshots/about-us/about-us.png)

##### About Us Page Tablet

![About Us Page Tablet](docs/screenshots/about-us/about-us-tablet.png)

##### About Us Page Mobile

![About Us Page Mobile](docs/screenshots/about-us/about-us-mobile.png)

</details>

---

#### Contact Us

The Contact Us page serves as a hub for users to connect with Apex Estates through various channels. At the top of the page, visitors will find essential contact information, including email, phone number, address, and links to our social media profiles. Additionally, a Google Map integration provides users with a visual representation of our location. Below this section or to the side depending on screen size is a "Send Us a Message" form, which offers a convenient way for users to reach out to us directly. The form prompts users to provide their first name, last name, email address, and message, enabling seamless communication between our team and our clients. We strive to make it easy for users to get in touch with us, whether they have inquiries, feedback, or are interested in our services.

Features:

- **Comprehensive Contact Information:** Provides users with essential contact details, including email, phone number, address, and social media links, ensuring multiple channels for communication.

- **Interactive Google Map Integration:** Offers users a visual representation of our location, enhancing accessibility and providing easy navigation.

- **User-Friendly Message Form:** Enables users to send messages directly to Apex Estates by filling out a simple form with their first name, last name, email address, and message, facilitating efficient communication.

<details>

<summary>Contact Us Page Screenshots</summary>

##### Contact Us Page Desktop

![Contact Us Page Desktop](docs/screenshots/contact-us/contact-us.png)

##### Contact Us Page Tablet

![Contact Us Page Tablet](docs/screenshots/contact-us/contact-us-tablet.png)

##### Contact Us Page Mobile

![Contact Us Page Mobile](docs/screenshots/contact-us/contact-us-mobile.png)

</details>

---

#### Request Valuation

Our request valuation page features a simple form where users can input their name, contact number, property address, and email, along with the option to select their property type before submitting their information for valuation by an agent.

<details>

<summary>Request Valuation Page Screenshots</summary>

##### Request Valutation Page Desktop

![Request Valutation Page Desktop](docs/screenshots/request-valutation/request-valuation-desktop.png)

##### Request Valutation Page Tablet

![Request Valutation Page Tablet](docs/screenshots/request-valutation/request-valuation-tablet.png)

##### Request Valuation Page Mobile

![Request Valutation Page Mobile](docs/screenshots/request-valutation/request-valuation-mobile.png)

</details>

---

#### Login

Our login page, powered by Django's built-in authentication system, offers a seamless login experience with fields for username and password, including a link if the user does not yet have an account to sign up.

<details>

<summary>Login Page Screenshots</summary>

##### Login Page Desktop

![Login Page Desktop](docs/screenshots/login/login-page.png)

##### Login Page Tablet

![Login Page Tablet](docs/screenshots/login/login-page-tablet.png)

##### Login Page Mobile

![Login Page Mobile](docs/screenshots/login/login-page-mobile.png)

</details>

---

#### Register

Our register page offers a comprehensive registration process, featuring fields for first name, last name, email, and password with checks for password strength. Users can confidently create their accounts and proceed to registration with ease, while those with existing accounts can conveniently access the login page via a provided link.

<details>

<summary>Register Page Screenshots</summary>

##### Register Page Desktop

![Register Page Desktop](docs/screenshots/register/register-page.png)

##### Register Page Tablet

![Register Page Tablet](docs/screenshots/register/register-page-tablet.png)

##### Register Page Mobile

![Register Page Mobile](docs/screenshots/register/register-page-mobile.png)

</details>

---

#### User Dashboard

Our user dashboard provides a seamless experience for users to access and manage their favorited properties. With an organized pagination system, users can effortlessly navigate through their favorite listings, with each page showcasing up to 4 property cards, ensuring a user-friendly experience

<details>

<summary>User Dashboard Screenshots</summary>

##### User Dashboard Desktop

![User Dashboard Desktop](docs/screenshots/dashboard/dashboard.png)

##### User Dashboard Tablet

![User Dashboard Tablet](docs/screenshots/dashboard/dashboard-tablet.png)

##### User Dashboard Mobile

![User Dashboard Mobile](docs/screenshots/dashboard/dashboard-mobile.png)

</details>

---

#### Admin Dashboard

#### User Dashboard

Our admin dashboard is meticulously crafted for agents, equipping them with the tools to efficiently review and manage user messages and valuations. Embracing a responsive design philosophy, our dashboard dynamically adjusts its layout to accommodate smaller screens, enabling agents to stay informed and productive whether they're in the office or on the move.

Features

- Responsive table design ensures usability across all device sizes.

- Read and delete functionalities enable agents to manage user messages and valuation requests efficiently.

- Agents can conveniently favorite properties for easy tracking and reference.

<details>

<summary>Admin Dashboard Screenshots</summary>

##### User Dashboard Desktop

![Admin Dashboard Desktop](docs/screenshots/admin-dashboard/admin-dashboard.png)

![Admin Dashboard Tablet](docs/screenshots/admin-dashboard/admin-dashboard-tablet.png)

![Admin Dashboard Mobile](docs/screenshots/admin-dashboard/admin-dashboard-mobile.png)

</details>

#### Design Changes

Throughout the development process, several design changes were implemented for various reasons.

One significant alteration was the decision to remove the Agent app and utilize Django's built-in groups instead. This adjustment was made due to the realization that utilizing Django's groups functionality would effectively achieve the same objective, streamlining the implementation process and improving overall efficiency.

Another significant alteration was that we opted against implementing form autocompletion for logged-in users, including areas such as newsletter sign-ups, user messages, or valuation requests. This decision was driven by the potential complexities that could arise if an agent is currently engaged with a client.

Allowing autocompletion in these scenarios could lead to awkward situations and potential misunderstandings. By deliberately refraining from this feature, we prioritize clarity and prevent inadvertent actions that may disrupt ongoing client-agent interactions.

[Return to contents](#contents)

---

### Future Features

In this section we will outline upcoming improvements and features designed to enhance the platforms experience.

| Feature                               | Description                                                      |
|---------------------------------------|------------------------------------------------------------------|
| Password Reset                        | Users can reset their password conveniently from the login page or dashboard by receiving a verification email.  |
| Property Search                       | Enhances user experience on the property listings page by enabling location-based searches with filters for price range, bedrooms, and title.  |
| Property Filter                       | Provides users with the ability to refine property listings based on property type (e.g., apartment, semi-detached), streamlining their search process.  |
| Write Newsletter                      | Empowers agents to craft and distribute newsletters effortlessly using collected subscriber data, fostering engagement and communication with users.  |
| Live Text Chat                        | Facilitates real-time communication between users and agents via a user-friendly pop-up chat feature, offering immediate assistance and support. |
| Interactive Property Listings Map     | Introduces an interactive map view option on the property listings page, allowing users to explore listings spatially for a more immersive browsing experience. |
| Image Gallery for Property Listings   | Simplifies property exploration for users by enabling agents to upload multiple images for each listing, presenting them in an intuitive carousel format for easy navigation. |
| Change Email                          | Enhances user account management by enabling email address updates directly from the user dashboard, ensuring seamless control and customization of user information. |
| For Sale, Sold, Unpublished Listings  | Provides agents with comprehensive control over property listings, enabling them to mark properties as sold or unpublished as needed, thereby optimizing listing management and user experience. |
| Account Deletion                      | Allows users to permanently delete their account from the platform, providing a streamlined process for account management and data privacy. |

[Return to contents](#contents)

---

## Languages

HTML, CSS, JavaScript, Python

## Frameworks and Libraries

| Framework/Library       | Description                                      |
|-------------------------|--------------------------------------------------|
| asgiref                 | ASGI (Asynchronous Server Gateway Interface) - A low-level library for building ASGI applications. |
| bleach                  | HTML sanitizer - A tool for sanitizing and cleaning HTML input. |
| certifi                 | Python SSL certificate authority - A collection of CA certificates for Python SSL verification. |
| charset-normalizer      | Charset normalization - A library for normalizing and converting character encodings. |
| cloudinary              | Cloud-based image and video management - A platform for storing, managing, and delivering images and videos. |
| crispy-bootstrap5       | Bootstrap 5 integration for Django Crispy Forms - Simplifies integration of Bootstrap 5 styles with Django forms. |
| dj-database-url         | Database configuration helper for Django - Parses database connection URLs for Django applications. |
| Django                  | High-level Python web framework - A powerful web framework for building web applications in Python. |
| django-crispy-forms     | DRY forms for Django apps - Simplifies form rendering and validation in Django applications. |
| django-summernote       | WYSIWYG editor for Django - Integrates the Summernote What You See Is What You Get editor into Django forms. |
| gunicorn                | Python WSGI HTTP server - A Python HTTP server for running WSGI applications. |
| idna                    | Internationalized Domain Names in Applications - A library for handling IDNA (Internationalized Domain Names in Applications) encoding and decoding. |
| psycopg2                | PostgreSQL adapter for Python - Provides Python bindings for PostgreSQL database connections. |
| requests                | HTTP library for Python - Simplifies making HTTP requests in Python. |
| setuptools              | Library for packaging Python projects - Facilitates the distribution of Python packages. |
| six                     | Python 2 and 3 compatibility utilities - Provides utilities for writing code that is compatible with both Python 2 and Python 3. |
| sqlparse                | SQL parser for Python - Parses SQL queries and statements in Python. |
| urllib3                 | HTTP library for Python - Provides a Python HTTP client for making HTTP requests. |
| webencodings            | Character encoding aliases for Python - Provides character encoding aliases for Python applications. |
| whitenoise              | Static file serving for Python web applications - Simplifies serving static files in Python web applications. |
| Bootstrap 5             | Front-end framework for building responsive websites - A popular framework for building responsive and mobile-first websites. |
| jQuery 3.6.0            | JavaScript library for DOM manipulation - Simplifies DOM manipulation and event handling in JavaScript. |

[Return to contents](#contents)

## Tools Used

[Visual Studio Code](https://code.visualstudio.com/): My primary IDE for project development.

[GitHub](https://github.com/): Hosts the project repository for collaborative viewing.

[git](https://git-scm.com/): Manages project versions for efficient tracking.

[Uizard](https://app.uizard.io/): Used for crafting intuitive wireframes.

[DrawSQL](https://drawsql.app/): A visual tool for planning and mapping the database structure.

[LucidChart](https://www.lucidchart.com/): Used to create comprehensive platform navigation diagrams.

[Eightshapes Contrast Grid](https://contrast-grid.eightshapes.com/): Ensures color accessibility with precision.

[Google Maps](https://www.google.com/maps): Used Google Maps for integrating an interactive map

[Cloudinary](https://cloudinary.com/): A versatile API platform for image and video manipulation.

[ElephantSQL](https://www.elephantsql.com/): Hosts the PostgreSQL database for efficient data storage.

[Heroku](https://www.heroku.com/): Deploys and hosts the project seamlessly.

[Image Resizer](https://imageresizer.com/): Efficiently scales down images for used for optimal ReadMe image presentation.

[Optimazilla](https://imagecompressor.com/): Compresses images without compromising quality.

[ChatGBT](https://chat.openai.com/): Utilized for generating property listings, user messages, and valuation requests.

[W3C HTML Validator](https://validator.w3.org/#validate_by_uri): Ensures HTML code adheres to standards.

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/): Validates CSS code for consistency and correctness.

[CI Python Linter](https://pep8ci.herokuapp.com/): Verifies Python code integrity for clean and maintainable scripts.

[JShint](https://jshint.com/): Guarantees JavaScript code quality with thorough analysis.



## Testing

Please the [TESTING.md](TESTING.md) file for all the testing and validation.

[Return to contents](#contents)

## Bugs & Fixes

### Bug: *Property Price Display Issue*

**Problem:**

The issue arose when attempting to display property prices on the homepage's latest properties cards. Despite the property prices being correctly displayed on the property listings page, they were not appearing on the latest properties cards of the homepage. These two sections are part of different Django apps, with the property listings page residing in the property app and the homepage in the main app.

**Cause:**

The absence of price information on the latest properties cards of the homepage was due to the context data passed to the homepage template. Unlike the property listings page, the homepage's view function did not include the formatted price information for each property in the context data.

**Fix:**

Modifications were made to the view function responsible for rendering the homepage (home view). Specifically, the home view was updated to retrieve the latest properties from the database and format their prices using the intcomma filter. By iterating over the queryset of latest properties and formatting their prices, the view ensured that the formatted price information was included in the context data passed to the homepage template. Consequently, the property prices started appearing correctly on the latest properties cards of the homepage.

---

### Bug: *Incorrect Favorite Button Redirection*

**Problem:**

Selecting the favorite button on a property card redirected users to the property details page instead of keeping them on the property listings page with the correct pagination. This behavior deviated from the intended user flow, causing confusion and disrupting the browsing experience.

**Cause:**

The incorrect redirection behavior occurred because the favorite button's URL was configured to direct users to the property details page. As a result, when users clicked the favorite button on a property card, they were redirected to the property details page, disrupting their browsing flow and removing them from the property listings page.

**Fix:**

The redirection logic for the favorite button was modified to keep users on the property listings page with the correct pagination. Instead of redirecting users to the property details page, the favorite button now redirects users back to the property listings page. Additionally, the code ensures that the pagination parameters are preserved during redirection, allowing users to seamlessly return to their previous pagination state after interacting with the favorite button on a property card. With this fix, the browsing experience is enhanced, and users can efficiently manage their favorite properties without disruption.

---

### Bug: *Navbar Alignment Issue*

**Problem:**

The central section of the navbar encountered alignment discrepancies, leading to an overall misalignment issue.

**Cause:**

The misalignment stemmed from the presence of unnecessary classes (such as text-center, m-4, col-11) and a convoluted structure in the original codebase. These elements contributed to the complexity of the layout, resulting in misalignment.

**Fix:**

To address this, several steps were taken. First, the unnecessary classes, including text-center, m-4, and col-11, were removed from the navbar, simplifying its structure. Next, the structure of the navbar underwent reorganization to eliminate redundant divs, streamlining the layout. Additionally, Bootstrap flexbox classes (d-flex, justify-content-between, ms-auto) were implemented to effectively manage alignment and positioning within the navbar. Finally, adjustments were made to the offcanvas body structure to ensure proper alignment of navbar items within the offcanvas, contributing to a cohesive layout.

---

### Bug: *Address Length DataError*

**Problem:**

When the address provided exceeds 50 characters, despite setting the address field to allow a maximum of 100 characters, Django raises a DataError during the save operation.

**Cause:**

Django's SlugField defaults to a maximum length of 50 characters. When the slugify() function generates a slug based on the address, it surpasses this limit if the address exceeds 50 characters. Consequently, Django raises a DataError because the generated slug exceeds the field's length constraint.

**Fix:**

To rectify this issue, explicitly set max_length=100 for the SlugField. This adjustment ensures that the SlugField can accommodate slugs derived from addresses of up to 100 characters, aligning with the maximum length allowed for the address field. As a result, instances with longer addresses can be saved without triggering a DataError.

---

### Bug: *Incorrect Error Handling in Newsletter Subscription Form*

**Problem:**

Users were not receiving the correct error messages when attempting to subscribe to the newsletter using an email address already existing in the database.

**Cause:**

The error handling logic in the home view was not appropriately handling the scenario where the user's email address already existed in the database. This led to inconsistent error messaging and confusion for users attempting to subscribe.

**Fix:**

To address this issue, the error handling logic in the home view was revised. The following steps were taken:

- We improved the error handling logic to ensure that the correct error messages are displayed based on the outcome of the form submission and the existence of the email address in the database.

- Before validating the form, we checked if the email address already exists in the database. If it does, we displayed the error message "You have already signed up for the newsletter!" and redirected the user back to the home page.

- After confirming that the email address does not exist in the database, we proceeded with form validation. If the form is valid, the user is successfully subscribed to the newsletter, and a success message is displayed. If the form validation fails for other reasons, the error message "Invalid email address!" is displayed.

---

### Known Issues:

During testing, three known issues were identified, requiring attention in the next development cycle. Due to time constraints, these issues could not be addressed promptly. While our team has raised these concerns, completing them within the allotted timeframe proved challenging. However, we remain committed to resolving these issues to ensure the product's stability and user satisfaction.

| Issue | Description | Status |
|-------|-------------|--------|
| Navbar | When the user is logged out, the middle links on the navbar move slightly on larger screens. | Deferred due to time constraints; higher priority tasks took precedence. |
| Messages | Messages on the homepage can overlap the offcanvas navbar, attributed to the navbar's absolute positioning. Z-index adjustments were attempted but unsuccessful. | Deferred due to time constraints; more urgent issues required immediate attention. |

[Return to contents](#contents)

## Deployment, Cloning and Forking

### Heroku Deployment:

This website has been deployed using Heroku.

Deployment Instructions:

1. In Heroku, navigate to the dashboard and click on the "New" button in the top right corner, then select "Create New App."

2. Provide a unique name for your app and choose the correct region based on your location. Click "Create App" to proceed.

3. Once your app is created, go to the settings tab.

4. Click on "Reveal Config Vars" to add any necessary keys for the application. For this project, keys such as `DISABLE_COLLECTSTATIC`, `DATABASE_URL`, `SECRET_KEY` and `CLOUDINARY_URL` were added, along with all key-value pairs from the env.py file.

5. Click on "Add Buildpack" to install any dependencies required. In this project, the "python" buildpack was installed.

6. Proceed to the "Deploy" tab. Select the deployment method, such as GitHub. Connect to your GitHub repository by searching for it and connecting to it.

7. For manual deployment, click on "Deploy Branch." Once the deployment is complete, a success message will appear, indicating that your app was successfully deployed. Click the "View" button to access the deployed page and make note of its URL.

8. Optionally, you can set up automatic deployment for continuous integration.

9. If you encounter issues with CSS not displaying correctly on the deployed site, running the following command in your workspace may help: `./manage.py collectstatic`

10. Before final deployment, ensure to set Debug mode back to False.

---

*Don't forget to perform the sacred ritual of offering a sacrifice to the Coding Gods for smooth deployment. A cup of coffee!!*

*Please note this step is not required, but highly recommended for optimal coding karma.*

---

### Cloning this Repository:

To clone this repository and start working on it, follow these instructions:

1. Navigate to the GitHub repository and locate the green "Code" button.

2. Click on the button to reveal the repository's link, and copy it.

3. Open your preferred IDE or local coding environment and use the copied link to clone the repository. For example, in VSCode, you can click on "Clone Git Repository..." and paste the link when prompted. In CodeAnywhere, click on "Add new workspace" and select "Create from your project repository," then paste the link.

4. If you're using VSCode, it's recommended to create a virtual environment. You can do this by running the command `python3 -m venv .venv` and activating the environment with `source .venv/bin/activate`.

5. Install all dependencies listed in the requirements.txt file using the command ```pip3 install -r requirements.txt```.

6. Create an env.py file in the main directory and enter key data (`DATABASE_URL, SECRET_KEY, CLOUDINARY_URL`) using `os.environ.setdefault()`.

7. Ensure that both the virtual environment and env.py are named in the .gitignore file to avoid committing sensitive information.

8. In settings.py, set Debug to `True` while developing and consider using Django's built-in SQLite database for testing purposes.

9. Finally, verify that everything is working by running the program with the command `python3 manage.py runserver`.

---

### Forking from the Repository:

1. Navigate to the GitHub repository and locate the branch symbol along with the number of existing branches.

2. Click on the symbol to access details about the current branches, then click the green "New branch" button.

3. Enter a name for the new branch and click the green "create new branch" button.

4. Your new branch should now be visible on the screen.

5. Click on the new branch and follow the cloning instructions to open and work on this branch.

[Return to contents](#contents)

## Credits

- I enhanced my understanding of User Authentication by watching and following along with a [TechwithTim](https://www.youtube.com/watch?v=WuyKxdLcw3w)'s Youtube tutorial.

- I revisited the [Code Institute](https://codeinstitute.net/) 'I think therefore I Blog' learning curriculum from Code Institute to refresh my understanding and further solidify my grasp of the material.

- The Code Institute Slack community helped me resolve an issue I encountered with Cloudinary. By securely importing the configuration into the settings file, I successfully rectified the problem highlighted by Lighthouse, which indicated that Cloudinary was being served as HTTP instead of HTTPS.

- [Django Documentation](https://docs.djangoproject.com/) was extensively utilized throughout this project to ensure the correct implementation of Django's models and built-in functions.

- [Bootstrap Documentation](https://getbootstrap.com/docs/) was thoroughly referenced throughout this project to effectively utilize its components and design principles.

### Image Credits:

**Images:**

We primarily used Unsplash for our images. However, all images are used within compliance with the licences and are properly attributed to their respective authors.

- Placeholder Home: [PNG Egg](https://www.pngegg.com/en/png-neput)
- Hero Image: [Richard R. Schünemann on Unsplash](https://unsplash.com/photos/landscape-photography-of-a-city--5y9Rse5ifk)
- Modern Living Image: [Robbie Duncan on Unsplash](https://unsplash.com/photos/a-living-room-filled-with-furniture-and-a-large-window-BxleF4zbbT8)
- London Alley Image: [Brad Starkey on Unsplash](https://unsplash.com/photos/green-plant-on-brown-wooden-table-rCuHu2yxyLU)
- Review Image: [Bruno Martins on Unsplash](https://unsplash.com/photos/white-and-brown-concrete-building-beside-brown-leaf-tree-under-clear-blue-sky-GkZvxVsHYWw)
- About Us Image: [Amy Hirschi on Unsplash](https://unsplash.com/photos/man-facing-a-woman-izxMVv2Z9dw)
- Background Image: [Huy Nguyen on Unsplash](https://unsplash.com/photos/white-ceramic-sink-near-brown-wooden-table-9vvp_nuVaJk)

**Agent Images:**
- Max Turner: [LinkedIn Sales Solutions on Unsplash](https://unsplash.com/photos/man-standing-beside-wall-pAtA8xe_iVM)
- Lily Evans: [PodMatch on Unsplash](https://unsplash.com/photos/woman-in-black-blazer-smiling-2mMhaoBGjCs)
- Owen Baker: [Andrew Power on Unsplash](https://unsplash.com/photos/man-wearing-black-suit-y9L5-wmifaY)
- Mia Hart: [Christina on Unsplash](https://unsplash.com/photos/shallow-focus-photo-of-woman-in-gray-jacket-0Zx1bDv5BNY)
- Jake Foster: [PodMatch on Unsplash](https://unsplash.com/photos/man-in-gray-suit-jacket-sitting-on-gray-concrete-bench-5gwZIKmtkIo)
- Zoe Carr: [Amy Hirschi on Unsplash](https://unsplash.com/photos/woman-standing-by-wall-holding-mug-b3AYk8HKCl0)
- Alex Martin: [Itay Verchik on Unsplash](https://unsplash.com/photos/man-wearing-gray-blazer-G3ZAhAJ2ojc)
- Lucy Shaw: [Christina on Unsplash](https://unsplash.com/photos/woman-on-focus-photography-SJvDxw0azqw)

**Listing Title Images:**
- Elegant Georgian Townhouse: [Jamie Street on Unsplash](https://unsplash.com/photos/black-steel-barricade-h6mj_9bCvBk)
- Contemporary City Apartment: [Luke Richardson on Unsplash](https://unsplash.com/photos/high-rise-building-near-body-of-water-Lx4OtAqlfO4)
- Charming Mews House with Private Garden: [Anthony Breesy on Unsplash](https://unsplash.com/photos/white-bicycle-beside-fence-PfYCAwGLMWY)
- Modern Riverside Apartment with Balcony: [Nick Fewings on Unsplash](https://unsplash.com/photos/a-body-of-water-with-a-factory-in-the-background-fd2NxyED__o)
- Elegant Victorian Townhouse in Kensington: [Josh Kirk on Unsplash](https://unsplash.com/photos/a-street-with-trees-and-buildings-on-the-side-tDi4dGMsh_U)
- Stylish City Apartment with Spectacular Views: [Evgeny Klimenchenko on Unsplash](https://unsplash.com/photos/city-skyline-across-body-of-water-during-daytime-O-J600qm45U)
- Regal Period Residence in Kensington Gardens: [Robert Bye on Unsplash](https://unsplash.com/photos/man-and-woman-walking-beside-building-VKps-Rx6a-k)
- Modern Riverside Townhouse in Battersea: [Benjamin Cheng on Unsplash](https://unsplash.com/photos/a-tall-white-building-sitting-next-to-a-street-light-TX_YNP21gqY)
- Victorian Splendor in Primrose Hill: [Sara Groblechner on Unsplash](https://unsplash.com/photos/photography-of-multicolored-building-during-daytime-_B-qMJfLPKk)
- Contemporary Mews House in Notting Hill: [Lawrence Chismorie on Unsplash](https://unsplash.com/photos/a-crosswalk-in-front-of-a-row-of-multi-colored-buildings-8gzPYm3bFCY)
- Enchanting Wizarding Residence in Diagon Alley: [Aditya Vyas on Unsplash](https://unsplash.com/photos/red-wooden-door-with-glass-3yfE6tF6N24)
- Riverside Penthouse with Panoramic Views in Chelsea: [Mostafa Sadadel on Unsplash](https://unsplash.com/photos/inside-condominium-unit-cHjAxnJk_wQ)


### Acknowledgments:

* **Code Institute**

    A heartfelt thank you goes out to the entire team at Code Institute for igniting my passion and guiding me on the path to becoming a proficient full-stack software developer. Their meticulously crafted lessons and unwavering support have been instrumental in shaping my journey, and I am deeply grateful for their dedication.

* **Richard Wells - Code Institute Mentor**

    I am immensely fortunate to have Richard as my mentor throughout this course. His guidance has been a beacon of light during challenging moments, ensuring I stay focused and empowered to overcome obstacles. I am truly indebted to him for his invaluable support and expertise.

* **Stack Overflow Community**

    I extend my gratitude to the vibrant Stack Overflow community for being an endless source of knowledge and assistance. Their collective wisdom has been pivotal in resolving countless coding dilemmas and expanding my understanding of software development.

* **My Family**

    I extend my heartfelt appreciation to my family for their unwavering support throughout this journey. Though they may not be versed in coding, their encouragement and willingness to assist have been indispensable in bringing this project to fruition.

* **My Girlfriend, Ciara**

    I am profoundly grateful to Ciara for her unwavering support since the inception of this project. Her patience, understanding, and unwavering belief in me have been the driving force behind my success so far.

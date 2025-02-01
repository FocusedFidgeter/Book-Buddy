# App Flow Document


### Introduction

"Book Buddy" is an innovative application designed to provide users with engaging and spoiler-free discussions about books. By utilizing a structured knowledge graph, Book Buddy ensures conversations are limited to the chapters or sections the user has read, making it a perfect companion for readers desiring an in-depth exploration of themes without risking future plot reveals. Primarily targeting general readers, students, and educators, the app constructively aids in book discussions and literary analyses. The main goal is to offer a personalized reading journey that maintains momentum and intrigue without compromising the unfolding narrative.


### Onboarding and Sign-In/Sign-Up

New users typically discover Book Buddy through its web interface built with Reflex. Upon visiting the site, users are greeted with an inviting landing page where they can learn more about its features. To get started, users need to sign up by choosing either email registration or one-click social login options. The sign-up process is straightforward, requiring minimal input such as email address and password, supported by Supabase for secure and efficient authentication. Upon successful registration, users receive a confirmation email to verify their account.


For returning users, the sign-in page provides a swift access route through email and password entry or social login. There is also a 'Forgot Password' option, allowing users to reset their password via a recovery email link. Users can easily sign out from the app through the account management section found within the settings, ensuring their session privacy is maintained.


### Main Dashboard or Home Page

Post login, users are navigated to the Main Dashboard, serving as the hub for all activities. The dashboard consists of several major sections that include a sidebar listing all available books, a central panel showcasing current reading progress, and a header with navigation tools leading to other features such as Settings and Preferences. This page is designed to offer a comprehensive overview of a user’s reading journey, with visual indicators of progress per book, and quick access to commence or resume book discussions.


Transitioning between different sections is seamless, primarily through the intuitive sidebar that allows users to switch easily from the Main Dashboard to individual books or discussion pages.


### Detailed Feature Flows and Page Transitions

A core feature of Book Buddy is the Discussion Interface. Upon selecting a book from the Main Dashboard, users are redirected to this chat-like screen. Here, users can initiate conversations with the AI model about the selected book within a spoiler-free scope. As users type questions or comments, the model, leveraging GPT-4o or Claude 3.5 Sonnet, generates responses based on the chapters the user has completed, sourced from the knowledge graph.


Users can explore themes, character development, and plot without concerns about spoilers. They have the flexibility to pause a discussion and switch to another book or return to the Main Dashboard without losing the context of their conversation. Book Buddy allows engaging with multiple books; however, active discussions are maintained with one book at a time.


### Settings and Account Management

Book Buddy provides a robust Settings and Preferences section, granting users control over personal data and app customization. From here, users can update their reading history, tweak chat preferences like text size and theme, and manage their account details. The app allows users to delete their account and related data at any time via a simple process within the settings. For users with a subscription, they can manage their billing details and adjust plans accordingly. After making changes, users can conveniently return to the Main Dashboard.


### Error States and Alternate Paths

Book Buddy is designed to handle errors gracefully. Should a user enter invalid data, like an unregistered email during login, clear error messages prompt corrective actions. In cases of connectivity issues, the app displays a “Connection Lost” notification and automatically retries to establish a connection. Restricted actions, such as accessing unauthorized books, trigger a permission warning with guidance on necessary actions.


### Conclusion and Overall App Journey

From the initial sign-up to daily use, Book Buddy provides an enriching user experience that encourages engagement without spoilers. Starting at the Main Dashboard, users navigate easily between selecting books and discussing content via the sophisticated Discussion Interface. With comprehensive settings management and robust handling of errors, Book Buddy ensures a seamless, user-friendly experience that meets the diverse needs of avid readers, students, and educators. The app not only promises an innovative reading companion but also a valuable educational tool that respects the user’s evolving reading journey.

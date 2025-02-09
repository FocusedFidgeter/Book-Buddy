# Project Requirements Document for "Book Buddy"

## 1. Project Overview

"Book Buddy" is an innovative chatbot designed to offer readers a unique, spoiler-free book discussion experience. It accomplishes this by utilizing a knowledge graph to map book content in a structured way, allowing the chatbot to only discuss plot points the user has already read. This makes it perfect for readers who are keen to explore book analyses, themes, and details without the risk of encountering unwanted spoilers. Book Buddy is developed with a keen eye on creating a delightful user experience for both casual book lovers and an educational audience of students and teachers.

The primary objectives of Book Buddy are to foster engaging book discussions and deepen literary appreciation without revealing future story developments. By integrating with a robust technology stack, the project aims to ensure seamless, personalized user interactions across multiple books while maintaining data privacy and security. Success will be measured by user engagement, satisfaction, and the app’s ability to scale efficiently for broader use.

## 2. In-Scope vs. Out-of-Scope

### **In-Scope**

- Spoiler-free book discussion based on user’s reading progress via a knowledge graph.
- User authentication and data storage through Supabase.
- A dashboard for book selection and progress tracking.
- Chat interface for book discussions.
- Customizable user settings and preferences.
- Exporting of knowledge and conversations into .md files in a GitHub repository.
- Basic wit chat powered by AI models GPT-4o or Claude 3.5 Sonnet for response generation.

### **Out-of-Scope**

- Integration with third-party e-readers for automated progress tracking.
- Voice command interaction and audio discussions.
- Integration with social media or other external educational platforms beyond exporting capabilities.
- Immediate monetization features; likely handled in future phases.

## 3. User Flow

When a new user signs up for Book Buddy, they begin their journey at the Main Dashboard, where they can select from a library of available books. Here, users have clear visibility of their reading progress, which is reflected through a personalized interface that helps manage ongoing and completed book interactions. From the dashboard, users can easily navigate to the Discussion Interface; a chat-like screen specifically designed for engaging with Book Buddy to ask questions and discuss plot points without spoilers. The discussion is intricately tailored to ensure users only receive information on parts of the book they have already read.

As users engage with Book Buddy, they have the option to personalize their experience through the Settings & Preferences section. This functionality allows users to adjust their reading history and chat preferences, ensuring a customized interaction for each session. The entire journey is crafted to offer a seamless, intuitive, and user-friendly experience that keeps book enthusiasts and educational users engaged.

## 4. Core Features

- **Knowledge Graph & Spoiler-Free Chat**: Leverages a knowledge graph to allow discussions only about parts of the book already read by the user.
- **Personal Reading Progress**: Tracks individual progress and preferences to tailor discussions and analyses.
- **AI-Powered Conversations**: Uses GPT-4o or Claude 3.5 Sonnet to generate interactive and informative responses.
- **Dashboard & Book Management**: Central hub for book selection and viewing reading progress.
- **Settings & Personalization**: Users can adjust reading history, preferences, and modify how they interact with the book_buddy.
- **Data Privacy & Security**: Comprehensive measures to protect user data through Supabase, with options for data deletion.
- **Export Functionality**: Chat and knowledge base can be exported into markdown files on GitHub for external use.

## 5. Tech Stack & Tools

- **Frontend Framework**: Reflex (the pure-python web framework) for building the user interface
- **Backend & Storage**: Supabase for handling authentication and storing user data securely.
- **Knowledge Graph Tools**: Neo4j deployed for effective book content structuring and query handling.
- **Version Control**: Managed using TerminusDB for reverting or handling updates as necessary.
- **AI Model Integration**: GPT-4o or Claude 3.5 Sonnet for enhancing conversational interaction.
- **IDE Tools**: Cursor AI, Windsurf, and VS Code for coding and collaboration.

## 6. Non-Functional Requirements

- **Performance**: The application and chat responses should operate with minimal lag, aiming for response times of less than 2 seconds to keep user engagement high.
- **Security**: Utilize robust encryption for data in transit and at rest. Implement strong access controls and compliance with data protection regulations.
- **Usability**: Design intuitive interfaces that accommodate user navigation with ease and ensure user satisfaction.
- **Scalability**: System should efficiently handle a growing user base and concurrent usage without performance degradation.

## 7. Constraints & Assumptions

- The app relies on the availability of the latest AI models for accurate chat responses.
- Users will manually input reading progress; integration with e-readers is not assumed.
- The freemium model is assumed for monetization, though this may evolve.

## 8. Known Issues & Potential Pitfalls

- **API Rate Limits**: Can impose restrictions on calling AI models or database queries. Implement caching strategies and optimize queries to mitigate.
- **Data Synchronization**: Potential lag in syncing user data across sessions. Employ efficient database practices.
- **Scalability Challenges**: Initially deploying on smaller infrastructure may limit capacity. Plan for cloud scaling options to accommodate growth.

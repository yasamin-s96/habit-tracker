### Habit Tracker REST API - Software Requirements

**Objective:**
Design and implement a RESTful API for a Habit Tracker application. The API should allow users to create, manage, and track their daily habits. The application will focus on simplicity, ensuring that users can easily interact with the API to track their progress.

---

#### **Functional Requirements:**

1. **User Management:**
   - **Sign Up:** Users should be able to register an account by providing their email, username, and password.
   - **Login:** Users should be able to log in using their email/username and password.
   - **Authentication:** The API should use JWT (JSON Web Tokens) for user authentication. After logging in, users should receive a token that they must include in the header of requests to access protected resources.

2. **Habit Management:**
   - **Create Habit:** Users should be able to create a new habit. Each habit should include:
     - Habit Name (e.g., "Exercise", "Read a Book")
     - Description (optional)
     - Frequency (e.g., daily, weekly, monthly)
     - Start Date (optional, defaults to creation date)
     - Target (optional, e.g., 30 days, 7 weeks)
   - **View Habits:** Users should be able to view a list of their habits.
   - **Update Habit:** Users should be able to update a habit's details (e.g., name, description, frequency).
   - **Delete Habit:** Users should be able to delete a habit.

3. **Habit Tracking:**
   - **Log Habit Completion:** Users should be able to mark a habit as completed for a specific day. Each log should store:
     - Date of completion
     - Notes (optional)
   - **View Habit Logs:** Users should be able to view the log of a specific habit, showing dates and statuses (e.g., completed or not completed).
   - **Habit Streaks:** The API should calculate and return the current streak of consecutive completions for each habit.

4. **Progress Tracking:**
   - **View Progress:** Users should be able to view their overall progress, including:
     - Total habits created
     - Total completions
     - Current streaks
     - Habits completed in the last week/month
   - **Habit Insights:** Users should be able to get insights, such as:
     - Most frequently completed habit
     - Least completed habit

---

#### **Non-Functional Requirements:**

1. **Scalability:**
   - The API should be designed to handle a growing number of users and habits efficiently.

2. **Security:**
   - All sensitive data (e.g., passwords) should be securely stored (e.g., hashed with bcrypt).
   - Authentication tokens should have an expiration time.
   - The API should be protected against common security threats such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).

3. **Performance:**
   - The API should be responsive, with a maximum acceptable latency of 200ms for any endpoint under normal load conditions.
   - Efficient database queries should be implemented to handle data retrieval and updates.

4. **Documentation:**
   - The API should be well-documented, providing clear information on all available endpoints, request parameters, and response formats.
   - Documentation should be accessible, either as a Swagger/OpenAPI interface or a similar tool.

5. **Testing:**
   - The API should have unit and integration tests for key functionalities, ensuring robustness and reliability.

6. **Versioning:**
   - The API should follow versioning practices (e.g., /api/v1/), allowing future updates without breaking existing clients.

---

#### **Deliverables:**

1. **API Endpoints Documentation:** 
   - A list of all API endpoints with descriptions, request/response examples, and expected status codes.

2. **Source Code:** 
   - Well-structured, maintainable codebase following best practices in backend development.
   - Use of a modern backend framework (e.g., Flask, Django, FastAPI).

3. **Database Schema:**
   - A clear schema for storing users, habits, and logs, optimized for query performance.

4. **Unit and Integration Tests:**
   - Test cases covering key functionality of the API.

5. **Deployment Instructions:**
   - Instructions for deploying the API to a cloud service (e.g., AWS, Heroku) or on-premise server.

---

This task assesses your ability to design a REST API with a focus on user authentication, data management, and tracking features. Pay special attention to security and performance considerations, and ensure that the code is clean and maintainable.
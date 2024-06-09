# Table of Contents

- [Code Validation](#code-validation)
- [Lighthouse Testing](#lighthouse-testing)
- [User Stories Testing](#user-stories-testing)
- [Features Testing](#features-testing)
- [Browser and Mode Testing](#browser-and-mode-testing)

_____

## Code Validation

### HTML

All HTML code was tested using [W3C Validator](https://validator.w3.org/) via text input. The only errors that showed up were to do with the use of Django Static Text and the validators inability to check it.

<details>
<summary>Screenshots and results for all templates.</summary>
<br>

    HOME
![No Errors or Warnings to show](images/html%20home%20check.png)

    ABOUT
![No Errors or Warnings to show](images/html%20about%20check.png)

    SCORECARD
![No Errors or Warnings to show](images/html%20scorecard%20check.png)

    STUDENT LOGIN
![No Errors or Warnings to show](images/html%20student%20signin%20check.png)

    LESSONS
![No Errors or Warnings to show](images/html%20lesson%20check.png)

    QUESTION PAGE
![No Errors or Warnings to show](images/html%20question%20page%20check.png)

    TEACHER LOGIN
![No Errors or Warnings to show](images/html%20teacher%20signin%20check.png)

    TEACHER DASHBOARD
![No Errors or Warnings to show](images/html%20dashboard%20check.png)

    TEACHER CREATE STUDENT
![No Errors or Warnings to show](images/html%20create%20student%20check.png)

    TEACHER VIEW STUDENTS
![No Errors or Warnings to show](images/html%20view%20students%20check.png)

</details>

<br>

[Back To Top](#table-of-contents)

_____

### CSS

CSS code was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

<details>

<summary>Screenshot with results for the styles.css file</summary>

**styles.css**

![No Error Found](images/css%20check.png)

</details>

<br>

[Back To Top](#table-of-contents)

_____

### Python

Python code was tested using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/).

<details>

<summary>Screenshots and results for all python files</summary>

Long lines still appear at points, despite using Black to format the Python lines to line length 79. No clear solution found to fix these minor errors.

- pine_hills_grammar

        settings.py
    ![All clear, no errors found](images/python%20settings.py%20check.png)

        urls.py
    ![All clear, no errors found](images/python%20pine%20hills%20maths%20urls.py%20check.png)

        views.py
    ![All clear, no errors found](images/python%20pine%20hills%20maths%20views.py%20check.png)

- student

        models.py
    ![All clear, no errors found](images/python%20student%20models.py%20check.png)

        urls.py
    ![All clear, no errors found](images/python%20student%20urls.py%20check.png)

        views.py
    ![All clear, no errors found](images/python%20student%20views.py%20check.png)

- teacher

        models.py
    ![All clear, no errors found](images/python%20teacher%20models.py%20check.png)

        urls.py
    ![All clear, no errors found](images/python%20teacher%20urls.py%20check.png)

        views.py
    ![All clear, no errors found](images/python%20teacher%20views.py%20check.png)

</details>

<br>

[Back To Top](#table-of-contents)

_____

## Lighthouse Testing

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to check the website for performance, accessibility, best practice and SEO..

<details>
<summary>Screenshots and results for all pages</summary>

- HOME

        Mobile
    ![Passed](images/lighthouse%20home%20mobile.png)

        Desktop
    ![Passed](images/lighthouse%20home%20desktop.png)

- ABOUT

        Mobile
    ![Passed](images/lighthouse%20about%20mobile.png)

        Desktop
    ![Passed](images/lighthouse%20about%20desktop.png)

- SCORECARD

        Mobile
    ![Passed](images/lighthouse%20scorecard%20mobile.png)

        Desktop
    ![Passed](images/lighthouse%20scorecard%20desktop.png)

- STUDENT LOGIN

        Mobile
    ![Passed](images/lighthouse%20student%20signin%20mobile.png)

        Desktop
    ![Passed](images/lighthouse%20student%20signin%20desktop.png)

- STUDENT LESSONS

        Mobile
    ![Passed](images/lighthouse%20question%20page%20mobile.png)

        Desktop
    ![Passed](images/lighthouse%20question%20page%20desktop.png)

- STUDENT QUESTIONS

        Mobile
    ![Passed](images/lighthouse%20questions%20mobile.png)

        Desktop
    ![Passed](images/lighthouse%20questions%20desktop.png)

- TEACHER LOGIN

        Mobile
    ![Passed](images/lighthouse%20teacher%20signin%20mobile.png)

        Desktop
    ![Passed](images/lighthouse%20teacher%20signin%20desktop.png)

- TEACHER DASHBOARD

        Mobile
    ![Passed](images/lighthouse%20dashboard%20mobile.png)

        Desktop
    ![Passed](images/lighthouse%20dashboard%20desktop.png)

- TEACHER CREATE STUDENTS

        Mobile
    ![Passed](images/lighthouse%20create%20student%20mobile.png)

        Desktop
    ![Passed](images/lighthouse%20create%20student%20desktop.png)

- TEACHER VIEW STUDENTS

        Mobile
    ![Passed](images/lighthouse%20view%20student%20mobile.png)

        Desktop
    ![Passed](images/lighthouse%20view%20student%20desktop.png)

</details>

<br>

[Back To Top](#table-of-contents)

_____

## User Stories Testing

To ensure that the project meets the needs of both students and teachers, I created detailed user stories and recorded them as GitHub Issues (see [Project](https://github.com/users/jftjenkins/projects/5) for all issues). These user stories guided the development process, ensuring that all features were implemented according to user needs. Each user story was thoroughly tested, and the results are detailed below.

<details>

<summary>As a Teacher</summary>

* User Story [#56695625](https://github.com/users/jftjenkins/projects/5/views/1?pane=issue&itemId=56695625)

As a Teacher, I can manage course content and user accounts so that I can ensure the platform operates smoothly.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I can add, edit, and delete user accounts | Achieved | All functions work as expected |
| I can view user performance and engagement | Achieved | All functions work as expected |

* User Story [#65632017](https://github.com/users/jftjenkins/projects/5/views/1?pane=issue&itemId=65632017)

As a Teacher, I can authenticate myself so that I can access the appropriate functionalities based on my role.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I can log in with my teacher credentials | Achieved | Login works correctly |
| I can access teacher-specific functionalities | Achieved | Access control works as expected |

* User Story [#65632256](https://github.com/users/jftjenkins/projects/5/views/1?pane=issue&itemId=65632256)

As a Teacher, I can log out of my account so that I can securely end my session.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I can log out securely | Achieved | Logout works correctly |

* User Story [#65632146](https://github.com/users/jftjenkins/projects/5/views/1?pane=issue&itemId=65632146)

As a Teacher, I can create, edit, and delete student accounts so that I can maintain an updated list of student users.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I can create new student accounts | Achieved | Creation works correctly |
| I can edit existing student accounts | Achieved | Editing works correctly |
| I can delete student accounts | Achieved | Deletion works correctly |

* User Story [#65632167](https://github.com/users/jftjenkins/projects/5/views/1?pane=issue&itemId=65632167)

As a Teacher, I can reset a student's password so that I can assist students who have forgotten their passwords.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I can reset passwords for student accounts | Achieved | Password reset works correctly |

* User Story [#65632079](https://github.com/users/jftjenkins/projects/5/views/1?pane=issue&itemId=65632079)

As a Teacher, I can access the admin dashboard so that I can manage student accounts and view their progress.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I can view student progress and manage accounts | Achieved | Admin dashboard works correctly |

</details>

<details>

<summary>As a Student</summary>

* User Story [#56695554](https://github.com/users/jftjenkins/projects/5/views/1?pane=issue&itemId=56695554)

As a Student, I can access different lessons by category and see my progress on a leaderboard so that I can monitor my learning journey.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I can view lessons by category | Achieved | Lessons are categorized correctly |
| I can see my progress on a leaderboard | Achieved | Progress tracking works correctly |

* User Story [#56695602](https://github.com/users/jftjenkins/projects/5/views/1?pane=issue&itemId=56695602)

As a Student, I can take quizzes and assessments within courses so that I can evaluate my understanding of the material.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I can take quizzes and receive feedback | Achieved | Quizzes work correctly and provide feedback |

* User Story [#57706511](https://github.com/users/jftjenkins/projects/5/views/1?pane=issue&itemId=57706511)

As a Student, I can view the home page when I access the website so that I can quickly understand the purpose of the website and navigate to different sections easily.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I can view the home page with relevant information | Achieved | Home page displays correctly |

* User Story [#65632215](https://github.com/users/jftjenkins/projects/5/views/1?pane=issue&itemId=65632215)

As a Student, I can view my scorecard so that I can track my progress and performance in the lessons.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I can view my scorecard with my progress | Achieved | Scorecard displays correctly |

* User Story [#65632187](https://github.com/users/jftjenkins/projects/5/views/1?pane=issue&itemId=65632187)

As a Student, I can access different levels of maths lessons so that I can practice and improve my skills.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| I can access lessons of varying difficulty | Achieved | Lessons are scaffolded and functional |

</details>

<br>

[Back To Top](#table-of-contents)

_____

## Features Testing

Each feature listed in the [README](README.md) has been manually tested.

<details>

<summary>User Authentication</summary>

- Unregistered / Not logged in User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Login Page                    | view          | Form is displayed     |
| Invalid login attempt         | submit invalid details | Error message displayed |
| Successful login              | submit valid details | Redirects to dashboard  |
| Logout                        | click logout  | Redirects to home page  |

ALL TESTS PASS

</details>

<details>

<summary>Lesson Access</summary>

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| View Lessons                  | click lessons link | Lessons are displayed |
| Access Lesson                 | click lesson link | Lesson content displayed  |

ALL TESTS PASS

</details>

<details>

<summary>Score Tracking</summary>

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| View Scorecard                | click scorecard link | Scorecard is displayed  |
| Filter by Username            | enter username | Scorecard filtered by username |

ALL TESTS PASS

</details>

<details>

<summary>User Management</summary>

- Teacher

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Add Student                   | submit new student form | Student added successfully |
| Edit Student                  | submit edit form | Student details updated  |
| Delete Student                | click delete button | Student removed from system |

ALL TESTS PASS

</details>

<details>

<summary>Main Menu</summary>

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Navigation Links              | click links   | Pages open correctly  |
| Burger Menu (Mobile)          | click burger icon | Menu expands and collapses  |

ALL TESTS PASS

</details>

<details>

<summary>Admin Dashboard</summary>

- Teacher

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| View Dashboard                | login as teacher | Dashboard displayed  |
| Manage Users                  | navigate to user management | User management interface displayed  |
| View Reports                  | navigate to reports | Reports displayed  |
| Reset Scoreboard              | click reset button | Scoreboard reset, all scores cleared |

ALL TESTS PASS

</details>

<br>

[Back To Top](#table-of-contents)

_____

## Browser and Mode Testing

The website was tested on multiple browsers to ensure compatibility and responsiveness. Additionally, tests were conducted in both light mode and dark mode to ensure a consistent user experience across different settings.

### Browsers Tested

- Google Chrome
- Microsoft Edge
- Opera

### Modes Tested

- Light Mode
- Dark Mode

### Test Results

| Browser       | Light Mode | Dark Mode |
| ------------- |:----------:|:---------:|
| Chrome        | Pass       | Pass      |
| Edge          | Pass       | Pass      |
| Opera        | Pass       | Pass      |

The website displayed consistently and functioned correctly across all tested browsers and modes.

<br>

[Back To Top](#table-of-contents)

[Back to README.md](README.md)

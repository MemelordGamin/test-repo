# Complete ERD Guide: Web-Based Learning System

This ERD represents a **Web-based Learning System** built for a **.NET / SQL Server web application**. It supports user registration, login, role-based access control, course browsing, course enrolment, lesson progress tracking, quizzes, classes, certificates, badges, issue reporting, notifications, subscriptions, payments and course approval workflows.

The ERD is suitable for a university Web Applications assignment because it shows:

* Clear entities
* Primary keys
* Foreign keys
* One-to-many relationships
* One-to-one relationships
* Many-to-many relationships resolved using bridge tables
* Role-based access control
* CRUD-ready database structure
* Academic module grouping
* SQL Server-friendly naming

---

# 1. Overall System Explanation

The system is an online learning platform where users can access learning content through a web interface. Public visitors can browse available courses without logging in. Registered users can log in and access member features depending on their role.

The system supports five main roles:

1. **Student**
2. **Lecturer**
3. **Course Creator**
4. **Leader / Reviewer**
5. **Admin**

Each role has different access rights. For example, a student can enrol in courses, complete lessons, attempt quizzes and earn certificates. A lecturer can create classes and manage students. A course creator can create courses and learning content. A leader or reviewer can approve courses. An admin can manage users, payments, issues and system content.

The database is designed around the main idea that **users interact with courses**, while the system records their enrolments, lesson progress, quiz attempts, certificates, badges, payments, notifications and support issues.

---

# 2. Naming Convention Used

In the ERD, some names were adjusted to make them safer for implementation.

## `APP_USER`

The entity is called `APP_USER` instead of `User`.

This is because `USER` can be a reserved or system-related keyword in some database environments. Using `APP_USER` makes the table clearer and safer for SQL Server implementation.

In the final report, you can explain:

> The `APP_USER` entity represents all registered users of the learning system. It is named `APP_USER` instead of `User` to avoid conflict with reserved database keywords.

## `COURSE_CLASS`

The entity is called `COURSE_CLASS` instead of `Class`.

This is because `Class` can conflict with programming language terminology and diagram parsers. `COURSE_CLASS` is more specific because the class belongs to a course.

In the final report, you can explain:

> The `COURSE_CLASS` entity represents a learning class created by a lecturer for a specific course.

---

# 3. ERD Notation Guide

Your ERD uses **crow’s foot notation**.

## Main symbols

| Symbol meaning | Explanation                                   |
| -------------- | --------------------------------------------- |
| One            | One record must exist                         |
| Zero or one    | The record is optional                        |
| Many           | Multiple related records can exist            |
| One-to-many    | One parent record can have many child records |
| Many-to-many   | Resolved using a bridge table                 |

Example:

`ROLE 1:M APP_USER`

This means one role can be assigned to many users but each user has one role.

---

# 4. Module Grouping Explanation

The ERD is grouped into nine modules:

1. **User & Authentication**
2. **Course Management**
3. **Learning & Progress**
4. **Quiz & Assessment**
5. **Class Management**
6. **Rewards & Certificates**
7. **Admin & Approval**
8. **Subscription & Payment**
9. **Support & Notifications**

This grouping makes the ERD easier to understand because a large learning system contains many entities. Instead of showing all entities as one messy structure, each group represents one functional area of the application.

---

# 5. User & Authentication Module

## Purpose

This module manages registered users, user roles, login details and user profile information. It is the foundation of the whole system because most other modules depend on the user account.

## Entities in this module

* `ROLE`
* `APP_USER`
* `STUDENT_PROFILE`
* `LECTURER_PROFILE`

---

## 5.1 ROLE Entity

The `ROLE` entity stores the access level or type of user.

### Attributes

| Attribute     | Description                                                                 |
| ------------- | --------------------------------------------------------------------------- |
| `RoleID`      | Primary key for the role                                                    |
| `RoleName`    | Name of the role such as Student, Lecturer, Course Creator, Leader or Admin |
| `Description` | Explains what the role is used for                                          |

### Example records

| RoleID | RoleName          |
| ------ | ----------------- |
| 1      | Student           |
| 2      | Lecturer          |
| 3      | Course Creator    |
| 4      | Leader / Reviewer |
| 5      | Admin             |

### Why this entity is needed

The system needs role-based access control. Instead of storing the role name directly inside the user table, the role is placed in a separate table. This avoids repeated role names and makes permission management cleaner.

---

## 5.2 APP_USER Entity

The `APP_USER` entity stores all registered users in the system.

### Attributes

| Attribute       | Description                                |
| --------------- | ------------------------------------------ |
| `UserID`        | Primary key for the user                   |
| `RoleID`        | Foreign key linking the user to a role     |
| `FullName`      | Full name of the user                      |
| `Email`         | Login email address                        |
| `PasswordHash`  | Secure hashed password                     |
| `PhoneNumber`   | Contact number                             |
| `ProfileImage`  | Profile image path or URL                  |
| `AccountStatus` | Active, inactive, suspended or pending     |
| `CreatedAt`     | Date and time the account was created      |
| `UpdatedAt`     | Date and time the account was last updated |

### Important point

The ERD stores `PasswordHash`, not plain password. This is correct because passwords should never be stored directly in the database.

### Relationship

`ROLE 1:M APP_USER`

One role can be assigned to many users. Each user belongs to one role.

Example:

* One role called Student can be assigned to many student users.
* One role called Admin can be assigned to many admin users.

---

## 5.3 STUDENT_PROFILE Entity

The `STUDENT_PROFILE` entity stores student-specific information.

### Attributes

| Attribute          | Description                           |
| ------------------ | ------------------------------------- |
| `StudentProfileID` | Primary key for the student profile   |
| `UserID`           | Foreign key linking to `APP_USER`     |
| `EducationLevel`   | Student’s education level             |
| `LearningGoal`     | Student’s learning objective          |
| `TotalPoints`      | Total points earned by the student    |
| `CreatedAt`        | Date and time the profile was created |

### Relationship

`APP_USER 1:0..1 STUDENT_PROFILE`

One user can have zero or one student profile.

This is optional because not every user is a student. A lecturer or admin does not need a student profile.

---

## 5.4 LECTURER_PROFILE Entity

The `LECTURER_PROFILE` entity stores lecturer-specific information.

### Attributes

| Attribute           | Description                          |
| ------------------- | ------------------------------------ |
| `LecturerProfileID` | Primary key for the lecturer profile |
| `UserID`            | Foreign key linking to `APP_USER`    |
| `Department`        | Lecturer’s academic department       |
| `ExpertiseArea`     | Area of expertise                    |
| `Bio`               | Short lecturer biography             |

### Relationship

`APP_USER 1:0..1 LECTURER_PROFILE`

One user can have zero or one lecturer profile.

This is optional because not every user is a lecturer.

---

# 6. Course Management Module

## Purpose

This module handles course creation, course categories, course sections and lessons. It represents the structure of learning content.

## Entities in this module

* `COURSE_CATEGORY`
* `COURSE`
* `COURSE_SECTION`
* `LESSON`

---

## 6.1 COURSE_CATEGORY Entity

The `COURSE_CATEGORY` entity groups courses into categories.

### Attributes

| Attribute      | Description                  |
| -------------- | ---------------------------- |
| `CategoryID`   | Primary key for the category |
| `CategoryName` | Name of the category         |
| `Description`  | Description of the category  |

### Example records

| CategoryName     |
| ---------------- |
| Web Development  |
| Cyber Security   |
| Database Systems |
| Programming      |
| Data Analytics   |

### Relationship

`COURSE_CATEGORY 1:M COURSE`

One category can contain many courses. Each course belongs to one category.

---

## 6.2 COURSE Entity

The `COURSE` entity stores the main course information.

### Attributes

| Attribute           | Description                                            |
| ------------------- | ------------------------------------------------------ |
| `CourseID`          | Primary key for the course                             |
| `CreatorID`         | Foreign key linking to the user who created the course |
| `CategoryID`        | Foreign key linking to course category                 |
| `CourseTitle`       | Course name                                            |
| `CourseDescription` | Course description                                     |
| `DifficultyLevel`   | Beginner, intermediate or advanced                     |
| `CourseImage`       | Course image path or URL                               |
| `CourseStatus`      | Draft, pending, approved, rejected or published        |
| `PriceType`         | Free, paid or subscription-based                       |
| `CreatedAt`         | Date and time the course was created                   |
| `UpdatedAt`         | Date and time the course was last updated              |

### Relationships

`APP_USER 1:M COURSE`

One user can create many courses.

`COURSE_CATEGORY 1:M COURSE`

One category can contain many courses.

### Why `CreatorID` links to `APP_USER`

Course creators are users of the system. Instead of creating a separate table for course creators, the ERD uses the `APP_USER` table and identifies course creators through their role.

---

## 6.3 COURSE_SECTION Entity

The `COURSE_SECTION` entity divides a course into sections or modules.

### Attributes

| Attribute            | Description                   |
| -------------------- | ----------------------------- |
| `SectionID`          | Primary key for the section   |
| `CourseID`           | Foreign key linking to course |
| `SectionTitle`       | Name of the section           |
| `SectionDescription` | Description of the section    |
| `SectionOrder`       | Display order of the section  |

### Relationship

`COURSE 1:M COURSE_SECTION`

One course can have many sections.

Example:

Course: Introduction to Web Development

Sections:

1. HTML Basics
2. CSS Styling
3. JavaScript Fundamentals
4. ASP.NET MVC Introduction

---

## 6.4 LESSON Entity

The `LESSON` entity stores individual learning lessons inside a course section.

### Attributes

| Attribute           | Description                                  |
| ------------------- | -------------------------------------------- |
| `LessonID`          | Primary key for the lesson                   |
| `SectionID`         | Foreign key linking to course section        |
| `LessonTitle`       | Name of the lesson                           |
| `LessonContent`     | Text-based lesson content                    |
| `VideoURL`          | Video link                                   |
| `ResourceFile`      | Downloadable file path                       |
| `LessonOrder`       | Display order of the lesson                  |
| `EstimatedDuration` | Estimated time needed to complete the lesson |

### Relationship

`COURSE_SECTION 1:M LESSON`

One course section can contain many lessons.

---

# 7. Learning & Progress Module

## Purpose

This module records course enrolments and tracks student progress through lessons.

## Entities in this module

* `ENROLLMENT`
* `LESSON_PROGRESS`

---

## 7.1 ENROLLMENT Entity

The `ENROLLMENT` entity resolves the many-to-many relationship between users and courses.

A user can enrol in many courses. A course can have many users enrolled. This cannot be stored directly using only `APP_USER` and `COURSE`, so the ERD uses `ENROLLMENT` as a bridge table.

### Attributes

| Attribute              | Description                               |
| ---------------------- | ----------------------------------------- |
| `EnrollmentID`         | Primary key for the enrolment             |
| `UserID`               | Foreign key linking to user               |
| `CourseID`             | Foreign key linking to course             |
| `EnrollmentDate`       | Date and time of enrolment                |
| `CompletionStatus`     | Not started, in progress or completed     |
| `CompletionPercentage` | Overall progress percentage               |
| `LastAccessedAt`       | Last time the student accessed the course |

### Relationships

`APP_USER 1:M ENROLLMENT`

One user can have many enrolments.

`COURSE 1:M ENROLLMENT`

One course can have many enrolments.

### Business rule

A user should not enrol in the same course twice. Therefore, the database should have a unique constraint on:

`UserID + CourseID`

---

## 7.2 LESSON_PROGRESS Entity

The `LESSON_PROGRESS` entity tracks lesson completion for each enrolment.

### Attributes

| Attribute      | Description                            |
| -------------- | -------------------------------------- |
| `ProgressID`   | Primary key for progress record        |
| `EnrollmentID` | Foreign key linking to enrolment       |
| `LessonID`     | Foreign key linking to lesson          |
| `IsCompleted`  | Shows whether the lesson is completed  |
| `CompletedAt`  | Date and time the lesson was completed |
| `TimeSpent`    | Time spent on the lesson               |

### Relationships

`ENROLLMENT 1:M LESSON_PROGRESS`

One enrolment can have many lesson progress records.

`LESSON 1:M LESSON_PROGRESS`

One lesson can appear in many progress records because many students can complete the same lesson.

### Business rule

A lesson should only have one progress record per enrolment. Therefore, the database should have a unique constraint on:

`EnrollmentID + LessonID`

---

# 8. Quiz & Assessment Module

## Purpose

This module manages quizzes, questions, answer options and quiz attempts. It allows the system to assess student learning.

## Entities in this module

* `QUIZ`
* `QUESTION`
* `ANSWER_OPTION`
* `QUIZ_ATTEMPT`

---

## 8.1 QUIZ Entity

The `QUIZ` entity stores quiz details.

### Attributes

| Attribute      | Description                            |
| -------------- | -------------------------------------- |
| `QuizID`       | Primary key for the quiz               |
| `CourseID`     | Foreign key linking to course          |
| `LessonID`     | Optional foreign key linking to lesson |
| `QuizTitle`    | Name of the quiz                       |
| `TotalMarks`   | Total marks for the quiz               |
| `PassingMarks` | Minimum marks required to pass         |
| `CreatedAt`    | Date and time the quiz was created     |

### Relationships

`COURSE 1:M QUIZ`

One course can have many quizzes.

`LESSON 1:M QUIZ`

One lesson can have zero or many quizzes.

### Important point

`LessonID` is nullable because a quiz may be attached to a whole course instead of a specific lesson.

Example:

* Lesson quiz: Quiz after Lesson 1
* Course quiz: Final quiz for the whole course

---

## 8.2 QUESTION Entity

The `QUESTION` entity stores quiz questions.

### Attributes

| Attribute      | Description                      |
| -------------- | -------------------------------- |
| `QuestionID`   | Primary key for the question     |
| `QuizID`       | Foreign key linking to quiz      |
| `QuestionText` | The question content             |
| `QuestionType` | MCQ, true or false, short answer |
| `Marks`        | Marks allocated to the question  |

### Relationship

`QUIZ 1:M QUESTION`

One quiz can contain many questions.

---

## 8.3 ANSWER_OPTION Entity

The `ANSWER_OPTION` entity stores possible answers for each question.

### Attributes

| Attribute    | Description                              |
| ------------ | ---------------------------------------- |
| `OptionID`   | Primary key for answer option            |
| `QuestionID` | Foreign key linking to question          |
| `OptionText` | The answer option text                   |
| `IsCorrect`  | Identifies whether the option is correct |

### Relationship

`QUESTION 1:M ANSWER_OPTION`

One question can have many answer options.

Example:

Question: What does HTML stand for?

Options:

* HyperText Markup Language
* HighText Machine Language
* Hyper Transfer Main Logic
* Home Tool Markup Language

---

## 8.4 QUIZ_ATTEMPT Entity

The `QUIZ_ATTEMPT` entity records each attempt made by a user.

### Attributes

| Attribute      | Description                  |
| -------------- | ---------------------------- |
| `AttemptID`    | Primary key for quiz attempt |
| `UserID`       | Foreign key linking to user  |
| `QuizID`       | Foreign key linking to quiz  |
| `Score`        | Score achieved by the user   |
| `AttemptDate`  | Date and time of attempt     |
| `PassedStatus` | Passed or failed             |

### Relationships

`APP_USER 1:M QUIZ_ATTEMPT`

One user can attempt many quizzes.

`QUIZ 1:M QUIZ_ATTEMPT`

One quiz can have many attempts from different users.

### Why this table is needed

Without this table, the system cannot track quiz history, scores or pass/fail status.

---

# 9. Class Management Module

## Purpose

This module allows lecturers to create classes for courses and manage student membership in those classes.

## Entities in this module

* `COURSE_CLASS`
* `CLASS_STUDENT`

---

## 9.1 COURSE_CLASS Entity

The `COURSE_CLASS` entity represents a class created by a lecturer for a course.

### Attributes

| Attribute     | Description                              |
| ------------- | ---------------------------------------- |
| `ClassID`     | Primary key for the class                |
| `LecturerID`  | Foreign key linking to lecturer user     |
| `CourseID`    | Foreign key linking to course            |
| `ClassName`   | Name of the class                        |
| `ClassCode`   | Unique joining code                      |
| `StartDate`   | Class start date                         |
| `EndDate`     | Class end date                           |
| `ClassStatus` | Active, inactive, completed or cancelled |

### Relationships

`APP_USER 1:M COURSE_CLASS`

One lecturer can create many classes.

`COURSE 1:M COURSE_CLASS`

One course can be assigned to many classes.

### Important point

`LecturerID` links to `APP_USER`. The user must have the lecturer role.

---

## 9.2 CLASS_STUDENT Entity

The `CLASS_STUDENT` entity resolves the many-to-many relationship between students and classes.

A class can have many students. A student can join many classes.

### Attributes

| Attribute        | Description                           |
| ---------------- | ------------------------------------- |
| `ClassStudentID` | Primary key for class membership      |
| `ClassID`        | Foreign key linking to class          |
| `UserID`         | Foreign key linking to student user   |
| `JoinedAt`       | Date and time the student joined      |
| `Status`         | Active, removed, pending or completed |

### Relationships

`COURSE_CLASS 1:M CLASS_STUDENT`

One class can have many students.

`APP_USER 1:M CLASS_STUDENT`

One user can join many classes.

### Business rule

A student should not join the same class twice. Therefore, the database should have a unique constraint on:

`ClassID + UserID`

---

# 10. Rewards & Certificates Module

## Purpose

This module handles student achievements such as badges and certificates.

## Entities in this module

* `BADGE`
* `USER_BADGE`
* `CERTIFICATE`

---

## 10.1 BADGE Entity

The `BADGE` entity stores available badges in the system.

### Attributes

| Attribute          | Description                       |
| ------------------ | --------------------------------- |
| `BadgeID`          | Primary key for the badge         |
| `BadgeName`        | Name of the badge                 |
| `BadgeDescription` | Description of the badge          |
| `BadgeImage`       | Badge image path or URL           |
| `Criteria`         | Requirement for earning the badge |

### Example badges

| BadgeName              | Criteria                         |
| ---------------------- | -------------------------------- |
| First Course Completed | Complete one course              |
| Quiz Master            | Pass five quizzes                |
| Fast Learner           | Complete ten lessons in one week |

---

## 10.2 USER_BADGE Entity

The `USER_BADGE` entity resolves the many-to-many relationship between users and badges.

A user can earn many badges. A badge can be earned by many users.

### Attributes

| Attribute     | Description                                       |
| ------------- | ------------------------------------------------- |
| `UserBadgeID` | Primary key for awarded badge                     |
| `UserID`      | Foreign key linking to user who earned the badge  |
| `BadgeID`     | Foreign key linking to badge                      |
| `AwardedBy`   | Foreign key linking to user who awarded the badge |
| `AwardedAt`   | Date and time the badge was awarded               |

### Relationships

`APP_USER 1:M USER_BADGE`

One user can earn many badges.

`BADGE 1:M USER_BADGE`

One badge can be awarded to many users.

`APP_USER 1:M USER_BADGE as AwardedBy`

One admin, lecturer or system user can award many badges.

---

## 10.3 CERTIFICATE Entity

The `CERTIFICATE` entity stores certificates issued to users after completing courses.

### Attributes

| Attribute         | Description                          |
| ----------------- | ------------------------------------ |
| `CertificateID`   | Primary key for the certificate      |
| `UserID`          | Foreign key linking to user          |
| `CourseID`        | Foreign key linking to course        |
| `CertificateCode` | Unique certificate verification code |
| `IssuedDate`      | Date the certificate was issued      |
| `CertificateURL`  | Link or file path to certificate     |

### Relationships

`APP_USER 1:M CERTIFICATE`

One user can receive many certificates.

`COURSE 1:M CERTIFICATE`

One course can issue many certificates.

### Business rule

A user should usually receive only one certificate per course. Therefore, the database should have a unique constraint on:

`UserID + CourseID`

---

# 11. Admin & Approval Module

## Purpose

This module controls course review and approval. It ensures that courses are checked before being published.

## Entity in this module

* `COURSE_APPROVAL`

---

## 11.1 COURSE_APPROVAL Entity

The `COURSE_APPROVAL` entity records approval history for courses.

### Attributes

| Attribute        | Description                          |
| ---------------- | ------------------------------------ |
| `ApprovalID`     | Primary key for approval record      |
| `CourseID`       | Foreign key linking to course        |
| `ReviewedBy`     | Foreign key linking to reviewer user |
| `ApprovalStatus` | Pending, approved or rejected        |
| `Feedback`       | Reviewer feedback                    |
| `ReviewedAt`     | Date and time of review              |

### Relationships

`COURSE 1:M COURSE_APPROVAL`

One course can have many approval records.

`APP_USER 1:M COURSE_APPROVAL`

One reviewer can review many courses.

### Why one course can have many approval records

A course may be submitted more than once. For example:

1. Course creator submits course
2. Reviewer rejects course with feedback
3. Creator edits course
4. Reviewer approves the updated version

Each review action is stored as a separate approval record.

---

# 12. Subscription & Payment Module

## Purpose

This module supports paid learning plans, subscriptions and payments.

## Entities in this module

* `PRICING_PLAN`
* `SUBSCRIPTION`
* `PAYMENT`

---

## 12.1 PRICING_PLAN Entity

The `PRICING_PLAN` entity stores available subscription plans.

### Attributes

| Attribute     | Description                  |
| ------------- | ---------------------------- |
| `PlanID`      | Primary key for pricing plan |
| `PlanName`    | Name of the plan             |
| `Price`       | Plan price                   |
| `Duration`    | Duration in days or months   |
| `Description` | Plan description             |

### Example plans

| PlanName        |  Price | Duration |
| --------------- | -----: | -------: |
| Free Plan       |   0.00 |  30 days |
| Monthly Premium |  29.90 |  30 days |
| Yearly Premium  | 299.00 | 365 days |

---

## 12.2 SUBSCRIPTION Entity

The `SUBSCRIPTION` entity records user subscriptions.

### Attributes

| Attribute            | Description                             |
| -------------------- | --------------------------------------- |
| `SubscriptionID`     | Primary key for subscription            |
| `UserID`             | Foreign key linking to user             |
| `PlanID`             | Foreign key linking to pricing plan     |
| `StartDate`          | Subscription start date                 |
| `EndDate`            | Subscription end date                   |
| `PaymentStatus`      | Paid, unpaid, pending or failed         |
| `SubscriptionStatus` | Active, expired, cancelled or suspended |

### Relationships

`APP_USER 1:M SUBSCRIPTION`

One user can have many subscriptions over time.

`PRICING_PLAN 1:M SUBSCRIPTION`

One pricing plan can be used in many subscriptions.

---

## 12.3 PAYMENT Entity

The `PAYMENT` entity stores payment transactions.

### Attributes

| Attribute              | Description                                    |
| ---------------------- | ---------------------------------------------- |
| `PaymentID`            | Primary key for payment                        |
| `SubscriptionID`       | Foreign key linking to subscription            |
| `UserID`               | Foreign key linking to user                    |
| `Amount`               | Payment amount                                 |
| `PaymentMethod`        | Card, online banking, e-wallet or other method |
| `PaymentDate`          | Date and time of payment                       |
| `PaymentStatus`        | Successful, failed, pending or refunded        |
| `TransactionReference` | Unique payment transaction reference           |

### Relationships

`SUBSCRIPTION 1:M PAYMENT`

One subscription can have many payments.

`APP_USER 1:M PAYMENT`

One user can make many payments.

### Why payment links to both user and subscription

`SubscriptionID` identifies what the payment is for. `UserID` makes reporting easier because the system can directly identify who made the payment.

---

# 13. Support & Notifications Module

## Purpose

This module handles issue reporting and system notifications.

## Entities in this module

* `ISSUE_REPORT`
* `NOTIFICATION`

---

## 13.1 ISSUE_REPORT Entity

The `ISSUE_REPORT` entity stores problems reported by users.

### Attributes

| Attribute          | Description                                        |
| ------------------ | -------------------------------------------------- |
| `IssueID`          | Primary key for issue report                       |
| `ReportedBy`       | Foreign key linking to user who reported the issue |
| `CourseID`         | Optional foreign key linking to course             |
| `LessonID`         | Optional foreign key linking to lesson             |
| `IssueTitle`       | Short issue title                                  |
| `IssueDescription` | Detailed issue explanation                         |
| `IssueStatus`      | Open, in progress, resolved or closed              |
| `CreatedAt`        | Date and time the issue was created                |
| `ResolvedAt`       | Date and time the issue was resolved               |

### Relationships

`APP_USER 1:M ISSUE_REPORT`

One user can submit many issue reports.

`COURSE 1:M ISSUE_REPORT`

One course can have many related issue reports.

`LESSON 1:M ISSUE_REPORT`

One lesson can have many related issue reports.

### Important point

`CourseID` and `LessonID` are optional because an issue may be general. For example, a user may report a login problem that is not related to any course or lesson.

---

## 13.2 NOTIFICATION Entity

The `NOTIFICATION` entity stores messages sent to users.

### Attributes

| Attribute             | Description                                      |
| --------------------- | ------------------------------------------------ |
| `NotificationID`      | Primary key for notification                     |
| `UserID`              | Foreign key linking to receiver                  |
| `NotificationTitle`   | Notification title                               |
| `NotificationMessage` | Notification content                             |
| `IsRead`              | Shows whether the user has read the notification |
| `CreatedAt`           | Date and time the notification was created       |

### Relationship

`APP_USER 1:M NOTIFICATION`

One user can receive many notifications.

### Example notifications

* Course enrolment successful
* New lesson added
* Quiz passed
* Certificate issued
* Subscription expiring soon
* Issue report resolved

---

# 14. Full Relationship Summary

| Relationship                      | Cardinality  | Explanation                                          |
| --------------------------------- | ------------ | ---------------------------------------------------- |
| `ROLE` to `APP_USER`              | 1:M          | One role can be assigned to many users               |
| `APP_USER` to `STUDENT_PROFILE`   | 1:0..1       | One user can optionally have one student profile     |
| `APP_USER` to `LECTURER_PROFILE`  | 1:0..1       | One user can optionally have one lecturer profile    |
| `APP_USER` to `COURSE`            | 1:M          | One creator can create many courses                  |
| `COURSE_CATEGORY` to `COURSE`     | 1:M          | One category can contain many courses                |
| `COURSE` to `COURSE_SECTION`      | 1:M          | One course can contain many sections                 |
| `COURSE_SECTION` to `LESSON`      | 1:M          | One section can contain many lessons                 |
| `APP_USER` to `ENROLLMENT`        | 1:M          | One user can have many enrolments                    |
| `COURSE` to `ENROLLMENT`          | 1:M          | One course can have many enrolments                  |
| `ENROLLMENT` to `LESSON_PROGRESS` | 1:M          | One enrolment can track many lesson progress records |
| `LESSON` to `LESSON_PROGRESS`     | 1:M          | One lesson can appear in many progress records       |
| `COURSE` to `QUIZ`                | 1:M          | One course can have many quizzes                     |
| `LESSON` to `QUIZ`                | 1:M optional | One lesson can optionally have quizzes               |
| `QUIZ` to `QUESTION`              | 1:M          | One quiz can contain many questions                  |
| `QUESTION` to `ANSWER_OPTION`     | 1:M          | One question can have many answer options            |
| `APP_USER` to `QUIZ_ATTEMPT`      | 1:M          | One user can make many quiz attempts                 |
| `QUIZ` to `QUIZ_ATTEMPT`          | 1:M          | One quiz can have many attempts                      |
| `APP_USER` to `COURSE_CLASS`      | 1:M          | One lecturer can create many classes                 |
| `COURSE` to `COURSE_CLASS`        | 1:M          | One course can be assigned to many classes           |
| `COURSE_CLASS` to `CLASS_STUDENT` | 1:M          | One class can have many student records              |
| `APP_USER` to `CLASS_STUDENT`     | 1:M          | One student can join many classes                    |
| `BADGE` to `USER_BADGE`           | 1:M          | One badge can be awarded many times                  |
| `APP_USER` to `USER_BADGE`        | 1:M          | One user can earn many badges                        |
| `APP_USER` to `CERTIFICATE`       | 1:M          | One user can receive many certificates               |
| `COURSE` to `CERTIFICATE`         | 1:M          | One course can issue many certificates               |
| `COURSE` to `COURSE_APPROVAL`     | 1:M          | One course can have many approval records            |
| `APP_USER` to `COURSE_APPROVAL`   | 1:M          | One reviewer can review many courses                 |
| `APP_USER` to `ISSUE_REPORT`      | 1:M          | One user can submit many issue reports               |
| `APP_USER` to `NOTIFICATION`      | 1:M          | One user can receive many notifications              |
| `PRICING_PLAN` to `SUBSCRIPTION`  | 1:M          | One plan can be used in many subscriptions           |
| `APP_USER` to `SUBSCRIPTION`      | 1:M          | One user can have many subscriptions                 |
| `SUBSCRIPTION` to `PAYMENT`       | 1:M          | One subscription can have many payment records       |
| `APP_USER` to `PAYMENT`           | 1:M          | One user can make many payments                      |

---

# 15. How Many-to-Many Relationships Are Solved

A proper relational database should not store many-to-many relationships directly. This ERD correctly uses bridge tables.

## User and Course

A user can enrol in many courses. A course can have many users.

Resolved using:

`ENROLLMENT`

## User and Quiz

A user can attempt many quizzes. A quiz can be attempted by many users.

Resolved using:

`QUIZ_ATTEMPT`

## User and Class

A user can join many classes. A class can have many users.

Resolved using:

`CLASS_STUDENT`

## User and Badge

A user can earn many badges. A badge can be earned by many users.

Resolved using:

`USER_BADGE`

## User and Pricing Plan

A user can subscribe to many pricing plans over time. A pricing plan can be used by many users.

Resolved using:

`SUBSCRIPTION`

---

# 16. CRUD Operation Support

The ERD supports all main CRUD operations required by the assignment.

CRUD means:

* Create
* Read
* Update
* Delete

## User CRUD

Admin can:

* Create users
* View users
* Update user details
* Suspend or delete user accounts

Affected tables:

* `APP_USER`
* `ROLE`
* `STUDENT_PROFILE`
* `LECTURER_PROFILE`

## Course CRUD

Course creator or admin can:

* Create courses
* View course list
* Update course information
* Delete or disable courses

Affected tables:

* `COURSE`
* `COURSE_CATEGORY`
* `COURSE_SECTION`
* `LESSON`

## Lesson CRUD

Course creator can:

* Add lessons
* Edit lesson content
* Upload lesson resources
* Delete lessons

Affected tables:

* `COURSE_SECTION`
* `LESSON`

## Quiz CRUD

Course creator or lecturer can:

* Create quizzes
* Add questions
* Add answer options
* Edit quiz details
* Delete quizzes

Affected tables:

* `QUIZ`
* `QUESTION`
* `ANSWER_OPTION`

## Enrolment CRUD

Student can:

* Enrol in a course
* View enrolled courses
* Continue learning
* Track progress

Affected tables:

* `ENROLLMENT`
* `LESSON_PROGRESS`

## Class CRUD

Lecturer can:

* Create class
* Generate class code
* Manage class students
* Update class status

Affected tables:

* `COURSE_CLASS`
* `CLASS_STUDENT`

## Support CRUD

User can:

* Submit issue report
* View issue status

Admin can:

* Update issue status
* Resolve issues

Affected tables:

* `ISSUE_REPORT`
* `NOTIFICATION`

## Subscription and Payment CRUD

User can:

* Select plan
* Subscribe
* Make payment
* View payment history

Admin can:

* View subscriptions
* Update payment status
* Manage pricing plans

Affected tables:

* `PRICING_PLAN`
* `SUBSCRIPTION`
* `PAYMENT`

---

# 17. Authentication and Authorization Explanation

The system supports authentication through the `APP_USER` table.

When a user registers, the system stores:

* Full name
* Email
* Password hash
* Phone number
* Role
* Account status

When a user logs in, the system checks:

1. Email exists
2. Password hash matches
3. Account status is active
4. User role is retrieved from `ROLE`

After login, the system uses the role to decide what the user can access.

Example:

| Role              | Access                                                              |
| ----------------- | ------------------------------------------------------------------- |
| Student           | Browse, enrol, learn, attempt quiz, earn badge, receive certificate |
| Lecturer          | Create class, manage class students, monitor progress               |
| Course Creator    | Create and manage course content                                    |
| Leader / Reviewer | Review and approve submitted courses                                |
| Admin             | Manage users, payments, issues, courses and reports                 |

---

# 18. Non-Registered User Support

The system supports non-registered users without needing a separate table.

A non-registered user can:

* Visit the website
* Browse course categories
* View public course details
* Read general information
* Register for an account

A non-registered user cannot:

* Enrol in a course
* Track lesson progress
* Attempt quizzes
* Earn badges
* Receive certificates
* Submit issue reports
* Make payments

This is correct because non-registered users do not need to be stored in the database unless the system tracks guest analytics or guest sessions.

---

# 19. Important Database Constraints

To make the ERD implementation-ready, the following constraints should be used.

## Unique constraints

| Table             | Unique field           |
| ----------------- | ---------------------- |
| `APP_USER`        | `Email`                |
| `COURSE_CATEGORY` | `CategoryName`         |
| `COURSE_CLASS`    | `ClassCode`            |
| `BADGE`           | `BadgeName`            |
| `CERTIFICATE`     | `CertificateCode`      |
| `PRICING_PLAN`    | `PlanName`             |
| `PAYMENT`         | `TransactionReference` |

## Composite unique constraints

| Table             | Composite unique fields   | Reason                                                            |
| ----------------- | ------------------------- | ----------------------------------------------------------------- |
| `ENROLLMENT`      | `UserID + CourseID`       | Prevent duplicate enrolment                                       |
| `LESSON_PROGRESS` | `EnrollmentID + LessonID` | Prevent duplicate progress records                                |
| `CLASS_STUDENT`   | `ClassID + UserID`        | Prevent same student joining same class twice                     |
| `USER_BADGE`      | `UserID + BadgeID`        | Prevent duplicate badge awards unless repeated badges are allowed |
| `CERTIFICATE`     | `UserID + CourseID`       | Prevent duplicate certificates for same course                    |

---

# 20. Recommended SQL Server Data Types

For implementation in SQL Server, the attributes can use these data types.

| ERD type          | SQL Server type                      |
| ----------------- | ------------------------------------ |
| `int`             | `INT IDENTITY(1,1)` for primary keys |
| `string`          | `NVARCHAR(255)` or `NVARCHAR(MAX)`   |
| `datetime`        | `DATETIME2`                          |
| `date`            | `DATE`                               |
| `decimal`         | `DECIMAL(10,2)`                      |
| `boolean`         | `BIT`                                |
| Long text         | `NVARCHAR(MAX)`                      |
| Image or file URL | `NVARCHAR(500)`                      |

Examples:

* `Email` → `NVARCHAR(255)`
* `PasswordHash` → `NVARCHAR(500)`
* `LessonContent` → `NVARCHAR(MAX)`
* `CourseDescription` → `NVARCHAR(MAX)`
* `Price` → `DECIMAL(10,2)`
* `IsRead` → `BIT`

---

# 21. Suggested Status Values

For consistency, status fields should use controlled values.

## AccountStatus

* Active
* Inactive
* Suspended
* Pending

## CourseStatus

* Draft
* PendingReview
* Approved
* Rejected
* Published
* Archived

## CompletionStatus

* NotStarted
* InProgress
* Completed

## PassedStatus

* Passed
* Failed

## ClassStatus

* Active
* Inactive
* Completed
* Cancelled

## ApprovalStatus

* Pending
* Approved
* Rejected

## IssueStatus

* Open
* InProgress
* Resolved
* Closed

## PaymentStatus

* Pending
* Successful
* Failed
* Refunded

## SubscriptionStatus

* Active
* Expired
* Cancelled
* Suspended

---

# 22. End-to-End System Flow

This is how the ERD supports the full user journey.

## Step 1: User registration

A new user registers through the website.

Data is stored in:

* `APP_USER`
* `STUDENT_PROFILE` if the user is a student
* `LECTURER_PROFILE` if the user is a lecturer

The user gets a role through:

* `ROLE`

---

## Step 2: Course creation

A course creator creates a course.

Data is stored in:

* `COURSE`
* `COURSE_CATEGORY`
* `COURSE_SECTION`
* `LESSON`

The course starts as draft or pending review.

---

## Step 3: Course approval

A leader or admin reviews the course.

Data is stored in:

* `COURSE_APPROVAL`

The course status in `COURSE` is updated to approved, rejected or published.

---

## Step 4: Student enrolment

A student enrols in a course.

Data is stored in:

* `ENROLLMENT`

This connects the student to the course.

---

## Step 5: Student learning progress

As the student completes lessons, progress is recorded.

Data is stored in:

* `LESSON_PROGRESS`

The completion percentage in `ENROLLMENT` is updated.

---

## Step 6: Quiz attempt

The student attempts a quiz.

Data is read from:

* `QUIZ`
* `QUESTION`
* `ANSWER_OPTION`

Attempt result is stored in:

* `QUIZ_ATTEMPT`

---

## Step 7: Rewards and certificate

When the student completes learning requirements, the system can award a badge or issue a certificate.

Data is stored in:

* `USER_BADGE`
* `CERTIFICATE`

---

## Step 8: Notification

The student receives notifications about enrolment, quiz results, certificates or issue updates.

Data is stored in:

* `NOTIFICATION`

---

## Step 9: Subscription and payment

If the course or platform requires payment, the user selects a pricing plan and makes payment.

Data is stored in:

* `PRICING_PLAN`
* `SUBSCRIPTION`
* `PAYMENT`

---

## Step 10: Issue reporting

If a user finds a problem, they submit an issue report.

Data is stored in:

* `ISSUE_REPORT`

Admin can update the status and notify the user.

---

# 23. Why This ERD Is Normalized

The ERD follows proper database normalization.

## First Normal Form

Each table stores atomic values. For example, user details are stored in separate fields like `FullName`, `Email` and `PhoneNumber`.

## Second Normal Form

Bridge tables such as `ENROLLMENT`, `CLASS_STUDENT` and `USER_BADGE` prevent repeating groups and correctly handle many-to-many relationships.

## Third Normal Form

Data is separated into logical entities. For example, role data is stored in `ROLE` instead of repeating role names inside every user record.

This reduces duplication and improves data consistency.

---

# 24. Why the ERD Is Suitable for .NET / SQL Server

This ERD is implementation-ready for a .NET web application because:

* Every entity can become an Entity Framework model class.
* Every primary key can become an identity column.
* Every foreign key can be configured using Entity Framework relationships.
* Status fields can be represented using enums.
* Authentication data is separated from profile data.
* CRUD operations map directly to controllers, services and repositories.
* SQL Server constraints can be applied easily.
* File fields can store upload paths or URLs.
* The ERD supports real-world web application modules.

Example .NET model mapping:

`APP_USER` → `AppUser.cs`

`COURSE` → `Course.cs`

`ENROLLMENT` → `Enrollment.cs`

`QUIZ_ATTEMPT` → `QuizAttempt.cs`

---

# 25. Suggested Report Explanation

You can paste this into your assignment report:

> The ERD represents a Web-based Learning System designed for a .NET and SQL Server environment. The system supports registered users, non-registered visitors, role-based access control, course management, lesson management, learning progress tracking, quiz assessment, class management, rewards, certificates, course approval, issue reporting, notifications, subscriptions and payments.
>
> The central entity of the system is `APP_USER`, which stores registered user information such as name, email, password hash, profile image and account status. Each user is assigned a role through the `ROLE` entity. The role determines system access for students, lecturers, course creators, leaders/reviewers and administrators.
>
> Course content is managed through `COURSE_CATEGORY`, `COURSE`, `COURSE_SECTION` and `LESSON`. A course belongs to one category and can contain many sections. Each section can contain many lessons. This structure allows learning content to be organised clearly.
>
> Student learning activity is handled through `ENROLLMENT` and `LESSON_PROGRESS`. The `ENROLLMENT` table resolves the many-to-many relationship between users and courses because one user can enrol in many courses and one course can have many users. The `LESSON_PROGRESS` table records lesson completion for each enrolment.
>
> Assessment is managed through `QUIZ`, `QUESTION`, `ANSWER_OPTION` and `QUIZ_ATTEMPT`. A course can have many quizzes and each quiz can contain many questions. Each question can have many answer options. Quiz attempts are recorded separately so the system can track student scores and pass/fail status.
>
> The class management module uses `COURSE_CLASS` and `CLASS_STUDENT`. A lecturer can create many classes for courses and each class can contain many students. The `CLASS_STUDENT` table resolves the many-to-many relationship between classes and users.
>
> The rewards module includes `BADGE`, `USER_BADGE` and `CERTIFICATE`. Users can earn many badges and receive certificates after completing courses. The `USER_BADGE` table resolves the many-to-many relationship between users and badges.
>
> The admin and approval module uses `COURSE_APPROVAL` to record course review decisions. This allows leaders or administrators to approve, reject or provide feedback for courses before publication.
>
> The subscription and payment module uses `PRICING_PLAN`, `SUBSCRIPTION` and `PAYMENT`. This allows the system to support free or paid learning plans.
>
> The support and notification module uses `ISSUE_REPORT` and `NOTIFICATION`. Users can report issues related to courses or lessons and receive notifications about system activities.
>
> Overall, the ERD is normalized and implementation-ready because it separates data into meaningful entities, reduces duplication, uses bridge tables for many-to-many relationships and clearly defines primary keys, foreign keys and cardinalities.

---

# 26. What to Say During Presentation

You can explain it like this:

> Our ERD is designed for a web-based learning platform. The main entity is `APP_USER` because every registered person in the system is stored there. The `ROLE` table controls what each user can do in the system. For example, students can enrol in courses and attempt quizzes while lecturers can create classes.
>
> The course structure is separated into course, section and lesson. This makes the system flexible because one course can have many sections and each section can have many lessons.
>
> The `ENROLLMENT` table is important because it solves the many-to-many relationship between users and courses. It also stores course completion percentage and last accessed date.
>
> The quiz module uses quiz, question, answer option and quiz attempt tables. This allows the system to store quiz content separately from student attempt results.
>
> We also included class management, badge rewards, certificates, course approvals, subscriptions, payments, issue reports and notifications. These modules make the ERD more complete and suitable for a real learning management system.
>
> Overall, the ERD is normalized, role-based and ready to be implemented using SQL Server and .NET.

---

# 27. Final Evaluation

This ERD is strong because it covers:

* Authentication
* User roles
* Student profiles
* Lecturer profiles
* Course creation
* Course categorisation
* Section and lesson structure
* Enrolment
* Progress tracking
* Quizzes
* Questions
* Answer options
* Quiz attempts
* Class management
* Student-class membership
* Badges
* Certificates
* Course approval
* Issue reporting
* Notifications
* Pricing plans
* Subscriptions
* Payments

It is not just a basic ERD. It is a complete learning management system database design that is suitable for a final university Web Applications assignment.

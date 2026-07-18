# CTRL+PASS — Current Project Status

## 1. Project foundation — completed

- ASP.NET Core MVC project using .NET 10.
- Microsoft SQL Server LocalDB connected.
- Entity Framework Core configured.
- Database migrations working.
- Bootstrap and Razor views working.
- Role-based authorization established.
- Registration, login and logout working.
- Inactive users are blocked from logging in.
- Application uses a custom `ApplicationUser`.
- `FullName`, account status, school assignment and creation date are stored.
- Database seeding is available.

## 2. Roles — completed

These roles exist:

- Student
- Instructor
- Course Creator
- Academic Leader
- Admin

Role-based navigation and dashboard redirection work.

## 3. Schools — completed

The four schools are stored in SQL Server:

- School of Computing
- School of Technology
- School of Business
- School of Engineering

The following roles can be assigned to one school:

- Instructor
- Course Creator
- Academic Leader

Course codes use separate school sequences:

- `COM-0001`
- `TEC-0001`
- `BUS-0001`
- `ENG-0001`

## 4. Admin user management — completed

The Admin can:

- View users.
- Create users.
- Edit users.
- Assign roles.
- Assign Instructors, Course Creators and Academic Leaders to schools.
- Activate and deactivate accounts.
- Prevent accidental self-deactivation.
- See each user’s role, school and account status.

## 5. Course model and workflow — completed

The `Course` structure includes course code, title, description, thumbnail path, school, Course Creator, access level, status, maintenance status, creation and update dates, and submission, approval and publication dates.

Course statuses:

- Draft
- Under Review
- Changes Requested
- Approved
- Published

Course access levels:

- Free
- Premium
- Enterprise

Implemented workflow:

```text
Course Creator creates Draft
        ↓
Course Creator submits for review
        ↓
Status becomes Under Review
        ↓
Academic Leader reviews
        ↓
Changes Requested or Approved
        ↓
Course Creator edits and resubmits if required
        ↓
Course Creator publishes an Approved course
        ↓
Status becomes Published
```

## 6. Course Creator dashboard — completed

The dashboard displays total courses, Draft courses, courses Under Review, Published courses, course code, title, access level, status, last updated time and actions.

Actions change according to status:

- Draft → Edit and Design
- Changes Requested → Edit and Design
- Under Review → View Design
- Approved → View Design and Publish Course
- Published → View Design

## 7. Course creation and editing — completed

The Course Creator can create a course, receive an automatic school-based course code, set title, description and access level, edit Draft and Changes Requested courses, view validation messages and update the modified date.

## 8. Course sections — completed

The Course Creator can add, edit, move and delete sections. Section order is generated automatically and repaired after deletion. Deleting a section also removes its activities, options and uploaded files.

## 9. Course activities — completed

The following 10 activity types are implemented:

1. Text Content
2. Image
3. Video
4. Document/File
5. External Link
6. Short Answer Question
7. Paragraph Question
8. Multiple Choice Question
9. Checkbox Question
10. Dropdown Question

The Course Creator can create, edit, move and delete activities. The activity type remains locked after creation. Uploaded files can be replaced and old files are cleaned up.

## 10. File uploads — completed

Images: `.jpg`, `.jpeg`, `.png`, `.webp`, maximum 5 MB.

Videos: `.mp4`, `.webm`, maximum 100 MB. A video uses either an upload or an external URL, not both.

Documents: `.pdf`, `.doc`, `.docx`, `.ppt`, `.pptx`, `.xls`, `.xlsx`, `.txt`, maximum 20 MB.

Files are stored under:

```text
wwwroot/uploads/course-activities/
```

Unique generated filenames are used.

## 11. Question options — completed

The Course Creator can add, edit, delete and reorder options.

Rules implemented:

- Multiple Choice and Dropdown questions allow only one correct answer.
- Checkbox questions can contain multiple correct answers.
- Deleted options are reordered automatically.
- Deleting a correct answer produces a warning.

## 12. Submission validation — completed

Before submission, the system checks:

- The course has at least one section.
- Each section has at least one activity.
- Required text, files and URLs exist.
- Video activities use exactly one source.
- Option-based questions contain at least two options.
- Multiple Choice and Dropdown questions have exactly one correct answer.
- Checkbox questions have at least one correct answer.

## 13. Academic Leader review — completed

The `CourseReview` table stores course, Academic Leader, decision, comments and review date.

The Academic Leader can:

- View only non-Draft courses from their assigned school.
- Review all sections, activities and options.
- View correct answers and model answers.
- Request changes with required comments.
- Approve a corrected course.
- Preserve full review history.

The Course Creator can see Academic Leader feedback, edit a Changes Requested course and resubmit it.

## 14. Course publication — completed

The Course Creator can publish an Approved course. Publication records the date, changes the status to Published and makes the course available for Instructor class creation.

## 15. Instructor dashboard — completed

The Instructor dashboard displays:

- Assigned school
- Total classes
- Active classes
- Inactive classes
- Available Published courses from the assigned school
- Instructor-owned classes

Only Published courses from the Instructor’s assigned school are available. Courses under maintenance are excluded.

## 16. Instructor class creation — completed

The `CourseClass` table has been created.

A class stores:

- Automatically generated class code
- Class name
- Optional description
- Selected Published course
- Instructor
- Start date
- End date
- Active status
- Creation and update dates

Class code format:

```text
CLS-0001
```

The Instructor can create a class only from a Published course belonging to their assigned school. The end date must be after the start date.

Current test class:

```text
CLS-0001 — Cybersecurity September Intake
```

## 17. Locked subclass decision

Each subclass will receive an automatically generated code:

```text
SUB-0001
```

A subclass will belong to one Instructor class.

# Confirmed but not implemented yet

## Course Creator

- Course thumbnail upload.
- Full learner-style course preview.
- Enter and leave maintenance mode.
- Notifications.
- Profile pages.

## Academic Leader

- Filter courses by status.
- Place Published courses under maintenance and remove maintenance status.
- Receive and manage reported issues.
- Forward issue details to the Course Creator.
- Reports.
- Notifications.
- Profile page.

## Instructor

- Manage a class.
- Edit class details.
- Activate or deactivate a class.
- Create, edit and delete subclasses.
- Enrol and remove students.
- View, search and filter enrolled students.
- View student progress.
- Add notes for students.
- Generate and export reports.
- Report course issues.
- Profile and notifications.

Likely remaining Instructor structures:

- `CourseSubclass`
- `ClassEnrollment`
- `InstructorNote`

## Student

Still required:

- Student dashboard.
- Published-course access based on membership.
- Class and subclass enrolment.
- Course activity completion.
- Short, paragraph, Multiple Choice, Checkbox and Dropdown submissions.
- Quiz results.
- Saved progress and completion status.
- Course history.
- Issue reporting.
- Notifications.
- Profile and membership tabs.

Likely Student structures:

- `StudentProgress`
- `ActivityCompletion`
- `ActivitySubmission`
- `StudentAnswer`
- `CourseEnrollment`

## Guest

Still required:

- Public home page or Guest dashboard.
- Browse Free courses.
- Temporary course access with no saved progress.
- No issue reporting.
- No profile.
- Sign-up and membership promotion.

## Membership plans

| Plan | Price | Access |
|---|---:|---|
| Free | RM0 | Free courses |
| Premium | RM240/year | Free and Premium courses |
| Enterprise | RM300/year | All courses |

Still required: membership records, plan selection, access checks, upgrade interface, expiry and renewal handling.

## Progress tracking

Still required: activity completion, completion dates, percentage calculation, progress bars, Not Started/In Progress/Completed states, quiz attempts and Instructor progress views.

## Issue reporting

Still required: issue form, course/activity reference, reporter, status, Academic Leader review, forwarding to Course Creator, response, resolution and notifications. Guests cannot report issues.

## Notifications

Still required: notification table, list, read/unread state, links and badge for enrolment, review, publication, maintenance and issue events.

## Profiles

Student, Instructor, Course Creator and Academic Leader profile pages and role-specific tabs remain to be implemented.

## Admin website management

Still required: About Us, Contact, Policies, general website information, all-course view, issue view and system statistics.

## Public pages

Still required: Home, About Us, Contact Us, Policies, course catalogue, course details and membership plans.

## Reports

Still required: student progress, class progress, course completion, Academic Leader review, issue reports, HTML reports and CSV export.

## Security and final validation

Still required: full role testing, ID-tampering tests, file validation review, workflow transition tests, error pages, deletion confirmations, inactive-account tests and unauthorised-access tests.

## Final UI work

Still required: final navigation, role-specific menu items, consistent styling, responsive layout, pagination, search/filtering, final `CTRL+PASS` branding, footer and public links.

# Overall position

Completed work now covers:

1. Core project setup
2. SQL Server and EF Core
3. Identity and roles
4. Admin user management
5. School assignment
6. Course creation and editing
7. Sections and ten activity types
8. File uploads and question options
9. Submission validation
10. Academic Leader review and approval
11. Review history and resubmission
12. Course publication
13. Instructor dashboard
14. Instructor class creation

Next stage:

```text
Instructor manages CLS-0001
        ↓
Instructor creates SUB-0001
        ↓
Instructor enrols Students into the subclass
```

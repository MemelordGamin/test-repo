
# Current project status

## 1. Project foundation — completed

* ASP.NET Core MVC project using .NET 10.
* Microsoft SQL Server LocalDB connected.
* Entity Framework Core configured.
* Database migrations working.
* Bootstrap and Razor views working.
* Role-based authorization established.
* Registration, login and logout working.
* Inactive users are blocked from logging in.
* Application uses a custom `ApplicationUser`.
* `FullName`, account status, school assignment and creation date are stored.
* Database seeding is available.

## 2. Roles — completed

These roles exist:

* Student
* Instructor
* Course Creator
* Academic Leader
* Admin

Role-based navigation and dashboard redirection work.

The dashboards currently exist, but several are still basic placeholders until their main features are created.

## 3. Schools — completed

The four schools are stored in SQL Server:

* School of Computing
* School of Technology
* School of Business
* School of Engineering

Course Creators and Academic Leaders can be assigned to one school.

Course codes use separate school sequences:

* `COM-0001`
* `TEC-0001`
* `BUS-0001`
* `ENG-0001`

## 4. Admin user management — completed

The Admin can:

* View users.
* Create users.
* Edit users.
* Assign roles.
* Assign Course Creators and Academic Leaders to schools.
* Activate and deactivate accounts.
* Prevent accidental self-deactivation.
* See each user’s role, school and account status.

## 5. Course model and workflow structure — completed

The `Course` database structure includes:

* Course code
* Title
* Description
* Thumbnail path
* School
* Course Creator
* Access level
* Status
* Maintenance status
* Creation and update dates
* Submission, approval and publication dates

The course statuses are locked as:

* Draft
* Under Review
* Changes Requested
* Approved
* Published

The access levels are:

* Free
* Premium
* Enterprise

The full review workflow is designed but not implemented yet.

## 6. Course Creator dashboard — completed

The Course Creator dashboard displays:

* Total courses
* Draft courses
* Courses under review
* Published courses
* Course code
* Course title
* Access level
* Status
* Last updated time
* Course actions

The Course Creator can create a course and save it as a Draft.

## 7. Course creation and editing — completed

The Course Creator can:

* Create a new course.
* Receive an automatically generated course code.
* Set the title.
* Set the description.
* Set the access level.
* Edit a Draft course.
* Edit a course after changes have been requested.
* View validation messages.
* Update the course’s last-modified time.

## 8. Course sections — completed

The `CourseSection` table has been created.

The Course Creator can:

* Add sections.
* Automatically assign section order.
* View sections in order.
* Edit section title and description.
* Move sections up.
* Move sections down.
* Prevent editing while the course is locked.
* See section order on the design page.

Each course can contain multiple sections.

## 9. Course activity types — completed

The following 10 activity types are locked:

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

## 10. Course activity database — completed

The `CourseActivity` table stores:

* Section
* Activity type
* Title
* Instructions
* Text content
* File path
* External URL
* Model answer
* Display order
* Required or optional status
* Creation and update dates

Each activity belongs to one section.

## 11. Activity file-upload rules — completed

The validation rules are implemented.

### Images

Allowed:

* `.jpg`
* `.jpeg`
* `.png`
* `.webp`

Maximum size:

* 5 MB

### Videos

Allowed:

* `.mp4`
* `.webm`

Maximum size:

* 100 MB

A video can use either:

* An uploaded file, or
* An external URL

It cannot use both simultaneously.

### Documents

Allowed:

* `.pdf`
* `.doc`
* `.docx`
* `.ppt`
* `.pptx`
* `.xls`
* `.xlsx`
* `.txt`

Maximum size:

* 20 MB

Files are stored under:

```text
wwwroot/uploads/course-activities/
```

Generated unique filenames are used.

## 12. Creating activities — completed

The Course Creator can:

* Select an activity type.
* Enter a title.
* Enter instructions.
* Add text content.
* Upload a file.
* Add an external URL.
* Enter a model answer.
* Mark an activity as required or optional.
* Save activities into SQL Server.
* Automatically assign activity order.

Input requirements change according to the selected activity type.

## 13. Displaying activities — completed

The Design Course page displays:

* Activity number
* Activity title
* Activity type
* Required or optional status
* Instructions
* Text content
* Images
* Uploaded videos
* Video links
* Documents
* External links
* Model answers
* Question options

Activities are grouped under their correct sections.

## 14. Question options — completed

The `CourseActivityOption` table has been created.

The Course Creator can:

* Create Multiple Choice questions.
* Create Checkbox questions.
* Create Dropdown questions.
* Open the Manage Question Options page.
* Add answer options.
* Mark options as correct.
* View existing options.
* See options on the Course Design page.

For Multiple Choice and Dropdown questions:

* Only one option can remain correct.

For Checkbox questions:

* Multiple options can be correct.

At least two options will be required before review submission, although submission validation has not been built yet.

# Confirmed but not implemented yet

These decisions are already locked but still need code.

## Course Creator

* Edit activities.
* Keep activity type locked after creation.
* Replace uploaded files.
* Delete activities.
* Move activities up and down.
* Delete question options.
* Edit question options.
* Reorder question options.
* Validate that option-based questions have at least two options.
* Ensure Multiple Choice and Dropdown questions have exactly one correct answer.
* Ensure Checkbox questions have at least one correct answer.
* Course thumbnail upload.
* Full learner-style course preview.
* Submit course for review.
* View Academic Leader comments.
* Re-edit a Changes Requested course.
* Publish an Approved course.
* Enter and leave maintenance mode for published courses.
* Course Creator notifications.
* Course Creator profile pages.

# Major modules still required

## 1. Academic Leader module

The Academic Leader still needs:

* School-specific dashboard.
* View only courses from their assigned school.
* Filter courses by status.
* Open a submitted course.
* Review it like a learner without saving progress.
* View all sections and activities.
* Write review comments.
* Request changes.
* Approve courses.
* Record approval date.
* Temporarily place a published course under maintenance.
* Remove maintenance status.
* Receive reported issues.
* Send issue details to the Course Creator.
* Generate reports.
* Notifications.
* Profile page.

A `CourseReview` table still needs to be created.

## 2. Course submission and publication workflow

The main workflow still needs implementation:

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
Course Creator edits if required
        ↓
Course Creator publishes Approved course
        ↓
Status becomes Published
```

Necessary validation includes:

* Course must have at least one section.
* Each section must have at least one activity.
* Question activities must have enough options.
* Correct answers must be configured.
* Required fields and files must exist.

## 3. Instructor module

The Instructor still needs:

* Instructor dashboard.
* Browse published courses.
* Select a published course.
* Create a Class.
* Create Subclasses.
* Enrol students.
* Remove students.
* View enrolled students.
* Search and filter students.
* View student progress using progress bars.
* View progress by class.
* View progress by course.
* Add notes or comments for students.
* Generate progress reports.
* Export reports as CSV.
* Report course issues.
* Instructor profile.
* Instructor notifications.

Likely database structures still required:

* `Class`
* `Subclass`
* `ClassEnrollment`
* `InstructorNote`

## 4. Student module

The Student still needs:

* Student dashboard.
* Browse available published courses.
* Access courses according to membership plan.
* Join or be enrolled into classes.
* Open course sections and activities.
* Complete required activities.
* Submit short and paragraph answers.
* Answer Multiple Choice questions.
* Answer Checkbox questions.
* Answer Dropdown questions.
* Receive quiz results.
* Save activity completion.
* Calculate course progress.
* View enrolled courses.
* View courses in progress.
* View completed courses.
* View learning history.
* Report course issues.
* Receive notifications.
* Profile details tab.
* Membership plan tab.
* Progress/history tab.

Likely database structures still required:

* `StudentProgress`
* `ActivityCompletion`
* `ActivitySubmission`
* `StudentAnswer`
* `CourseEnrollment`

## 5. Guest module

Guests still need:

* Guest dashboard or public home page.
* Browse public Free courses.
* Open course content.
* Complete activities temporarily.
* No saved progress.
* No issue-reporting button.
* No profile.
* Sign-up button.
* Membership promotion.

Guest access must remain separate from Student progress records.

## 6. Membership plans

The plans are agreed:

| Plan       |      Price | Access                   |
| ---------- | ---------: | ------------------------ |
| Free       |        RM0 | Free courses             |
| Premium    | RM240/year | Free and Premium courses |
| Enterprise | RM300/year | All courses              |

Still required:

* Membership plan database structure.
* Student plan selection.
* Current membership display.
* Access checks.
* Upgrade interface.
* Expiry and renewal handling.
* Enterprise access rules.

A real payment gateway is not essential unless required by the lecturer. A simulated membership selection can demonstrate the feature.

## 7. Progress tracking

Progress still needs to be implemented.

Required functions include:

* Mark activities complete.
* Save activity completion date.
* Track required activities.
* Calculate percentage completed.
* Display progress bars.
* Mark courses as:

  * Not Started
  * In Progress
  * Completed
* Store quiz attempts.
* Store submitted answers.
* Allow instructors to view progress.

## 8. Issue-reporting system

Students and Instructors should be able to report issues.

Still required:

* Issue-report form.
* Issue title.
* Description.
* Course and activity reference.
* Reporter.
* Date reported.
* Issue status.
* Academic Leader review.
* Forwarding the problem to the Course Creator.
* Course Creator response.
* Resolution status.
* Notifications.

Guests cannot report issues.

## 9. Notification system

Notifications still need to be built for events such as:

* Student enrolled.
* Student removed.
* Course submitted.
* Course under review.
* Changes requested.
* Course approved.
* Course published.
* Course under maintenance.
* Issue reported.
* Issue forwarded.
* Issue resolved.

Still required:

* Notification table.
* Notification list.
* Read/unread state.
* Notification links.
* Notification badge.

## 10. Profiles

Profiles still need to be completed.

### Student

* Profile details
* Membership
* Course history
* Progress
* Enrolled courses

### Instructor

* Profile details
* Membership
* Classes
* Student completion statistics
* Reports

### Course Creator

Recommended tabs:

* Profile details
* My courses
* Drafts
* Courses under review
* Approved and published courses
* Review history

### Academic Leader

* Profile details
* Assigned school
* Reviews completed
* Courses approved
* Issues handled

## 11. Admin website management

Admin user management is complete, but general website management remains.

Still required:

* Edit About Us content.
* Edit Contact information.
* Edit Policies.
* Manage general website information.
* View all courses.
* View reported issues.
* Basic system statistics.

## 12. Public pages

Still required:

* Home page
* About Us
* Contact Us
* Policies
* Course catalogue
* Course details
* Membership plans page

## 13. Reports

Still required:

* Student progress report.
* Class progress report.
* Course completion report.
* Academic Leader review report.
* Issue report.
* Instructor report dashboard.
* HTML report display.
* CSV export.

## 14. Security and final validation

Before completion, the system will need:

* Authorization testing for every role.
* Protection against changing IDs in URLs.
* File-name and file-extension validation.
* File cleanup when an activity is deleted.
* File replacement cleanup.
* Safe external links.
* Validation of all workflow transitions.
* Error pages.
* Confirmation screens before deletion.
* Input validation.
* Testing of inactive accounts.
* Testing of unauthorised role access.

## 15. Final UI work

The interface still needs:

* Final navigation menu.
* Role-specific menu items.
* Consistent buttons and status colours.
* Responsive mobile layout.
* Empty-state messages.
* Confirmation modals.
* Pagination for large lists.
* Search and filtering.
* Better dashboard statistics.
* Final branding using `CTRL+PASS` rather than `CtrlPass.Web`.
* Footer and public page links.

# Overall position

The parts already built cover:

* Core project setup
* SQL Server database
* Identity and roles
* Admin user management
* Schools
* Course creation
* Course sections
* Course design
* Ten learning activity types
* File uploads
* Question options

The largest remaining parts are:

1. Course review, approval and publication
2. Academic Leader features
3. Instructor class management
4. Student learning and progress tracking
5. Guest course access
6. Notifications
7. Issue reporting
8. Membership access
9. Profiles
10. Reports and final testing

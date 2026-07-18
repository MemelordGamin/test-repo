# CTRL+PASS — Full Development Status Through Step 237

## Confirmed enrolment rule

An Instructor may enrol **any active Student account**, regardless of school.

Students do not require a school assignment. The enrolment selector must therefore filter by:

- Role = `Student`
- Account status = active

It must not filter by `SchoolId`.

---

# A. Completed work through Step 237

The numbered development process has reached **Step 237**. The work below is grouped by module rather than repeating every tiny code-edit step separately.

## 1. Project foundation

Completed:

- ASP.NET Core MVC project created.
- .NET 10 configured.
- SQL Server LocalDB connected.
- Entity Framework Core configured.
- Database migrations working.
- Bootstrap installed and working.
- Razor views working.
- Dependency injection configured.
- Static files working.
- Identity authentication configured.
- Login, registration and logout working.
- Inactive accounts blocked from login.
- Custom `ApplicationUser` implemented.
- User creation date stored.
- User full name stored.
- User active status stored.
- Optional user school assignment stored.
- Seed data available.

## 2. Roles and authorization

Completed roles:

- Student
- Instructor
- CourseCreator
- AcademicLeader
- Admin

Completed:

- Role-based controller authorization.
- Role-based dashboard redirection.
- Role-specific navigation support.
- Default registration role is Student.
- Admin account seeded.
- Course Creator test account created.
- Academic Leader test account created.
- Instructor test account created.

## 3. Schools

Completed schools:

- School of Computing
- School of Technology
- School of Business
- School of Engineering

Completed rules:

- Instructor belongs to one school.
- Course Creator belongs to one school.
- Academic Leader belongs to one school.
- Student does not require a school.
- Admin does not require a school.

Completed course-code prefixes:

- Computing → `COM`
- Technology → `TEC`
- Business → `BUS`
- Engineering → `ENG`

Each school has an independent sequence:

- `COM-0001`
- `TEC-0001`
- `BUS-0001`
- `ENG-0001`

## 4. Admin dashboard and user management

Completed:

- Admin dashboard.
- Total-user count.
- Active-user count.
- Inactive-user count.
- Manage Users page.
- View all users.
- Display full name.
- Display email.
- Display role.
- Display school.
- Display active status.
- Create User page.
- Edit User page.
- Assign roles.
- Assign schools.
- School is required for Instructor.
- School is required for Course Creator.
- School is required for Academic Leader.
- School is cleared for roles that do not require it.
- Activate accounts.
- Deactivate accounts.
- Prevent Admin from deactivating their own account.
- Prevent Admin from removing their own Admin role.
- Prevent duplicate email addresses.
- Validate selected role.
- Validate selected school.

## 5. Course database structure

Completed `Course` fields:

- Id
- CourseCode
- Title
- Description
- ThumbnailPath
- SchoolId
- CourseCreatorId
- AccessLevel
- Status
- IsUnderMaintenance
- CreatedAt
- UpdatedAt
- SubmittedAt
- ApprovedAt
- PublishedAt

Completed course statuses:

- Draft
- UnderReview
- ChangesRequested
- Approved
- Published

Completed access levels:

- Free
- Premium
- Enterprise

## 6. Course Creator dashboard

Completed:

- Total Courses card.
- Draft Courses card.
- Under Review card.
- Published Courses card.
- Course table.
- Course code display.
- Course title display.
- Access-level display.
- Status badges.
- Last-updated display.
- Status-specific actions.

Completed action rules:

- Draft → Edit and Design
- Changes Requested → Edit and Design
- Under Review → View Design
- Approved → View Design and Publish Course
- Published → View Design

## 7. Course creation and editing

Completed:

- Create Course form.
- Automatic school-based course-code generation.
- Title validation.
- Description validation.
- Access-level selection.
- New courses saved as Draft.
- Edit Draft course.
- Edit Changes Requested course.
- Prevent editing Under Review course.
- Prevent editing Approved course.
- Prevent editing Published course.
- Course ownership checks.
- Updated timestamp changes after editing.

Current test course:

- `COM-0001 — Introduction to Cybersecurity Fundamentals`

## 8. Course sections

Completed `CourseSection` structure:

- Id
- CourseId
- SectionTitle
- SectionDescription
- DisplayOrder

Completed functionality:

- Add section.
- Automatically assign section order.
- Edit section.
- Delete section.
- Move section up.
- Move section down.
- Display sections in order.
- Reorder remaining sections after deletion.
- Protect section actions by Course Creator ownership.
- Allow edits only in Draft or Changes Requested.
- Delete section activities and options through cascade.
- Delete associated uploaded activity files when deleting a section.

Current test section:

- Section 1: Introduction to Cybersecurity

## 9. Course activity types

Completed activity types:

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

## 10. Course activity database

Completed `CourseActivity` fields:

- Id
- CourseSectionId
- ActivityType
- Title
- Instructions
- TextContent
- FilePath
- ExternalUrl
- ModelAnswer
- DisplayOrder
- IsRequired
- CreatedAt
- UpdatedAt

Completed relationships:

- Activity belongs to one section.
- Activity order is unique inside a section.
- Deleting a section deletes its activities.

## 11. Activity creation

Completed:

- Add Activity page.
- Type selector.
- Title field.
- Instructions field.
- Required/optional switch.
- Text-content input.
- File upload.
- External URL.
- Model answer.
- Type-specific validation.
- Automatic display order.
- Save to SQL Server.
- Redirect option-based questions to option management.

## 12. File upload rules

Completed image rules:

- `.jpg`
- `.jpeg`
- `.png`
- `.webp`
- Maximum 5 MB

Completed video rules:

- `.mp4`
- `.webm`
- Maximum 100 MB
- Upload or URL, not both

Completed document rules:

- `.pdf`
- `.doc`
- `.docx`
- `.ppt`
- `.pptx`
- `.xls`
- `.xlsx`
- `.txt`
- Maximum 20 MB

Completed storage:

- `wwwroot/uploads/course-activities/`
- Generated unique file names
- File cleanup after replacement
- File cleanup after activity deletion
- File cleanup after section deletion

## 13. Activity display

Completed on Design Course and Academic Leader review pages:

- Activity order.
- Activity title.
- Activity type badge.
- Required/optional badge.
- Instructions.
- Text content.
- Image display.
- Uploaded-video playback.
- External-video link.
- Document link.
- External link.
- Model answer.
- Question options.
- Correct-answer badge for authorised staff.

## 14. Activity editing and deletion

Completed:

- Edit Activity page.
- Activity type locked after creation.
- Edit title.
- Edit instructions.
- Change required/optional status.
- Edit text content.
- Replace image.
- Replace document.
- Replace video.
- Change video from upload to URL.
- Edit external URL.
- Edit model answer.
- Delete activity.
- Move activity up.
- Move activity down.
- Reorder activities after deletion.
- Ownership and course-status checks.

## 15. Question options

Completed `CourseActivityOption` fields:

- Id
- CourseActivityId
- OptionText
- IsCorrect
- DisplayOrder

Completed:

- Manage Question Options page.
- Add option.
- Edit option.
- Delete option.
- Move option up.
- Move option down.
- Display options in order.
- Automatic option order.
- Reorder after deletion.
- Correct-answer indicators.
- Warning when deleting the correct answer.

Completed rules:

- Multiple Choice allows exactly one correct option.
- Dropdown allows exactly one correct option.
- Checkbox allows multiple correct options.

## 16. Course submission validation

Completed checks:

- Course must contain at least one section.
- Every section must contain at least one activity.
- Text activities must contain text.
- Image activities must contain an uploaded image.
- Document activities must contain an uploaded file.
- External Link activities must contain a URL.
- Video activities must use exactly one source.
- Multiple Choice questions must have at least two options.
- Dropdown questions must have at least two options.
- Checkbox questions must have at least two options.
- Multiple Choice must have exactly one correct answer.
- Dropdown must have exactly one correct answer.
- Checkbox must have at least one correct answer.

Completed:

- Submit Course validation page.
- Course totals.
- Validation-problem list.
- Server-side revalidation.
- Submit button enabled only when valid.
- Status changes to UnderReview.
- SubmittedAt timestamp recorded.
- Course locked after submission.

## 17. Course review model

Completed `CourseReview` fields:

- Id
- CourseId
- AcademicLeaderId
- Decision
- Comments
- ReviewedAt

Completed decisions:

- ChangesRequested
- Approved

Completed:

- Multiple reviews per course.
- Full review history.
- Reviewer relationship.
- Migration and SQL table.

## 18. Academic Leader dashboard

Completed:

- Assigned-school display.
- Total Courses count.
- Under Review count.
- Changes Requested count.
- Approved count.
- Published count.
- School-only course list.
- Draft courses hidden.
- Course Creator name displayed.
- Access level displayed.
- Status badges.
- Last-updated display.
- Review Course action.
- View Course action.

## 19. Academic Leader course review

Completed:

- Course-information display.
- Course code.
- Title.
- Description.
- Course Creator.
- School.
- Access level.
- Submission date.
- All sections.
- All activities.
- Files and links.
- Model answers.
- Question options.
- Correct answers.
- Previous review history.
- Review decision form.
- Changes Requested option.
- Approved option.
- Comments required for Changes Requested.
- Comments optional for Approved.
- Server-side school ownership checks.
- Course status checks.

## 20. Changes Requested workflow

Completed:

- Academic Leader requests changes.
- Review comments stored.
- Course changes to ChangesRequested.
- Course Creator sees feedback.
- Course Creator regains edit controls.
- Course Creator edits course content.
- Course Creator resubmits.
- Course returns to UnderReview.
- Previous review remains saved.
- Academic Leader can review again.

## 21. Course approval

Completed:

- Academic Leader approves corrected course.
- Approval review stored.
- Course status changes to Approved.
- ApprovedAt timestamp recorded.
- Course Creator editing remains locked.
- Course Creator receives Publish Course action.

## 22. Course publication

Completed:

- Publish Course confirmation ViewModel.
- Publish Course GET action.
- Publication confirmation page.
- Course details displayed.
- Approval date displayed.
- Section count displayed.
- Activity count displayed.
- Publish Course POST action.
- Ownership check.
- Approved-status check.
- Status changes to Published.
- PublishedAt timestamp recorded.
- Course becomes available to Instructors.
- Publish button disappears after publication.

Completed workflow:

```text
Draft
  ↓
Under Review
  ↓
Changes Requested
  ↓
Under Review
  ↓
Approved
  ↓
Published
```

## 23. Instructor school rule

Completed:

- Instructor must have a school.
- Admin Create User supports Instructor school assignment.
- Admin Edit User supports Instructor school assignment.
- Instructor can only choose Published courses from their assigned school.
- Courses under maintenance are excluded.

## 24. Instructor dashboard

Completed:

- Assigned school display.
- Total Classes count.
- Active Classes count.
- Inactive Classes count.
- Available Published Courses count.
- Instructor-owned class list.
- Class code.
- Class name.
- Course.
- Start date.
- End date.
- Status.
- Last updated.
- Create Class button.
- Manage Class action.

## 25. Course class database and creation

Completed `CourseClass` fields:

- Id
- ClassCode
- ClassName
- Description
- CourseId
- InstructorId
- StartDate
- EndDate
- IsActive
- CreatedAt
- UpdatedAt

Completed:

- Unique automatic class codes.
- Format: `CLS-0001`
- Create Class ViewModel.
- Published-course dropdown.
- Same-school restriction.
- Maintenance exclusion.
- Start-date validation.
- End-date validation.
- End date must be after start date.
- Instructor ownership.
- Save class.
- Display class on dashboard.

Current test class:

- `CLS-0001 — Cybersecurity September Intake`

## 26. Manage Class page

Completed:

- Manage Class ViewModel.
- GET action.
- Instructor ownership check.
- Class information.
- Class code.
- Class name.
- Course.
- Description.
- Start date.
- End date.
- Active status.
- Subclass list.
- Create Subclass link.
- Back to Dashboard link.

## 27. Course subclass database

Completed `CourseSubclass` fields:

- Id
- SubclassCode
- SubclassName
- Description
- CourseClassId
- IsActive
- CreatedAt
- UpdatedAt

Completed:

- Unique subclass code.
- Format: `SUB-0001`
- Parent-class relationship.
- Cascade deletion when parent class is deleted.
- Migration and SQL table.

## 28. Subclass creation

Completed:

- Create Subclass ViewModel.
- GET action.
- Parent-class ownership check.
- Active-class check.
- Create Subclass page.
- Automatic subclass-code generator.
- POST action.
- Save subclass.
- Update parent class timestamp.
- Display subclass in Manage Class.

Current test subclass:

- `SUB-0001 — Group A`

## 29. Class enrolment database

Completed `ClassEnrollment` fields:

- Id
- CourseSubclassId
- StudentId
- EnrolledAt
- IsActive
- RemovedAt

Completed database rules:

- Enrolment belongs to one subclass.
- Enrolment belongs to one Student.
- Same Student cannot have duplicate records in the same subclass.
- Removed enrolment remains in history.
- Re-enrolment will reactivate the existing record.
- Deleting a subclass deletes its enrolment records.
- Deleting a referenced Student is restricted.
- Migration and SQL table completed.

## 30. Manage Subclass page

Completed:

- Manage Subclass ViewModel.
- GET action.
- Instructor ownership check through parent class.
- Subclass details.
- Parent class details.
- Course details.
- Active status.
- Active Enrolments count.
- Removed Enrolments count.
- Student enrolment table.
- Enrolment date display.
- Removal date display.
- Enrol Student placeholder button.
- Remove placeholder button.
- Re-enrol placeholder button.
- Manage Subclass action connected from Manage Class.

Current state:

- Active enrolments: 0
- Removed enrolments: 0

---

# B. What remains to complete the system

## 1. Finish Instructor enrolment management

Immediate next tasks:

- Create Enrol Student ViewModel.
- Search/list all active Student accounts.
- Do not filter Students by school.
- Exclude Students already actively enrolled in the same subclass.
- Enrol a Student.
- Reactivate a previously removed enrolment.
- Remove a Student without deleting history.
- Record RemovedAt.
- Enable Enrol Student button.
- Enable Remove button.
- Enable Re-enrol button.
- Search students by name or email.
- Filter active and removed enrolments.

## 2. Instructor class and subclass maintenance

Still required:

- Edit class name.
- Edit class description.
- Edit start and end dates.
- Activate/deactivate class.
- Edit subclass.
- Activate/deactivate subclass.
- Delete subclass with confirmation.
- Decide whether class deletion is required.
- Prevent enrolment into inactive classes.
- Prevent enrolment into inactive subclasses.

## 3. Instructor notes and student monitoring

Still required:

- `InstructorNote` table.
- Add private note for Student.
- Edit note.
- Delete note.
- View notes per Student.
- Student progress list.
- Progress bars.
- Filter by class.
- Filter by subclass.
- Filter by progress status.
- View individual Student progress.

## 4. Student dashboard

Still required:

- Dashboard cards.
- Enrolled classes.
- Enrolled subclasses.
- Enrolled courses.
- Courses in progress.
- Completed courses.
- Recent activity.
- Notifications.
- Membership summary.
- Learning history.

## 5. Student course access

Still required:

- Student course player.
- Course sections.
- Activity navigation.
- Previous/next activity controls.
- Required/optional display.
- Text content.
- Image.
- Video.
- Document.
- External link.
- Short Answer.
- Paragraph.
- Multiple Choice.
- Checkbox.
- Dropdown.
- Student must not see correct answers before submission.
- Student must not see model answers before submission.

## 6. Student submissions and quiz results

Likely database structures:

- `ActivityCompletion`
- `ActivitySubmission`
- `StudentAnswer`
- Quiz-attempt structure if separate

Still required:

- Submit Short Answer.
- Submit Paragraph response.
- Submit Multiple Choice answer.
- Submit Checkbox answers.
- Submit Dropdown answer.
- Evaluate objective questions.
- Store submitted answer.
- Store score.
- Store submission date.
- Display result.
- Decide retry rules.
- Decide whether model answers appear after submission.

## 7. Progress tracking

Still required:

- Track activity completion.
- Required-activity count.
- Completed-required-activity count.
- Course progress percentage.
- Progress bar.
- Not Started status.
- In Progress status.
- Completed status.
- Completion date.
- Progress history.
- Instructor progress view.
- Student progress view.

Suggested formula:

```text
Progress =
Completed required activities
÷
Total required activities
× 100
```

## 8. Membership plans and access control

Confirmed plans:

| Plan | Price | Access |
|---|---:|---|
| Free | RM0 | Free courses |
| Premium | RM240/year | Free and Premium courses |
| Enterprise | RM300/year | All courses |

Still required:

- Membership model.
- Student membership record.
- Default Free plan.
- Plan selection.
- Upgrade page.
- Membership start date.
- Expiry date.
- Renewal.
- Access checks.
- Free Student cannot open Premium course.
- Free and Premium Student cannot open Enterprise course.
- Simulated payment/upgrade if real payment is not required.

## 9. Guest module

Still required:

- Public/Guest home page.
- Course catalogue.
- Free-course browsing.
- Open Free course.
- Temporary activity interaction.
- No saved progress.
- No enrolment record.
- No issue reporting.
- No profile.
- Sign-up button.
- Membership promotion.

## 10. Course preview and thumbnails

Still required:

- Course thumbnail upload.
- Thumbnail file validation.
- Thumbnail replacement cleanup.
- Learner-style preview for Course Creator.
- Preview must hide staff-only controls.
- Preview must not save progress.
- Academic Leader preview could reuse learner-style rendering.

## 11. Published-course maintenance

Still required:

- Enter maintenance mode.
- Leave maintenance mode.
- Academic Leader controls maintenance.
- Course Creator edits during maintenance.
- Decide whether reapproval is required after maintenance edits.
- Published course hidden/unavailable while under maintenance.
- Maintenance notifications.
- Maintenance history if required.

## 12. Issue-reporting system

Still required:

- Issue model.
- Issue title.
- Description.
- Course reference.
- Optional activity reference.
- Reporter.
- Reporter role.
- Date reported.
- Status.
- Academic Leader review.
- Forward to Course Creator.
- Course Creator response.
- Resolution.
- Resolved date.
- Student issue submission.
- Instructor issue submission.
- Guests blocked from reporting.
- Issue filters and search.

Possible statuses:

- Reported
- Under Review
- Forwarded
- In Progress
- Resolved
- Closed

## 13. Notification system

Still required notification model:

- Recipient
- Title
- Message
- Link
- Read/unread
- Created date

Events to notify:

- Student enrolled.
- Student removed.
- Student re-enrolled.
- Course submitted.
- Changes requested.
- Course approved.
- Course published.
- Maintenance started.
- Maintenance ended.
- Issue reported.
- Issue forwarded.
- Issue resolved.

UI still required:

- Notification badge.
- Notification list.
- Mark as read.
- Mark all as read.
- Open linked record.

## 14. Profiles

### Student profile

Still required:

- Profile details.
- Membership tab.
- Enrolled courses.
- Progress/history.
- Completed courses.

### Instructor profile

Still required:

- Profile details.
- Classes.
- Subclasses.
- Student statistics.
- Reports.

### Course Creator profile

Still required:

- Profile details.
- My Courses.
- Drafts.
- Under Review.
- Approved.
- Published.
- Review history.

### Academic Leader profile

Still required:

- Profile details.
- Assigned school.
- Reviews completed.
- Courses approved.
- Issues handled.

## 15. Reports

Still required:

- Student progress report.
- Subclass progress report.
- Class progress report.
- Course completion report.
- Instructor report dashboard.
- Academic Leader review report.
- Issue report.
- HTML report pages.
- CSV export.

## 16. Admin website management

Still required:

- View all courses.
- View all classes.
- View all issues.
- Site statistics.
- Edit About Us.
- Edit Contact information.
- Edit Policies.
- General website settings.

## 17. Public pages

Still required:

- Home.
- About Us.
- Contact Us.
- Policies.
- Course catalogue.
- Course details.
- Membership plans.
- Sign-up calls to action.

## 18. Search, filtering and pagination

Still required where lists can grow:

- User search.
- Course search.
- Status filter.
- Student search.
- Enrolment filter.
- Class filter.
- Subclass filter.
- Pagination.
- Empty-state messages.

## 19. Final security testing

Still required:

- Test every role against every protected controller.
- Test URL ID tampering.
- Test one Instructor accessing another Instructor’s class.
- Test one Instructor accessing another Instructor’s subclass.
- Test school restrictions for published courses.
- Test Student-role validation during enrolment.
- Test inactive Student exclusion.
- Test inactive-account login block.
- Test all workflow transitions.
- Test invalid uploads.
- Test oversized uploads.
- Test external links.
- Test deletion file cleanup.
- Test CSRF protection.
- Test validation on GET and POST actions.

## 20. Final UI and branding

Still required:

- Replace `CtrlPass.Web` with `CTRL+PASS`.
- Final navigation bar.
- Role-specific navigation.
- Consistent status colours.
- Consistent button labels.
- Responsive tables.
- Mobile layout.
- Confirmation dialogs.
- Footer.
- Public-page links.
- Accessibility review.
- Final lecturer/demo data.

## 21. Final testing and submission preparation

Still required:

- Seed realistic demo accounts.
- Seed multiple courses.
- Seed multiple classes and subclasses.
- Seed Students.
- End-to-end workflow testing.
- Screenshots for report.
- Use-case testing.
- CRUD evidence.
- Database evidence.
- Role-access evidence.
- Presentation/demo script.
- Backup source code.
- Backup database.
- Final clean build.

---

# C. Current end-to-end workflow already working

```text
Admin creates users and assigns roles/schools
        ↓
Course Creator creates COM-0001
        ↓
Course Creator adds sections and activities
        ↓
Course Creator configures question options
        ↓
Course Creator submits the course
        ↓
Academic Leader requests changes
        ↓
Course Creator edits and resubmits
        ↓
Academic Leader approves
        ↓
Course Creator publishes
        ↓
Instructor creates CLS-0001
        ↓
Instructor creates SUB-0001
        ↓
Next: Instructor enrols active Students
```

# D. Immediate next development step

**Step 238: Create the Enrol Student ViewModel**

The enrolment page must:

- Show the subclass.
- List any active Student account.
- Ignore school assignment.
- Exclude Students already actively enrolled in the subclass.
- Allow a removed Student to be re-enrolled.

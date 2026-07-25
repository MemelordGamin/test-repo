# Code Snippet Screenshot Locations

Use this for the implementation document screenshots.

In Visual Studio, press `Ctrl+Shift+F`, set **Look in** to **Entire Solution**, paste the search phrase, then open the matching file and screenshot the highlighted snippet.

## Snippet Checklist

| # | Snippet in document | File to open in Visual Studio | Search phrase |
|---|---|---|---|
| 1 | Bootstrap/CSS links and role placeholders | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Site.Master` | `<asp:PlaceHolder ID="phAdminLinks"` |
| 2 | Role-based navbar visibility | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Site.Master.cs` | `phAdminLinks.Visible` |
| 3 | Responsive base font size | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Content\Site.css` | `html {` |
| 4 | Focus styling for buttons/forms | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Content\Site.css` | `.btn:focus` |
| 5 | Course thumbnail styling | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Content\Site.css` | `.course-card-thumb` |
| 6 | Mobile dashboard table styling | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Content\Site.css` | `@media (max-width: 767.98px)` |
| 7 | SQL Server connection string | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Web.config` | `<connectionStrings>` |
| 8 | Database connection helper | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Data\Database.cs` | `public static SqlConnection CreateConnection` |
| 9 | ADO.NET repository pattern | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Repositories\UserRepository.cs` | `using (SqlConnection connection = Database.CreateConnection())` |
| 10 | Database seeding on startup | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Global.asax.cs` | `Application_Start` |
| 11 | Login form validation and login service call | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Account\Login.aspx.cs` | `AuthenticationResult result = _authenticationService.ValidateLogin` |
| 12 | Login password/user validation | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\AuthenticationService.cs` | `AppUser user = _userRepository.GetUserByEmail` |
| 13 | Role authorization helper | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Helpers\AuthorizationHelper.cs` | `public static void RequireRole` |
| 14 | PBKDF2 password hashing | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Helpers\PasswordHelper.cs` | `Rfc2898DeriveBytes` |
| 15 | MFA accepted time-step update | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\MfaService.cs` | `MfaLastAcceptedTimeStep = @AcceptedStep` |
| 16 | Password reset token generation | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\PasswordResetService.cs` | `GenerateUrlToken(32)` |
| 17 | Password reset token row lock | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\PasswordResetService.cs` | `FROM PasswordResetTokens WITH (UPDLOCK, HOLDLOCK)` |
| 18 | Course title required validator | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\CourseCreator\CreateCourse.aspx` | `rfvTitle` |
| 19 | Register email regex validator | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Account\Register.aspx` | `revEmail` |
| 20 | Academic Leader feedback validation | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\AcademicLeaderService.cs` | `Feedback comments are required when requesting changes` |
| 21 | Admin page role protection | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Admin\Users.aspx.cs` | `AuthorizationHelper.RequireRole(this, "Admin")` |
| 22 | User management duplicate email/role validation | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\UserManagementService.cs` | `EmailExists(user.Email` |
| 23 | Public website content update SQL | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Repositories\WebsiteContentRepository.cs` | `UPDATE WebsiteContentPages` |
| 24 | Course Creator course defaults | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\CourseCreatorService.cs` | `course.CourseCreatorId = creator.UserId` |
| 25 | Course insert SQL | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Repositories\CourseRepository.cs` | `INSERT INTO Courses` |
| 26 | Course design ownership validation | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\CourseDesignService.cs` | `ValidateCourseAccess(courseId, creatorUserId` |
| 27 | Activity Question / Title field | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\CourseCreator\AddActivity.aspx` | `Activity Question / Title` |
| 28 | Activity type JavaScript panel switching | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\CourseCreator\AddActivity.aspx` | `function switchActivityTypePanel` |
| 29 | Academic Leader school isolation | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\AcademicLeaderService.cs` | `Course not found or you do not have permission to review it` |
| 30 | Course review object creation | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\AcademicLeaderService.cs` | `CourseReview review = new CourseReview` |
| 31 | Review status update SQL | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Repositories\CourseRepository.cs` | `SET Status = @NewStatus` |
| 32 | Public preview published-course check | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\PreviewCourse.aspx.cs` | `This course is not available for public preview` |
| 33 | Protected preview panel | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\PreviewCourse.aspx.cs` | `pnlProtectedPreview.Visible = true` |
| 34 | Student enrolment/access check | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Student\OpenCourse.aspx.cs` | `CanStudentAccessEnrollment(studentId, enrollmentId)` |
| 35 | Multiple-choice/dropdown answer marking | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\StudentProgressService.cs` | `case CourseActivityType.MultipleChoiceQuestion` |
| 36 | Membership plan access rules | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Repositories\CourseRepository.cs` | `case CourseAccessLevel.Premium` |
| 37 | Instructor class course eligibility SQL | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\InstructorService.cs` | `FROM Courses WITH (UPDLOCK, HOLDLOCK)` |
| 38 | CSV export formula protection | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\InstructorService.cs` | `public static string Csv` |
| 39 | Protected activity file path check | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Student\DownloadActivityFile.ashx` | `uploadsRoot = Path.GetFullPath` |
| 40 | Notify course school's Academic Leader | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\IssueReportService.cs` | `Role = 'AcademicLeader'` |
| 41 | Issue report insert SQL | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\IssueReportService.cs` | `INSERT INTO IssueReports` |
| 42 | Notification insert SQL | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\NotificationService.cs` | `INSERT INTO Notifications` |
| 43 | Student profile tabs | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Services\UserProfileService.cs` | `if (IsStudent(profile.Role))` |
| 44 | ViewStateUserKey session binding | `C:\Users\dinee\Downloads\Projects\CtrlPass\CtrlPass.WebForms\Global.asax.cs` | `Application_PreRequestHandlerExecute` |

## Best Screenshot Order

1. Start with snippets 1 to 8 for layout, CSS and database connection.
2. Take snippets 11 to 17 for login, authorization, password hashing, MFA and reset.
3. Take snippets 18 to 23 for validation and admin.
4. Take snippets 24 to 31 for Course Creator and Academic Leader.
5. Take snippets 32 to 39 for public preview, student learning, membership, instructor and protected files.
6. Take snippets 40 to 44 for issues, notifications, profile tabs and ViewState security.

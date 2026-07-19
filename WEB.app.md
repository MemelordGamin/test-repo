## Phase 1 – Foundation

* ASP.NET Core MVC (.NET 10)
* Entity Framework Core
* SQL Server
* ASP.NET Core Identity
* Database migrations
* Role seeding
* School seeding
* Admin seeding
* ApplicationUser customization

---

## Phase 2 – Authentication

Completed:

* Registration
* Login
* Logout
* Role redirects
* Inactive account protection
* Remember Me
* Session management

---

## Phase 3 – Authorization

Implemented all permissions for:

* Guest
* Student
* Instructor
* Course Creator
* Academic Leader
* Admin

Every controller and workflow was tested.

---

## Phase 4 – Course System

Completed:

* Course creation
* Editing
* Publishing
* Review
* Maintenance
* Status workflow
* Automatic course codes
* Course thumbnails
* School assignment

---

## Phase 5 – Course Activities

All ten activity types:

* Text
* Image
* Video
* Document
* External Link
* Short Answer
* Paragraph
* Multiple Choice
* Checkbox
* Dropdown

Including:

* ordering
* validation
* uploads
* correct answers

---

## Phase 6 – Academic Workflow

Completed:

* Submit for Review
* Review
* Approve
* Request Changes
* Resubmit
* Publish

---

## Phase 7 – Maintenance Workflow

Completed:

* Start maintenance
* Student blocking
* Editing
* Resubmission
* Review
* Approval
* Notifications
* Progress preservation

---

## Phase 8 – Instructor

Completed:

* Classes
* Subclasses
* Student enrolment
* Remove/Re-enrol
* Progress dashboard
* Notes
* CSV exports

---

## Phase 9 – Student

Completed:

* Dashboard
* Course player
* Progress
* Question attempts
* Membership checks
* Notifications
* Issue reporting

---

## Phase 10 – Membership

Completed:

Free

Premium

Enterprise

Including expiry handling.

---

## Phase 11 – Guest

Completed:

* Homepage
* Browse courses
* Preview courses
* Register
* Login

Blocked from:

* Progress
* Issue reporting
* Student-only features

---

## Phase 12 – Notifications

Implemented every notification in the workflow.

---

## Phase 13 – Admin

Completed:

* User management
* Membership management
* Active/inactive accounts
* Issue management
* Notifications

---

# Security Features

## Password policy

Implemented:

* Minimum 8 characters
* Uppercase
* Lowercase
* Number
* Special character
* Unique characters

---

## Account lockout

Implemented:

* 5 failed attempts
* 15-minute lockout
* Failed count reset

---

## Password reset

Implemented:

* SendGrid
* Real email delivery
* One-hour reset tokens
* Secure Identity tokens

---

## Multi-Factor Authentication

Implemented:

* Microsoft Authenticator
* Google Authenticator
* Recovery codes
* Remember device
* Reset authenticator
* Disable MFA

---

## Security hardening

Completed:

* API key moved to User Secrets
* Exposed key revoked
* New key created
* Source code contains no secrets
* Password reset clears lockout

---

# Testing

Successfully tested:

Guest

Student

Instructor

Course Creator

Academic Leader

Admin

Password Reset

SendGrid

MFA

Recovery Codes

Course workflow

Maintenance workflow

Notifications

CSV exports

Issue reporting

Authorization

Role restrictions

Everything passed.


Congratulations—you've reached the point where the application itself is complete. The rest is about presenting and documenting the work you've built.

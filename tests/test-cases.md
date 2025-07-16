# 🧪 Zephyr Test Cases

## ✅ TC-CC-001: Register using valid credentials by clicking the Register navigation button

**Objective:**
The test case asserts that a user is able to register to cleancity using valid credentials

**Related Issues:**
- `SCRUM-59` - Test valid registration data

**Preconditions:**
* The test environment should be prepared

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:13:44 UTC

---

### 🧪 Test Steps:

**Step:** 1. Navigate to [CleanCity: Waste Pickup Scheduler](https://cleancity-testersng.netlify.app/)
**Expected Result:** The URL directs user to clean city Waste Pickup Scheduler

**Step:** Click the Register button on the navigation bar
**Expected Result:** User is ​directed to the ​Signup page

**Step:** Enter the full name, email and password
**Expected Result:** Credentials are entered successfully
**Test Data:**
```
Name: **J****ohn Doe**  
Email: **user1@test.com**  
Password:**TestPass123**
```

**Step:** Click the register button
**Expected Result:** User is redirected to the login page

**Step:** In the login page, enter your email and password credentials
**Expected Result:** User should be redirected to the profile page
**Test Data:**
```
Email: **user1@test.com**  
Password:**TestPass123**
```


---

## ✅ TC-CC-002: Register using an invalid email

**Objective:**
The test case asserts that the application prevents a user to register using an invalid email address

**Related Issues:**
- `SCRUM-60` - Test invalid email formats

**Preconditions:**
* The test environment should be prepared

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:19:21 UTC

---

### 🧪 Test Steps:

**Step:** * Navigate to [CleanCity: Waste Pickup Scheduler](https://cleancity-testersng.netlify.app/)

**Step:** Click the Register button on the navigation bar
**Expected Result:** User is directed to the Signup page

**Step:** Enter the full name, email and password
**Expected Result:** The application should notify a user that they have entered an invalid email
**Test Data:**
```
Name: J**ohn Doe**  
Email: **user1@testcom**  
Password:**TestPass123**
```

**Step:** Click the register button
**Expected Result:** * The application should notify the user to enter a valid email address.
* The app should not register the user with an invalid email
* The credentials should be cleared to allows the user to enter valid credentials


---

## ✅ TC-CC-003: Password validation during registration

**Objective:**
The test case asserts that the application validates the password meet the minimal requirements

**Related Issues:**
- `SCRUM-61` - Test password validation

**Preconditions:**
* The test environment should be prepared

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:19:24 UTC

---

### 🧪 Test Steps:

**Step:** * Navigate to [CleanCity: Waste Pickup Scheduler](https://cleancity-testersng.netlify.app/)
**Expected Result:** The URL directs user to clean city Waste Pickup Scheduler

**Step:** Click the Register button on the navigation bar
**Expected Result:** User is ​directed to the ​Signup page

**Step:** Enter the full name, email and password
**Test Data:**
```
Name: **J****ohn Doe**  
Email: **user1@test.com**  
Password:**TestPass**  
  
Name:****J****ohn Doe****Email:****user1@test.com****Password:****Test****  
  
​Name:******J****ohn Doe******Email:******user1@test.com******Password:******Te******  
  
​Name:********J****ohn Doe********Email:********user1@test.com********Password:********1********
```

**Step:** Click the register buon
**Expected Result:** * If the password does not meet the minimal requirements, the application should notify the user with an informative message
* The registration should not succeed


---

## ✅ TC-CC-004: Duplicate Email Handling

**Objective:**
This test case asserts that the application prevents a user from registering more than once using the same email address

**Related Issues:**
- `SCRUM-62` - Test duplicate email handling

**Preconditions:**
* The test environment should be prepared
* The user should have an existing CleanCity account

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:19:27 UTC

---

### 🧪 Test Steps:

**Step:** * Navigate to [CleanCity: Waste Pickup Scheduler](https://cleancity-testersng.netlify.app/)
**Expected Result:** The URL directs user to clean city Waste Pickup Scheduler

**Step:** Click the Register button on the navigation bar
**Expected Result:** User is directed to he Signup page

**Step:** Enter he full name, email and password
**Expected Result:** Credentials are entered successfully
**Test Data:**
```
Name: **J****ohn Doe**  
Email: **user1@test.com**  
Password:**TestPass123**
```

**Step:** Click the Register button
**Expected Result:** * The application should notify the user that an account with the email the user is trying to register with already exists
* User should be redirected to the login page to try and log in


---

## ✅ TC-CC-005: Login with valid credentials

**Objective:**
The test case asserts that a user is able to login with valid credentials

**Related Issues:**
- `SCRUM-63` - Test login with valid credentials
- `SCRUM-69` - Test login with valid password

**Preconditions:**
* The test environment should be prepared
* User should have an existing account on the CleanCity application

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:19:34 UTC

---

### 🧪 Test Steps:

**Step:** * Navigate to [CleanCity: Waste Pickup Scheduler](https://cleancity-testersng.netlify.app/)
**Expected Result:** The URL directs user to clean city Waste Pickup Scheduler

**Step:** 1. Click the Login button on the navigation bar
**Expected Result:** The user is redirected to the login page

**Step:** Enter the email and password credentials
**Test Data:**
```
Email: **user1@test.com**  
Password:**TestPass123**
```

**Step:** Click the Login button
**Expected Result:** User is redirected to the profile page


---

## ✅ TC-CC-006: Login with invalid credentials

**Objective:**
The test case asserts that the app prevents a user from logging in with invalid credentials

**Related Issues:**
- `SCRUM-64` - Test login with invalid credentials
- `SCRUM-70` - Test login with invalid password

**Preconditions:**
* The test environment should be prepared
* User should have an existing user account on CleanCity app

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:19:38 UTC

---

### 🧪 Test Steps:

**Step:** * Navigate to [CleanCity: Waste Pickup Scheduler](https://cleancity-testersng.netlify.app/)
**Expected Result:** The URL directs user to clean city Waste Pickup Scheduler

**Step:** Click the Login button on the navigation bar
**Expected Result:** The user is redirected to the login page

**Step:** Enter the email and password credentials
**Test Data:**
```
Email: **uesr1@test.com**  
Password:**TestPass123**  
  
Email:****user1@test.com****Password**:**testpass3****
```

**Step:** Click the Login button
**Expected Result:** * The application should notify the user that they have entered either the wrong email or password
* The user should not be logged in to the application


---

## ✅ TC-CC-007: Successful redirection after login

**Objective:**
The test case asserts that a user is redirected to the profile page after a successful login

**Related Issues:**
- `SCRUM-66` - Test redirection after successful login

**Preconditions:**
* The test environment should be prepared
* User should have an existing account

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:19:41 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to [CleanCity: Waste Pickup Scheduler](https://cleancity-testersng.netlify.app/)
**Expected Result:** The URL redirects the user to clean city Waste Pickup Scheduler

**Step:** Click the Login button on the navigation bar
**Expected Result:** The user is redirected to the login page

**Step:** Enter the email and password credentials
**Test Data:**
```
Email: **user1@test.com**  
Password:**TestPass123**
```

**Step:** Click the login button


---

## ✅ TC-CC-008: Logout Function

**Objective:**
The test case asserts that a user is successfully logged out

**Related Issues:**
- `SCRUM-67` - Test logout functionality

**Preconditions:**
* The test environment should be prepared
* User should be logged in

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:19:44 UTC

---

### 🧪 Test Steps:

**Step:** ​Click the Logout button on the ​top right part of your window
**Expected Result:** * The user should be successfully logged out
* The system should notify the user that they have been successfully logged out
* The URL of the page should only contain /home


---

## ✅ TC-CC-009: Successful Redirection upon Logout

**Objective:**
The test case asserts that a user is redirected to the homepage upon logging out

**Related Issues:**
- `SCRUM-68` - Test redirection after logging out

**Preconditions:**
* The test environment should be prepared
* User should be logged in

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:19:48 UTC

---

### 🧪 Test Steps:

**Step:** ​Click the Logout button on the ​top right part of your window
**Expected Result:** * The user should be successfully logged out
* The URL of the page should only contain /home


---

## ✅ TC-CC-010: Test session persistence upon refreshing a page

**Objective:**
The test case asserts that a session is maintained when a page is refreshed.

**Related Issues:**
- `SCRUM-65` - Test user session management when logged in

**Preconditions:**
* The test environment should be prepared
* User should be logged in

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:19:51 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to [CleanCity: Waste Pickup Scheduler](https://cleancity-testersng.netlify.app/)

**Step:** Login to the application
**Expected Result:** Email: **user1@test.com**  
Password:**TestPass123**

**Step:** Click the Login button
**Expected Result:** User is directed to the profile page

**Step:** ​Refresh the page
**Expected Result:** The user should still be logged in and in the page they were in


---

## ✅ TC-CC-011: Session Clearance upon Logging out

**Objective:**
The test case asserts that a user session is cleared after logging out

**Related Issues:**
- `SCRUM-71` - Test session clearance after logging out

**Preconditions:**
* The test environment should be prepared
* User should be logged in

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:01 UTC

---

### 🧪 Test Steps:

**Step:** Click the logout button
**Expected Result:** * The user should be successfully logged out
* The system should notify the user that they have been successfully logged out

**Step:** Navigate the dashboard page by clicking the dashboard button in the navigation menu
**Expected Result:** The user should be redirected to the login page


---

## ✅ TC-CC-012: Form Validation without input

**Objective:**
To verify that the waste pickup request form does not submit when required fields are empty

**Preconditions:**
* The application must be running at [CleanCity: Waste Pickup Scheduler](http://localhost:3000/)
* The test environment should be prepared

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:01 UTC

---

### 🧪 Test Steps:

**Step:** Open the browser and go to `http://localhost:3000/`
**Expected Result:** Home page should load with the **Waste Pickup Request Form** visible.

**Step:** Do not enter any values in the form fields (leave all fields blank).
**Expected Result:** All form input remain empty

**Step:** Click on the **Submit** or **Request Pickup** button
**Expected Result:** Form should not be submitted

**Step:** Observe any error messages that appear below or near the form fields
**Expected Result:** Validation error message should appear


---

## ✅ TC-CC-013 Filtering by location in dashboard

**Objective:**
Ensure pickup requests can be filtered by location.

**Related Issues:**
- `SCRUM-149` - Incorrect Filter Results: "Eldoret" filter shows Nairobi requests

**Preconditions:**
* At least one request from "Eldoret" exists.

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:01 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to the dashboard
**Expected Result:** The dashboard page will load

**Step:** Click on the filter dropdown for location
**Test Data:**
```
Eldoret
```

**Step:** Select "Eldoret" from the list
**Expected Result:** The request should only show Eldoret
**Test Data:**
```
Eldoret
```

**Step:** Observed filter results


---

## ✅ TC-CC-014: Filtering by status on dashboard

**Objective:**
Validate filtering requests by status (e.g., &quot;Scheduled&quot;).

**Preconditions:**
* At least one request has a “Scheduled” status.

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:01 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to dashboard
**Expected Result:** Dashboard loads

**Step:** Click on "Status" filter dropdown

**Step:** Select scheduled
**Expected Result:** Only scheduled requests should appear
**Test Data:**
```
Scheduled
```


---

## ✅ TC-CC-015 : Submitting Feedback with Valid Request ID

**Objective:**
Verify that a user can successfully submit feedback using a valid Request ID after pickup has occurred.

**Preconditions:**
* At least one waste pickup request (e.g., **REQ004**) has been submitted and marked as **"Completed"** or **"Picked Up"** in the system.
* The feedback form at is accessible

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:01 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to the dashboard page
**Expected Result:** List of requirements are displayed

**Step:** Identify a completed request (e.g., REQ004)
**Expected Result:** Status shows as "Completed"/"Picked Up"

**Step:** Go to the `feedback` page
**Expected Result:** Feedback form loads

**Step:** Enter the Request ID
**Expected Result:** Input accepted, no error
**Test Data:**
```
REQ004
```

**Step:** Fill in feedback text
**Expected Result:** Field accepts input
**Test Data:**
```
Pickup was late but resolved
```

**Step:** Click the "Submit Feedback" button


---

## ✅ TC-CC-016 :Submitting Feedback with Invalid Request ID

**Objective:**
Feedback should be rejected for invalid ID.

**Related Issues:**
- `SCRUM-150` - No error message displayed for invalid Request ID in Feedback Form

**Preconditions:**
* Feedback form (`/feedback`) is accessible.
* Use a **Request ID that does not exist** in the system (e.g., **REQ999**).

**Priority:** High  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:01 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to feedback
**Expected Result:** Feedback form loads

**Step:** Enter an invalid request
**Expected Result:** Field accepts input
**Test Data:**
```
REQ999
```

**Step:** Select a reason
**Expected Result:** The field accepts input

**Step:** Fill in feedback text
**Expected Result:** Field accepts input
**Test Data:**
```
Services not delivered
```

**Step:** Click the submit button
**Expected Result:** System attempts to submit the form


---

## ✅ TC-CC-017:  Form Input Type Validation: Date Field Should Not Accept Text

**Objective:**
<p id="isPasted">To verify that the <strong>Pickup Date field</strong> on the Waste Pickup Request form only accepts valid date input and <strong>rejects non-date values</strong> (e.g., plain text or symbols).</p>

**Preconditions:**
* The application is running and the home page (`/`) is accessible.
* Waste Pickup form is visible.
* A physical keyboard is available to try entering invalid input types.

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:01 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to the home page (`/`)
**Expected Result:** Waste pickup request form is displayed

**Step:** Click on the **Date** field
**Expected Result:** A calendar date picker should open

**Step:** Try typing invalid characters
**Expected Result:** Field should not accept or should immediately clear input
**Test Data:**
```
ab1234
```

**Step:** Submit the form
**Expected Result:** Form should not submit if date is invalid
**Test Data:**
```
All other fields are valid
```


---

## ✅ TC-CC-018 : Test Profile Activity on Requests

**Objective:**
The test case asserts that the system updates a user's request on the profile page.

**Related Issues:**
- `SCRUM-41` - Blog System Testing

**Preconditions:**
* The test environment should be prepared
* User should be logged in

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:01 UTC

---

### 🧪 Test Steps:

**Step:** Login to the CleanCity web application by entering the email and password.
**Expected Result:** User should be logged in and redirected to the profile page.
**Test Data:**
```
Email: **user1@test.com**  
Password: **TestPass123**
```

**Step:** * Navigate to the schedule pickup page by clicking the "**Schedule Pickup**" button on the navigation bar

**Step:** Enter the waste pickup request details in the fields provided.
**Test Data:**
```
Full Name: **John Doe**  
Email: **User1@test.com**  
Pickup Locaiton: **Nairobi**  
Waste Type: **General Waste**  
Preferred Pickup Date:**20/07/2025**  
Additional Description: **Please ring the bell**
```

**Step:** Click the "Submit Request" button
**Expected Result:** The request should be submitted successfully.

**Step:** Navigate to the Profile page by clicking the Profile button
**Expected Result:** The user should be redirected to the profile page.

**Step:** Click the "My Requests" button
**Expected Result:** The waste pickup requests should be displayed.


---

## ✅ TC-CC-019: Test Filtering on Posts

**Objective:**
The test case asserts that applying filters on posts shows only the posts under the chosen category

**Related Issues:**
- `SCRUM-97` - Test blog configuration with categories, tags, etc

**Preconditions:**
* The test environment should be prepared
* The user is logged in

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:01 UTC

---

### 🧪 Test Steps:

**Step:** 


---

## ✅ TC-CC-020: Test Search Funcion on Blog

**Objective:**
The test case asserts that the application returns the posts searched for through the search bar.

**Related Issues:**
- `SCRUM-95` - Test user interaction with the blog content

**Preconditions:**
* The test environment should be prepared
* User should be logged in

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:01 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to the cleancity application
**Expected Result:** The system should redirect you to the profile page

**Step:** Navigate the blogs page by clicking the blog button in the navigation bar
**Expected Result:** The user should be redirected to he blogs page

**Step:** In the search bar, search for various posts
**Expected Result:** For every search, the sysem should show that particular post in the "All Articles" section.
**Test Data:**
```
* How cleancity improved my neighborhood
* Understanding recycling symbols
* 5 ways to reduce household waste
* random blog post
```


---

## ✅ TC-CC-021: Test viewing of profile information

**Objective:**
The test case asserts that the application allows a user to view their profile

**Preconditions:**
* The test environment should be prepared
* User should have an existing account.

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:15 UTC

---

### 🧪 Test Steps:

**Step:** Login to the cleancity application
**Expected Result:** * The application should login the user
* The application should redirect the user to the profile page.
* The user should be able to view their profile.
**Test Data:**
```
email: user1@test.com  
password: Pass123
```


---

## ✅ TC-CC-022: Test Profile Editing

**Objective:**
The test case asserts that application allows a user to edit their profile information and validates updates

**Related Issues:**
- `SCRUM-102` - Test viewing and edition of profile information
- `SCRUM-155` - Invalid email is sucessfully passed as an update
- `SCRUM-156` - Empty fields can be passed when updating a user profile

**Preconditions:**
* The test environment should be prepared
* User should have an existing account.

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:15 UTC

---

### 🧪 Test Steps:

**Step:** Login to the cleancity application
**Expected Result:** The user should be successfully logged in  
The user should be redirceted to the profile page
**Test Data:**
```
Email: user1@test.com  
Password: Pass123
```

**Step:** Edit the profile details by clicking the 'Edit Profile' button
**Expected Result:** For an invalid input, the application should now allow the user to make changes. (error message should be displayed)  
For an invalid input, the applicatioh should notify the user that they have successfully upated their details, and the new information reflected in the profile page.
**Test Data:**
```
Email Updates:* johndoe@gmail.com
* user2.com
* blank input

Name Udates* John Due
* blank input
```


---

## ✅ TC-CC-023: Test past pickup requests

**Objective:**
The test case asserts that a user is able to view all their pickup requests

**Related Issues:**
- `SCRUM-154` - System does not update requests in the profile page

**Preconditions:**
* The test environment should be prepared.
* User should be logged in.
* User should have previously waste pickup requests.

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:15 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to [CleanCity: Waste Pickup Scheduler](https://cleancity-testersng.netlify.app/)
**Expected Result:** The URL redirects the user to clean city Waste Pickup Scheduler ​web application.

**Step:** Click the profile button to open the profile page.
**Expected Result:** ​The ​user should be redirected to ​the profile page.

**Step:** Click the 'My Requests' ​button.
**Expected Result:** ​The ​user should be able to view past requests ​they have previously made.


---

## ✅ TC-CC-024: Test User Can Update Profile Image

**Objective:**
The test case asserts that the application allows a user to update their profile picture

**Related Issues:**
- `SCRUM-104` - Test uploading of profile pictures by users
- `SCRUM-157` - Application does not update a profile picture

**Preconditions:**
* The test environment should be prepared
* User should have an existing account

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:15 UTC

---

### 🧪 Test Steps:

**Step:** Login to the cleancity application
**Expected Result:** The user should be logged in.  
The user should be redirectetd to the profile page
**Test Data:**
```
email: user1@test.com  
password: Pass123
```

**Step:** Click the profile image
**Expected Result:** The application should open a menu to allow the user to select a new image for updating

**Step:** Click ok in the device's window.
**Expected Result:** The image should be updated in the user's account in the application


---

## ✅ TC-CC-025: Test The Creation of Community Post

**Objective:**
The test case asserts that a user is able to successfuly create a community post.

**Related Issues:**
- `SCRUM-99` - Test creation of community posts functionality
- `SCRUM-162` - Entering a spacebar in the community field has no result

**Preconditions:**
* The test environment should be prepared
* User should be logged in with an existing account.

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:15 UTC

---

### 🧪 Test Steps:

**Step:** Log in to the cleancity application
**Expected Result:** User should be redirected to the profile page.
**Test Data:**
```
email: user1@test.com  
password: user123
```

**Step:** Navigate to the community page by clicking the community button in the navigation bar
**Expected Result:** User should be redircted o he community page

**Step:** Creaet a new post by keying a sample community post
**Test Data:**
```
community post: **A clean enironment is an environment that thrives**
```

**Step:** Click the "POST" buttton
**Expected Result:** The community post should be saved successfully.


---

## ✅ TC-CC-026: Test The Existence of a Created Community Post

**Objective:**
The test case asserts that a user is community post created by a user is displayed on the profile section

**Related Issues:**
- `SCRUM-158` - Test updating of a user's post on  their profile
- `SCRUM-159` - A creaed blog post is not shown in a user's profile.

**Preconditions:**
* The test environment should be prepared
* User should be logged in

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:15 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to the community page by clicking the "Community" button in the navigation bar
**Expected Result:** The application should redirect the usser to the Community page

**Step:** Creaate a community post by entering a post in the input field
**Test Data:**
```
Community post: **A clean environment is an environment that thrives**
```

**Step:** Click the "**POST**" button
**Expected Result:** The post should be successfully created

**Step:** Navigate to the profile page by clicking the "**Profile**" button in the navigation bar
**Expected Result:** The application should redirect the user to the profile page

**Step:** Click the "**My Posts**" button
**Expected Result:** The application should display the recently created post by the user.


---

## ✅ TC-CC-027: Test Liking of a Community Post

**Objective:**
The test case asserts that users are able to like a community post

**Preconditions:**
* The test environment should be prepared

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:15 UTC

---

### 🧪 Test Steps:

**Step:** Login to the cleancity application
**Expected Result:** The application should take a user to the profile page.
**Test Data:**
```
email: user1@test.com  
password: Pass123
```

**Step:** Navigate to the community page
**Expected Result:** ​The user should be redirected to ​the community page

**Step:** On a random post, click the like button
**Expected Result:** The like count should increase by one.


---

## ✅ TC-CC-028: Test the viewing of comments by user on the profile page

**Objective:**
The test case asserts that application displays the comments made by a user and are shown in the profile page of the user.

**Related Issues:**
- `SCRUM-160` - Comments not visible on the profile page

**Preconditions:**
* The test environment should be prepared
* The user should have an existing account.

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:15 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to the community page of the cleancity application
**Expected Result:** ​Application should redirect the user to the community page.

**Step:** ​In one of the posts displayed on tthe ​posts section, click tthe comment buton and make a comment by keyiing in ​some informaion
**Expected Result:** The input field should allows the user to enter textual information
**Test Data:**
```
Comment: **This is a great idea! It shall definitely benefit us and the environment at large**
```

**Step:** Click the enter key on your keyboard to post your comment under the community post
**Expected Result:** The comment should be posted under the post

**Step:** Navigate to the profile section
**Expected Result:** Application should redirect user to the profile page

**Step:** Click the "My Comments" button to view the comments made through the user accoun signed in.
**Expected Result:** ​The section should display the ​comments ​made by ​a user, including the recent comment made.


---

## ✅ TC-CC-029: Test Full Name Length Validation during User Registraiton

**Objective:**
The test case asserts that the application validates the length of the name entered during registration

**Related Issues:**
- `SCRUM-30` - User Registration Testing
- `SCRUM-161` - Application does not validate full name length during registration

**Preconditions:**
* The test environment should be prepared
* User should not have an existing account.

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:15 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to the cleancity application
**Expected Result:** The application should redirect the user to the home page

**Step:** Click the "Sign Up" button
**Expected Result:** The application should redirect you to the register page

**Step:** Enter the user details to register. Ensure to use a set of values for the name field
**Expected Result:** For names that meet the requirements (2-50) characters, the application should redirect them to the login page upon clicking the "Register" page.
**Test Data:**
```
Names:* J (1 character)
* Jo (2 characters)
* John Doe JJohn Doe JJohn Doe JJohn Doe JJohn Doe J (50 characters)
* John Doe JJohn Doe JJohn Doe JJohn Doe JJohn Doe JJ (51 characters)
```


---

## ✅ TC-CC-030: Test That Application Provided breadcrumbs

**Objective:**
The test case asserts that the application provides breadcrumbs, therefore providing clear navigation and backtracking options.

**Related Issues:**
- `SCRUM-130` - Test provision of breadcrumbs for complex pages
- `SCRUM-163` - Missing provision of breadcrumbs

**Preconditions:**
* The test environment should be prepared

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:15 UTC

---

### 🧪 Test Steps:

**Step:** Navigate to cleancity website
**Expected Result:** User should be redirected to cleancity's home page

**Step:** Navigate to the blog page and click a blog to open
**Expected Result:** User should be redirected to the blog page and a blog post opened (https://cleancityapplication/blog/1)  
The application should show the path from the application's homepage to the current page (our first blog)  
Upon clicking a relevant breadcrumb link, the user should be able to quickly navigate back to previous levels.


---

## ✅ TC-CC-031: Test Application Responsiveness on Mobile Devices

**Objective:**
The test case asserts that the application is responsive on mobile applications

**Preconditions:**
* The test environment should be prepared
* User should be logged in to the CleanCity application via mobile

**Priority:** Normal  
**Status:** Draft  
**Created By:** Denis Macharia Ndiritu  
**Created On:** 2025-07-07 05:20:15 UTC

---

### 🧪 Test Steps:

**Step:** Login to the cleancity application via mobile
**Expected Result:** Application should be redirect the user to the profile page


---
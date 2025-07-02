# Test Plan Document for CleanCity:  A Waste Pickup Scheduler Web Application

## 1.0 Test Plan Identifier

* ID: TP-WPS-1.0.1
* Title: Waste Pickup Scheduler Test Plan
* Created on: 2025-06-30
* Modified on: 2025-07-02

## 1.1 References

* [faq.md](../docs/faq.md)
* [functional-requirements.md](../docs/functional-requirements.md)
* [jira-setup.md](../docs/jira-setup.md)
* [README.md](../docs/README.md)

## 1.2 Overview

This test plan outlines the strategy, scope, resources, and schedule for QA testing of the CleanCity Waste Pickup Scheduler web application. The application is designed to help communities schedule waste pickups and promote environmental awareness.

## 1.3 Objectives

* Ensure all functional requirements (FR-001 to FR-097) are verified
* Detect intentional and hidden bugs across modules
* Validate usability, accessibility, and performance
* Ensure cross-browser and responsive design compatibility

## 1.4 Scope

* In Scope: Functional testing, non-functional testing, accessibility, edge case testing
* Out of Scope: Backend/API testing (localStorage only)

## 1.5 Test Items

* Authentication
* Waste Management
* Dashboard & Analytics
* Content Management
* Admin Panel
* Notifications

| Module           | Description                                 |
| ---------------- | ------------------------------------------- |
| Authentication   | Register, log in, log out, session handling |
| Waste Management | Schedule pickups, manage requests           |
| Dashboard        | User-specific stats and visualizations      |
| Admin Panel      | Manage users, content, and metrics          |
| Notifications    | pickup confirmation and updates, blog posts, community interactions and achivements unlocks              |



## 1.6 Features to be tested

| Feaure                | Risk Level           |
|-----------------------|----------------------|
| User Registration     | High                 |
| User login            | High                 |
| Session Management    | High                 |
| Pickup Scheduling     | High                 |
| Request Management    | High                 |
| Request Tracking      | High                 |
| User Dashboard        | High                 |
| Analytics and Reports | Medium               |
| Gamification          | Low                  |
| Blog System           | Medium               |
| Awareness Section     | Medium               |
| User Profile          | Medium               |
| Social Feature        | Low                  |
| User Management       | Medium               |
| Content Moderation    | Medium               |
| System Notifications  | High                 |
| Keyboard Navigation   | Medium               |


## 1.7 Features Not to be Tested

* Backend: The application using localStorage

## 1.8 Test Deliverables

* Test Plan
* Test Cases
* Defect Log
* Test Execution Summary
* Final Report
* Video Presentation

## 1.9 Remaining Test Tasks

* Writing functional test cases for all modules
* Reviewing test cases with devs for correctness
* Preparing test execution checklist

## 1.10 Environmental Needs

* Chrome, Firefox, Edge and Safari browsers (2 latest versions)
* Desktop computers
* Android devices
* Test data provided [here](../docs/test-data.md)
* React application deployed [here](https://cleancity-testersng.netlify.app/) 

## 1.11 Testing Tools

* Manual: Browser Dev Tools
* Automation: Optional (Jest, Pytest)
* Accessibility: Axe DevTools, WAVE
* Performance: Lighthouse, Google PageSpeed
* Project Management: GitHub Kanban

## 1.12 Roles & Responsibilities

| Name          | Role                                              | Responsibilities                         |
| ------------- | ------------------------------------------------- | ---------------------------------------- |
| Denis Ndiritu | Test Lead/ Functional Tester/ Document Specialist | Plan, organize, lead execution           |
| Ciku Kariuki  | Test Lead/ Functional Tester/ Document Specialist | Execute test cases, report bugs          |
| Samuel Murugu | Test Lead/ Functional Tester/ Document Specialist | Maintain test artifacts, compile reports |

## 1.13 Schedule

| Phase                    | Start Date | End Date   |
| -------------------------| -----------| ---------- |
| Phase 1: Test Planning   | 26-06-2025 | 02-07-2025 |
| Phase 2: Test Design     | 03-07-2025 | 09-07-2025 |
| Phase 3: Test Execution  | 10-07-2025 | 16-07-2025 |

## 1.14 Entry Criteria

* Functional requirements understood
* Test environment is prepared
* Application deployed and accessible
* Test data available
* Test plan approved by team

## 1.15 Exit Criteria

* All planned test cases executed
* All bugs classified and reported
* Test coverage ≥ 90% on all critical paths
* Final test report
* Video presentation recorded

## 1.16 Risk Management

| Risk                       | Mitigation                   |
| -------------------------- | ---------------------------- |
| Lack of documentation      | Use README and FRS strictly  |
| Limited test time          | Prioritize critical features |
| Team member unavailability | Distribute tasks flexibly    |


# 1.17 Approvals

| Name          | Role                                              |
| --------------| ------------------------------------------------- | 
| Denis Ndiritu | Test Lead/ Functional Tester/ Document Specialist |
| Ciku Kariuki  | Test Lead/ Functional Tester/ Document Specialist |
| Samuel Murugu | Test Lead/ Functional Tester/ Document Specialist | 

---
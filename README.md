## Team Name
### TiTej
## Team members
|S.No | Name |
| ----- | ----- |
| 1 | Pandu Ranga Varma Ankani |
| 2 | Krishna Raj |
| 3 | Sanjay Krishnan |
| 4 | Vinayak Inamadar |
| 5 | Lavanya KR |

Version - 0.1

Public codebase repo - https://github.com/tibil-it/ti-ace


# Ti Tej - Ti ACE 

This document repo created for Ti ACE from Tibil Solutions for the Skill-a-thon

## About Ti ACE

Ti ACE is a comprehensive career guidance solution that helps Citizens explore the right career options and achieve their desired goals.

## Product document	

### Problem statement 

In many cases, individuals are unaware of the career options available to them and may end up pursuing a career based on their surroundings, especially in the context of the Indian middle class. This can lead to individuals realizing that they are not well-suited for their current career at a later point in time, but they are unable to change direction due to the time, money, and effort already invested. As a result, they are forced to continue on their current path even if they are dissatisfied and unable to excel. 

This not only affects the person's overall lifestyle but also represents a loss to society and the country as the individual may have otherwise contributed more effectively to a more suitable career.
 
### Solution description 

Ti ACE is a career guidance solution designed to help individuals navigate career options based on their verified skills, interests, and other relevant factors. Ti ACE comprises five modules - Aware, Aspire, Assess, Able, and Access - which work together to provide comprehensive career guidance. 

 **Aware**: This module helps individuals get awareness about varied career choices.

 **Aspire**: This module recommends and helps individuals select a matching career option.
 
 **Assess**: This module assesses all the skill sets required for the selected career option.
 
 **Able**: This module helps individuals navigate through the right courses and mentors.
 
 **Access**: This module helps individuals access a fulfilling career.


As individuals progress in their chosen career paths, the roadmap could become clearer and more detailed. The options presented could narrow down as individuals narrow down their skill sets and preferences. This approach helps individuals make informed decisions about their career paths, leading to more fulfilling lives and increased contributions to society.

Overall, Ti ACE provides valuable support to individuals struggling to navigate the complex landscape of career options and requirements. It helps them make informed decisions and choose career paths that align with their passions and strengths.

 
### Target Audience 

## For high school level students who want to think and plan their career well in advance 
Aware & Aspire can be the focussed modules for them
## Pre University & Undergraduate students who want to know and pick some of the career options which suit them based on their current alignment
Aspire & Assess can be the focus for them
## Graduates & Postgraduates, who are well equipped and set to build their career
Assess & Able can be the best modules to focus
## All others including  White & Blue collar workers with some experience, either want to excel or switch their careers
Assess, Able & Access can be the central aspects


### UserFlows

 - User Registers using   ( Aadhaar  ) as ID, and the username can be a phone number or email id and password in the Ti Ace client UI application.

 - Registered users can log in using username and password, and Ti  Ace uses Keycloak as the Authentication and Authorization system.

 - Users search for the desired Job role, the Aware module uses Beckn protocol, Sunbird RC, and AI/ML, based on the job role, the aware module collects all the skills catalogs specific to the Job role from the open network and skill registry. And recommends the career path/learning path to the user.

 - Users choose the recommended career path. Now the User starts his learning journey, here the Able module uses Sunbird Knowlg and Sunbird Ed which provides the courses and their skill content. 

 - Post completion of the skills the Assess module is used to assess the skill through which quiz, question sets, etc  using Sunbird Inquiry,  and a certificate  is provided by leveraging Sunbird RC.

 - Once the user passes the skill assessments, verifiable skill credentials are provided. In the Access module Beckn protocol is used to discover jobs and internship opportunities across the open network by showcasing the skill certificates.
 


### Features  

Refer this document (https://docs.google.com/document/d/14YXOkMnor6nRJsMjFS4fnm5r75Px_Hz1_dDLgWeRz0w/edit?usp=sharing)

### Architecture

Refer this document (https://docs.google.com/document/d/14YXOkMnor6nRJsMjFS4fnm5r75Px_Hz1_dDLgWeRz0w/edit?usp=sharing)

## Tech Stack

1. BAP/BPP (Beckn)

   Citizen and Provider modules will be designed and developed to be connected to  open networks by using Beckn protocols. 

2. Keycloak

   Keycloak is used for authentication and authorization

3. Sunbird RC

   Sunbird RC is used as a registry to store  all the skill sets information and to provide digitally verifiable certificates

4. Sunbird Knowlg

   Sunbird Knowlg is used to develop the Able module, where the training contents are uploaded, curated, and accessed. 
   Training contents are grouped as courses based on the career goal.
   Ti Ace Aspire module uses the courses  from Sunbird Knowlg and recommends the career path to the user.

5. Sunbird inQuiry

   Sunbird inQuiry is leveraged to build Assess module, where Citizens are evaluated using question sets, quizzes, and surveys. This module will help the    Citizen understand where he/she stands with respect to the required skills for any given career choice. 

6. Sunbird UCI

   Ti Ace modules use Sunbird UCI  as a communication interface, through chatbot and  notification services to the Citizens as well as Providers.

## Product demo	

## Demo Video

Refer this document (https://docs.google.com/document/d/14YXOkMnor6nRJsMjFS4fnm5r75Px_Hz1_dDLgWeRz0w/edit?usp=sharing)

## User guide	

Refer this document (https://docs.google.com/document/d/14YXOkMnor6nRJsMjFS4fnm5r75Px_Hz1_dDLgWeRz0w/edit?usp=sharing)

## Source code	

Application code 
https://github.com/tibil-it/ti-ace

## Developer guide

- Frontend setup

  Prerequisites
 
  Install the below
 
  Angular v14.x
 
  Node v16X (LTS)
 
  clone the code from <github link>
 
  cd src/user-interface 
 
  Run the command ng serve

  Frontend can be accessed using http://localhost:4000

- Backend setup

  Prerequisites 
  
  Install the below
  
  Python v3.8

  clone the code from <github link>
  
  cd app/
  
  Run the below command
   python main.py

  Backend API can be accessed using http://localhost:5000



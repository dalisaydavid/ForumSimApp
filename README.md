ForumSimApp
===========

Title: Forum Simulation (ForumSim.py)
Platform: Python (Python Shell w/ Interpreter)
Purpose: Simulates a simple forum application
Most similar to a web forum and old BBS system

Forum Structure Layout
+ Forum --> Discussion --> Post --> Comment

Data Dictionary
+ “Forum Administrator” (Forum Admin) - Those Forum Members that can administer the entire forum application.
Forum Admins can perform any function in the application.
+ “Forum Member” - Those who can perform only certain functions in the application.

Main Use Cases
+ Forum Member Use Cases
  + View Actions
    + Login → View Actions
  + View Forum Members
    + Login → View Members
  + Message Forum Members
    + Login → View Members → Message Specific Member
  + Creation aka “Posting”
  + Create Discussion
    + Login → Create Discussion → Confirm → Notify Discussion Creator
  + Create Post
    + Login → View Discussions → Select Specific Discussion → Create Post → Notify Discussion Creator
  + Create Comment
    + Login → View Discussions → View Specific Discussion → View Posts → View Specific Post → Create Comment → Notify   Post Creator and Discussion Creator 
  + View Discussions
    + Login → View Discussions
  + View Posts
    + Login → View Discussions → Select Specific Discussion → View Posts → View Specific Post
  + View Comments
    + Login → View Discussions → View Specific Discussion → View Posts → View Specific Post → View Comments → View Specific Comment  
+ Forum Admin Use Cases
  + Create Forum Member
  + Deletion of Discussions
    + Login → View Discussions → Delete Specific Discussion
  + Deletion of Posts
    + Login → View Discussions → View Specific Discussion → View Posts → Delete Specific Post
  + Deletion of Comments
    + Login → View Discussions → View Specific Discussion → View Posts → View Specific Post → View Comments → Delete   Specific Comment
  + Ban Forum Members
    + Login → View Members → Ban Specific Member
+ Primary Design Decisions
+ Module-based design
+ Make several python modules that perform different functions, and structurally build the application

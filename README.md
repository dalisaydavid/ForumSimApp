ForumSimApp
===========

Title: Forum Simulation (ForumSim.py)
Platform: Python (Python Shell w/ Interpreter)
Purpose: Simulates a simple forum application
Most similar to a web forum and old BBS system

Forum Structure Layout
+ Forum → Topic → Post → Comment

Data Dictionary`
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
  + Create Topic
    + Login → Create Topic → Confirm → Notify Topic Creator
  + Create Post
    + Login → View Topics → Select Specific Topic → Create Post → Notify Topic Creator
  + Create Comment
    + Login → View Topics → View Specific Topic → View Posts → View Specific Post → Create Comment → Notify   Post Creator and Topic Creator 
  + View Topics
    + Login → View Topics
  + View Posts
    + Login → View Topics → Select Specific Topic → View Posts → View Specific Post
  + View Comments
    + Login → View Topics → View Specific Topic → View Posts → View Specific Post → View Comments → View Specific Comment  
+ Forum Admin Use Cases
  + Create Forum Member
  + Deletion of Topics
    + Login → View Topics → Delete Specific Topic
  + Deletion of Posts
    + Login → View Topics → View Specific Topic → View Posts → Delete Specific Post
  + Deletion of Comments
    + Login → View Topics → View Specific Topic → View Posts → View Specific Post → View Comments → Delete   Specific Comment
  + Ban Forum Members
    + Login → View Members → Ban Specific Member
+ Primary Design Decisions
+ Module-based design
+ Make several python modules that perform different functions, and structurally build the application

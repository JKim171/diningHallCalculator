# diningHallCalculator
Inspiration:
We were inspired by the inconsistent menus which some of the dining halls provided. A lot of time the types of protein that we wanted weren't available in all dining halls, and only in select ones. We wanted to develop a solution for our problem by creating a program which would search through all of the dining halls and give us all of the available options to suit our needs. That way, we could look through this list and choose how far we wanted to travel and locate where the best food was.

What it does:
Our program scrapes data from the online dining hall menus. It then gets processed through our backend to store the data. A user inputs their desired calorie and protein amounts, dietary preferences, and allergies into a GUI. Our GUI then sends that information back to the backend which processes it and outputs the results into a new GUI screen.

How we built it:
We built our project using python using tkinter and selenium libraries. The tkinter library was used to create the interactive GUI which would send data back and forth with our backend which was made with python. We used selenium to web scrape the data off of the menus on the UW-Madison website.

Challenges we ran into:
We ran into many challenges when creating our program. One of the biggest challenges was being able to interact with the HTML files of the online menus. We originally tried using BeautifulSoup, but then realized that it couldn't see the individual menu items since they needed to be clicked on in order to be seen. We then decided it would be best to switch to selenium so that our program could actually interact with the page.

Accomplishments that we're proud of:
We're proud of pushing through problems like the one above by finding workarounds. There were many small problems in this project which we were able to find different workarounds for, using creative methods and outside of the box thinking.

What we learned:
We learned that sleep is important :). We also learned how to work together on a tough coding project as a team and how to brainstorm and solve problems together. In terms of hard skills, we learned a lot about web scraping and the development of GUIs.

What's next for Dining Hall Calculator:
In the future, we wish to add more macros which can be controlled by the user. We want the user to have full control over what restrictions they want on their meals so that we can find the best food in the campus for them.

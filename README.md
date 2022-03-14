# Bellevue Club Tennis Reservation App

An application that automates making Bellevue Club Tennis reservations through the [Bellevue Club Tennis](https://www.bellevueclub.com/move/tennis/) website.

## Why does this application exist?
I made this app due to friends needing to get tennis reservations but needing to be online at ~7:45am to get one. Sometimes reservations for the indoor courts (of which there are 4) can be reserved within 30 seconds of them opening. 

Rather than requiring people to get online early and try to beat other Bellevue Club member's personal assistants you can now run the program and get the times you want

## Can other people use the application?
Yes, though I did make this with a specific person in mind, in theory this should work for any Bellevue Club member. 

Fill in your personal request information in the  ```philPasswords``` file, make sure you have login credentials for the Bellevue Club website, and run the application.

## What is the application doing exactly?
I use [selenium web driver for python](https://selenium-python.readthedocs.io/index.html) to navigate to the Bellevue Club, login, and go through the reservation steps. To ensure that we log in at the moment it opens we load the page and the day that we want (the furthest out we can look, one week) and at the strike of the minute click through the open appointment, as viewed through the website's code. 

The bot makes sure to look in terms of it's priority -- Court 1 > Court 2 > Court 3 > Court 4. This, combined with the time selection found within the code for each given day lets you get the ideal spot.

## Does it work?
Yeah! It gets reservations ~90% of the time, averaging a reservation time of 1.5 seconds after opening. This, at least now, is enough to beat the other aspiring tennis players.

It also handles errors well by continuing to run if there aren't slots available for the desired day (for example, if there is a tournament going on that day and the whole tennis area is booked it will just try again the next day).

This took many iterations to get the speed down to a point where it would reliably beat others but now we are there :)

## Future Features

"...a work is never truly completed [...] but abandoned..." Paul Valéry

Nice-to-have features:
- idk its fine

## Questions or feedback?
Feel free to submit a github issue or pull request

This is an open souce project.  If you want to get involved, reach out to Becka (beckastar@gmail.com) or Leslie(leslie.tom@gmail.com). 

The goal of this group and web app is to both gather and display data relating to cycling in the SF Bay Area.  We want to be able to improve access to data related to cycling safety, recreation, community and theft in for the vibrant cycling community.  

Noting that the current datasets on bicycle crashes in San Francisco lacks several critical data points (such as time, what caused the crash, weather at time of crash, etc), our initial project is to build a survey which will visualize user input on bicycle crashes to determine where and when they are most likely to occur, and under what conditions. 

The cycling community is known for its engagement and strong opinions, and we are building this with the expectation that members of this group will give their time to providing datasets in order to support efforts to better local services. 

For an initial, immediate MVP, we have the following goal:

Build Flask framework as backend
Generate a user survey which will collect relevant data
Store the data
Interpret data using Python and R
Query the data 
Create a dashboard which will visualize the data along user-selected pivots
Provide user interface which allows queries along various pivot points
Deploy app so it is accessible online
Reach out to local cycling community for data

Ultimately, we'd like to be able to extend the app based on internal team ideas and external community needs. We want a better trip planner which will take accident frequency into account as well as hills and cycling route, building on top of the Bikesy capabilities.  We also want to be able to analyze bike theft frequency against other factors, like overall crime rate and access to designated bike parking.  

Datasets:
We have access/are using the following datasets.   
(see description here: https://github.com/enjalot/transit-datathon/tree/master/Bicycles)


Bikesy is a great app that has an API, decent documentation, and a developer who is local and communicative.  From Bikesy you can get the lat long of a start and an end point, and it will calculate a route based on a user’s preference for safety vs hills.  Additional information:
http://blog.bikesy.com/source/

The great app Baytripper is built with  Bikesy:
http://www.baytripper.org/

Bicycle theft: (keyword: bicycle) https://data.sfgov.org/Public-Safety/SFPD-Incidents-Previous-Three-Months/tmnf-yvry
Bicycle Crashes - pretty JSON: https://gist.github.com/pranavr/11348749
Bike Crashes: csvhttps://github.com/BayCitizen/dataapps/blob/master/data_apps/bc_data_apps/bike_accidents/files/bike_accidents.csv
Raw data (thefts, possibly injuries, etc) - http://iswitrs.chp.ca.gov/Reports/jsp/userRegistration.jsp
Repo for their project -https://github.com/BayCitizen/dataapps/blob/master/data_apps/bc_dataapps_templates/bike_accidents/bike_accidents_methodology.html
Bicycle Parking - https://data.sfgov.org/Transportation/Bicycle-Parking-Public-/w969-5mn4
Open Street Maps GEOJSON bike routes in SF: https://github.com/enjalot/transit-datathon/tree/master/bike_routes


During our first transit datathon <https://www.eventbrite.com/e/transit-datathon-tickets-13355459539> we created a mapping of discovered that if we had more data points we might be able to explore bike crashes.  We set out to connect with the Bike Coalition and other SF groups to query bike crashes to see if there could be future conversations to protect bicyclists.   

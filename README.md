# Application README

Application gets a random user and analyzes their profile picture for beauty scores.
Geolocation of user is gathered and distance from the random user is calculated.
Random user's name, picture, beauty score, and user's distance is displayed in a tkinter GUI.
Custom log files are generated to indicate time and success status for each API request

Application relies on an internet connection to make requests. Default data is avaliable for testing when no connection is available 


Design Patterns used:

* MVC
    * Utilizes Tkinter in the view
* Facade
    * Model portion of MVC is implemented using a facade pattern to create a single
    interface to access three API proxy classes
    * Log file
* Proxy
    * Four remote proxy classes are used to access four different API


API Used:
 1. RandomUser: https://randomuser.me/
    * Used to generate random user photo, name, and location coordinates
 2. Faceplusplus: https://www.faceplusplus.com/beauty/#demo
    * Used to get beauty scores
 3. ipvigilante: https://ipvigilante.com/
    * Used to get geolocation information on user
 4. ipify: https://www.ipify.org/
    * Used to get public ipv6 of user
 
Additional Details:
* Requests are done using Python's requests module
* Geographic distance between the user and randomly generated user is
    calculated using GeoPy module
 
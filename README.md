5K-Race-Timekeeper
==================

A web application for tracking times during the HIS Dragon Run 

This was an experimental program I wrote to help keep track of the finish times of more than 150 runners at this year's 5K race. We do not use an automatic time keeping system on account of the cost and the size of our race. Typically these times are captured by pencil and paper and a big group of volunteers. This was my attempt to automate part of this process.

Some notes:
  *The main application is contained in timekeeper.py. It is written in Python 3.2 using the Bottle (http://bottlepy.org) framework. The hostname, admin password, and port can all be set here.
  
  *Bootstrap, jQueryMobile, and JQuery are all served locally (rather than through a CDN) since this system was used on a wireless network that did not have internet access. These local directories can be set for your system by adjusting the /static/ route in timekeeper.py.
  
  *To run this on your system (after setting up Bootstrap & jQueryMobile as you choose), run 'python timekeeper.py' in a terminal or in the IDLE application. The application will run at the url http://HOSTNAME:8080/ where HOSTNAME is the name assigned in the timekeeper.py file.

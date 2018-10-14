# IoT-Bikes

#Inspiration
We realized that riding a bicycle to and fro from within a selected region should not be charged as it does not involve any fuel.
Now, making a bicycle free of cost would compromise the security and that is why we made use of IOT devices Dragonboard and Arduino in order to make the cycle secured.
Apart from that since the bicycle is free of cost people will prefer it over fueled vehicles thus, reducing the emissions and creating a environment friendly smart city.
It can also help people in maintaining a healthy lifestyle by taking up bicycles more often than cars.

#What it does
Dragonboard keeps track of the location of the bicycle.
Arduino looks after it's security.
Together these two devices help in creating a solution which makes bicycles available to everyone free of charge.

#How we built it
We have used Dragon Board and Arduino to receive the sensors data.
The GPS data is transmitted from the dragonboard to Google Cloud Platform(GCP) and stored on Firebase.
A Twilio API sends the SMS if the readings of the sensors goes beyond a threshold.
A Debian OS is mounted on the Dragonboard.
A Node.js application receives the location data from a python API and sends it to Google Cloud Platform.
The sensors on Arduino are present to detect any damages done to the box( mounted on bike and the dragonboard is present inside this box.

#Challenges we ran into
The GPS sensor cannot be activated on the dragonboard because specific gps modules cannot be used on Debian version. Samsung gear s3 gps and bluetooth transfer issues.
Configuration and setup issues specifically conflict with the python version on google cloud platform.
Accomplishments that we're proud of
Utilized HERE maps to location dynamically of the bikes in a confined zone.
Setting up Google Cloud Platform and Firebase.

#What we learned
We should be prepared with all sensors that are required for implementing a hardware hack. Else you might run into issues of sensors not being supported for the particular hardware/device that you are working on.
What's next for Shield Bikes
Shield bikes have a tremendous potential to completely change the way bicycle industry operates by making it more accessible to people.

#Built With
node.js
dragonboard-410c
arduino
google-cloud
firebase
express.js
fitbit
twilio
python

###################
###   General   ###
###################

Location_name = "Location 1"

scan_event = "scan_event"

job_table = "jobs"

break_table = "breaks"

employee_table = "employees"

Locations = ["Location 1", "Location 2", "Location 3"]

LocationsAll = ["All Locations"] + Locations

# Delete scans after 'x' amount of days
# To stop deletion set to negative number
clear_after_number_of_days = -1

#######################
###   MQTT Broker   ###
#######################

mqttBroker= "raspberrypi"

mqtt_port = 1883

########################
###   SQL Database   ###
########################

host = "127.0.0.1"

user="root"

password="winston!!2"

database="jobstafftrackingdatabase"

port = 3306

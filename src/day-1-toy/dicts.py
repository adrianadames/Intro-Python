# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Write a loop that prints out all the field values for all the waypoints

for i in waypoints:
    for x, y in i.items():
        print(y)

# #I wonder why this form of the solution outputs digits for lat and lon instead of the strings data type that was specified.
# for i in waypoints:
# 	print ('latitude: %s, longitude: %s, name: %s' % (i["lat"],i["lon"],i["name"]))

# # alternative solution
# for w in waypoints:
#     print("lat: %d, lon: %d, name: %s" % (w["lat"], w["lon"], w["name"]))


# Add a new waypoint to the list

waypoints.append({
    "lat": 80,
    "lon": -160,
    "name": "bleep bloop place"
})

# for i in waypoints:
#     print(i)

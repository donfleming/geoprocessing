import arcpy, os
from arcpy import env

# Set the workspace and allow overwriting
env.workspace = "yourfilepath/output"
env.overwriteOutput = True

# Set local variables for the state 
states = "yourfilepath/tlgdb_2014_a_us_nationgeo.gdb/State"
roads = "yourfilepath/tlgdb_2014_a_us_roads.gdb/Roads"

# Create a search cursor on the states feature class
#  with the data access module of arcpy.
with arcpy.da.SearchCursor(states, ("NAME", "SHAPE@")) as state_cursor:
	# And now iterate through every state and perform the clip operation
	for state in state_cursor:
		name = state[0]
		geom = state[1]
		outPoly = os.path.join(env.workspace, name + "_rds")
		arcpy.Clip_analysis(roads, geom, outPoly)

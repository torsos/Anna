## Import system modules
import arcpy
from arcpy import env

## Setting environments
env.workspace = "C:/Data/Unit5"
env.overwriteOutput = True

## Setting variables
fc = "airports.shp"
fc1 = "roads.shp"

## Delete area and perimeter fields
field_del = arcpy.DeleteField_management(fc, ["AREA", "PERIMETER"])
## Add Latlong text field 
field_plane = arcpy.AddField_management(fc, "LATLONG", "TEXT")
## Update latlong field with xy coordinates
with arcpy.da.UpdateCursor(fc, ["SHAPE@XY", "LATLONG"]) as cursor:
    for row in cursor:
        row[1] == row[0]
        cursor.updateRow(row)
        
## Add Seaplane short field
field_rd = arcpy.AddField_management(fc1, "SEAPLANE", "SHORT")
## Assign 1, 2, 3, 4 in for loop if feature attribute applies
with arcpy.da.UpdateCursor(fc1, ["SEAPLANE", "FEATURE"]) as cursor:
    for row in cursor:
        if row[1] == "Other Highway":
            row[0] = 1
        elif row[1] == "Principal Highway":
            row[0] = 2
        elif row[1] == "Ferry Crossing":
            row[0] = 3
        elif row[1] == "Other Through Highway":
            row[0] = 4 
        cursor.updateRow(row)


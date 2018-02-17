import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:/Data/Unit6"

def addField():
    FC = "roads.shp"
    arcpy.AddField_management(FC, "FERRY", "TEXT", "", "", 20)
    cursor = arcpy.da.UpdateCursor(FC, ["FEATURE", "FERRY"])
    for row in cursor:
        if row[0] == "Ferry Crossing":
            row[1] = "YES"
        else:
            row[1] = "NO"
            cursor.updateRow(row)
    del row
    del cursor

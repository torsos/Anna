import arcpy
from arcpy import env
env.overwriteOutput = True

def addField(path):
    env.workspace = path
    FC = "roads.shp"
    arcpy.AddField_management(FC, "FERRY", "TEXT", "", "", 20)
    with arcpy.da.UpdateCursor(FC, ["FEATURE", "FERRY"]) as cursor:
        for row in cursor:
            if row[0] == "Ferry Crossing":
                row[1] = "YES"
            else:
                row[1] = "NO"
                cursor.updateRow(row)

if __name__ == '__main__':
    addField("C:/Data/Unit6")
    
   

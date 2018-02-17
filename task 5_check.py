import arcpy
from arcpy import env
env.workspace = "C:/Data/Unit5"
env.overwriteOutput = True

fc = "airports.shp"
fc1 = "roads.shp"
try:
    field_del = arcpy.DeleteField_management(fc, ["AREA", "PERIMETER"])
except:
    print "Error"
field_plane = arcpy.AddField_management(fc, "LATLONG", "LONG")
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@XY"], "LATLONG")

del cursor
##populate = arcpy.AddXY_management(fc)
##field_plane.append(populate)
try:
    field_rd = arcpy.AddField_management(fc1, "SEAPLANE", "SHORT")
except:
    print "Error"
with arcpy.da.UpdateCursor(fc1, "SEAPLANE", "FEATURE = ['Other Highway', 'Principal Highway', 'Ferry Crossing', 'Other Through Highway']") as cursor2:
                           for row in cursor2:
                               cursor2.updateRow([1, 2, 3, 4])
                           del row
del cursor2

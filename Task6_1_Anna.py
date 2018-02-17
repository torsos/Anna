import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:/Data/Unit6"
fc = "dams.shp"
desc = arcpy.Describe(fc)
spatialref = desc.spatialReference
cursor = arcpy.da.SearchCursor(fc, ["@SHAPE","DAM_NAME"])
lstDAMS = []
counter = 1
for row in cursor:
    counter += 1
    print counter + ". " + row[1]
    lstDAMS.append(row[1])
del cursor
lstDAMS.sortAsc()
print 'Last value in the list {} '.format(lstDAMS[-1])

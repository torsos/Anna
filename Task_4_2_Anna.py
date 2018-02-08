## Import Systems
import arcpy
from arcpy import env

## Setting Environments
env.workspace = "C:/Data/Unit4"
env.overwriteOutput = True
outfc = "C:/Data/Unit4/Results/"


for shps in arcpy.ListFeatureClasses():
    desc = arcpy.Describe(shps)
    type = desc.shapeType
    if type == "Point":
        arcpy.CopyFeatures_management(shps, outfc + shps)
        for lists in arcpy.ListFields(shps):
            print "{} - {}".format(shps, lists.name)
    

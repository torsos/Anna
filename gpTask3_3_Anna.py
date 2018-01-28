## System imports
import arcpy
from arcpy import env

## Setting Environments
env.workspace = "C:\Data\Unit3"
arcpy.env.overwriteOutput = True

## Set local variables
in_features = "hospitals.shp"
clip_features = "zip.shp"
out_feature_class = "C:\Data\Unit3\Results\hospital_Clip.shp"

## Execute Clip
arcpy.Clip_analysis(in_features, clip_features, out_feature_class)

msg_out = arcpy.GetMessageCount()
print arcpy.GetMessage(msg_out-1)

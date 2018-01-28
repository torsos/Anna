## System imports
import arcpy
from arcpy import env

## Setting Environments
env.workspace = "C:\Data\Unit3"
arcpy.env.overwriteOutput = True

## Set local variables
in_features = ["parks.shp", "zip.shp"]
out_feature_class = "C:\Data\Unit3\Results\parks_intersect.shp"

## Intersect tool
arcpy.Intersect_analysis(in_features, out_feature_class)

## Message output
msg_out = arcpy.GetMessageCount()
print arcpy.GetMessage(msg_out-1)

## Optional parameters: Join_attributes, Cluster_tolerance, Output_type
## required parameters: In_features, Out_feature_class

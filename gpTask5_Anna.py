## Import Ssystem modules
import arcpy
from arcpy import env

## Setting Environments
env.workspace = "C:/Data/Unit5"
env.overwriteOutput = True

## Setting variables
in_fc = "roads.shp"
out_fc = "rds_PH.shp"
where_clause = '"FEATURE" = \'Principal Highway\''

## Select 2 different features in the FEATURE field
arcpy.Select_analysis(in_fc, out_fc, where_clause)
arcpy.Select_analysis(in_fc, "rds_ferry.shp", '"FEATURE" = \'Ferry Crossing\'')

## Buffer output of selected features
roads = arcpy.Buffer_analysis(out_fc, "PH_buf.shp", "14 METERS")
ferry = arcpy.Buffer_analysis("rds_ferry.shp", "ferry_buf.shp", "9 METERS")

## Union 2 features 
arcpy.Union_analysis([roads, ferry], "rds_buff")





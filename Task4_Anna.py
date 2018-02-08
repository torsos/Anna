## System imports
import arcpy
from arcpy import env

## Setting environments
env.workspace = "C:/Data/Unit4"
env.overwriteOutput = True

shp = arcpy.ListFeatureClasses()

## Loop through listed features, describe feature shape, list spatial reference. 
i = 0;
for shps in shp:
    desc = arcpy.Describe(shps)
    types = desc.shapeType
    sr = desc.spatialReference
    
    print "FC {} is {} and {}".format(shps, types, sr)
    i += 1
    
## Copying features
arcpy.CopyFeatures_management("amtrak_stations.shp", "/Results/amtrak_stations_copy.shp")
arcpy.CopyFeatures_management("cities.shp", "/Results/cities_copy.shp")
arcpy.CopyFeatures_management("counties.shp", "/Results/counties_copy.shp")
arcpy.CopyFeatures_management("new_mexico.shp", "/Results/new_mexico_copy.shp")
arcpy.CopyFeatures_management("railroads.shp", "/Results/railroads_copy.shp")


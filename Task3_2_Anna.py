import arcpy

if arcpy.CheckExtension("Tracking") == "Available":
    print "The Tracking extension is available."
else:
    print "The Tracking extension is not available."
if arcpy.CheckExtension("Network") == "Available":
    print "The Network extension is available."
else:
    print "The Network extension is not available."
if arcpy.CheckExtension("ArcScan") == "Available":
    print "The ArcScan extension is available."
else:
    print "The ArcScan extension are not available."

from pyrevit import forms
from Autodesk.Revit.DB import *

doc = __revit__.ActiveUIDocument.Document

doors = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_Doors)\
    .WhereElementIsNotElementType()\
    .ToElements()

count_missing_width = 0

for door in doors:
    width_param = door.LookupParameter("Width")
    
    if width_param is None or not width_param.HasValue:
        count_missing_width += 1

forms.alert("Doors without width: {}".format(count_missing_width))
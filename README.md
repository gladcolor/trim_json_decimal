# trim json decimal
Keep 5 digits after the decimal points of the coordinates in GeoJSON files.

```
Original
{
    "geometry": {
      "type": "Point",
      "coordinates": [
        31.763246540000001,
        68.570144650000003
      ]
    },
    "type": "Feature",
    "properties": {}
}
Processed
{
    "geometry": {
      "type": "Point",
      "coordinates": [
        31.76324,
        68.57014
      ]
    },
    "type": "Feature",
    "properties": {}
}
```
# How to use
Environment: Python 3.7

In Windows, copy `run_script.bat` to the json file directory, then run it. The results will be stored in the "trimed" directory. Save about 40% of size.


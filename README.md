# global_population_api
This is an API built with django rest framework utilizing the 2015 Population Density data at 15 minutes resolution from Gridded Population of the World (GPW), v4 dataset from NASA’s Socioeconomic Data and Applications Center (sedac)

## Requirements
- Django==2.0.3
- djangorestframework==3.9.0
- numpy==1.15.4
- pytz==2018.7

## Parameters
latutude: numeric value between -90 and 90
longitude: numeric value between -180 and 180
radius: numeric value greater than or equal to 0

## Example: query
**Lahore, Pakistan: Coordinates (31.5204° N, 74.3587° E) and radius 42.10 km**

**query:** http://127.0.0.1:8000/api/v1/get_population/?latitude=31.5204&longitude=74.3587&radius=42.10

```json

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "longitude": 74.3587,
    "latitude": 31.5204,
    "radius": 42.1,
    "population": 10166154
}
```
**Leiden, Netherlands: Coordinates (52.1601° N, 4.4970° E) and radius 4.82 km**

**query:** http://127.0.0.1:8000/api/v1/get_population/?latitude=52.1601&longitude=4.4970&radius=4.82

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "longitude": 4.497,
    "latitude": 52.1601,
    "radius": 4.82,
    "population": 251333
}
```

**Note: For details of how the population for a set of coordinates and radius is evaluation, please go through the [population_calculation_methodology.pdf](population_calculation_methodology.pdf) file**


<!-- ---
permalink: api_readme

--- -->

# API usage 

## Usage 
The base url is: [https://centre-for-invasive-species-solutions.github.io/demo_json_api/](https://centre-for-invasive-species-solutions.github.io/demo_json_api/)

<!-- base_url: https://centre-for-invasive-species-solutions.github.io/demo_json_api/ -->

## Use Cases 
1. [Weed List](#weed-list)
2. [Weed Details](#weed-details)
3. [All API Endpoints](#all-endpoints)
4. [Images](#images)


### Weed List 

``` http 
GET [base_url]/api.json 
Content-Type: application/json
``` 

```curl 
curl -X GET "https://centre-for-invasive-species-solutions.github.io/demo_json_api/api.json" \
-H "accept: application/json" \
```
#### Arguments 
None. 
#### Response
A single json, some processing will allow you to find all supported species


*Sample* 

``` json 
// Return JSON 
{
  "Species": {
    "Acanthaceae": {
      "Asystasia_gangetica_subsp._micrantha": { ... },
      "Barleria_lupulina": { ... },
      "Barleria_prionitis": { ... },
    },
    "Alismataceae": {      
        "Alisma_lanceolatum": { ... },
        ...
    }
  }
}
```

*Python Example* 

``` python 
#json = GET {url}
family_list = json["Species"].keys()
species_list = []
for family in family_list:
    family_species = json["Species"][family].keys()
    for species in family_species:
        species_list += family + family_species
``` 


### Weed Details 

```http
GET [base_url]/data/Species/[Family]/[Species]/SpeciesDescription.json 
``` 

#### Arguments

| Element     | Description   |
|-------------|-------------- |
| Family      |  Weed Family  |
| Species     | Weed Species  |


#### Response

*Description* 

| Element            | Description   |  Type  | 
|-------------       |-------------- | ------ | 
| Family             |  Weed Family  | String |
| ScientificName     | Scientific Name | String |
| CommonNames        | Weed Species  | String |
| Synonyms           | Previous scientific names   | String |
| PlantForm         | Weed Species  | String |
| Size              | Weed Species  | String |
| Stem              | Weed Species  | String |
| Leaves            | Weed Species  | String |
| Flowers           | Weed Species  | String |
| FruitSeeds        | Weed Species  | String |
| Habitat           | Weed Species  | String |
| DistinguishingFeatures     | Weed Species  | String |
| Photos            | Example photos | array   |
| -- FileName       | File  | String |
| -- Caption        | Caption   | String |


*Sample* 

``` json 
// Return JSON 
{
"Family":"Sapindaceae",
"ScientificName":"Acer negundo",
"CommonNames":"box elder",
"Synonyms":"",
"PlantForm":"Medium trees.",
"Size":"6-15 m tall.",
"Stem":"Smooth light grey or brown bark, becoming rougher with age.",
"Leaves":"Large leaves 20-30 cm long, divided into 3-9 oval or egg-shaped leaflets.",
"Flowers":"Greenish to pinkish, wihtout petals, in clusters (male) or drooping on stalk (female).",
"FruitSeeds":"Dry, winged green to brown as mature. V-shaped and fly like propellors.",
"Habitat":"Along watercourses, wet forests, woodlands, roadsides and other disturbed areas.",
"DistinguishingFeatures":"Smaller and more complex leaves than similar Sycamore maple. Propellor like fruits differ from ashes.",
"Photos":[
{"FileName":"4768_IMG_2568.jpg","Caption":"compound leaves"},
{"FileName":"9074_P6890332.jpg","Caption":"green seed"},
]
} 
```

### All Endpoints 

``` http 
GET [base_url]/api.json 
Content-Type: application/json
``` 

```curl 
curl -X GET "https://centre-for-invasive-species-solutions.github.io/demo_json_api/api.json" \
-H "accept: application/json" \
```

#### Arguments 

None. 

#### Response

A single json containing the entire file tree of accessible resources, including images, and species profiles in json and markdown. 

*Sample*

``` json 
{
  "./data/Species": {
     "./data/Species/[Family]": {
       "./data/Species/[Family]/[Species]": {
            "11485_P6940501.jpg": "[base_url]/Species/[Family]/[Species]/11485_P6940501.jpg",
            "SpeciesDescription.json": "[base_url]/Species/[Family]/[Species]/SpeciesDescription.json",
            "SpeciesDescription.md": "[base_url]/Species/[Family]/[Species]/SpeciesDescription.md",
      },
    }
   },
   "./data/[other keys]": {}
}
```

### Images 
Getting an image list, and getting the image file. 

``` http 
GET [base_url]/data/Species/[Family]/[Species]/SpeciesDescription.json
Content-Type: application/json
``` 

#### Arguments 

| Element     | Description  |
|-------------|--------------|
| Family      |  Weed Family  |
| Species     | Weed Species  |

#### Response

*Python Example* 

``` python 
species_images = json["Photos"]
for image in species_images:
    image_filename=image['FileName']
    image_url = [base_url]/data/Species/[Family]/[Species]/[filename]
    image_caption = image['Caption']

# GET image_urls 
``` 

## Limits 

This api is limited by the github limits - these are considerable, but not infinite. 

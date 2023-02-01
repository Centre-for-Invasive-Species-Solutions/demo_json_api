# demo_json_api

Checking the use of a github page to serve static / mostly static API data 

Pages available:
- index  - base page, with links to the following. 
- index_hr  - generated page showing all species pages 
- api - generated page showing all species end points 
- api_readme - API usage information
- Species info is available in a rendered format at .../data/Species/{Family}/{Species}/SpeciesDescription
- Species info is available in a markdown format at .../data/Species/{Family}/{Species}/SpeciesDescription.md
- Species info is available in a json format at .../data/Species/{Family}/{Species}/SpeciesDescription.json


## CICD 
- Auto deploys for commits to *main* and *develop* branches.
- linter and test build are done on all pull requests. 

## Helper/ Generator functions 
- ./helper/generate_index.py
   - auto generates the index pages and api summaries
- ./helper/generate_Species Mardown.py
   - Formats the JSON into a markdown page for human consumption
- ./helper/linter.py
   - loads and checks all .json files in the repo for usability 


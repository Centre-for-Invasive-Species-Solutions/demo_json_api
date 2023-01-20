import os
import json

data_source = "./data"
# api_page = "./api.json"
# api_page_hr = "./api.md"
# index_human = "./index_hr.md"
base_url = "https://centre-for-invasive-species-solutions.github.io/demo_json_api/"

def generateSpeciesMarkdown():
        print(os.getcwd())

        for current_dir, subdirs, files in os.walk( data_source ):
            # Reletive directory 
            write_dir = current_dir[len(data_source)+1:]

            # Files
            for filename in files:
                if filename.lower().endswith('json'):
                    out_file = filename.strip('json')
                    out_file += ("md")
                    relative_path = os.path.join( current_dir, filename )
                    with open(relative_path) as json_file:
                        try:
                            data = json.load(json_file) 
                            md_string = writeSpeciesMarkdown(data, current_dir )
                            with open(current_dir + "/" + out_file, "w") as out_file:
                                out_file.write(md_string)
                        except Exception as e:
                            print("   json parse failure:" +write_dir+"/   "+ filename)
                            print(e)
  
def writeSpeciesMarkdown(data, path):
    md_string = ""
    if (data.get("Family")):
        md_string += "# " + data.get("Family") + "\n"
    if (data.get("ScientificName")):
        md_string += "## " + data.get("ScientificName") + "\n"
    if (data.get("CommonNames")):
        md_string += "**Common Names:** " + data.get("CommonNames")  + "\n"
    if (data.get("Synonyms")):
        md_string += ("**Synonyms:** " + data.get("Synonyms")) + "\n"
    md_string += ("\n")
    if (data.get("PlantForm")):
        md_string += "**Plant Form:** " + data.get("PlantForm") + "\n"
    if (data.get("Size")):
        md_string += "**Size:** " + data.get("Size") + "\n"
    if (data.get("Stem")):
        md_string += "**Stem:** " + data.get("Stem") + "\n"
    if (data.get("Leaves")):
        md_string += "**Leaves:** " + data.get("Leaves") + "\n"
    if (data.get("Flowers")):
        md_string += "**Flowers:** " + data.get("Flowers") + "\n"
    if (data.get("FruitSeeds")):
        md_string += "**Fruit and Seeds:** " + data.get("FruitSeeds") + "\n"
    if (data.get("Habitat")):
        md_string += "**Habitat:** " + data.get("Habitat") + "\n"
    if (data.get("DistinguishingFeatures")):
        md_string += "**Distinguishing Features:** " + data.get("DistinguishingFeatures") + "\n"
    md_string += ("\n\n\n")

    if (data.get("Photos")):
        for photo in data.get("Photos"):
            md_string += "<figure>"
            md_string += ('<img src="'+ "./"+photo.get("FileName")+ '" style="display: block; margin: auto;" />\n\n')
            md_string += "<figcaption>" + photo.get("Caption") + "</figcaption>"
            md_string += "</figure>"
    return md_string


# Using the special variable 
# __name__
if __name__=="__main__":
    generateSpeciesMarkdown()

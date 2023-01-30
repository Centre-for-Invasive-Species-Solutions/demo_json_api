import os
import json

data_source = "./data"
api_page = "./api.json"
api_page_hr = "./api.md"
index_human = "./index_hr.md"
api_weeds = "./weeds.json"
base_url = "https://centre-for-invasive-species-solutions.github.io/demo_json_api/"

def pathto_dict(path):
    """ helper to generate a dict containing the entilre data file structure
    """
    for root, dirs, files in os.walk(path):
        tree = {}
        for d in dirs : 
            tree[os.path.join("", d)] = pathto_dict(os.path.join(root, d))
        if files: 
            tree = {}
            for f in files:
                tree[f] = os.path.join(base_url,root[2:], f) 
        return tree

def write_md_directory_tree(out_file, data: dict, depth=0, current_dir = "", path = "" ):
    """ Pushes dict to markdown in out_file, according to depth
    Requires Python 3.10+ 
    """
    if isinstance(data, dict):
        for key in sorted(data):
            if isinstance(data[key], dict): # another node
                match depth:
                    case 0:
                        this_string = "## " + key.split("/")[-1] + "\n" # First dir under data
                    case 1:
                        this_string = "### " + key.split("/")[-1] + "\n" # Family name
                    case 2:
                        this_string = ""#"**" + key + "**\n" # Species name - already covered. 
                    case 3:
                        this_string = "*" + key + "*\n"
                    case _:
                        this_string =  key + "\n"
                out_file.write(this_string)
                write_md_directory_tree(out_file, data[key], depth+1, key, path +"/"+ key)
            else:   # leaf
                if (key == "SpeciesDescription.json"):
                    md_species(out_file, key, path)
                else: 
                    this_string =  "" #key + "\n"
                    out_file.write(this_string)


def md_species(out_file, filename, current_dir):
    """ Print SpeciesDescription.json to markdown with link formatting
    """
    relative_path = os.path.join( current_dir, filename )
    with open(relative_path) as json_file:
        try:
            data = json.load(json_file)
            name = data.get('ScientificName', filename) 
            display_path = os.path.join( current_dir, filename )
            url = base_url + display_path.removesuffix('.json')
            out_file.write('- ['+ name + "](" + url + ')\t\t\t\t\t')
            out_file.write("\([.md](" + url + '.md)')
            out_file.write("  [.json](" + url + '.json)\)\n\n')

        except Exception as e:
            print(e)

def generateIndex_HR():
    """ generate a human readable index in markdown 
    """
    with open(index_human,"w") as file:
        tree = pathto_dict(data_source)
        write_md_directory_tree(file, tree, 0,  "", "./data")

def generateIndex_API():
    """
    API readable list of all api endpoints 
    Generates to markdown, and a JSON for api retrieval 
    """
    with open(api_page,"w") as api_file:
        tree = {}
        tree = pathto_dict(data_source)

        json.dump(tree, api_file, indent = 2, sort_keys=True)
        # and the human readable page
        hr_api_file = open(api_page_hr, "w")
        hr_api_file.write("# API Endpoints")
        hr_api_file.write("\n\n ```json\n")
        json.dump(tree, hr_api_file, indent = 2, sort_keys=True)
        hr_api_file.write("\n```\n")
        hr_api_file.close()
  
if __name__=="__main__":
    generateIndex_HR()
    generateIndex_API()

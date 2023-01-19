import os
import json

data_source = "./data"
api_page = "./api.json"
api_page_hr = "./api.md"
index_human = "./index_hr.md"

def generateIndex_HR():
    with open(index_human,"w") as file:
        file.write("---\n")
        file.write("permalink: index_hr\n")
        file.write("---\n")
        print(os.getcwd())

        for current_dir, subdirs, files in os.walk( data_source ):
            write_dir = current_dir[len(data_source)+1:]
            # Current Iteration Directory
            if not (write_dir):
                write_dir = "Data"
            file.write( "## " + write_dir + "\n\n" )

            # Directories
            # for dirname in subdirs:
            #     file.write( ' - ' + dirname + '\n' )

            # Files
            for filename in files:
                relative_path = os.path.join( current_dir, filename )
                with open(relative_path) as json_file:
                    try:
                        data = json.load(json_file)  ## should be in a try 
                        name = data.get('ScientificName', filename) 
                        display_path = os.path.join( write_dir, filename )
                        url = "https://centre-for-invasive-species-solutions.github.io/demo_json_api/data/" + display_path
                        file.write('- ['+ name + "](" + url + ')\n\n')
                    except Exception as e:
                        print(e)


def generateIndex_API():
    data = {}
    with open(api_page,"w") as api_file:
        for current_dir, subdirs, files in os.walk( data_source ):
            write_dir = current_dir[len(data_source)+1:]
            # Current Iteration Directory
            if (len(files)):   
                data[write_dir] = files

            # Directories
            # for dirname in subdirs:
            #     data[dirname] = files
        holder = {'data': data}
        json.dump(holder, api_file, indent = 6)
        hr = open(api_page_hr, "w")
        hr.write("# API Endpoints")
        json.dump(holder, hr, indent = 6)
        hr.close

def generateIndex_API_hr():
    data = {}
    with open(api_page_hr,"w") as hr_api_file:
        for current_dir, subdirs, files in os.walk( data_source ):
            write_dir = current_dir[len(data_source)+1:]
            # Current Iteration Directory
            if (len(files)):   
                data[write_dir] = files
        holder = {'data': data}
        hr_api_file.write("# API Endpoints")
        hr_api_file.write("\n\n```")

        json.dump(holder, hr_api_file, indent = 6)
        hr_api_file.write("```")

  

# Using the special variable 
# __name__
if __name__=="__main__":
    generateIndex_HR()
    generateIndex_API()
    generateIndex_API_hr()
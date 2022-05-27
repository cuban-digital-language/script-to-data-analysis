import json
import datetime
from json import JSONEncoder
#from locale import LC_ALL
from facebook_scraper import get_posts,get_profile


# subclass JSONEncoder
class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

#links = ['groups/1746673108822943','groups/271609852994505','groups/507355953581910']
links =     ["groups/2602375306723194",'groups/1669400126613634','groups/2015057042124445']

file_comment=open("comentarios de facebook",'w')
file_post = open("facebook_post",'w')
listposts = []
for link in links:
     for post in get_posts(link, pages=5,options={"comments": True}):
          listposts.append(post)

for dict in listposts:
     for key in dict :
          try:
               if(key =='comments_full'):
                    file_comment.write(dict[key])
                    continue
               
               file_post.write(dict[key])
          except:
               continue  

with open("facebook3.json", "w") as outfile: 
     for dictionary in listposts:
          json.dump(dictionary, outfile,cls=DateTimeEncoder) 


file_comment.close()
file_post.close()

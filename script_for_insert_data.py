import json
import requests
with open("shopnow_data.json", "r") as file:
    data = json.load(file)
# The URL for your Elasticsearch instance

for item in data:
    if item:
        dict={}
        dict["name"]=item["Address1"]
        dict["location"]={
            "lon": item["Longitude"],
            "lat": item["Latitude"]
        }
        dict["Combined"]="SHWAPNO,"+" "+item["Address1"]
        dict["type"]="shwapno outlet"
    
       
        json_data=json.dumps(dict)
        print(json_data)
        # Perform the POST request
        response = requests.post("http://localhost:9200/mapdb/_doc/?pretty", json=dict, headers={"Content-Type": "application/json"})

        # Check the response
        print(response.text)
        














        
# {
#     "addr:bn": "২ ডি, রোড, ঢাকা ১২১২, বাংলাদেশ",
#     "addr:en": "2 d, Road, Dhaka 1212, Bangladesh",
#     "name": "Ideal School And College Banasree Branch.",
#     "location": {
#         "lon": 90.432119,
#         "lat": 23.7630605
#     },
#     "Division": "Dhaka",
#     "Combined": "Ideal School And College Banasree Branch.,2 d, Road, Dhaka 1212, Bangladesh",
#     "type": "school"
# }
# "test_insert_id":"lR8nuokBQXxJvRwZxfT2"

# curl -X POST "localhost:9200/node_tags/_doc/?pretty" -H 'Content-Type: application/json' -d' {"name": "ARCADIA, Darshan Deuri, Amberkhana, Sylhet-3100", "location": {"lon": 91.8649825, "lat": 24.906119}, "Combined": "SHWAPNO, ARCADIA, Darshan Deuri, Amberkhana, Sylhet-3100", "type": "shwapno outlet"} '
# for query shopnow data
# curl -X GET "http://localhost:9200/mapdb/_search" -H 'Content-Type: application/json' -d' { "query": { "term": { "type.keyword": "shwapno outlet" } } }'
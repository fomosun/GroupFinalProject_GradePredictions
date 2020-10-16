import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'G1':5, 'G2':200, 'absences':400, 'studytime':400, 'failures':400})

print(r.json())
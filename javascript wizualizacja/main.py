from plotly.graph_objs import Bar
from plotly import offline
import requests

URL = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'

headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(URL,headers=headers)
print(f"Kod statusu: {r.status_code}")

response_dict = r.json()

repo_dict = response_dict['items']

stars, repo_names, labels = [],[],[]

for dict in repo_dict:

    repo_user = dict['owner']['login']
    repo_description = dict['description']
    label = f"{repo_user} <br /> {repo_description}"
    repo_url = dict['url']
    all_info = f"{label} <br /> <a href='{repo_url}'> "

    stars.append(dict['stargazers_count'])
    repo_names.append(dict['name'])
    labels.append(all_info)


data = [{
    'type':'bar',
    'x' : repo_names,
    'y': stars,
    'hovertext' : labels,
    'marker' : {
        'color': 'rgb(200,70,100)',
        'line': {
            'color' : 'rgb(150,50,80)',
            'width':4
        },
    },
    'opacity': 0.7
}]

my_layout = {
    'title':'Najlepiej oceniane projekty w jezyku JavaScript według GitHub',
    'xaxis':{
    'title' : 'Repozytorium'
        },
    'yaxis':{
    'title': 'Liczba Gwiazdek'
        }
    }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='javascriptrepositories.html')



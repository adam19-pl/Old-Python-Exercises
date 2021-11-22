from plotly.graph_objs import Bar
from plotly import offline
import requests

URL = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(URL,headers=headers)

print(f"Status : {r.status_code}")

response_dict = r.json()
repo_dict = response_dict['items']

stars,repo_names,labels = [],[],[]

for dict in repo_dict:
    repo_name = dict['name']
    repo_user = dict['owner']['login']
    repo_description = dict['description']
    label = f"{repo_user}<br />{repo_description}"
    repo_url = dict['html_url']
    repo_link = f"<a href='{repo_url}'> {label}"

    labels.append(repo_link)
    stars.append(dict['stargazers_count'])
    repo_names.append(dict['name'])

print(len(stars))
print(len(repo_names))

data = [{
    'type': 'bar',
    'x':repo_names,
    'y':stars,
    'hovertext': labels,
    'marker':{
    'color':'rgb(60,100,150)',
    'line': {
        'width': 1.5,
        'color':'rgb(60,190,180)'
        },
    },
    'opacity': 0.6
}]

my_layout = {
    'title':'Projekty Pythona oznaczone największą ilością gwiazdek w serwisie GitHub',
    'xaxis': {
        'title':'Repozytorium'
    },
    'yaxis': {
        'title':'Gwiazdki'
    }
}
fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='python_repos.html')
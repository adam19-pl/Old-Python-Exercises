from operator import itemgetter

import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

stories_id = r.json()
stories_dict = []

for storie_id in stories_id[:30]:

    url = f"https://hacker-news.firebaseio.com/v0/item/{storie_id}.json"
    r = requests.get(url)

    print(f"ID:{storie_id} -- {r.status_code}")
    response_dict = r.json()

    storie_dict = {
        'title' : response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={storie_id}",
    }
    if 'descendants' in response_dict:
        storie_dict['comments'] = response_dict['descendants']
    else:
        storie_dict['comments'] = 0

    stories_dict.append(storie_dict)

stories_dict = sorted(stories_dict, key= itemgetter('comments'),
                            reverse=True)


titles, links, comments_list = [],[],[]

for element in stories_dict:
    title = element['title']
    link = element['hn_link']
    link_info = f"<a href={link}><br />{title[:15]}... </a>"

    titles.append(title)
    links.append(link_info)
    comments_list.append(element['comments'])

data = [{
    'type': 'bar',
    'x' : links,
    'y' : comments_list,
    'hovertext':titles,
    'marker': {
        'color':'rgb(100,150,180)',
        'line':{
                'width': 3,
                'color' : 'rgb(150,130,160)'
        },
    'opacity': 0.7
    }
}]


my_layout = {
    'title': 'Najbardziej dyskusyjne artykuły w HackerNews',
    'xaxis' : {
        'title':'Artykuły',
        'titlefont' : {'size': 24},
        'tickfont' : {'size' : 18}

    },
    'yaxis' : {
       'title' : 'Liczba komentarzy',
        'titlefont': {'size': 24},
        'tickfont': {'size': 18, 'color': 'rgb(0,255,70)'}
    }

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='wizualizacjahackernwes.html')

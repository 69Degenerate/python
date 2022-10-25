from pymongo import MongoClient

c = MongoClient("mongodb+srv://vishal:root@cluster0.4g6eqfu.mongodb.net/?retryWrites=true&w=majority")
data=c.db.movieinfo

data.insert_one({
    'name':'Blade Runner 2049',
    'image':'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRPy3V6DD-NB3mNaObNlXqdE80zou2yK4Zk4xkq98vmKDI-6i3B',
    'release_year':'2017',
    'imdb':'8',
    'rt':'88',
    'gerne':'sci-fi,action',
    'desc':'''A young blade runner’s discovery of a long-buried secret leads him to track down former blade runner Rick Deckard, who’s been missing for thirty years.''',
    'cast':'Ryan Gosling,Harrison Ford,Ana de Armas,Sylvia Hoeks,Robin Wright,Mackenzie Davis,Lennie James,Dave Bautista,Jared Leto',
    'link480p':'#',
    'link720p':'#',
    'link1080p':'#',
})
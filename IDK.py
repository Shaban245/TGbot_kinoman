

DataBaseFilms = {'comedy':{
    '2001': ['kara', 'kara_remaster']
}
}

def get_list_films(genre, year, db: DataBaseFilms):
    if genre  in db.keys():
        if year in db[genre].keys():
            return db[genre][year]


    return None
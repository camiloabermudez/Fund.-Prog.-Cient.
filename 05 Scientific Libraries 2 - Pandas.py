import pandas as pd
import numpy as np

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

print(movies)
print(ratings)

# aqui se juntan las dos tablas y  solo muestra los 10 primeros datos
merguer_ratings_movies = pd.merge(movies, ratings)
print('#mergue tables movies + ratings by movies_id field \n%s' % merguer_ratings_movies[:20])

# Merge data
mergeRatings = pd.merge(movies,ratings)

# Clone DataFrame
def cloneDF(df):
    return pd.DataFrame(df.values.copy(), df.index.copy(), df.columns.copy()).convert_objects(convert_numeric=True)

# Show Films with more votes. (groupby + sorted)
numberRatings = cloneDF(mergeRatings)
numberRatings = numberRatings.groupby('title').size().sort_values(ascending=False)#groupy permite agrupar la columna que se indique
print ('Peliculas mas votadas: \n%s' % numberRatings[:20])

# ver el valor medio del rating(groupby + avg)
avgRatings = cloneDF(mergeRatings)
avgRatings = avgRatings.groupby(['movieId', 'title']).mean()#al alicar "mean" calcula todas las medias de las columnas
print ('Avg ratings: \n%s' % avgRatings['rating'][:20])

# ver clasificación de datos de peliculas (groupby + several funtions)#agrupa por titulo e identificador
dataRatings = cloneDF(mergeRatings)
dataRatings = dataRatings.groupby(['movieId', 'title'])['rating'].agg(['mean', 'sum', 'count', 'std'])
print ('Información de calificacìon de peliculas: \n%s' % dataRatings[:20])

# Agrupar por titulo e identificador (groupby + lambda function + sorted)"calcula el # de votos y la nota media",ordena peliculas por el numero de votos
# ver la nota media de las peliculas mas votadas
sortRatingsField = cloneDF(mergeRatings)
sortRatingsField = sortRatingsField.groupby(['movieId', 'title'])['rating'].agg({'COUNT': np.size, 'myAVG': lambda x: x.sum() / float(x.count())}).sort_values('COUNT', ascending=False)
print ('Mi información ordenada: \n%s' % sortRatingsField[:20]) 

import pandas as pd
import matplotlib.pyplot as plt

# 1) On veut extraire le pays le plus peuplé

df_countries= pd.read_csv("countries.csv")

# Trouver la ligne avec la population maximale
pays_plus_peuple = df_countries.loc[df_countries['population'].idxmax()]

# Afficher le pays avec la plus grande population
print("Le pays avec la plus grande population est :", pays_plus_peuple['country'])
print("Il y a", pays_plus_peuple['population'],"habitants")


# 2) On veut extraire le pays le plus densément peuplé, et le moins densément peuplé


# On commence par créer un nouvelle colonne "density"
df_countries['density']=df_countries['population']/df_countries['area']

# On procède de même que précedemment pour extraire le pays avec la densité maximale en habitants
pays_plus_dense = df_countries.loc[df_countries['density'].idxmax()]

#Pour la densité minimale on utilise idmin 
pays_moins_dense = df_countries.loc[df_countries['density'].idxmin()]

# Afficher les résultats
print("")
print("Le pays avec la plus grande densité de population est :", pays_plus_dense['country'])
print("Il y a", pays_plus_dense['density'],"habitants par km^2")
print("")
print("Le pays avec la plus faible densité de population est :", pays_moins_dense['country'])
print("Il y a", pays_moins_dense['density'],"habitants par km^2")


#3) Cherchons à classer les continents par ordre décroissant de population 

# Grouper les données par continent et sommer les populations
population_continent = df_countries.groupby('continent')['population'].sum()

# Classer les continents par population décroissante
classement_population_continents = population_continent.sort_values(ascending=False)

# Afficher le classement
print ("")
print("Classement des continents par population décroissante:")
print(classement_population_continents)

# 4) Classons les continents par ordre décroissant de densité

# Grouper les données par continent et sommer les surfaces des pays
surface_continent=df_countries.groupby('continent')['area'].sum()
densite_continent= population_continent/surface_continent

#Classer par densité décroissante
classement_densite_continents = densite_continent.sort_values(ascending=False)

# Afficher le classement
print ("")
print("Classement des continents par densité décroissante:")
print(classement_densite_continents)

'''Etonnamment, le classement est inchangé par rapport au précédent '''

# 5) Cherchons la grande ville la plus au Sud et la plus au Nord
df_cities= pd.read_csv("cities.csv")
plus_au_nord= df_cities.loc[df_cities['latitude'].idxmax()]
print("")
print("La grande ville la plus au Nord est :", plus_au_nord['city_name'],"qui se situe en", plus_au_nord["country"])
plus_au_sud= df_cities.loc[df_cities['latitude'].idxmin()]
print("La grande ville la plus au Sud est :", plus_au_sud['city_name'],"qui se situe en", plus_au_sud["country"])

# 6) Traçons l'évolution des températures moyennes dans les grandes capitales Européennes

df_weather=pd.read_csv("daily-weather-cities.csv")

# On s'assure que la dataframe est au format datetime pour éviter toute erreur
df_weather['date'] = pd.to_datetime(df_weather['date'])

# On veut faire des études annuelles, donc on crée une colonne 'year'
df_weather['year'] = df_weather['date'].dt.year

# On groupe les données par capitale et année, puis on calcule la température moyenne annuelle
# On ajoute un 'reset index' pour pouvoir continuer à utiliser les index 'year' et 'city_name'
moyennes_annuelles = df_weather.groupby(['city_name', 'year'])['avg_temp_c'].mean().reset_index()

# On extrait les moyennes annuelles pour chaque capitale

for capitale in moyennes_annuelles['city_name'].unique():
    data_capitale = moyennes_annuelles[moyennes_annuelles['city_name'] == capitale]
    # On trace la courbe pour chaque capitale
    plt.plot(data_capitale['year'], data_capitale['avg_temp_c'], label=capitale)


plt.title("Évolution des températures moyennes annuelles dans les capitales européennes")
plt.xlabel("Année")
plt.ylabel("Température moyenne (°C)")
#On légende le graphe et on ajoute un quadrillage
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Capitale")
plt.grid(True)

plt.tight_layout()  # Ajuste l'espacement pour éviter les chevauchements

plt.show()
plt.clf()
'''Globalement, on observe des tendances de températures très correlées entre les capitales.
Il serait sûrement plus pertinent d'étudier l'évolution de la température Européenne 
en faisant une moyenne sur toutes les capitales.
On observe des valeurs étonnantes pour Vienne vers 1950'''

# 7) Température moyenne Européenne
moyennes_annuelles_EU = df_weather.groupby(['year'])['avg_temp_c'].mean().reset_index()
plt.plot(moyennes_annuelles_EU['year'], moyennes_annuelles_EU['avg_temp_c'])

plt.title("Évolution de la température moyenne annuelle en europe")
plt.xlabel("Année")
plt.ylabel("Température moyenne (°C)")
plt.grid(True)
plt.show()
plt.clf()

"""Quelsues valeurs paraissent fausses, mais le tracé permet de clairement conclure 
à un réchauffement climatique net à l'échelle européenne"""


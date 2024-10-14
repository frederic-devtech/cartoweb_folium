import folium
 
# Position latitude, longitude sur laquelle la carte est centrée
location = [47, 1]


# Niveau de zoom initial
# 3-4 pour un continent, 5-6 pour un pays, 11-12 pour une ville
zoom = 6

# Style de la carte
tiles = 'cartodbpositron'

carte = folium.Map(location=location,
                   zoom_start=zoom,
                   tiles=tiles)

# Ajout de marqueur à la carte
# Position du marqueur
latlong_margueur = [45.8, 1.2]

# Texte à afficher lorsqu'on clique sur le marqueur
texte_marqueur = "Limoge est là (à peu près)"

# création du marqueur
marqueur = folium.Marker(location=latlong_margueur,
                         popup=texte_marqueur)

# Ajout du marqueur à la carte
marqueur.add_to(carte)

# display(carte)
carte.save("src/index.html")
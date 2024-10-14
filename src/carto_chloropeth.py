import folium
import pandas as pd
import geopandas as gpd

# utilisation des fichiers shapefiles
# Chemin vers le fichier shapefile et csv
shp_path = 'src/data/shp/georef-france-region-millesime.shp'
csv_path = 'src/data/ensoleillement.csv'

# Traitement du shapefile
# Ouverture du fichier shape en geodataframe
regions_gdf = gpd.read_file(shp_path, encoding='utf-8')


# Slection des regions de métropole avec comme code : FXX
regions_gdf = regions_gdf[regions_gdf.reg_area_co == "FXX"]

# Simplification de la geodataframe de Normandie
regions_gdf = regions_gdf.set_index('reg_name')
regions_gdf  = regions_gdf['geometry']

# Conversion en GeoJson
regions_json  = regions_gdf.to_json()


# Traitement du csv
# Ouverture des onnées csv
ensoleillement = pd.read_csv(csv_path,
                             encoding='utf-8',
                             index_col=0)

# Conversion de J/m2 vers kwh/m2 et arrondi
ensoleillement['ensoleillement'] = ensoleillement['ensoleillement'] / 3600000
ensoleillement['ensoleillement'] = ensoleillement['ensoleillement'].round(1)

# Crééation d'une carte vierge
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

# Création du Chloropeth et ajout de la carte
chloropeth = folium.Choropleth(geo_data=regions_json)
chloropeth.add_to(carte)


# display(carte)
carte.save("src/carto_chloropeth.html")
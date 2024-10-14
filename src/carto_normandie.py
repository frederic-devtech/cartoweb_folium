import folium
import geopandas as gpd

# utilisation des fichiers shapefiles
# Chemin vers le fichier shapefile
path = 'src/data/shp/georef-france-region-millesime.shp'

# Ouverture du fichier shape en geodataframe
regions_gdf = gpd.read_file(path, encoding='utf-8')


# Slection des regions de métropole avec comme code : FXX
regions_gdf = regions_gdf[regions_gdf.reg_area_co == "FXX"]

# Séléction de la normandie
normandie_gdf = regions_gdf[regions_gdf.reg_name_up == "NORMANDIE"]

# Simplification de la geodataframe de Normandie
normandie_gdf = normandie_gdf.set_index('reg_name')
normandie_gdf = normandie_gdf['geometry']


# Conversion en GeoJson
normandie_json = normandie_gdf.to_json()

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
chloropeth = folium.Choropleth(geo_data=normandie_json)
chloropeth.add_to(carte)


# display(carte)
carte.save("src/map_chloropeth.html")
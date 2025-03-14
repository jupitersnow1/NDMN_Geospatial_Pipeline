import folium
from folium.plugins import MarkerCluster

def plot_geometry(geo_df):
    if geo_df.empty:
        print("No valid geometries to plot.")
        return None

    center_lat = geo_df.geometry.y.mean()
    center_lon = geo_df.geometry.x.mean()

    m = folium.Map(location=[center_lat, center_lon], zoom_start=8)

    marker_cluster = MarkerCluster().add_to(m)  # Speed up rendering with clustering

    for _, row in geo_df.iterrows():
        if row.geometry.geom_type == "Point":
            folium.Marker(
                location=[row.geometry.y, row.geometry.x],
                popup=f"ID: {row.get('id', 'N/A')}"
            ).add_to(marker_cluster)

    return m

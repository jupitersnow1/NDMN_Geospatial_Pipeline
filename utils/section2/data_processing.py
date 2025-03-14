import geopandas as gpd
from shapely import wkt
# from shapely.geometry import Point, LineString, Polygon

def inspect_and_convert(data):
    """Ensure data contains a geometry column and convert it to GeoDataFrame efficiently."""
    if "geometry" in data.columns:
        try:
            # Use `.str.startswith` directly on the column to quickly filter valid WKT rows
            valid_wkt = data["geometry"].astype(str).str.startswith(("POINT", "LINE", "POLYGON"))
            if not valid_wkt.any():
                print("Warning: No valid WKT data found.")
                return None

            # Convert using vectorized `.map()` instead of `apply()`
            data = data[valid_wkt].copy()
            data["geometry"] = data["geometry"].map(wkt.loads)

            # Convert to GeoDataFrame
            geo_df = gpd.GeoDataFrame(data, geometry="geometry", crs="EPSG:4326")
            return geo_df
        except Exception as e:
            print(f"Error converting geometry: {e}")
            return None
    else:
        print("No geometry column found!")
        return None

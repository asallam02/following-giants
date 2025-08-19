# from pathlib import Path
# import xarray as xr

# DATA_DIR = Path(__file__).parent.parent / "data" / "weather"

# def get_weather_summary():
#     """Load weather (e.g., sea surface temperature) from NetCDF"""
#     results = {}
#     for file in DATA_DIR.glob("*.nc"):
#         ds = xr.open_dataset(file)
#         # Get basic stats
#         results[file.stem] = {
#             "variables": list(ds.data_vars.keys()),
#             "time_range": str(ds["time"].values[0]) + " → " + str(ds["time"].values[-1]),
#             "lat_range": [float(ds["lat"].values.min()), float(ds["lat"].values.max())],
#             "lon_range": [float(ds["lon"].values.min()), float(ds["lon"].values.max())],
#         }
#     return results

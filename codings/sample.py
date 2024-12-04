def tile_to_bbox(x, y, zoom):
    # Constants for Web Mercator (EPSG:3857)
    ORIGIN_SHIFT = 20037508.34  # Half the Earth's circumference in meters
    TILE_SIZE = 40075016.68 / (2 ** zoom)  # Tile size in meters at this zoom level

    # Calculate the bounding box
    min_x = x * TILE_SIZE - ORIGIN_SHIFT
    max_x = (x + 1) * TILE_SIZE - ORIGIN_SHIFT
    min_y = ORIGIN_SHIFT - (y + 1) * TILE_SIZE
    max_y = ORIGIN_SHIFT - y * TILE_SIZE

    return min_x, min_y, max_x, max_y

# Example usage
zoom = 4
x = 11
y = 8
bbox = tile_to_bbox(x, y, zoom)
bbox = map(str,bbox)
print("Bounding box in EPSG:3857:", '%2C'.join(bbox))

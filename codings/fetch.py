import requests
from PIL import Image
from io import BytesIO
import numpy as np
import imageio
import time

def stitch_images(images, x_count, y_count):
    tile_width, tile_height = images[0].size
    stitched_image = Image.new('RGB', (tile_width * x_count, tile_height * y_count))
    for i, img in enumerate(images):
        x = i % x_count
        y = i // x_count
        stitched_image.paste(img, (x * tile_width, y * tile_height))
    return stitched_image

def fetch_tile_image(bbox,time):
    url = f'https://mosdac.gov.in/live_data/wms/live3RL1BSTD1km/products/Insat3r/3R_IMG/2024/14NOV/3RIMG_14NOV2024_{time}_L1B_STD_V01R00.h5?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&FORMAT=image%2Fpng&TRANSPARENT=true&LAYERS=IMG_VIS&COLORSCALERANGE=18%2C329&BELOWMINCOLOR=extend&ABOVEMAXCOLOR=extend&transparent=true&format=image%2Fpng&STYLES=boxfill%2Fgreyscale&WIDTH=256&HEIGHT=256&CRS=EPSG%3A3857&BBOX={bbox}'
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        print(f"Failed to fetch image for BBOX {bbox}: HTTP {response.status_code}")
        return None
    
def tile_to_bbox(x, y, zoom):
    ORIGIN_SHIFT = 20037508.34  # Half the Earth's circumference in meters
    TILE_SIZE = 40075016.68 / (2 ** zoom)  # Tile size in meters at this zoom level

    min_x = x * TILE_SIZE - ORIGIN_SHIFT
    max_x = (x + 1) * TILE_SIZE - ORIGIN_SHIFT
    min_y = ORIGIN_SHIFT - (y + 1) * TILE_SIZE
    max_y = ORIGIN_SHIFT - y * TILE_SIZE

    bbox = [min_x, min_y, max_x, max_y]
    return "%2C".join(map(str, bbox))
    


x_tiles,y_tiles,zoom= 15,15,4

# images = []
# for i in range(x_tiles):
#     for j in range(y_tiles):
#         bbox = tile_to_bbox(i, j, zoom)
#         img = fetch_tile_image(bbox)
#         if img:
#             images.append(img)

# if images:
#     final_image = stitch_images(images, x_tiles, y_tiles)
#     final_image.show()  # Display the image
#     final_image.save("stitched_image.png")  # Save to file
# else:
#     print("No images fetched. Check the WMS URL or network connectivity.")
    

def video_gen(images,output_file,fps=5,duration=3):
  num_frames = int(fps * duration)
  writer = imageio.get_writer(output_file, fps=fps)

  start_time = time.time()
  
      

  writer.close()

  print(f"Video saved as {output_file}")


times = ['1215','1245','1315','1345']

for i in range(x_tiles):
    for j in range(y_tiles):
        images = []
        for t in times:
            bbox = tile_to_bbox(i, j, zoom)
            img = fetch_tile_image(bbox,t)
            if img:
                images.append(img)
        video_gen(images,f'data/{t}/{i}/{j}.mp4')
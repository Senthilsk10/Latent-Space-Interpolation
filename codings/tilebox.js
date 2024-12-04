function getTileBounds(tileX, tileY, zoom) {
  const tileSize = 256;
  const mapSize = tileSize * Math.pow(2, zoom);
  const originShift = 20037508.34;

  const minX = (tileX * tileSize / mapSize) * (2 * originShift) - originShift;
  const maxY = originShift - (tileY * tileSize / mapSize) * (2 * originShift);
  const maxX = ((tileX + 1) * tileSize / mapSize) * (2 * originShift) - originShift;
  const minY = originShift - ((tileY + 1) * tileSize / mapSize) * (2 * originShift);

  return [minX, minY, maxX, maxY];
}



function createTileData(zoom, topLeft, bottomRight) {
  const tiles = [];
  const minX = topLeft[0];
  const minY = topLeft[1];
  const maxX = bottomRight[0];
  const maxY = bottomRight[1];

  for (let x = minX; x <= maxX; x++) {
      for (let y = minY; y <= maxY; y++) {
          const bbox = getTileBounds(x, y, zoom).join("%2C");
          tiles.push({ z: zoom, x, y, bbox });
      }
  }
  return tiles;
}

// Configuration for top-left and bottom-right corners
const zoomLevel = 4;
const topLeft = [9, 2];       // [x, y] for the top-left corner
const bottomRight = [13, 13]; // [x, y] for the bottom-right corner

// Generate tiles
const tileData = createTileData(zoomLevel, topLeft, bottomRight);
console.log(tileData);


//x =5 y = 15



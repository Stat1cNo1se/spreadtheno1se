const canvas = document.getElementById('noiseCanvas');
const ctx = canvas.getContext('2d');

const noiseInterval = 200; // Change this value to set the interval (milliseconds)

function drawNoise() {
  const width = window.innerWidth;
  const height = window.innerHeight;

  canvas.width = width;
  canvas.height = height;

  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      const value = Math.floor(Math.random() * 256);
      ctx.fillStyle = `rgb(${value},${value},${value})`;
      ctx.fillRect(x, y, 1, 1);
    }
  }

  setTimeout(drawNoise, noiseInterval);
}

drawNoise(); // Start generating noise

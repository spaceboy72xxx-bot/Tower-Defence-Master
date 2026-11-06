import os
import zipfile

# Gumawa ng folder
base_dir = "JS_MOBA_Game"
os.makedirs(base_dir, exist_ok=True)

# Isulat ang mga files
with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write('<!DOCTYPE html><html><head><title>MOBA</title><link rel="stylesheet" href="style.css"></head><body><canvas id="gameCanvas"></canvas><script src="game.js"></script></body></html>')

with open(f"{base_dir}/style.css", "w", encoding="utf-8") as f:
    f.write("body { margin: 0; background: #111; overflow: hidden; } canvas { display: block; }")

with open(f"{base_dir}/game.js", "w", encoding="utf-8") as f:
    f.write('const canvas = document.getElementById("gameCanvas"); const ctx = canvas.getContext("2d");\nlet hero = {x: 100, y: 100, targetX: 100, targetY: 100, speed: 3};\nwindow.addEventListener("contextmenu", e => { e.preventDefault(); hero.targetX = e.clientX; hero.targetY = e.clientY; });\nfunction loop() { ctx.clearRect(0,0,canvas.width,canvas.height); let dx = hero.targetX - hero.x; let dy = hero.targetY - hero.y; let dist = Math.sqrt(dx*dx + dy*dy); if(dist > 1) { hero.x += (dx/dist)*hero.speed; hero.y += (dy/dist)*hero.speed; } ctx.fillStyle = "blue"; ctx.beginPath(); ctx.arc(hero.x, hero.y, 20, 0, Math.PI*2); ctx.fill(); requestAnimationFrame(loop); }\ncanvas.width = window.innerWidth; canvas.height = window.innerHeight; loop();')

# I-zip ang folder
with zipfile.ZipFile("JS_MOBA_Game.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, base_dir))

print("Nagawa na ang JS_MOBA_Game.zip sa iyong storage!")

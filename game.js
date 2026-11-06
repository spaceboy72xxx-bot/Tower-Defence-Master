// Simpleng MOBA Game Logic gamit ang JavaScript (Canvas / Web)
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Hero Object
let hero = {
    x: 100,
    y: 100,
    radius: 20,
    color: "blue",
    speed: 3,
    targetX: 100,
    targetY: 100,
    health: 1000,
    maxHealth: 1000
};

// Click-to-Move Listener (Right Click)
window.addEventListener("contextmenu", (e) => {
    e.preventDefault();
    hero.targetX = e.clientX - canvas.offsetLeft;
    hero.targetY = e.clientY - canvas.offsetTop;
});

// Game Loop
function update() {
    // Movement patungo sa target (Click-to-Move ala MOBA)
    let dx = hero.targetX - hero.x;
    let dy = hero.targetY - hero.y;
    let distance = Math.sqrt(dx * dx + dy * dy);

    if (distance > 1) {
        hero.x += (dx / distance) * hero.speed;
        hero.y += (dy / distance) * hero.speed;
    }
}

function draw() {
    // Linisin ang screen
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // I-draw ang Map Background / Lanes
    ctx.fillStyle = "#222";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // I-draw ang Hero
    ctx.beginPath();
    ctx.arc(hero.x, hero.y, hero.radius, 0, Math.PI * 2);
    ctx.fillStyle = hero.color;
    ctx.fill();
    ctx.closePath();

    // Health Bar
    ctx.fillStyle = "red";
    ctx.fillRect(hero.x - 25, hero.y - 35, 50, 6);
    ctx.fillStyle = "green";
    ctx.fillRect(hero.x - 25, hero.y - 35, (hero.health / hero.maxHealth) * 50, 6);
}

function loop() {
    update();
    draw();
    requestAnimationFrame(loop);
}

// Simulan ang laro
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
loop();

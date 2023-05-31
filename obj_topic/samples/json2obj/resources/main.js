points = []


maxDistance = 60;

for(let i = 0; i < 1000; i++){
    points.push( {
        "type": "point",
        "position": [Math.random() * maxDistance, Math.random() * maxDistance, Math.random() * maxDistance],
        "texture": {
            "color": {
                "r": Math.random()*255,
                "g": Math.random()*255,
                "b": Math.random()*255
            },
            "matted": true,
            "reflection": 1,
            "alpha": 1
        },
        "size": Math.random()
    })
}

console.log(JSON.stringify(points, null, 2));
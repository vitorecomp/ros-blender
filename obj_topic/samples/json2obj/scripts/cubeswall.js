points = []

for(let i = 0; i < 20; i++){
    for(let j = 0; j < 10; j++){
        points.push( {
            "type": "point",
            "position": [i*3,j*3, 0],
            "texture": {
                "color": {
                    "r": 255,
                    "g": 255,
                    "b": 255
                },
                "hard_material": {
                    "ka": [0, 0, 0],
                    "ks": [0, 0, 0],
                    "ns": 0,
                    "d": i/20,
                    "ni": j*0.1,
                    "illum": 3,
                },
                "matted": true,
                "reflection": 1,
                "alpha": 1
            },
            "size": 1
        })
    }
}

console.log(JSON.stringify(points, null, 2));
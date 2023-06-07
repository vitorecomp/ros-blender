const fs = require('fs');

const data = fs.readFileSync('./csvs/teapot_in_shrubbery.csv', 'utf8');
json = [{
    "type": "3d-object",
    "position": [0, 0, 0],
    "points": [],
    "texture": {
        "color": {
            "r": 255,
            "g": 255,
            "b":255
        },
        "matted": true,
        "reflection": 1,
        "alpha": 1
    },
    "size": Math.random()
}];
data.split('\n').forEach((line, index) => {
    if(line.split(',').length < 3) return;
    json[0]["points"].push([Number(line.split(',')[0]), Number(line.split(',')[1]), Number(line.split(',')[2])]);
});

console.log(JSON.stringify(json, null, 2));
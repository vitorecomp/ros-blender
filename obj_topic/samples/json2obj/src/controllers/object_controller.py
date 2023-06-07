
def vertexFromPoint(x, y, z):
    return "v " + str(x) + " " + str(y) + " " + str(z) + "\n"

def _generatePoint(index, point, definedVertices):
    w = point["size"]
    _definedVertices = 0
    content = "#point " + str(index) + "\n"
    content += "\n"

    content += "usemtl material_" + str(index) + "\n"

    content += "#vetices\n"
    for z in range(2):
        for y in range(2):
            for x in range(2):
                _definedVertices+=1
                content += vertexFromPoint(point["position"][0] + x*w*2 -1*w, point["position"][1] + y*w*2 -1*w, point["position"][2] + z*w*2 -1*w)
    
    content += "#faces\n"
    content += "f " + str(definedVertices + 1) + " " + str(definedVertices+2) + " " + str(definedVertices+4) + "\n"
    content += "f " + str(definedVertices + 1) + " " + str(definedVertices+3) + " " + str(definedVertices+4) + "\n"


    content += "f " + str(definedVertices + 1) + " " + str(definedVertices+2) + " " + str(definedVertices+6) + "\n"
    content += "f " + str(definedVertices + 1) + " " + str(definedVertices+5) + " " + str(definedVertices+6) + "\n"

    content += "f " + str(definedVertices + 1) + " " + str(definedVertices+3) + " " + str(definedVertices+7) + "\n"
    content += "f " + str(definedVertices + 1) + " " + str(definedVertices+5) + " " + str(definedVertices+7) + "\n"

    content += "f " + str(definedVertices + 2) + " " + str(definedVertices+4) + " " + str(definedVertices+8) + "\n"
    content += "f " + str(definedVertices + 2) + " " + str(definedVertices+6) + " " + str(definedVertices+8) + "\n"

    content += "f " + str(definedVertices + 3) + " " + str(definedVertices+4) + " " + str(definedVertices+8) + "\n"
    content += "f " + str(definedVertices + 3) + " " + str(definedVertices+7) + " " + str(definedVertices+8) + "\n"

    content += "f " + str(definedVertices + 5) + " " + str(definedVertices+6) + " " + str(definedVertices+8) + "\n"
    content += "f " + str(definedVertices + 5) + " " + str(definedVertices+7) + " " + str(definedVertices+8) + "\n"

    content += "\n"
    content += "\n"

    return content, definedVertices + _definedVertices

def _generateObject(index, objDescription, definedVertices):
    _definedVertices = 0
    content = "#object " + str(index) + "\n"
    content += "\n"

    content += "usemtl material_" + str(index) + "\n"

    content += "#vetices\n"
    vertexs = {}
    faces = []

    for face in objDescription["faces"]:
        for point in face["points"]:
            vertex = vertexFromPoint(point[0], point[1], point[2])
            if(vertex not in vertexs):
                vertexs[vertex] = point

    vertex_indexes = {}
    for point in vertexs.values():
        content += vertexFromPoint(point[0]+objDescription["position"][0], point[1]+objDescription["position"][1], point[2]+objDescription["position"][2])
        _definedVertices+=1
        vertex_indexes[vertexFromPoint(point[0], point[1], point[2])] = _definedVertices

    for face in objDescription["faces"]:
        content += "f "
        for point in face["points"]:
            content += str(vertex_indexes[vertexFromPoint(point[0], point[1], point[2])]) + " "
        content += "\n"
        
    content += "\n"
    content += "\n"

    return content, definedVertices + _definedVertices

def _generateCloudObject(index, objDescription, definedVertices):
    _definedVertices = 0
    content = "#object " + str(index) + "\n"
    content += "\n"

    content += "usemtl material_" + str(index) + "\n"

    content += "#vetices\n"

    for point in objDescription["points"]:
        content += vertexFromPoint(point[0], point[1], point[2])

    content += "\n"

    return content, definedVertices + _definedVertices

POINT_TYPE = "point"
OBJECT_TYPE = "3d-object"
POINT_CLOUD_TYPE = "3d-points"

def generateObj(index, objDescription, definedVertices):
    if(objDescription["type"] == POINT_TYPE):
        return _generatePoint(index, objDescription, definedVertices)
    if(objDescription["type"] == OBJECT_TYPE):
        return _generateObject(index, objDescription, definedVertices)
    if(objDescription["type"] == POINT_CLOUD_TYPE):
        return _generateCloudObject(index, objDescription, definedVertices)
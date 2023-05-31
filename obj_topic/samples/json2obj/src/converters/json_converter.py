import numpy as np

from controllers.object_controller import generateObj
from controllers.mtl_controller import generateMtl

def transformJson2Obj(baseName, jsonObject):
    objContent = ""
    mtlContent = ""
    definedVertices = 0
    for index in range(len(jsonObject)):
        _objContent, _definedVertices = generateObj(index, jsonObject[index], definedVertices)
        _mtlContent = generateMtl(index, jsonObject[index])
        objContent += _objContent
        definedVertices = _definedVertices
        mtlContent += _mtlContent

    return objContent, mtlContent, [(baseName + "-textureName", np.zeros((100,100,3), dtype=np.uint8))]
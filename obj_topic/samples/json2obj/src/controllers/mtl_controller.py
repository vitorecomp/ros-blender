

def generateMtl(index, objDescription):

    content = "#mtl " + str(index) + "\n"
    content += "\n"
    content += "newmtl material_" + str(index) + "\n"
   
    # the ns control the shininess/glossines
    if(objDescription["texture"]["reflection"] > 0):
        content += "Ns " + str(objDescription["texture"]["reflection"] * 1000) + "\n"
    else:
        content += "Ns 200" + "\n"

    # ambient color
    
    
    # the ks control the color
    content += "#color" + "\n"
    content += "Kd " + str(objDescription["texture"]["color"]["r"]/255) + " " + str(objDescription["texture"]["color"]["g"]/255) + " " + str(objDescription["texture"]["color"]["b"]/255) + "\n"
    # the ks control the color
    if(not objDescription["texture"]["matted"] or objDescription["texture"]["reflection"] > 0):
        content += "Ka " + str(objDescription["texture"]["color"]["r"]/255) + " " + str(objDescription["texture"]["color"]["g"]/255) + " " + str(objDescription["texture"]["color"]["b"]/255) + "\n"
    
    if(objDescription["texture"]["reflection"] > 0):
        content += "Ks 0.000000 "+ str(objDescription["texture"]["reflection"]) +" 0.000000" + "\n"
    else:
        content += "Ks 0.9000 0.9000 0.9000" + "\n"
    
    
    #the parameters below control the transparency
    content += "#tranparence"  + "\n"
    content += "d " + str(objDescription["texture"]["alpha"]) + "\n"
    content += "Ni 1.2000" + "\n"
    
    if(objDescription["texture"]["matted"]):
        #illumination - 1 is the value to enable "Color on and Ambient on"
        content += "illum 1" + "\n"
    else:
        #illumination - 3 is the value to enable "Reflection on and Ray trace on"
        content += "illum 3" + "\n"

    content += "\n"
    content += "\n"
    
    return content
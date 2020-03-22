SampleJson = {
    "image": {
        "366": "3D_L0441_41.jpg",
        "367": "3D_L0441_41.jpg",
        "368": "3D_L0441_41.jpg",
        "369": "3D_L0441_41.jpg"},
    "xmin": {
        "366": 1771.9044368601,
        "367": 1336.3112627986,
        "368": 1395.3747440273,
        "369": 1194.1897610921},
    "ymin": {
        "366": 922.2587015738,
        "367": 93.8373940678,
        "368": 1147.3531325666,
        "369": 483.3995157385},
    "xmax": {
        "366": 1984.1638225256,
        "367": 1687.0006825939,
        "368": 1519.0389078498,
        "369": 1380.6088737201},
    "ymax": {
        "366": 1184.2538589588,
        "367": 274.6509533898,
        "368": 1304.1812197337,
        "369": 758.0504691283},
    "label": {
        "366": "Ssid",
        "367": "Antillo",
        "368": "Antillo",
        "369": "Antillo"},
    "height": {
        "366": 261.995157385,
        "367": 180.813559322,
        "368": 156.8280871671,
        "369": 274.6509533898},
    "width": {
        "366": 212.2593856655,
        "367": 350.6894197952,
        "368": 123.6641638225,
        "369": 186.419112628},
    "objArea": {
        "366": 55610.9311538808,
        "367": 63409.402209753,
        "368": 19394.0142634019,
        "369": 51200.1870133627},
    "objPortion": {
        "366": 0.013494864,
        "367": 0.0153872852,
        "368": 0.0047062615,
        "369": 0.0124245278}}

object_id = str(366)

print(SampleJson["image"][object_id])
print(SampleJson["xmin"][object_id])
print(SampleJson["xmax"][object_id])
print(SampleJson["ymin"][object_id])
print(SampleJson["ymax"][object_id])
print(SampleJson["label"][object_id])
print(SampleJson["height"][object_id])
print(SampleJson["width"][object_id])
print(SampleJson["objArea"][object_id])
print(SampleJson["objPortion"][object_id])

im_0 = '3D_L0441_41.jpg'  # 4 objects lowest 3.


def cropper(imageList):

    # I defined THINGS_CLASSES.

    # You can edit the jpg1_str later. -> Here I am testing it only on one image.
    for jpg1_str in imageList:
        #    print('jpg_str:', jpg1_str)
        for object_id, row in DF[DF.image == jpg1_str].iterrows():

            xmin = row.xmin
            xmax = row.xmax
            ymin = row.ymin
            ymax = row.ymax
            # Might be unnecessary but I am keeping it here for a while + better speed performance. (To be checked later.)
            width = row.width
            height = row.height

            # I print the object_id and height and width of each object here. ( Or bounding Box.)
            # print('object_id: '+str(object_id), "objWidth: " +
            #      str(width), "objHeight: "+str(height))

            input_image = Image.open(JPGPATH + jpg1_str)
            # print(input_image)  # Test to see if the image is being read.

            for index in range(len(classes)):
                if row.label == classes[index]:
                    # print("classes[index]: ", classes[index])

                    imcr = input_image.crop((xmin, ymin, xmax, ymax))  # Test
                    # imcr.show()  # Test

                    FINALDIR = parent_dir+list_Of_DirsInside[index] + '/'
                    renameIt = jpg1_str[:-4]
                    imcr.save(FINALDIR + str(object_id) + "_" +
                              str(classes[index]) + "_" + renameIt + '.png')

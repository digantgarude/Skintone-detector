import face_detect
import kMeansImgPy
import cv2
import allotSkinTone


while True:
    img_link = input("Image file name : ")
    image = cv2.imread(img_link)

    # Detect face and extract
    face_extracted = face_detect.detect_face(image)
    # Pass extracted face to kMeans and get Max color list 
    colorsList = kMeansImgPy.kMeansImage(face_extracted)

    print("Main File : ")
    print("Red Component : "+str(colorsList[0]))
    print("Green Component : "+str(colorsList[1]))
    print("Blue Component : "+str(colorsList[2]))

    allotedSkinToneVal = allotSkinTone.allotSkin(colorsList)
    print("alloted skin tone : ")
    print(allotedSkinToneVal)
    # Algorithm stop code.
    stopQ = input("Stop ? ( y || n ) ")
    if stopQ == 'y':
        break

from imageai.Detection import ObjectDetection
import requests
import os
import sys



FILE = 'image.jpg'
dFILE = os.path.join('data', FILE)

def download_image(url):
    img_data = requests.get(url).content
    with open(dFILE, 'wb') as handler:
        handler.write(img_data)

def image_stats():
    return os.stat(FILE).st_size

def run_model():
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
    detector.loadModel()
    outputFile = 'result-' + str(FILE)
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, 'data' , FILE), output_image_path=os.path.join(execution_path ,'data',  outputFile))
    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    person = 0
    for i in detections:
        if i['name'] == 'person':
            person = person + 1
    print(('Persons detected in the image = %s') % (person))

def run():
    if len(sys.argv) > 1:
        download_image(sys.argv[1])
        run_model()
    else:
        print('You need to pass at least one parameter to docker')

if '__main__' in __name__:
    run()


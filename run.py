from application import app
from application.models import User


from flask import Flask, render_template, Response

import cv2
import os
import numpy as np
import os.path
from keras.preprocessing import image as Img
from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.models import Model, load_model
from keras.layers import Input

#Checks if the run.py file has executed directly and not imported

camera = cv2.VideoCapture(0)

base_model = None
model = None
inception_model = None

classes = ['Drinking', 'Eating', 'Enter', 'Laydown', 'Leave', 'Sitdown', 'Standup', 'Takepills', 'Usetelephone', 'Walk']


def getModel():
    global model
    global base_model
    global inception_model

    if model == None:
        print("here")
        model = load_model('model/model.hdf5')
        print("loaded")

    if base_model == None:
        base_model = InceptionV3(
            weights='imagenet',
            include_top=True
        )
        # We'll extract features at the final pool layer.
        inception_model = Model(
            inputs=base_model.input,
            outputs=base_model.get_layer('avg_pool').output
        )

        print("loaded--")


def rescale_list(input_list, size):
    assert len(input_list) >= size
    skip = len(input_list) // size
    output = [input_list[i] for i in range(0, len(input_list), skip)]
    return output[:size]

def gen_frames(id):  
    Activitytext = ""
    currentframe = 0 
    counter = 0

    frames=[]
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, Activitytext, (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
                    
            if counter <= 40:                
                # if video is still left continue creating images 
                name = 'Frames/frame'+"frame_no"+ str(currentframe) + '.jpg'
                cv2.imwrite(name, frame) 
                frames.append(name)  
                currentframe += 1
                counter = counter + 1
            
            else:     
                counter = 0
                currentframe = 0
                rescaled_list = rescale_list(frames,40)
                sequence = []
                for image in rescaled_list:
                        img = Img.load_img(image, target_size=(299, 299))
                        x = Img.img_to_array(img)
                        x = np.expand_dims(x, axis=0)
                        x = preprocess_input(x)
                        features = inception_model.predict(x)
                        sequence.append(features[0])

                sequence = np.array([sequence])
                prediction = model.predict(sequence)
                maxm = prediction[0][0]
                maxid = 0
                for i in range(len(prediction[0])):
                    if(maxm<prediction[0][i]):
                        maxm = prediction[0][i]
                        maxid = i
                
                Activitytext = classes[maxid]
                print("Activity name",' ------- ',classes[maxid])

                ans = User().addactivities(Activitytext,id)
                print(ans)
                
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def runv():
    ans = User().addactivities("Walk")
    print(ans)


#video Streaming and detection of activities

@app.route('/video_feed/<id>')
def video_feed(id):
    getModel()
    return Response(gen_frames(id), mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == '__main__':
    app.run(debug=True)
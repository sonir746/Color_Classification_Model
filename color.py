from ultralytics import YOLO
import pyttsx3

def color(out):
    for result in out:
        color= out[0].names[out[0].probs.top1]
        alert = pyttsx3.init()
        alert.say(F"{color} colour detected in {path}")
        alert.runAndWait()
        alert= None
    return color
    

alert = pyttsx3.init()
# Load a model
model = YOLO('Source\Models\model.pt')  #Trained model
path = RF'Source/Images/img3.jpg'

# Run batched inference on a list of images
results = model(path)  

# finding color
output=color(results)
# Printing Color
print(output)

from ultralytics import YOLO
import pyttsx4

# 🔊 Speak detected color aloud (Windows SAPI5)
def speak_color(color_name, path=None):
    engine = pyttsx4.init(driverName='sapi5')
    engine.setProperty('rate', 130)
    engine.setProperty('volume', 1.0)
    engine.say("Initializing")
    engine.runAndWait()

    text = f"The detected color is {color_name}."
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()

# 📦 Load trained model
model = YOLO('Source/Models/model.pt')
path = 'Source/Images/img2.jpg'

# 🔍 Predict color
results = model(path)
color_name = results[0].names[results[0].probs.top1]

# 🖨️ Show + Speak
print("Detected Color:", color_name)
speak_color(color_name, path)

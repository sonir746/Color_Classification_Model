# Color_Classification_Model

This Deep Learning project detects the color and alerts the human being with the name of the color.

We use the latest deep learning model which provides an accuracy of approximately 75%-85%. We use a custom YOLOv8 model which can classify multiple colors.

## Packages Used

| **Package** | **Version** |
| ----------- | ----------- |
| Python      | 3.8         |
| OpenCV      | 4.8.1       |
| Yolo        | 8.0.2       |
| PyTorch     | 2.1.2       |
| Pyttsx3     | 2.90        |


## Run Locally

### NOTE: Orignal Source folder upload [here](https://drive.google.com/drive/folders/1vbjWbTJuW7OtubahUk9dGdVWMkoR9jhC?usp=sharing)

Clone the project

```bash
  https://github.com/sonir746/Color_Classification_Model.git
```

Go to the project directory

```bash
  cd <directory_path>
```

Install dependencies

```Python
  pip install -r requirements.txt
```

## Training

We use 8 classes of color images to create a label data set and train our model

<img src="Source\Images\Label.png" alt="loading..." style="width:800px;"/>

### Traning Data
<img src="Source\Images\TraningData.png" alt="loading..." style="width:800px;"/>

## Traning Rusult

<img src="Source\Images\results.jpg" alt="loading..." style="width:800px;"/>

## Testing
1.	After that we provide input image to model.

2.	Model will extract the feature from the model and perform conditional  operation on the given feature.

3.	After that, it will print and alert with the name of the color.

## Source Code

```Python
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
path = RF'Source/Images/img2.jpg'

# Run batched inference on a list of images
results = model(path)  

# finding color
output=color(results)
# Printing Color
print(output)


```

## Input Image
<img src="Source\Images\img3.jpg" alt="loading..." style="width:800px; height:500px;"/>

## Predicted Image
<img src="Source\Images\output.png" alt="loading..." style="width:800px;"/>



## Auther

👨🏻‍💼RAHUL SONI

[![linkedin](https://img.shields.io/twitter/url?url=https%3A%2F%2Fwww.linkedin.com&style=social&logo=Linkedin&logoColor=White&label=Linkedin&labelColor=blue&color=blue&cacheSeconds=3600
)](https://www.linkedin.com/in/rahul-soni-004861227)
[![GitHub](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2F&style=social&logo=GitHub&logoColor=Black&label=GitHub&labelColor=abcdef&color=fedcba&cacheSeconds=3600
)](https://github.com/sonir746)



## Feedback

If you have any feedback, please reach out to us at rahulsoni7469@gmail.com

Or

Report any issue here
<br>
👇👇👇
<br>
[![GitHub](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com&style=social&logo=GitHub&label=issue&labelColor=grey&color=grey
)](https://github.com/sonir746/Color_Classification_Model/issues)

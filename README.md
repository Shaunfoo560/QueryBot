<h1 align="center"> Multipurpose AI Chatbot </h1>

___Training the bot:___

- __Tokenizes__ and __lemmatizes__ the patterns in intents.json, compiling them into a list
- From the __Tensorflow__ library, implements __dense__ and __dropout__ layers following a __sequential__ model, using the __Rectified Linear Unit__ as the activation function for all layers except the final layer, which uses the __softmax__ activation function to scale the data into probabilities
- Couldn't reach a clear conclusion on which optimizer algorithm was better __(SGD vs Adam)__ even after a ton of tests, so I just left them both in (commented out SGD).
- __Categorical cross-entropy__ used as loss function for my ANN due to __multi-label/class classification__
<br></br>

___How the bot picks responses:___

- Uses __Bag-Of-Words__ model to get an appropriate response to an input message based on probability
<br></br>

# Built With:
<p>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="VS Code" height="65" style="vertical-align:top; margin:4px">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/1200px-Tensorflow_logo.svg.png" alt="VS Code" height="60" style="vertical-align:top; margin:4px">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/1200px-Keras_logo.svg.png" alt="VS Code" height="60" style="vertical-align:top; margin:4px">
<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png" alt="VS Code" height="60" style="vertical-align:top; margin:4px">
<img src="https://cdn.worldvectorlogo.com/logos/html-1.svg" alt="VS Code" height="60" style="vertical-align:top; margin:4px">
<img src="https://cdn4.iconfinder.com/data/icons/social-media-logos-6/512/121-css3-512.png" alt="VS Code" height="60" style="vertical-align:top; margin:4px">
<img src="https://www.pngkey.com/png/detail/98-985032_flask-logo-flask-python-icon.png" alt="VS Code" height="60" style="vertical-align:top; margin:4px">
</p>
<br></br>

# Getting Started:
After downloading all files:
- Create a virtual environment and activate it
- Install all required dependencies: tensorflow, nltk, flask, pickle, numpy
- In order to update the bot's response capabilities, modify intents.json as you wish
- Train the bot by running the train.py file
- Start the bot by running the app.py file
<br></br>

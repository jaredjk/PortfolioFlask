from flask import Flask, render_template #this imports Flask to allow us to creat our app
                            # render_template to allow us to render index.html
app = Flask(__name__) #this is global veriable __name__ tells Flask whether or not we are running the file
                            # directly, or importing it as a module.
# @app.route('/success') #The "@" symbol designates a "decorate" whcih attaches the following
# def success():                    # function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
#     return render_template('success.html')

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello World!' # Return the string ' Hellow World' as a response.abs
app.run(debug=True)         # Run the app in debug mode.
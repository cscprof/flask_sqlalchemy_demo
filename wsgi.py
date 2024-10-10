'''
This is the main entry point into the application.  From the command line
you can run python flasky.py from the project's base directory and it will
launch the built-in web server.  this web server is for development purposes
only (and for doing the demo of our code to the TAs.)

There should be no need to make any changes to this file.
'''

from app import create_app

'''
    This is where we can define the specific configuration to load
'''
app = create_app() # 'default')

if __name__ == '__main__':
    app.run(debug=True)
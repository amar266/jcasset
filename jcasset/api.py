from flask_restful import Api
from  views import Server, Spawn
from app import app


api = Api(app)
api.add_resource(Server, '/Server', '/Server/<serial_no>')
api.add_resource(Spawn, '/Spawn/<serial_no>')
if __name__ == "__main__":
    app.run(debug=True)



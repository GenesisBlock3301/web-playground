import jsonpickle
from flask import Flask, request, jsonify
from models import db, EmployeeModel
from flask_restful import Api, Resource
import jsonpickle

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CRUD.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_request
def create_table():
    db.create_all()


class BookListView(Resource):
    def get(self):
        """Todo get all object from BookModel
        and return the json object
        """
        employees = EmployeeModel.query.all()

        return {'Employees': [x.json() for x in employees]}

    def post(self):
        """Todo user send data and convert this data as Json
        and then this json format data converted into python
        native code and then after solving specific task this
        will return as a Json again.
        """
        # get json from user or from api.
        data = request.get_json()
        # print("dattttttttttttttttttttta",data)
        new_employee = EmployeeModel(employee_id=data['employee_id'], name=data['name'], age=data['age'],
                                     position=data['position'])
        new_employee.create()
        # again python readable code to json
        return new_employee.json(), 201


class Employee(Resource):
    def get(self, name):
        """Todo get a employee from user
        if book exist return it else return 404
        """
        employee = EmployeeModel.query.filter_by(name=name).first()
        if employee:
            return employee.json()
        return {"message": "emloyee not found "}, 404

    def put(self, name):
        """Todo convert the json data to python format"""
        """Todo search the book if exists update it 
        else not found 404"""
        data = request.get_json()
        employee = EmployeeModel.query.filter_by(name=name).first()
        if employee:
            employee.employee_id = data['employee_id']
            employee.name = data['name']
            employee.age = data['age']
            employee.position = data['position']
        else:
            employee = EmployeeModel(name=name, **data)
        # hit on data base using database class method
        employee.create()
        return employee.json()

    def delete(self, name):
        employee = EmployeeModel.query.filter_by(name=name).first()
        if employee:
            employee.delete()
            return {"message": "Delete employee successfully"}
        else:
            return {"message": "employee not found"}, 404


api.add_resource(BookListView, '/employees/')
api.add_resource(Employee, '/employee/<string:name>/')

if __name__ == "__main__":
    app.run(host='localhost', port=5000)

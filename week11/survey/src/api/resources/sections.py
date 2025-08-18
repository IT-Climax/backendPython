from flask import request, jsonify
from flask_restful import Resource, Api 
from flask import Blueprint
from src.db.model.sections import Section
from src.db.core import db

#create blueprints for section routes 

sections_bp = Blueprint('sections', __name__)
api = Api(sections_bp)


# class SectionResource(Resource):

class sectionList(Resource):
    def get(self):
        sections= Section.query.all()
        return jsonify([section.serialize()for section in sections])
    
    def post(self):
        #create New sections

        data = request.get_json()
        if not data or 'name' not in data:
            return {'error :please provide a name '}, 400
        
        if Section.query.filter_by(name=data['name']).first():
            return {'message': 'section already exists'}, 400
        
        new_section = Section(name=data['name'])
        db.session.add(new_section)
        db.session.commit()

        #Ensure serialize() returns a dictionary
        # return jsonify(new_section.serialize()), 201

        return jsonify({'message': 'creating record is successful'}), 201
    
class sectionResource(Resource):
        def get(self,section_id):
            sections=Section.query.get(section_id)
            if not sections:
                 return ({'message:section not found'})
            return jsonify(sections.serialize())
        
        def put (self,section_id):
            data = request.get_json()
            sections = Section.query.get(section_id) 
            if not sections:
                 return ({'message:section not found'})
            if 'name' in data:
                 if Section.query.filter_by(name=data['name']).first():
                     return ({'message:section already exists'})
            sections.name = data['name']

            db.session.commit()
            return jsonify({'message':'section updated successfully','Section':Section.serialize()}), 200
        

        def delete(self,section_id):
            sections= Section.query.get(section_id) 
            if not sections:
                return ({'message:section not found'})
            db.session.delete(sections)
            db.session.commit()
            return jsonify({'message':'user deleted successfully'}), 200
             

# register routes
api.add_resource(sectionResource, '/sections/<int:section_id>')
api.add_resource(sectionList, '/sections')




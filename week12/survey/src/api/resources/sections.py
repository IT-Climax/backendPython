from flask import request,jsonify
from flask_restful import Resource, Api
from flask import Blueprint
from src.db.models.sections import Section
from src.db.core import db

#  create blueprint for sections routes
sections_bp = Blueprint("sections",__name__)
api = Api(sections_bp)


#  to create, getSingle, update and delete
class SectionList(Resource):
    def get(self):
        sections = Section.query.all()
        return jsonify([section.serialize()for section in sections])
    
    def post(self):

        """create new section"""
        data = request.get_json()
        if not data or "name" not in data:
            return {"message":"missing name in request"},400
        
        if Section.query.filter_by(name=data["name"]).first():
            return {"message":"section name already exists"},400
        
        new_section = Section(name=data["name"])
        db.session.add(new_section)
        db.session.commit()

        # ensure serialize() returns a  dictionary
        # return jsonify(new_section.serialize()),201

        return jsonify({"message":"creating record is successful"}),201
    def get(self,section_id):
        """get a single section by ID"""
        section = Section.query.get(section_id)
        if not section:
            return {"message": "section not found"}, 404

        return jsonify(section.serialize())


# to get all
class SectionResource(Resource):
    """handle collection of sections"""
    def get(self):
        """list all sections"""
        sections = Section.query.all()
        return jsonify([section.serialize() for section in sections])
    
    
    


# register routes
api.add_resource(SectionResource, "/sections")
api.add_resource(SectionList, "/sections", "/sections/<int:section_id>")
from flask_restful import Resource, reqparse
from flask import request, jsonify
from models import db, Tutor, Pet, TutorSchema, PetSchema

tutor_schema = TutorSchema()
tutors_schema = TutorSchema(many=True)

pet_schema = PetSchema()
pets_schema = PetSchema(many=True)

class TutorResource(Resource):
    def get(self, tutor_id=None):
        if tutor_id is None:
            tutors = Tutor.query.all()
            return tutors_schema.dump(tutors), 200
        
        tutor = Tutor.query.get(tutor_id)
        return tutor_schema.dump(tutor), 200
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True, help="O campo 'nome' é obrigatório")
        args = parser.parse_args()
        tutor = Tutor(nome=args['nome'])
        db.session.add(tutor)
        db.session.commit()
        return tutor_schema.dump(tutor), 201

    def put(self, tutor_id):
        tutor = Tutor.query.get(tutor_id)
        if not tutor:
            return {"message": "Tutor não encontrado"}, 404
        
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True, help="O campo 'nome' é obrigatório")
        args = parser.parse_args()

        tutor.nome = args['nome']
        db.session.commit()
        return tutor_schema.dump(tutor), 200

    def delete(self, tutor_id):
        tutor = Tutor.query.get(tutor_id)
        if not tutor:
            return {"message": "Tutor não encontrado"}, 404

        db.session.delete(tutor)
        db.session.commit()
        return {"message": "Tutor deletado com sucesso"}, 204

class PetResource(Resource):
    def get(self, pet_id):
        pet = Pet.query.get(pet_id)
        if not pet:
            return {"message": "Pet não encontrado"}, 404
        return pet_schema.dump(pet), 200
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True, help="O campo 'nome' é obrigatório")
        parser.add_argument('tutor_id', type=int, required=True, help="O campo 'tutor_id' é obrigatório")
        args = parser.parse_args()

        tutor = Tutor.query.get(args['tutor_id'])
        if not tutor:
            return {"message": "Tutor não encontrado"}, 404

        pet = Pet(nome=args['nome'], tutor_id=args['tutor_id'])
        db.session.add(pet)
        db.session.commit()
        return pet_schema.dump(pet), 201
    
    def put(self, pet_id):
        pet = Pet.query.get(pet_id)
        if not pet:
            return {"message": "Pet não encontrado"}, 404
        
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True, help="O campo 'nome' é obrigatório")
        parser.add_argument('tutor_id', type=int, required=True, help="O campo 'tutor_id' é obrigatório")
        args = parser.parse_args()
        
        tutor = Tutor.query.get(args['tutor_id'])
        if not tutor:
            return {"message": "Tutor não encontrado"}, 404
        
        pet.nome = args['nome']
        pet.tutor_id = args['tutor_id']
        db.session.commit()
        return pet_schema.dump(pet), 200
        

    def delete(self, pet_id):
        pet = Pet.query.get(pet_id)
        if not pet:
            return {"message": "Pet não encontrado"}, 404

        db.session.delete(pet)
        db.session.commit()
        return {"message": "Pet deletado com sucesso"}, 204

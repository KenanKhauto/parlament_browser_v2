
from flask import Blueprint
from app.server.extensions import db, factory

class RawDataRoutes:

    raw = Blueprint('raw_data', __name__)

    @raw.route("/protocol-raw")
    def protocol_raw():
        protolcols = db.get_protocols()
        send = []
        for protocol in protolcols:
            doc = protocol.document
            send.append(doc)
        response = {"message": "success", "data": send}
        return response
    
    @raw.route("/protocol-raw/<string:protocol_id>", methods=["GET"])
    def protocol_raw_by_id(protocol_id):
        protocol = db.get_protocol_by_id(protocol_id)
        doc = protocol.document
        response = {"message": "success", "data": doc}
        return response

    @raw.route("/speech-raw")
    def speech_raw():
        speeches = db.get_speeches()
        send = []
        for speech in speeches:
            doc = speech.document
            send.append(doc)
        response = {"message": "success", "data": send}
        return response
    

from flask import Blueprint
from backend.app.server.extensions import db, factory

class RawDataRoutes:

    raw = Blueprint('raw_data', __name__)

    @raw.route("/protocol-raw")
    def protocol_raw():
        protolcols = db.get_protocols()
        send = []
        for protocol in protolcols:
            send.append(protocol.to_json())
        return {
            "protocols": send,
        }
    
    @raw.route("/protocol-raw/<string:protocol_id>", methods=["GET"])
    def protocol_raw_by_id(protocol_id):
        protocol = db.get_protocol_by_id(protocol_id)
        
        return protocol.to_json()
        

    @raw.route("/speech-raw")
    def speech_raw():
        speeches = db.get_speeches()
        send = []
        for speech in speeches:
            send.append(speech.to_json())
        
        return {
            "speeches": send,
        }
    
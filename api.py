import os
import playsound


from flask import Flask, request, abort, jsonify, send_from_directory


UPLOAD_DIRECTORY = "project/api_uploaded_files"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


"""
Problem: unable to send and recieve .wav files, can only work with .mp3 files and maybe some other extensions
as well. When I open 

"""

api = Flask(__name__)


@api.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@api.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@api.route("/files/<filename>", methods=["POST"])
def post(filename):
    """Upload a file."""

    #?if "/" in filename:
        #?# Return 400 BAD REQUEST
        #?abort(400, "no subdirectories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(request.data)

    
    "Just play it to verify if it is corrupted."
    playsound.playsound(UPLOAD_DIRECTORY +"/"+ filename)
    



    #os.system("wav", + filename) When I do this, it throws some error, i think that the wav file to be sent is not properly serialized..

    # Return 201 CREATED
    return "", 201


if __name__ == "__main__":
    api.run(debug=True)
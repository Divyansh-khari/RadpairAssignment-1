# flask-app/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Hardcoded template text for demonstration
template_data = {
    1: """EXAM:
CT Left Ankle, without IV contrast

CLINICAL HISTORY:
Left ankle injury.

TECHNIQUE:
Axial images were acquired through the left ankle without IV contrast.
Reformatted images were reviewed.
Dose reduction technique was used including one or more of the following:
automated exposure control, adjustment of mA and kV according to patient size,
and/or iterative reconstruction.

COMPARISON:
None provided.

FINDINGS:

BONES:
There is an acute obliquely oriented fracture of the lateral malleolus with minimal lateral displacement.

JOINTS:
No dislocation. There is a small ankle joint effusion. 

SOFT TISSUES:
Lateral malleolar soft tissue swelling is present. 

IMPRESSION:

1. Acute obliquely oriented fracture of the lateral malleolus as described above. 
""",
    
}

@app.route('/api/template/<int:template_id>', methods=['GET'])
def get_template(template_id):
    if template_id in template_data:
        return jsonify({'template_text': template_data[template_id]})
    return jsonify({'template_text': 'Template not found'}), 404

@app.route("/")
def hello_world():
    return "<p>Flask backend is running</p>"

if __name__ == '__main__':
   app.run()

import classifier
import os
from flask import Flask, request, jsonify

UPLOAD_FOLDER = '/tmp'

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@application.route('/tensor/classify', methods=['POST'])
def classify_event():
    uploaded_file = request.files['file']
    fn = os.path.join(application.config['UPLOAD_FOLDER'], 'image.jpg')
    uploaded_file.save(fn)
    return jsonify(classifier.run_inference_on_image(fn))


@application.route('/health', methods=['GET'])
def health():
    return 'OK'


if __name__ == '__main__':
    classifier.maybe_download_and_extract()
    application.run(host='0.0.0.0', debug=True)

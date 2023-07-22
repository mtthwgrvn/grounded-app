from flask import Flask, jsonify, request
from text_processor import process_text
from keyword_extractor import extract_keywords
from code_extractor import extract_codes
from report_generator import generate_report

app = Flask(__name__)

@app.route('/keywords', methods=['GET'])
def get_keywords():
    corpus_file = request.args.get('corpus_file')
    stopwords_file = request.args.get('stopwords_file')
    keywords = extract_keywords(corpus_file, stopwords_file)
    return jsonify(keywords)

@app.route('/open_codes', methods=['GET'])
def get_open_codes():
    open_codes_file = request.args.get('open_codes_file')
    with open(open_codes_file, 'r') as f:
        open_codes = f.read().splitlines()
    return jsonify(open_codes)

@app.route('/open_codes', methods=['POST'])
def post_open_codes():
    open_codes_file = request.form.get('open_codes_file')
    new_open_code = request.form.get('new_open_code')
    with open(open_codes_file, 'a') as f:
        f.write(new_open_code + '\n')
    return '', 204

@app.route('/codes', methods=['POST'])
def post_codes():
    corpus_file = request.form.get('corpus_file')
    keywords = request.form.get('keywords')
    codes = request.form.get('codes')
    extract_codes(corpus_file, keywords, codes)
    return '', 204

@app.route('/axial_codes', methods=['GET'])
def get_axial_codes():
    axial_codes_file = request.args.get('axial_codes_file')
    with open(axial_codes_file, 'r') as f:
        axial_codes = f.read().splitlines()
    return jsonify(axial_codes)

@app.route('/axial_codes', methods=['POST'])
def post_axial_codes():
    axial_codes_file = request.form.get('axial_codes_file')
    new_axial_code = request.form.get('new_axial_code')
    with open(axial_codes_file, 'a') as f:
        f.write(new_axial_code + '\n')
    return '', 204

@app.route('/selective_codes', methods=['GET'])
def get_selective_codes():
    selective_codes_file = request.args.get('selective_codes_file')
    with open(selective_codes_file, 'r') as f:
        selective_codes = f.read().splitlines()
    return jsonify(selective_codes)

@app.route('/selective_codes', methods=['POST'])
def post_selective_codes():
    selective_codes_file = request.form.get('selective_codes_file')
    new_selective_code = request.form.get('new_selective_code')
    with open(selective_codes_file, 'a') as f:
        f.write(new_selective_code + '\n')
    return '', 204

@app.route('/axial', methods=['GET'])
def get_axial():
    corpus_file = request.args.get('corpus_file')
    open_codes_file = request.args.get('open_codes_file')
    axial_codes_file = request.args.get('axial_codes_file')
    text = process_text(corpus_file)
    with open(open_codes_file, 'r') as f:
        open_codes = f.read().splitlines()
    with open(axial_codes_file, 'r') as f:
        axial_codes = f.read().splitlines()
    axial_data = []
    for open_code in open_codes:
        open_instances = [instance for instance in text if open_code in instance]
        for open_instance in open_instances:
            axial_instance = {
                'keyword': open_code,
                'instance': open_instance,
                'axial_codes': []
            }
            for axial_code in axial_codes:
                axial_instances = [instance for instance in text if axial_code in instance and open_instance in instance]
                axial_instance['axial_codes'].extend(axial_instances)
            axial_data.append(axial_instance)
    return jsonify(axial_data)

if __name__ == '__main__':
    app.run()


from flask import Blueprint, render_template, request, jsonify
from .main import calculate_plagiarism_score
from .models import PlagiarismCheck
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/check_plagiarism', methods=['POST'])
def check_plagiarism():
    code1 = request.form['code1']
    code2 = request.form['code2']
    
    similarity_score = calculate_plagiarism_score(code1, code2)
    
    check = PlagiarismCheck(code1=code1, code2=code2, similarity_score=similarity_score)
    db.session.add(check)
    db.session.commit()
    
    return jsonify({'similarity_score': similarity_score})
# Plagiarism Detector

This web application detects plagiarism between two code snippets using various similarity detection techniques.

## Features

- Compares two code snippets and calculates a similarity score
- Uses multiple similarity detection methods:
  - Sequence matching
  - TF-IDF vectorization
  - Word2Vec embeddings
- Provides a web interface for easy use
- Stores plagiarism check results in a SQLite database

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/k1suxu/plagiarism_detector.git
   cd plagiarism-detector
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```
   python init_db.py
   ```

## Running the Application

1. Ensure you're in the project root directory and your virtual environment is activated.

2. Run the application:
   ```
   python run.py
   ```

3. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Enter two code snippets in the provided text areas.
2. Click the "Check Plagiarism" button.
3. The similarity score will be displayed on the page.

## Troubleshooting

If you encounter any issues during setup or execution, try the following:

1. Ensure all dependencies are correctly installed:
   ```
   pip install -r requirements.txt
   ```

2. If you get a "Template not found" error, check that your project structure is correct and that `templates/index.html` exists.

3. If you encounter database-related errors:
   - Ensure the database is initialized by running `python init_db.py`
   - Check that the `plagiarism_detector.db` file exists in the `app` directory
   - If issues persist, delete the existing database file and re-run `python init_db.py`

4. Clear Python cache files:
   ```
   find . -type d -name __pycache__ -exec rm -r {} +
   find . -name '*.pyc' -delete
   ```

5. If you're still experiencing issues, check the console output for specific error messages and refer to the Flask documentation or seek help in Python and Flask communities.

## Project Structure

```
plagiarism_detector/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── tests/
│   └── test_plagiarism_detector.py
├── .gitignore
├── README.md
├── requirements.txt
├── run.py
└── init_db.py
```

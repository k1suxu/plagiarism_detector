# Plagiarism Detector

This web application detects plagiarism between two code snippets using various similarity detection techniques.

## Features

- Compares two code snippets and calculates a similarity score
- Uses multiple similarity detection methods:
  - Sequence matching
  - TF-IDF vectorization
  - Word2Vec embeddings
- Provides a web interface for easy use
- Stores plagiarism check results in a database

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/plagiarism-detector.git
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

4. Run the application:
   ```
   python run.py
   ```

5. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Enter two code snippets in the provided text areas.
2. Click the "Check Plagiarism" button.
3. The similarity score will be displayed on the page.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
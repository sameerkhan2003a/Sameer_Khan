from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default to port 10000 if PORT is not set
    app.run(host='0.0.0.0', port=port, debug=True)

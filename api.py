import string, random, json
from flask import Flask, redirect, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/short/<path:link>', methods=["GET"])
def short(link):
    gen = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    db = json.loads(open("db.json", "r").read())
    db[gen] = link
    json.dump(db, open("db.json", "w"))
    return jsonify({"success": True, "data": {"id": gen, "link": f"https://{request.host}/{gen}"}})

@app.route('/<id>', methods=["GET"])
def link(id):
    db = json.loads(open("db.json", "r").read())
    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="refresh" content="0;url={db.get(id)}">
        </head>
        <body>
            <p>Redirecting...</p>
            <p>Powered by <a href="https://github.com/vodkarm/UShorten/>UShorten</a>UShorten</p>
        </body>
        </html>
        """ if db.get(id) else jsonify({"success": False, "error": "Link not found."}), 400

if __name__ == "__main__":
    app.run("0.0.0.0", 6969)

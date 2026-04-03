from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()

    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")

        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
        os.makedirs(folder_path, exist_ok=True)

        input_files = []

        # Save files
        for file in request.files.values():
            if file:
                filename = secure_filename(file.filename)
                filename = filename.replace(" ", "_").replace("(", "").replace(")", "")
                
                file.save(os.path.join(folder_path, filename))
                input_files.append(filename)  # ✅ FIXED

        # Save description (OUTSIDE loop)
        with open(os.path.join(folder_path, "desc.txt"), "w") as f:
            f.write(desc)

        # Create input.txt (CLEAN FORMAT)
        with open(os.path.join(folder_path, "input.txt"), "w") as f:
            for fl in input_files:
                full_path = os.path.join(folder_path, fl).replace("\\", "/")
                f.write(f"file '{full_path}'\n")
                f.write("duration 1\n")
                
    return render_template("create.html", myid=myid)
    
@app.route("/gallery")
def gallery():
    reels=os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html",reels=reels)

app.run(debug=True)
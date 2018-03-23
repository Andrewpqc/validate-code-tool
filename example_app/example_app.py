import validateCodeTool
from io import BytesIO
from flask import Flask
from flask import request
from flask import render_template, make_response

app = Flask(__name__)


@app.route('/example-app/')
def index():
    """index page"""
    return render_template("index.html")


@app.route("/example-app/check-code/", methods=["POST"])
def check_code():
    """to check whether the code is right"""
    code = request.form.get("code", None)
    if code.lower() == request.cookies.get("checkcode").lower():
        return "successful!"
    else:
        return "failed!"


@app.route("/example/get-check-code/")
def get_check_code():
    """
    to generate the image and the char.
    set the chars to cookie and save the image
    in memory.
    """
    stream = BytesIO()
    img, code = validateCodeTool.create_validate_code()
    img.save(stream, "PNG")  #将图片直接保存到内存中，避免读写磁盘
    resp = make_response(stream.getvalue())
    resp.set_cookie("checkcode", code)
    return resp


if __name__ == '__main__':
    app.run()

from flask import render_template


def error_view(error):
    return render_template("error/not_found.html")

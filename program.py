#!/usr/bin/env python3
from flask import Flask, request, render_template, abort
import subprocess, shlex

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', result=None)
    elif request.method == 'POST':
        res = run_command(request.form['command'])
        return render_template('index.html', result=res)
    else:
        abort(404)



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

def run_command(command: str) -> str:
    """Runs a system command and returns the output from stdout"""
    banned = ['sudo']

    if any(x in command.lower() for x in banned):
        return "[X] Error: Command contains banned keyword!\n" + \
               "[X] Command Entered: {command}"

    inp = command
    print(inp)
    res = subprocess.run(inp, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    return res.stdout.decode('utf-8')


def main():
    print("Running")
    app.run('0.0.0.0', 8000)


if __name__ == "__main__":
    main()
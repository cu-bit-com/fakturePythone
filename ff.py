# -*- coding: utf-8 -*-

import subprocess
import os
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
lista = ["banana", "jabuka", "kruška"]
cijene = [5.00, 10.00, 15.00]
total = 0
#print(range(len(lista)))
racun = [f"{_+1}. {lista[_]} {cijene[_]:.2f} €" for _ in range(len(lista))]
for _ in racun:
    #print(_)
    total += float(_.split()[2])

#print("TOTAL:", round(total, 2), "€")

pdf_directory = "/home/ubuntu" 
@app.route('/generate_pdf', methods=['GET'])
def generate_pdf():
    try:
        if not os.path.exists(pdf_directory):
            os.makedirs(pdf_directory)

        output_pdf = os.path.join(pdf_directory, "output.pdf")
        url = "https://www.google.com/"
	#dio subprocessa koji se spaja na wkhtmltopdf
        command = [
            "/usr/bin/wkhtmltopdf",
            "--disable-smart-shrinking", 
# "	    "--javascript-delay", "5000", ovo je u slučaju da stranici treba dugo da se loada
            url,
            output_pdf
        ]
	#package zadužen za komuniciranje s wkhtmltopdf
        subprocess.run(command, check=True)
#basic generiranje totalne sume i printanje iste na stranicu, testno!
        total = sum(float(_.split()[2]) for _ in racun)
        items_info = "<br>".join(racun)
        response_message = f'Items:<br>{items_info}<br>TOTAL: {round(total, 2)} €.<br>Click <a href="/download_pdf/output.pdf" download>here</a> to download the PDF.'
#printa poruku u terminal
        return response_message, 200
#error ako ne radi 
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/download_pdf/<filename>', methods=['GET'])
def download_pdf(filename):
    return send_file(os.path.join(pdf_directory, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# -*- coding: utf-8 -*-
import subprocess
import os
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
lista = ["banana", "jabuka", "kruška€"]
cijene = [5.00, 10.00, 15.00]
total = 0
#print(range(len(lista)))
racun = [f"{_+1}. {lista[_]} {cijene[_]:.2f} e" for _ in range(len(lista))]
for _ in racun:
    #print(_)
    total += float(_.split()[2])

#print("TOTAL:", round(total, 2), "e")

pdf_directory = "/home/ubuntu" 
@app.route('/generate_pdf', methods=['GET'])
def generate_pdf():
    try:
        if not os.path.exists(pdf_directory):
            os.makedirs(pdf_directory)

        output_pdf = os.path.join(pdf_directory, "output.pdf")
        url = "https://www.google.com/"
	#dio subprocessa koji se spaja na wkhtmltopdf
        command = [
            "/usr/bin/wkhtmltopdf",
            "--disable-smart-shrinking", 
# "	    "--javascript-delay", "5000", ovo je u slučaju da stranici treba dugo da se loada
            url,
            output_pdf
        ]
	#package zadužen za komuniciranje s wkhtmltopdf
        subprocess.run(command, check=True)
#basic generiranje totalne sume i printanje iste na stranicu, testno!
        total = sum(float(_.split()[2]) for _ in racun)
        items_info = "<br>".join(racun)
        response_message = f'Items:<br>{items_info}<br>TOTAL: {round(total, 2)} e.<br>Click <a href="/download_pdf/output.pdf" download>here</a> to download the PDF.'
#printa poruku u terminal
        return response_message, 200
#error ako ne radi 
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/download_pdf/<filename>', methods=['GET'])
def download_pdf(filename):
    return send_file(os.path.join(pdf_directory, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


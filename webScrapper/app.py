from flask import Flask, render_template, request, send_file
from scraper import *
import csv
import io
app = Flask(__name__)
results = {}
query = ''
@app.route("/")
def show_page():
    return render_template('home.html')

@app.route("/show_data", methods=['POST'])
def show_results():
    global query
    global results
    query = request.form['query']
    results = main(query)
    return render_template('show_data.html', results=results)

@app.route('/download', methods=['POST'])
def download():
    global results
    global query
    fieldnames = ['Sr.no', 'shop_name', 'shop_address', 'shop_phone', 'whatsapp_link']
    csv_filename = query+'.csv'
    
    with open(csv_filename, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for sr_no, shop_data in results.items():
            if shop_data['shop_phone'] is not None:
                whatsapp_link = f"https://wa.me/91{shop_data['shop_phone']}"
                link_formula = f'=HYPERLINK("{whatsapp_link}", "WhatsApp")'
            else :
                whatsapp_link = ""
            row = {'Sr.no': sr_no, 'whatsapp_link': whatsapp_link}
            row.update(shop_data)
            writer.writerow(row)

    return send_file(csv_filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
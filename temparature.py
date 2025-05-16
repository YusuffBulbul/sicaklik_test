from flask import Flask, jsonify
from jtop import jtop
from datetime import datetime

app = Flask(__name__)
log_file = "tum_sicakliklar_kaydi.txt"

def oku_sicaklik():
    veri = {}
    now = datetime.now().strftime("%H:%M:%S")
    veri["Zaman"] = now

    with jtop() as jetson:
        if jetson.ok():
            for key, value in jetson.stats.items():
                if "Temp" in key:
                    veri[key] = f"{value} °C"

    # Dosyaya yaz
    log_line = " | ".join([f"{k}: {v}" for k, v in veri.items()]) + "\n"
    with open(log_file, "a") as f:
        f.write(log_line)

    return veri

@app.route('/sicaklik', methods=['GET'])
def sicaklik_endpoint():
    veri = oku_sicaklik()
    return jsonify(veri)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
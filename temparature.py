import time
from datetime import datetime
from jtop import jtop

log_file = "tum_sicakliklar_kaydi.txt"

with jtop() as jetson:
    while jetson.ok():
        now = datetime.now().strftime("%H:%M:%S")
        log_lines = [f"Zaman: {now}"]

        for key, value in jetson.stats.items():
            if "Temp" in key:
                log_lines.append(f"{key}: {value} °C")

        log_entry = " | ".join(log_lines) + "\n"

        # Dosyaya yaz
        with open(log_file, "a") as f:
            f.write(log_entry)

        print(log_entry.strip())
        time.sleep(5)
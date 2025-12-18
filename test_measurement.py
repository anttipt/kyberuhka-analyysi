import requests
import time

# InfluxDB asetukset
INFLUX_URL = "http://localhost:8086/api/v2/write"
ORG = "myorg"
BUCKET = "mybucket"
TOKEN = "mytoken123"

headers = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "text/plain"
}

params = {
    "org": ORG,
    "bucket": BUCKET,
    "precision": "s"
}

# Luodaan muutama datapiste line protocol -muodossa
# Mittaus: test_measurement, tag: host, kenttä: value
points = []
for i in range(5):
    line = f"test_measurement,host=server01 value={i} {int(time.time())}"
    points.append(line)
    time.sleep(1)  # pieni viive, jotta aikaleimat eroavat

data = "\n".join(points)

# Lähetetään datapisteet InfluxDB:hen
resp = requests.post(INFLUX_URL, params=params, headers=headers, data=data)
print("Status:", resp.status_code)
print("Response:", resp.text)
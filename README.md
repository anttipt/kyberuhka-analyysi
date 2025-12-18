## Kyberuhka-analyysi Stack (InfluxDB + Grafana + Docker)

Tämä projekti demonstroi, miten InfluxDB ja Grafana voidaan käynnistää Dockerin avulla, verkottaa yhteen ja visualisoida dataa. 
Projekti sisältää myös testiskriptin, jolla voidaan puskea datapisteitä InfluxDB:hen

## 📦 Projektin sisältö

- docker-compose.yml
Käynnistää InfluxDB:n ja Grafanan samassa verkossa.

- test_measurement.py
Pieni Python-skripti, joka puskee testidataa InfluxDB:hen.

- README.md
Dokumentaatio projektin käytöstä.

## 🚀 Käynnistys

- Asenna Docker Desktop
Lataa ja asenna Docker Desktop.

- Käynnistä palvelut
Siirry projektikansioon ja aja:
```docker-compose up -d```

- Tarkista kontit

```docker ps```

- Näet influxdb ja grafana kontit käynnissä.


JATKOA TULOSSA









Skripti, joka kerää ja analysoi uhkatietoa eri lähteistä (esim. VirusTotal, Shodan) ja visualisoi uhkatiedot **Grafana**-dashboardilla. 
Vie hiiri kuvan päälle saadaksesi lisätietoja.

Grafana-dashboard on näkymä, jossa eri datalähteistä haettu tieto esitetään visuaalisesti paneeleina, kuten kaavioina, taulukoina ja mittareina. 
Se on ikään kuin ohjauspaneeli, josta näet järjestelmän tilan yhdellä silmäyksellä.

<img src="kuvat/grafana.png" alt="Grafana käyttöliittymä" title="Grafana käyttöliittymä"> 

<img src="kuvat/grafana_influxdb_yhteys.png" alt="Datasource-yhteys testattu: Grafana saa dataa InfluxDB:stä." title="Datasource-yhteys testattu: Grafana saa dataa InfluxDB:stä.">

<img src="kuvat/kontit.png" alt="Docker desktop ja kontit" title="Docker desktop ja kontit">

<img src="kuvat/kontti.png" alt="kontti influxdb tehty" title="kontti influxdb tehty">

<img src="kuvat/konttienkaynnistyskomento.png" alt="Konttien käynnistyskomento tehty" title="konttien käynnistyskomento">






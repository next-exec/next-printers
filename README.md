# next-printers
> A script to monitor the status of the Next House wing printers.

next-printers is a simple Python script that pings a series of printers at
Next House periodically in order to report on their ink levels. It will also
warn you if any printers it attempts to contact are offline so that they can
be addressed.

## Usage
This script must be run on MIT's network and have access to MIT's DNS servers
in order to properly resolve the Next House printers.

All that needs to be done is to run the script through either Docker or with
just `python3`:
```bash
# Python method:
sudo python3 printer.py
# Docker method:
docker run -it --restart=unless-stopped -p 8000:8000 --name next-printers \ 
next-printers
```
This script will attempt to contact the Next House printers once a minute and
report on their status in the standard output. This also serves the data at
port 8000, which can be scraped by a Prometheus and Grafana installation in
order to store and display the metrics.

## Installation
There are two ways to set up this script: manually or with Docker.

## Manual Method
Simply clone this repository to your system and install the needed 
dependencies:
```bash
git clone git@github.com:next-exec/next-printers
cd next-printers
pip3 install --requirement requirements.txt
```
Once this is done, see [Usage](#usage) for how to run this application.

## Docker Method
The Docker method is useful if you have a working Docker installation and just
want to run this script as a high-availability application. First, build the
container:
```bash
docker build -t=next-printers .
```
Once this is done, see [Usage](#usage) for how to run this application.
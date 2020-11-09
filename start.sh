#!/bin/bash

echo "[start] Starting crawler setup..."

# remove existent settings.py
echo "[start] Removing previous scrapy settings file."
mv ./generic_crawler/settings.py ./generic_crawler/backup-settings.py

# make initial setup: template settings base on env vars
echo "[start] Running script to create new settings file."
python3 -B setup.py

# run scrapy process
echo "[start] Running spider."
python3 -B go_spider.py

echo "[start] Finished."
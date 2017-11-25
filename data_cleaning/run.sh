#/bin/bash

remote_path="~/stock-AI/data_cleaning/"
scp -r *.py gpu.l:$remote_path
echo ======== copy done ==========

ssh gpu.l "cd $remote_path && python pickup_ticker.py /mnt/data/stock"

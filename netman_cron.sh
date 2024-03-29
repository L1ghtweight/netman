#!/bin/bash

# Define the project location
# example: /home/user/folder/netman/
PROJECT_LOCATION="path/to/folder/"

# Function to run the job and log timestamp
run_job() {
    # Your actual commands for the job go here
    # For example:
    python netman.py
    date +"[+] %Y-%m-%d %H:%M:%S - successful" >> run.log
    date +"[+] %Y-%m-%d %H:%M:%S - successful" >> cron.log
}

# Check if the last line of run.log is today's timestamp
check_last_run() {
    if [ -f "run.log" ]; then
        last_run=$(tail -n 1 run.log | cut -d' ' -f2)
        today=$(date +"%Y-%m-%d")
        if [ "$last_run" == "$today" ]; then
            date +"[+] %Y-%m-%d %H:%M:%S - skipped" >> cron.log
            exit 0
        fi
    fi
}

# Main script starts here
cd "$PROJECT_LOCATION" || exit 1

check_last_run
run_job


#!/bin/bash

# Initialize variables
start=$1
stop=$2

# Infinite loop to keep the script running
while true; do
    # Execute the Python script with the initialized variables as arguments
    ./rc_num_db.py "$start" "$stop"

    # Capture the exit code of the Python script
    status=$?

    # Check if the Python script executed successfully
    if [ $status -eq 0 ]; then
        echo "Python script executed successfully with start=$start and stop=$stop. Preparing to update variables..."
        #Send out an email
        ./send_email.py "$start" "$stop"
        # Update start and stop variables
        start=$stop
        stop=$((stop + 10))  # Increment stop by 10; adjust this value as needed

        # Wait for a brief moment before restarting (optional, can adjust sleep duration)
        sleep 2
    else
        # If the Python script failed, print an error message and repeat the last execution
        echo "Execution failed with start=$start and stop=$stop, retrying..."
        # Optionally, you can add a brief pause here as well to prevent immediate retry in case of repetitive failures
        sleep 2
    fi
done

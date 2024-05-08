# Temperature Logger using Sense HAT

This Python script logs the current temperature using the Raspberry Pi's Sense HAT to a text file. The script records the temperature along with the current time and appends this data to a file named based on the current date.

## Requirements

- Raspberry Pi with Sense HAT
- Python 3.x
- `sense_hat` library (install using `pip install sense-hat`)

## Usage

1. Connect the Sense HAT to your Raspberry Pi.
2. Ensure Python 3 is installed on your Raspberry Pi.
3. Install the `sense_hat` library if not already installed (`pip install sense-hat`).
4. Download or clone the repository containing the script.

### Running the Script

1. Navigate to the directory containing the script.
2. Make the script executable:

   ```console
   chmod +x temperature_logger.py
   ```
3. Run the script manually using Python:

    ```console
    python3 SenseHat-Temp.py
    ```

### Continuous Execution with Crontab

1. To run the temperature logging script continuously in the background, you can use crontab to schedule it to run at specific intervals.

    Open the crontab editor:

    ```console
    crontab -e
    ```

2. Add the following line to the crontab file to run the script every hour (adjust the interval as needed):

    ```console
    0 * * * * /path/to/SenseHat-Temp.py
    ```
    
    - 0 * * * *: This specifies that the script will run at the start of every hour (i.e., 0 minutes past the hour).
        
3. Save and close the crontab editor (Ctrl + X, then Y, then Enter).

Now, the temperature logging script will be executed automatically by cron every hour. Make sure the script and log file paths are correctly specified in the crontab entry.

## File Structure

    temperature_logger.py: Python script that reads temperature from Sense HAT and logs it to a file.
    README.md: This file providing information about the script and its usage.

## Notes

    - Ensure that the script has write permissions to the directory where the log file is located.
    - Customize the crontab schedule (0 * * * *) according to your desired execution interval (e.g., every 30 minutes: */30 * * * *).
    - Adjust file paths or permissions as needed based on your setup.   

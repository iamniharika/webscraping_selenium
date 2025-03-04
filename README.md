# Google Form Automation using Selenium

This repository demonstrates how to use Selenium in Python to automate the process of filling out a Google Form.

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver
- Selenium library

## Setup

1. **Install Python dependencies**:

    ```bash
    pip install selenium
    ```

2. **Install ChromeDriver**:

    Download the appropriate version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your system's PATH.

3. **Clone the repository** (if applicable) or create a Python script file.

## Configuration

1. **Update form details**:

    Replace the placeholders in the script (`URL_OF_THE_FORM_PAGE`, `XPATH_OF_NAME_FIELD`, `XPATH_OF_EMAIL_FIELD`, `XPATH_OF_DOB_FIELD`, `XPATH_OF_THE_SUBMIT_BUTTON`) with the actual values corresponding to your Google Form.

2. **Adjust the input data**:

    Modify the `form_data` dictionary to match the fields of your form and the data you wish to submit.

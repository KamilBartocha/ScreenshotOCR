*** Settings ***
Library    ScreenshotOcrLibrary.py

*** Test Cases ***
Capture And Extract Text From Screenshot
    [Documentation]    Captures a screenshot and extracts text from it.
    Capture Screenshot
    ${extracted_text}    Extract Text
    Log    Extracted Text: ${extracted_text}

Load And Extract Text From File
    [Documentation]    Loads a screenshot from a file and extracts text.
    Load Screenshot From File    path/to/your/screenshot.jpg
    ${extracted_text}    Extract Text
    Log    Extracted Text: ${extracted_text}

Extract Text From Region
    [Documentation]    Extracts text from a specific region of the screenshot.
    Load Screenshot From File    path/to/your/screenshot.jpg
    ${extracted_text}    Extract Text From Region    100    100    400    400
    Log    Extracted Text from Region: ${extracted_text}

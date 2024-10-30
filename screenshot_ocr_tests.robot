*** Settings ***
Library    ScreenshotOcrLibrary.py

*** Test Cases ***
Capture And Extract Text From Screenshot
    [Documentation]    This test case captures a screenshot and extracts text from it.
    Capture Screenshot
    ${extracted_text}    Extract Text
    Log    Extracted Text: ${extracted_text}

Load And Extract Text From File
    [Documentation]    This test case loads a screenshot from a file and extracts text.
    Load Screenshot From File    path/to/your/screenshot.jpg
    ${extracted_text}=    Extract Text
    Log    Extracted Text: ${extracted_text}

Extract Text From Region
    [Documentation]    This test case extracts text from a specific region of the screenshot.
    Load Screenshot From File    path/to/your/screenshot.jpg
    ${extracted_text}=    Extract Text From Region    100    100    400    400
    Log    Extracted Text from Region: ${extracted_text}

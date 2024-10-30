from ScreenshotOCR import ScreenshotOCR
ocr_tool = ScreenshotOCR(languages=['en'])

ocr_tool.capture_screenshot()  # or ocr_tool.load_screenshot_from_file("screenshot.jpg")

ocr_tool.preprocess_image(threshold=150)

print("Extracted Text (Plain):", ocr_tool.extract_text())
print("Extracted Text (JSON):", ocr_tool.extract_text(output_format='json'))

region_text = ocr_tool.extract_text_from_region((100, 100, 400, 400))
print("Extracted Text (Region):", region_text)

ocr_tool.set_languages(['en', 'es'])
print("Extracted Text (Multilingual):", ocr_tool.extract_text())

from ScreenshotOCR import ScreenshotOCR
from robot.api.deco import keyword

class ScreenshotOcrLibrary:
    def __init__(self):
        self.ocr_tool = ScreenshotOCR()

    @keyword
    def capture_screenshot(self):
        """Capture a screenshot from the screen."""
        self.ocr_tool.capture_screenshot()

    @keyword
    def load_screenshot_from_file(self, file_path):
        """Load a screenshot from a specified file path."""
        self.ocr_tool.load_screenshot_from_file(file_path)

    @keyword
    def preprocess_image(self, threshold=128):
        """Preprocess the image with a binary threshold."""
        self.ocr_tool.preprocess_image(threshold)

    @keyword
    def extract_text(self, output_format='text'):
        """Extract text from the loaded image in the specified format."""
        return self.ocr_tool.extract_text(output_format)

    @keyword
    def extract_text_from_region(self, x1, y1, x2, y2):
        """Extract text from a specific region of the image."""
        return self.ocr_tool.extract_text_from_region((x1, y1, x2, y2))

    @keyword
    def set_languages(self, languages):
        """Set the languages for OCR."""
        self.ocr_tool.set_languages(languages)

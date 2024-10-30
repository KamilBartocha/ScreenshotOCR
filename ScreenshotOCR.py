from PIL import ImageGrab, Image
import easyocr
import logging

class ScreenshotOCR:
    def __init__(self, languages=['en']):
        self.reader = easyocr.Reader(languages)
        self.screenshot_gray = None
        self.languages = languages
        logging.basicConfig(level=logging.INFO)

    def capture_screenshot(self):
        screenshot = ImageGrab.grab()
        self.screenshot_gray = screenshot.convert("L")
        logging.info("Screenshot captured from screen.")

    def load_screenshot_from_file(self, file_path):
        try:
            screenshot = Image.open(file_path)
            self.screenshot_gray = screenshot.convert("L")
            logging.info(f"Screenshot loaded from file: {file_path}")
        except Exception as e:
            raise ValueError(f"Unable to load image from {file_path}: {e}")

    def set_languages(self, languages):
        self.languages = languages
        self.reader = easyocr.Reader(languages)
        logging.info(f"Languages set to: {languages}")

    def extract_text(self, output_format='text'):
        if self.screenshot_gray is None:
            raise ValueError("Screenshot not available. Call capture_screenshot() or load_screenshot_from_file() first.")

        results = self.reader.readtext(self.screenshot_gray)
        logging.info("OCR extraction complete.")

        if output_format == 'text':
            return " ".join([text for _, text, _ in results])
        elif output_format == 'json':
            return [{"text": text, "bbox": bbox} for bbox, text, _ in results]
        else:
            raise ValueError("Invalid output format. Choose 'text' or 'json'.")

    def extract_text_from_region(self, region):
        if self.screenshot_gray is None:
            raise ValueError("Screenshot not available. Call capture_screenshot() or load_screenshot_from_file() first.")

        region_image = self.screenshot_gray.crop(region)
        results = self.reader.readtext(region_image)
        return " ".join([text for _, text, _ in results])

    def preprocess_image(self, threshold=128):
        if self.screenshot_gray is None:
            raise ValueError("Screenshot not available. Call capture_screenshot() or load_screenshot_from_file() first.")

        self.screenshot_gray = self.screenshot_gray.point(lambda x: 0 if x < threshold else 255)
        logging.info("Image preprocessing applied (binary threshold).")

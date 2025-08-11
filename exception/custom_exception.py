import sys
import traceback
from logger.custom_logger import CustomLogger

logger = CustomLogger().get_logger("exception_experiment")

class DocumentPortalException(Exception):
    def __init__(self, error_message, error_details=None):
        self.error_message = str(error_message)
        self.file_name = None
        self.line_no = None
        self.traceback_str = None

        if error_details is not None:
            try:
                _, _, exc_tb = error_details.exc_info()
                if exc_tb:
                    self.file_name = exc_tb.tb_frame.f_code.co_filename
                    self.line_no = exc_tb.tb_lineno
                    self.traceback_str = "".join(traceback.format_exception(*error_details.exc_info()))
            except Exception as e:
                logger.error(f"Failed to extract traceback info: {e}")

    def __str__(self):
        details = []
        if self.file_name and self.line_no:
            details.append(f"Error in [{self.file_name}] at line [{self.line_no}]")
        details.append(f"Message: {self.error_message}")
        if self.traceback_str:
            details.append(f"Traceback: {self.traceback_str}")
        return "\n".join(details)

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        app_exc = DocumentPortalException(e, sys)
        logger.error(app_exc)
        raise app_exc

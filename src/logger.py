
class Logger:
    @staticmethod
    def log_info(message: str):
        Logger._log(message, "INFO")
    
    @staticmethod
    def log_error(message: str):
        Logger._log(message, "ERROR")

    @staticmethod
    def _log(message: str, log_type: str):
        print(f"[{log_type.ljust(5)}] {message}")
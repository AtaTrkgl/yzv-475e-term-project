class Logger:
    log_level = 0

    @staticmethod
    def set_log_level(level: str) -> None:
        if level == "info":
            Logger.log_level = 0
        elif level == "error":
            Logger.log_level = 1
        else:
            Logger.log_level = 2

    @staticmethod
    def log_info(message: str) -> None:
        Logger._log(message, "INFO", 0)
    
    @staticmethod
    def log_error(message: str) -> None:
        Logger._log(message, "ERROR", 1)

    @staticmethod
    def _log(message: str, log_type: str, level: int) -> None:
        if Logger.log_level > level: return
        print(f"[{log_type.ljust(5)}] {message}")
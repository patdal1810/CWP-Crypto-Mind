class AppException(Exception):
    """Base exception for application-level errors."""


class ExternalProviderException(AppException):
    """Raised when an external provider like Bybit/Binance fails."""


class ConfigurationException(AppException):
    """Raised when application configuration is invalid."""
class SovereignException(Exception):
    pass

class PolicyViolation(SovereignException):
    def __init__(self, message: str, severity="medium"):
        super().__init__(message)
        self.severity = severity

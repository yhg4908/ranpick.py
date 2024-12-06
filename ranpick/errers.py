class RanpickError(Exception):
    """기본 Ranpick 에러 클래스"""
    def __init__(self, message, line_number=None, code_snippet=None):
        super().__init__(self._format_message(message, line_number, code_snippet))

    @staticmethod
    def _format_message(message, line_number, code_snippet):
        base_message = "ranpickError:"
        if line_number is not None and code_snippet is not None:
            return f"{base_message} (Line {line_number}: {code_snippet}) {message}"
        return f"{base_message} {message}"

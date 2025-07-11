class RangeExpander:
    def __init__(self, delimiters=None):
        self.delimiters = delimiters or ['-']

    def _split_range(self, token):
        for delim in self.delimiters:
            if delim in token:
                return token.split(delim)
        return None

    def expand(self, input_str):
        result = []
        tokens = input_str.split(',')
        for token in tokens:
            token = token.strip()
            if not token:
                continue
            parts = self._split_range(token)
            if parts:
                start, end = parts
                start = int(start.strip())
                end = int(end.strip())
                result.extend(range(start, end + 1))
            else:
                result.append(int(token.strip()))
        return result

class RangeExpander:
    def __init__(self, delimiters=None, step_delimiter=':'):
        self.delimiters = delimiters or ['-']
        self.step_delimiter = step_delimiter

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
                step = 1
                if self.step_delimiter in parts[-1]:
                    range_part, step_str = parts[-1].split(self.step_delimiter)
                    parts[-1] = range_part
                    step = int(step_str.strip())

                if len(parts) != 2:
                    raise ValueError(f"Invalid range: {token}")

                start, end = parts
                start = start.strip()
                end = end.strip()

                if not start.isdigit() or not end.isdigit():
                    raise ValueError(f"Invalid range: {token}")

                start = int(start)
                end = int(end)

                if step == 0:
                    raise ValueError(f"Step cannot be zero: {token}")

                direction = 1 if start <= end else -1
                if (direction == 1 and step < 0) or (direction == -1 and step > 0):
                    step = abs(step) * direction

                result.extend(range(start, end + direction, step))

            else:

                if not token.isdigit():
                    raise ValueError(f"Invalid number: {token}")
                result.append(int(token))

        return result

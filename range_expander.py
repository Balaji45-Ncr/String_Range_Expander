class RangeExpander:
    def expand(self, input_str):
        result = []
        tokens = input_str.split(',')
        for token in tokens:
            token=token.strip()
            if not token:
                continue
            if '-' in token:
                start, end = token.split('-')
                start = int(start)
                end = int(end)
                result.extend(range(start, end + 1))
            else:
                result.append(int(token))
        return result

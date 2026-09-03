def detect_collocations(
    tokens: list[tuple[str, bool]],
    whitelist: frozenset[tuple[str, str]],
) -> list[tuple[str, bool]]:
    """Detect multi-word expressions that
    should be treated as a single tag using a
    sliding window with whitelist lookup."""

    result = []

    i = 0

    while i < len(tokens):
        if i + 1 < len(tokens):
            w1, p1 = tokens[i]
            w2, p2 = tokens[i + 1]

            if (w1, w2) in whitelist:
                result.append((f"{w1}-{w2}", p1 or p2))
                i += 2
                continue

        result.append(tokens[i])
        i += 1

    return result

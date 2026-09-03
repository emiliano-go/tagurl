import re


def tokenize(query: str) -> list[str]:
    query = query.lower()
    query = re.sub(r"(?<!\w)-|-(?!\w)", "", query)
    query = re.sub(r"[^\w\s-]", "", query)
    return [t for t in query.split() if t]


def filter_stopwords(
    tokens: list[str], hard: frozenset[str], soft: frozenset[str]
) -> list[tuple[str, bool]]:

    result = []

    for tok in tokens:
        if tok in hard:
            continue
        result.append((tok, tok in soft))

    return result

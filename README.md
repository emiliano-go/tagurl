# tagurl

> WIP Library

`tagurl` is a Python library that accepts a natural language query and returns a structured JSON payload containing ranked semantic tags and a generated SEO-friendly URL path.

It is designed to be consumed by external applications (CMSs, data pipelines, API gateways, analytics tools) either via an optional FastAPI wrapper or directly as an importable Python package.

`tagurl` is intentionally scoped to one responsibility: turning a query string into a ranked tag list and a URL path. It does not normalize URLs, enforce HTTPS, strip tracking params, or generate Open Graph metadata. Those concerns belong to `seoslug`, which is [already feature complete](https://github.com/emiliano-go/seoslug/).

def prepare_anthropic_headers(url: str, key: str, headers: dict[str, str]) -> dict[str, str]:
    """Use Anthropic-native authentication for direct Anthropic API requests."""
    if 'api.anthropic.com' not in url:
        return headers

    prepared_headers = {name: value for name, value in headers.items() if name.lower() != 'authorization'}
    if key:
        prepared_headers['x-api-key'] = key
    prepared_headers.setdefault('anthropic-version', '2023-06-01')
    return prepared_headers

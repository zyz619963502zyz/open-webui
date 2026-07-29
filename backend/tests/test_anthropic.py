from open_webui.utils.anthropic import prepare_anthropic_headers


def test_prepare_anthropic_headers_uses_native_authentication() -> None:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer configured-key',
        'X-Custom-Header': 'custom-value',
    }

    result = prepare_anthropic_headers('https://api.anthropic.com/v1', 'configured-key', headers)

    assert result == {
        'Content-Type': 'application/json',
        'X-Custom-Header': 'custom-value',
        'x-api-key': 'configured-key',
        'anthropic-version': '2023-06-01',
    }
    assert headers['Authorization'] == 'Bearer configured-key'


def test_prepare_anthropic_headers_removes_case_insensitive_authorization() -> None:
    result = prepare_anthropic_headers(
        'https://api.anthropic.com/v1',
        'configured-key',
        {'authorization': 'Bearer wrong-key'},
    )

    assert all(name.lower() != 'authorization' for name in result)


def test_prepare_anthropic_headers_preserves_non_anthropic_provider_headers() -> None:
    headers = {'Authorization': 'Bearer configured-key'}

    result = prepare_anthropic_headers('https://litellm.example.com/v1', 'configured-key', headers)

    assert result is headers
    assert result == {'Authorization': 'Bearer configured-key'}

from injection.providers import ResourceProvider, SingletonProvider


def _some_func() -> int:
    """Dummy function that always returns 42."""
    return 42


def _some_other_func() -> int:
    """Dummy function that always returns 43."""
    return 43


def test_resource_provider_resolve() -> None:
    provider = ResourceProvider[int](_some_func)

    assert provider.resolve() == 42


def test_resource_provider_override() -> None:
    provider = ResourceProvider[int](_some_func)

    with provider.override(_some_other_func):
        assert provider.resolve() == 43

    assert provider.resolve() == 42


def test_singleton_provider() -> None:
    """Test the singleton provider resolution and override functionality."""

    class _Stub(object):
        """Dummy class with a counter to track the number of initializations."""

        init_count = 0

        def __init__(self):
            _Stub.init_count += 1

    class _OverrideStub(object):
        """Dummy class with a counter to track the number of initializations."""

        init_count = 0

        def __init__(self):
            _OverrideStub.init_count += 1

    def _stub_func() -> _Stub:
        return _Stub()

    def _override_stub_func() -> _OverrideStub:
        return _OverrideStub()

    provider = SingletonProvider[_Stub](_stub_func)

    assert provider.resolve().init_count == 1, "Singleton provider should return resolved instance."
    assert provider.resolve().init_count == 1, "Singleton provider should return the same instance."

    with provider.override(_override_stub_func):
        assert provider.resolve().init_count == 1, "Singleton provider should return the new instance."
        assert provider.resolve().init_count == 1, "Singleton provider should return the same new instance."

    assert provider.resolve().init_count == 1, "Singleton provider should return the original instance after override."

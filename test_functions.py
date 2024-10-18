import pytest
from unittest.mock import patch


from main import with_tracable_decorator, no_tracable_decorator

@pytest.mark.anyio
class TestWithDecorator:
    @patch("main.some_async_function", return_value="not done")
    async def test_decorator(self, patched_some_async_function):
        
        result = await with_tracable_decorator()
        assert result == "not done"
        assert patched_some_async_function.called


@pytest.mark.anyio
class TestWithoutDecorator:
    @patch("main.some_async_function", return_value="not done")
    async def test_no_decorator(self, patched_some_async_function):
        
        result = await no_tracable_decorator()
        assert result == "not done"
        assert patched_some_async_function.called
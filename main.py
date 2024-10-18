from langsmith import traceable

from helper import some_async_function


@traceable(
    run_type="llm",
    project_name="Tracable Decorator Example",
)
async def with_tracable_decorator():
    return await some_async_function()


async def no_tracable_decorator():
    return await some_async_function()
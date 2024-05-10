from behave import given, when, then
from algorithms.strings import strong_password


@given('a password of length "{length:d}" and content "{password}"')
def step_impl(context, length, password):
    context.length = length
    context.password = password

@when('I check if the password is strong')
def step_impl(context):
    context.result = strong_password(context.length, context.password)

@then('I should be told to add "{needed_chars:d}" more characters to make it strong')
def step_impl(context, needed_chars):
    assert context.result == needed_chars, f"Expected {needed_chars}, got {context.result}"

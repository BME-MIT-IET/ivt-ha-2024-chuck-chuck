from behave import *
import os
from algorithms.compression.huffman_coding import HuffmanCoding


@given('I have a text file "{file_name}" with content "{content}"')
def step_impl(context, file_name, content):
    with open(file_name, "w") as file:
        file.write(content)


@given('I have a text file with content "{content}"')
def step_impl(context, content):
    context.filename = 'test.txt'
    with open(context.filename, 'w') as file:
        file.write(content)


@when('I encode the file using Huffman Coding')
def step_impl(context):
    HuffmanCoding.encode_file(context.filename, 'encoded.bin')


@when('I decode the file back')
def step_impl(context):
    HuffmanCoding.decode_file('encoded.bin', 'decoded.txt')


@then('the decoded content should match the original content')
def step_impl(context):
    with open('decoded.txt', 'r') as file:
        decoded_content = file.read()
    with open(context.filename, 'r') as file:
        original_content = file.read()
    assert decoded_content == original_content
    # Clean up files
    os.remove(context.filename)
    os.remove('encoded.bin')
    os.remove('decoded.txt')

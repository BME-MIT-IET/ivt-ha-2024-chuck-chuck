from behave import *
import os
from algorithms.compression.huffman_coding import HuffmanCoding


@given('a text file with content "{text}"')
def step_impl(context, text):
    context.input_file_name = "test_input.txt"
    with open(context.input_file_name, "w") as file:
        file.write(text)
    context.output_file_name = "test_output.huff"  # Predefine this early for safety

@when('the file is encoded using Huffman coding')
def step_impl(context):
    if not hasattr(context, 'input_file_name'):
        raise AssertionError("Input file is not set.")
    HuffmanCoding.encode_file(context.input_file_name, context.output_file_name)

@then('the encoded file should be smaller than the original file')
def step_impl(context):
    if not hasattr(context, 'output_file_name'):
        raise AssertionError("Output file is not set.")
    original_size = os.path.getsize(context.input_file_name)
    encoded_size = os.path.getsize(context.output_file_name)
    assert encoded_size < original_size, f"Encoded file size {encoded_size} is not smaller than original size {original_size}"

@given('an encoded file using Huffman coding')
def step_impl(context):
    if not hasattr(context, 'output_file_name'):
        raise AssertionError("Encoded file is not available for decoding.")
    context.encoded_file_name = context.output_file_name

@when('the file is decoded using Huffman coding')
def step_impl(context):
    if not hasattr(context, 'encoded_file_name'):
        raise AssertionError("Encoded file is not set.")
    context.decoded_file_name = "test_decoded.txt"
    HuffmanCoding.decode_file(context.encoded_file_name, context.decoded_file_name)

@then('the decoded file should match the original content "{text}"')
def step_impl(context, text):
    if not hasattr(context, 'decoded_file_name'):
        raise AssertionError("Decoded file is not available for verification.")
    with open(context.decoded_file_name, "r") as file:
        content = file.read()
    assert content == text, f"Decoded content does not match the original. Got '{content}'"

Feature: Huffman Encoding and Decoding
  Scenario: Encoding a file using Huffman coding
    Given a text file with content "example text to encode"
    When the file is encoded using Huffman coding
    Then the encoded file should be smaller than the original file

  Scenario: Decoding a file using Huffman coding
    Given an encoded file using Huffman coding
    When the file is decoded using Huffman coding
    Then the decoded file should match the original content "example text to encode"

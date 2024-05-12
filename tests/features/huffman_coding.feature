Feature: Huffman Coding Compression and Decompression
  In order to save storage space
  As a user
  I want to encode files using Huffman coding and decode them back to the original

Scenario: Encode and decode a simple text file
    Given I have a text file with content "example content"
    When I encode the file using Huffman Coding
    And I decode the file back
    Then the decoded content should match the original content

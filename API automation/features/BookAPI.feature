# Created by siddh at 24-08-2024
Feature: Verify if Books are added and deleted in Using library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to library
    When we execute the Addbook API test
    Then book is successfully added



  Scenario Outline:
    Examples:
      |  |
Feature: Google Search Test

Scenario: Test Google Search
    Given navigate to google website
    When i type in text to search
    And i hit Search button
    Then i should be the search result page
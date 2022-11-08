Feature: Place x or o in a empty field

  Scenario: Place x in a empty field
     Given player x turn
      When the chosen field for player x is empty
      Then the player places x in the chosen field

  Scenario: Place o in a empty field
     Given player o turn
      When the chosen field for player o is empty
      Then the player places o in the chosen field   
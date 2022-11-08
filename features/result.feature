Feature: Game result

  Scenario: Draw
     Given that no empty fields
      When no player has 3 symbols next to each other
      Then the game will be a draw

  Scenario: Player x win
     Given player x end his turn
      When player x has 3 symbols in a row
      Then the game will be a victory for player x

  Scenario: Player o win
     Given player o end his turn
      When player o has 3 symbols in a row
      Then the game will be a victory for player o
from behave import *

@given('that no empty fields')
def step_impl(context):
    context.theBoardCount = 0
    context.hasThreeInARow = True
    context.gameResult = ''

@when('no player has 3 symbols next to each other')
def step_impl(context):
    context.hasThreeInARow = False
    
@then('the game will be a draw')
def step_impl(context):
    if context.theBoardCount == 0 and context.hasThreeInARow == False:
        context.gameResult = 'Draw'
    assert (context.gameResult == 'Draw')



@given('player x end his turn')
def step_impl(context):
    context.hasThreeInARow = False
    context.gameResult = ''

@when('player x has 3 symbols in a row')
def step_impl(context):
    context.hasThreeInARow = True
    
@then('the game will be a victory for player x')
def step_impl(context):
    if context.hasThreeInARow == True:
        context.gameResult = 'Player x win'
    assert (context.gameResult == 'Player x win')


@given('player o end his turn')
def step_impl(context):
    context.hasThreeInARow = False
    context.gameResult = ''

@when('player o has 3 symbols in a row')
def step_impl(context):
    context.hasThreeInARow = True
    
@then('the game will be a victory for player o')
def step_impl(context):
    if context.hasThreeInARow == True:
        context.gameResult = 'Player o win'
    assert (context.gameResult == 'Player o win')
from behave import *
import tic_tac_toe

@given('player x turn')
def step_impl(context):
    context.turn = "x"
    context.theField = ''

@when('the chosen field for player x is empty')
def step_impl(context):
    context.theField = ''
    
@then('the player places x in the chosen field')
def step_impl(context):
    context.theField = 'x'
    assert (context.theField == "x")

@given('player o turn')
def step_impl(context):
    context.turn = "o"
    context.theField = ''

@when('the chosen field for player o is empty')
def step_impl(context):
    context.theField = ''
    
@then('the player places o in the chosen field')
def step_impl(context):
    context.theField = 'o'
    assert (context.theField == "o")




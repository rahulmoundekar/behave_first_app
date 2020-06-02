from behave import *



@given("navigate to google website")
def step_impl(context):
    print("navigate to google website")


@when("i type in text to search")
def step_impl(context):
    print("i type in text to search")


@step("i hit Search button")
def step_impl(context):
    print("i hit Search button")


@then("i should be the search result page")
def step_impl(context):
    print("i should be the search result page")

from behave import given, when, then
from menus.models import Menu, MenuItem


@given('the standard menu exists and is active')
def step_create_standard_menu(context):
    context.standard_menu, created = Menu.objects.get_or_create(
        name="Menu",
        defaults={'is_active': True, 'is_seasonal': False}
    )
    if not created:
        context.standard_menu.is_active = True
        context.standard_menu.is_seasonal = False
        context.standard_menu.save()


@given('a seasonal menu "{menu_name}" exists and is {status}')
def step_create_seasonal_menu(context, menu_name, status):
    is_active = True if status == "active" else False
    context.seasonal_menu, created = Menu.objects.get_or_create(
        name=menu_name,
        defaults={'is_active': is_active, 'is_seasonal': True}
    )
    if not created:
        context.seasonal_menu.is_active = is_active
        context.seasonal_menu.is_seasonal = True
        context.seasonal_menu.save()


@given(
        'the standard menu has a menu item "{item_name}" with ingredients '
        '"{ingredients}"'
        )
def step_create_standard_menu_item(context, item_name, ingredients):
    menu = Menu.objects.get(name="Menu")
    MenuItem.objects.get_or_create(
        menu=menu,
        name=item_name,
        defaults={'ingredients': ingredients}
    )


@given(
        'the menu "{menu_name}" has a menu item "{item_name}" with '
        'ingredients "{ingredients}"'
       )
def step_create_seasonal_menu_item(
    _context,
    menu_name,
    item_name,
    ingredients
):
    menu = Menu.objects.get(name=menu_name)
    MenuItem.objects.get_or_create(
        menu=menu,
        name=item_name,
        defaults={'ingredients': ingredients}
    )


@when('the customer visits the menu page')
def step_customer_visits_menu_page(context):
    url = context.get_url("/menus/")
    context.browser.get(url)


@then('they should see "{menu_name}"')
def step_should_see_menu_name(context, menu_name):
    assert menu_name in context.browser.page_source


@then(
        '"{menu_name}" should include "{item_name}" with ingredients '
        '"{ingredients}"'
        )
def step_menu_should_include_item(context, menu_name, item_name, ingredients):
    menu_section = context.browser.find_element_by_xpath(
        f"//section[contains(., '{menu_name}')]"
        )
    assert item_name in menu_section.text
    assert ingredients in menu_section.text


@then('they should not see "{menu_name}"')
def step_should_not_see_menu_name(context, menu_name):
    assert menu_name not in context.browser.page_source

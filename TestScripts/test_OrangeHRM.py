"""
test_OrangeHRM.py contains the test cases.

Test Scripts File
"""

from PageObject.OrangeHRM import OrangeHRMAutomation

# test case for starting automation
def test_start():
    assert OrangeHRMAutomation().start() == True
    print("Success: Automatin started!")

# test case for Login orangeHRM webpage
def test_login():
    assert OrangeHRMAutomation().login() == True
    print("Success: Logged In!")

# test case to click on PIM button
def test_click_pim():
    assert OrangeHRMAutomation().click_pim() == None
    print("SUCCESS: Clicked on PIM button!")

# test case to click on add button
def test_click_add():
    assert OrangeHRMAutomation().click_add() == None
    print("SUCCESS: Clicked on add!")
    
# test case to add employee 
def test_add_employee():
    assert OrangeHRMAutomation().add_employee() == True
    print("SUCCESS: New employee added!")    

# test case for shutdown the browser
def test_shutdown():
    assert OrangeHRMAutomation().shutdown() == None
    print("SUCCESS: Automation shutdown!")

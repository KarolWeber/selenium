from datetime import datetime
import os
import allure


@allure.step("Check assertion")
def assertion_teardown(driver, expected_result, current_result):
    test_status = expected_result == current_result
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    if not test_status:
        driver.save_screenshot(f'../screenshots/{test_name}_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.png')
    driver.quit()
    print(f'\n{40 * "+"}\nExpected: {expected_result}\nCurrent : {current_result}\n{40 * "+"}\n')
    assert test_status

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ProductTest(LiveServerTestCase):
    fixtures = [ 'admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_project_via_admin_site(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/admin/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # user types in username and passwords add hits return
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)

        # username and pass are accepted
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site admin', body.text)

        # TODO: Gertrude uses the admin site to create a new Poll
        self.fail('todo: finish tests')

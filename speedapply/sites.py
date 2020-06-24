from itertools import product
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC


class JobSiteBase:
    url = None

    def __init__(self, auth, settings):
        self.auth = auth
        self.settings = settings
        if self.settings.DRIVER == 'chrome':
            options = ChromeOptions()
            for setting in self.settings.DRIVER_OPTIONS:
                options.add_argument(setting)
            self.driver = webdriver.Chrome(options=options)
        elif self.settings.DRIVER == 'firefox':
            options = FirefoxOptions()
            for setting in self.settings.DRIVER_OPTIONS:
                options.add_argument(setting)
            self.driver = webdriver.Firefox()
        else:
            raise ValueError('settings.DRIVER must be one of ("chrome", "firefox")')
        self.driver.implicitly_wait(2)
        if self.url is not None:
            self.driver.get(self.url)


class Monster(JobSiteBase):
    url = 'https://monster.com/jobs/search'
    seen = set()
        
    def _login(self):
        # click sign in
        sign_in = self.driver.find_element_by_xpath('//*[@id="mobile-navbar-search"]/ul/li[1]/a')
        sign_in.click()

        # fill in form
        email_input = self.driver.find_element_by_xpath('//*[@id="EmailAddress"]')
        email_input.send_keys(self.auth[0])
        password_input = self.driver.find_element_by_xpath('//*[@id="Password"]')
        password_input.send_keys(self.auth[1])
        submit_btn = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        submit_btn.click()

    def _search(self, title, loc):
        job_title = self.driver.find_element_by_xpath('//*[@id="keywords2"]')
        job_title.send_keys(title)
        job_location = self.driver.find_element_by_xpath('//*[@id="location"]')
        job_location.send_keys(loc)
        search_btn = self.driver.find_element_by_xpath('//*[@id="doQuickSearch"]')
        search_btn.click()

    def _scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @property
    def _jobs_on_page(self):
        for _ in range(5):  # mess with pagination to get more
            self._scroll_down()
            sleep(5)
        soup = BeautifulSoup(self.driver.page_source, features="html.parser")
        return list(filter(bool, [tag.get('data-jobid') for tag in soup.find_all('section', class_='card-content')]))

    def auto_apply(self):
        print('Starting applications ...')
        applied = 0
        self._login()
        for title, loc in product(self.settings.TITLES, self.settings.LOCATIONS):
            try:
                self._search(title, loc)
                sleep(10)
                for job_id in self._jobs_on_page:
                    if job_id in self.seen:
                        continue
                    else:
                        self.seen.add(job_id)
                    self.driver.get(self.url + f'?jobid={job_id}')
                    try:
                        self._speed_apply()
                    except:
                        continue
                    else:
                        applied += 1
                        print(f'#{applied:5} Applied to job {job_id:40}')
            except:
                continue
        print(f'Applied to {applied:5} jobs.')

    def _speed_apply(self):
        self.driver.find_element_by_id('speedApply').click()


class Indeed(JobSiteBase):
    pass


class LinkedIn(JobSiteBase):
    pass

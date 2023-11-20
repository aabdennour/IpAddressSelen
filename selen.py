 
 import time

 profile = webdriver.FirefoxProfile()
 profile.set_preference('network.proxy_type', 1)
 profile.set_preference('network.proxy.http', "165.227.124.179")
 profile.set_preference('network.proxy.http_port', 3128)
 profile.update_preference()

 driver = webdriver.Firefox(firefox_profile = profile)
 driver.get("http://whatismyipaddress.com/")
 time.sleep(4)
 driver.close

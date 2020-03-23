# apt install crhomedriver
# run with python3

# -*- coding: utf-8 -*-

import time
import json
import collections as cl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# get data from webpage with webdriver and store them in lists
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(chrome_options = opt)
time.sleep(5)

driver.get('URL') # target URL
time.sleep(5)

title_list = []
img_list = []

elems = driver.find_elements_by_xpath("//div[@class='images']") # extract from <div class="images"... block
time.sleep(2)
for elem in elems:
  title_list.append(elem.find_element_by_tag_name("h1").text)
  img_list.append(elem.find_element_by_tag_name("img").get_attribute("src"))
time.sleep(3)


# create dictionary from list data
dct = cl.OrderedDict()
for i in range(len(title_list)):
  data = cl.OrderedDict()
  data["title"] = title_list[i]
  data["img"] = img_list[i]
  dct[i] = data


# write data to JSON file
fw = open('jsonfile','w') # JSON filename
json.dump(dct,fw,indent=4)


# kill webdriver process at last
driver.quit() 


# functions for webdriver
# driver.__class__(
# driver.__delattr__(
# driver.__dict__
# driver.__dir__(
# driver.__doc__
# driver.__enter__(
# driver.__eq__(
# driver.__exit__(
# driver.__format__(
# driver.__ge__(
# driver.__getattribute__(
# driver.__gt__(
# driver.__hash__(
# driver.__init__(
# driver.__le__(
# driver.__lt__(
# driver.__module__
# driver.__ne__(
# driver.__new__(
# driver.__reduce__(
# driver.__reduce_ex__(
# driver.__repr__(
# driver.__setattr__(
# driver.__sizeof__(
# driver.__str__(
# driver.__subclasshook__(
# driver.__weakref__
# driver._file_detector
# driver._is_remote
# driver._mobile
# driver._switch_to
# driver._unwrap_value(
# driver._web_element_cls(
# driver._wrap_value(
# driver.add_cookie(
# driver.application_cache
# driver.back(
# driver.capabilities
# driver.close(
# driver.command_executor
# driver.create_options(
# driver.create_web_element(
# driver.current_url
# driver.current_window_handle
# driver.delete_all_cookies(
# driver.delete_cookie(
# driver.desired_capabilities
# driver.error_handler
# driver.execute(
# driver.execute_async_script(
# driver.execute_cdp_cmd(
# driver.execute_script(
# driver.file_detector
# driver.file_detector_context(
# driver.find_element(
# driver.find_element_by_class_name(
# driver.find_element_by_css_selector(
# driver.find_element_by_id(
# driver.find_element_by_link_text(
# driver.find_element_by_name(
# driver.find_element_by_partial_link_text(
# driver.find_element_by_tag_name(
# driver.find_element_by_xpath(
# driver.find_elements(
# driver.find_elements_by_class_name(
# driver.find_elements_by_css_selector(
# driver.find_elements_by_id(
# driver.find_elements_by_link_text(
# driver.find_elements_by_name(
# driver.find_elements_by_partial_link_text(
# driver.find_elements_by_tag_name(
# driver.find_elements_by_xpath(
# driver.forward(
# driver.fullscreen_window(
# driver.get(
# driver.get_cookie(
# driver.get_cookies(
# driver.get_log(
# driver.get_network_conditions(
# driver.get_screenshot_as_base64(
# driver.get_screenshot_as_file(
# driver.get_screenshot_as_png(
# driver.get_window_position(
# driver.get_window_rect(
# driver.get_window_size(
# driver.implicitly_wait(
# driver.launch_app(
# driver.log_types
# driver.maximize_window(
# driver.minimize_window(
# driver.mobile
# driver.name
# driver.page_source
# driver.quit(
# driver.refresh(
# driver.save_screenshot(
# driver.service
# driver.session_id
# driver.set_network_conditions(
# driver.set_page_load_timeout(
# driver.set_script_timeout(
# driver.set_window_position(
# driver.set_window_rect(
# driver.set_window_size(
# driver.start_client(
# driver.start_session(
# driver.stop_client(
# driver.switch_to
# driver.switch_to_active_element(
# driver.switch_to_alert(
# driver.switch_to_default_content(
# driver.switch_to_frame(
# driver.switch_to_window(
# driver.title
# driver.w3c
# driver.window_handles


# functions for elements list
# .__add__(
# .__class__(
# .__contains__(
# .__delattr__(
# .__delitem__(
# .__dir__(
# .__doc__
# .__eq__(
# .__format__(
# .__ge__(
# .__getattribute__(
# .__getitem__(
# .__gt__(
# .__hash__
# .__iadd__(
# .__imul__(
# .__init__(
# .__iter__(
# .__le__(
# .__len__(
# .__lt__(
# .__mul__(
# .__ne__(
# .__new__(
# .__reduce__(
# .__reduce_ex__(
# .__repr__(
# .__reversed__(
# .__rmul__(
# .__setattr__(
# .__setitem__(
# .__sizeof__(
# .__str__(
# .__subclasshook__(
# .append(
# .clear(
# .copy(
# .count(
# .extend(
# .index(
# .insert(
# .pop(
# .remove(
# .reverse(
# .sort(


# functions for single element
# .__class__(
# .__delattr__(
# .__dict__
# .__dir__(
# .__doc__
# .__eq__(
# .__format__(
# .__ge__(
# .__getattribute__(
# .__gt__(
# .__hash__(
# .__init__(
# .__le__(
# .__lt__(
# .__module__
# .__ne__(
# .__new__(
# .__reduce__(
# .__reduce_ex__(
# .__repr__(
# .__setattr__(
# .__sizeof__(
# .__str__(
# .__subclasshook__(
# .__weakref__
# ._execute(
# ._id
# ._parent
# ._upload(
# ._w3c
# .clear(
# .click(
# .find_element(
# .find_element_by_class_name(
# .find_element_by_css_selector(
# .find_element_by_id(
# .find_element_by_link_text(
# .find_element_by_name(
# .find_element_by_partial_link_text(
# .find_element_by_tag_name(
# .find_element_by_xpath(
# .find_elements(
# .find_elements_by_class_name(
# .find_elements_by_css_selector(
# .find_elements_by_id(
# .find_elements_by_link_text(
# .find_elements_by_name(
# .find_elements_by_partial_link_text(
# .find_elements_by_tag_name(
# .find_elements_by_xpath(
# .get_attribute(
# .get_property(
# .id
# .is_displayed(
# .is_enabled(
# .is_selected(
# .location
# .location_once_scrolled_into_view
# .parent
# .rect
# .screenshot(
# .send_keys(
# .size
# .submit(
# .tag_name
# .text
# .value_of_css_property(

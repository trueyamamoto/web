# apt install crhomedriver
# run with python3

# -*- coding: utf-8 -*-

import time
import json
import collections as cl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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

dct = cl.OrderedDict()
for i in range(len(title_list)):
  data = cl.OrderedDict()
  data["title"] = title_list[i]
  data["img"] = img_list[i]
  dct[i] = data


fw = open('jsonfile','w') # JSON filename
json.dump(dct,fw,indent=4)

driver.quit() # kill webdriver process at last


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
import time
import os
import uiautomator2 as u2


d = u2.connect('AN2FVB1913011348')
d.uiautomator.start()
d.watcher.when("立即抢购").click()
d.watcher.when("提交订单").click()
d.watcher.start(0.01)
while d(text="我的预约").exists:
    d.click(920, 934)
while d(text="填写订单").exists:
    d.click(900, 2244)
while(1):
    time.sleep(5)

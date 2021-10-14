import time
import os
import uiautomator2 as u2


d = u2.connect('AN2FVB1913011348')
d.uiautomator.start()
d.watcher.when("立即抢购").click()
d.watcher.when("提交订单").click()
d.watcher.when("知道了").click()
d.watcher.start(0.01) # 默认监控间隔2.0s
while(1):
    time.sleep(5)

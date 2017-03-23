#coding=utf-8
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

device=MonkeyRunner.waitForConnection()

device.startActivity(component='com.mxtech.videoplayer.ad/com.mxtech.videoplayer.ad.ActivityMediaList')


MonkeyRunner.sleep(5)

result=device.takeSnapshot()
result.writeToFile('/Users/lichailin/PycharmProjects/learning/At/firstSnapshot.png','png')
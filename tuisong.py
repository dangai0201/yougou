#-*-coding:utf-8-*-



#需要先下载demo获取app_key，master_secret的值然后加入下放代码就可以了
import jpush as jpush
import common


app_key="8b2a258462e396d98a402f5d"
master_secret ="ebd3149858cd082e320398e4"


_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")

def all():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="大连必胜！大连一方111")
    push.platform = jpush.all_
    try:
        response=push.send()
    except common.Unauthorized:
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        raise common.APIConnectionException("conn")
    except common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")
# 连续推送4次
for i in range(1,5):
    all()

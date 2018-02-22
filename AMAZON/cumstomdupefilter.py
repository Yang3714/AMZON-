'''
判断需要不要实例化
         @classmethod
            def from_settings(cls, settings):
                return cls()
if hasattr(MydupeFilter,'from_settings'):
    func=getattr(MydupeFilter,'from_settings')
    obj=func()
else:
#就自己用构造方法去实例化
    obj=MyDupeFilter()
'''


class MyDupeFilter(object):
    def __init__(self):
        self.visited = set() #或者放到数据库

    @classmethod
    def from_settings(cls, settings):     #跟配置文件有关，能够从配置文件读取配置项，就没必要自己导入settings配置文件了
        return cls()

    def request_seen(self, request):     #每次请求过来都会自动执行request_seen查看请求的url是否在集合里面，在则不管，不在则添加
        if request.url in self.visited:
            return True
        self.visited.add(request.url)

    def open(self):  # can return deferred
        pass

    def close(self, reason):  # can return a deferred
        pass

    def log(self, request, spider):  # log that a request has been filtered
        pass
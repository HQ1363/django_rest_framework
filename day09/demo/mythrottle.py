# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.throttling import SimpleRateThrottle


class MyThrottle(SimpleRateThrottle):
    scope = 'auth'
    THROTTLE_RATES = {'auth': '2/m'}

    def get_cache_key(self, requestt, view):
        if requestt.user:
            # 获取用户的id
            ident = requestt.user.id
            MyThrottle.THROTTLE_RATES = {'auth': '5/m'}
        else:
            # 没有就获取ip
            ident = self.get_ident(request)
            MyThrottle.THROTTLE_RATES = {'auth': '2/m'}
        return self.cache_format % {'scope': self.scope, 'ident': ident}

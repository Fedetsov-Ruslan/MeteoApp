
from .models import UserQuery


def user_query(ip, city_name):
    if UserQuery.objects.filter(user_ip=ip, city_name=city_name).count() == 0:
        obj = UserQuery(
            user_ip = ip,
            city_name = city_name,
            count = 1
        )
        obj.save()
    else:
        obj = UserQuery.objects.get(user_ip=ip, city_name=city_name)
        obj.count = obj.count + 1
        obj.save()
    print(ip, city_name, obj.count)  
    return obj.count


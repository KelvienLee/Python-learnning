import requests

# 获取用于比对地区是否存在的省市列表数据
province_url = 'https://lab.isaaclin.cn//nCoV/api/provinceName'

# 用户输入想要查询的地区，同时将数据分发给省市比对是否存在函数和疫情数据获取函数
province = input('请输入想要查询的地区：')

# 获取疫情各地区疫情数据
url = f'https://lab.isaaclin.cn//nCoV/api/area?latest=1&province={province}'


# 获取所有的地区名称，用于比对用户输入的地区是否存在
def get_province_name(province_url):
    try:
        response = requests.get(province_url)
        data = response.json()
        return data
    except:
        return None


# 实例化获取地区列表函数，获得数据(字典)
province_data = get_province_name(province_url)

# 将字典数据转换为列表，用于比对用户输入的地名是否存在
province_list = province_data['results']


# 获取疫情详细数据
def get_nCov_details(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except:
        return None


# 将获取疫情数据函数实例化，获得疫情数据（字典）
data = get_nCov_details(url)

# 如果用户输入的地名存在于地区列表中：
if province in province_list:
    # 如果获取到的数据为空：
    if not data['results']:
        print('未获取到数据')
    # 如果获取的数据不为空：
    else:
        provinceName = data['results'][0]['provinceName']
        currentConfirmedCount = data['results'][0]['currentConfirmedCount']
        confirmedCount = data['results'][0]['confirmedCount']
        suspectedCount = data['results'][0]['suspectedCount']
        curedCount = data['results'][0]['curedCount']
        deadCount = data['results'][0]['deadCount']
        print(
            f"总览：\n地区:{provinceName}\n现存确诊人数:{currentConfirmedCount}\n累计确诊人数:{confirmedCount}\n"
            f"疑似感染人数:{suspectedCount}\n治愈人数:{curedCount}\n死亡人数:{deadCount}\n\n")

        # 如果查询地区存在下属地区（如果存在cities数据）
        try:
            # 获取下属地区的数量（通过cities数值来获取）
            province_city_num = len(data['results'][0]['cities'])
            print('下属地区详细信息：\n')
            # 如果存在下属城市：
            if province_city_num > 0:
                # 依次遍历下属城市
                for i in range(province_city_num):
                    cityName = data['results'][0]['cities'][i]['cityName']
                    cityCurrentConfirmedCount = data['results'][0]['cities'][i]['currentConfirmedCount']
                    cityConfirmedCount = data['results'][0]['cities'][i]['confirmedCount']
                    citySuspectedCount = data['results'][0]['cities'][i]['suspectedCount']
                    cityCuredCount = data['results'][0]['cities'][i]['curedCount']
                    cityDeadCount = data['results'][0]['cities'][i]['deadCount']
                    print(f"下属地区:{cityName}\n现存确诊人数:{cityCurrentConfirmedCount}\n累计确诊人数:{cityConfirmedCount}\n"
                          f"疑似感染人数:{citySuspectedCount}\n治愈人数:{cityCuredCount}\n死亡人数:{cityDeadCount}\n")
            # 如果下属城市的cities数据为空：
            else:
                print('该地区下属地区详细信息未纳入统计范围')
        # 如果查询地区没有下属地区（不存在cities数据<null>）
        except:
            print('')
# 如果用户输入的地名不在地区列表中：
else:
    print('地区名不存在或输入不正确/不完整')

import json
# 出现文件读取错误时可以尝试声明读取的编码格式

file = open('top_movies.json', 'r', encoding='utf-8')       # 声明编码格式
result = json.load(file)
print(result['title'])
print(type(result))

for rank, movie in enumerate(result["subjects"]):
    print('——' * 20)
    print(f"第{rank + 1}名： {movie['title']}")
    print(f"评分： {movie['rating']['average']}")
    print(f"上映时间：{movie['year']}")






















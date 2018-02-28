import re
# 将正则表达式编译成 Pattern 对象
pattern=r'<div>.*?</div>'
# 使用 search() 查找匹配的子串，不存在匹配的子串时将返回 None
# 这里使用 match() 无法成功匹配
m = re.search(pattern,'aa<div>test1</div>bb<div>test2</div>cc')
if m:
    # 使用 Match 获得分组信息
    print ('matching string:',m.group())
    # 起始位置和结束位置
    print ('position:',m.span())
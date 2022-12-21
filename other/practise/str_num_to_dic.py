# 字串字數統計
text = 'This is a very big and red apple.'
statistic = {}

for word in text:
    statistic[word] = statistic.get(word,0) + 1

for key in statistic:
    print(key, statistic[key])

print(statistic)

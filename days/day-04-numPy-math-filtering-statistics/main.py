import numpy as np




#first mini task


prices = np.array([100, 250, 400, 150, 500])

print(prices * 1.2)
print(prices - 50)
print(prices/2)

#second mini task

temperatures = np.array([18, 22, 25, 19, 30, 27])

print(temperatures.sum())
print(temperatures.mean())
print(temperatures.min())
print(temperatures.max())



#third mini task

sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400],
    [250, 350, 450]
])

print(sales.mean(axis=0))
print(sales.mean(axis=1))
print(sales.max(axis=0))
print(sales.sum(axis=1))

#minitask

data = np.array([10, 12, 11, 13, 50])

print(data.mean())
print(data.std())
print(data.min())
print(data.max())



#minitask

temperatures = np.array([12, 18, 25, 31, 15, 28, 35, 22, 8])

print(temperatures[(temperatures > 15) & (temperatures < 30)])
print(temperatures[(temperatures < 15) | (temperatures > 30)])


#minitask

scores = np.array([45, 72, 88, 91, 63, 55, 79])

print(np.where(scores >= 60, "Passed", "Failed"))


#minitask

temperatures = np.array([18, 22, 27, 31, 19, 25])

print((temperatures > 30).any())
print((temperatures > 15).all())
print((temperatures < 25).all())


#minitask

prices = np.array([120, 340, 90, 560, 230, 410])

print(prices.max())
print(prices.argmax())
print(prices.min())
print(prices.argmin())


data = np.array([
    [10, 40, 30],
    [50, 20, 60],
    [70, 90, 80]
])

print(data.argmax(axis=0))
print(data.argmax(axis=1))
print(data.argmin(axis=1))



#finaltask

scores = np.array([
    [70, 80, 90],
    [55, 65, 60],
    [88, 92, 85],
    [40, 50, 45],
    [95, 78, 82]
])

mean_score_each_student = scores.mean(axis=1)
print(mean_score_each_student)

print(scores[mean_score_each_student >= 70])

print(np.where(mean_score_each_student >= 70, "Passed", "Failed"))

print((mean_score_each_student > 90).any())
print((mean_score_each_student > 40).all())
print(mean_score_each_student.argmax())

print(scores.argmax(axis=1))

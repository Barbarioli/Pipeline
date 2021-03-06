import matplotlib.pyplot as plt


x = [11.16, 11.44, 11.31,10.81, 10.58 , 9.71, 9.54 , 9.16 , 8.17, 7.71 , 7.59 , 7.19, 6.33, 6.01, 5.50]
y = [88.41, 88.17, 87.84, 87.66, 87.49, 86.24, 85.85, 84.6, 81.31, 79.39, 77.74, 74.27, 59.45, 52.05, 30.71]

x_1 = [11.13,11.47,11.31,10.81, 10.58, 9.71, 9.54, 9.16, 8.17, 7.71, 7.6, 7.2, 6.33, 6.01, 5.5]
y_1 = [87.66, 88.03, 87.66, 87.39, 87.31, 86.53, 86.27,85.5, 83.31, 82.0, 80.56, 77.52, 66.03, 57.64, 34.29]

x_2 = [11.13, 11.47, 11.30, 10.82, 10.59, 9.71, 9.55, 9.17, 8.18, 7.71, 7.60, 7.2,6.34, 6.02, 5.5]
y_2 = [87.78, 87.79, 87.89, 87.76, 87.68,87.31, 87.11, 86.4, 84.54,83.26, 82.07, 79.36, 69.58, 60.58, 37.65]

x_3 = [11.14, 11.47, 11.31, 10.82, 10.59, 9.71, 9.55, 9.17, 8.18, 7.71, 7.6, 7.2, 6.35, 6.03, 5.5]
y_3 = [87.04, 87.11, 87.14, 87.27, 87.28, 87.2, 86.98, 86.7, 85.72,84.96, 84.15, 82.79, 78.25, 73.18,57.83]

plt.xlabel('Inference Time (ms)')
plt.ylabel('Accuracy')
plt.axis([5,12,0,100])
plt.plot(x, y, label = '0%')
plt.plot(x_1,y_1, label = '5%')
plt.plot(x_2, y_2,label = '10%')
plt.plot(x_3, y_3, label = '30%')
plt.legend()
plt.title('Inference Time x Accuracy for ResNet-18 on Cifar-10')
plt.savefig('/Users/brunobarbarioli/Desktop/compression_resnet-18_cifar-10.png')
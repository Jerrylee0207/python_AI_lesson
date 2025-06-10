import matplotlib.pyplot as plt
'''
figure = plt.figure();
axis1 = figure.add_subplot(3, 2, 1);
axis2 = figure.add_subplot(3, 2, 2);
axis3 = figure.add_subplot(3, 2, 3);
axis4 = figure.add_subplot(3, 2, 6);
plt.show();
'''

figure, axis = plt.subplots();
x = [0,1,2,3,4,5,6];
y = [1,1,2,3,5,8,11];
axis.plot(x, y, marker="o", label="line", linestyle="--", markersize=10, linewidth=3, color="#b00b69");
axis.set_title("fibonacci");
axis.set_xticks([0,1,2,3,4,5,6], ["0", "1", "2", "3", "4", "5", "6"]);

axis.legend();
plt.show();


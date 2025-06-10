import matplotlib as mpl
import matplotlib.pyplot as plt

student1 = {"CN":65, "EN":78, "MAT":83, "SC":61, "HIS":94};
student2 = {"CN":50, "EN":99, "MAT":34, "SC":50, "HIS":88};

subject = list(student1.keys());
student1_val = list(student1.values());
student2_val = list(student2.values());

figure = plt.figure(figsize=(8, 5), dpi=150, facecolor="#FFFFFF");
axes = figure.add_subplot(1, 1, 1);
axes.plot(subject, student1_val, marker="o", label="stu01");
axes.plot(subject, student2_val, marker="o", label="stu02", linestyle="-.");
axes.legend();
axes.set_title("students' score");

x_coor = axes.get_xticks();
for i in range(len(x_coor)):
    x = x_coor[i];
    stu1_y = student1_val[i];
    stu2_y = student2_val[i];
    axes.annotate(str(stu1_y), (x-0.05, stu1_y+1));
    axes.annotate(str(stu2_y), (x-0.05, stu2_y+1));

axes.set_xlim(-0.5, 4.5);
axes.set_ylim(20, 105);
axes.grid(axis='y', color="#777777", alpha=0.1);
plt.show();





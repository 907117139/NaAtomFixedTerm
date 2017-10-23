import tkinter as tk
import interpolation
import os
"""
    控件命名规则：xxx_控件类名
        xxx是用来区分的真实名字, 如xxx_button, xxx_label
"""

class generate_ui():
    unkonwn = 'Unknown'
    current_dir = os.getcwd()
    def __init__(self):
        self.top = tk.Tk()
        self.top.title("钠原子光谱波数及固定项计算")
        self.top.columnconfigure(0, weight=1)
        self.top.columnconfigure(1, weight=1)
        self.top.columnconfigure(2, weight=1)
        self.top.columnconfigure(3, weight=1)
        self.top.columnconfigure(4, weight=1)
        self.top.columnconfigure(5, weight=1)

        # 搭配lambda1 和输入
        lambda1_image = tk.PhotoImage(file = self.current_dir + r'\resource\picture\lambda1.png')
        self.lambda1_label = tk.Label(self.top, text="λ 1(nm):", image=lambda1_image)
        self.lambda1_label.image = lambda1_image
        self.lambda1_label.grid(row=0)
        self.lambda1_entry = tk.Entry(self.top)
        self.lambda1_entry.grid(row=0, column=1)

        # 搭配lambda2 和输入
        lambda2_image = tk.PhotoImage(file=self.current_dir + r'\resource\picture\lambda2.png')
        self.lambda2_label = tk.Label(self.top, text="λ 2(nm):", image=lambda2_image)
        self.lambda2_label.image = lambda2_image
        self.lambda2_label.grid(row=1)
        self.lambda2_entry = tk.Entry(self.top)
        self.lambda2_entry.grid(row=1, column=1)

        # 搭配wave number 1和数值标签
        wave_number1_image = tk.PhotoImage(file=self.current_dir + r'\resource\picture\wave_number1.png')
        self.wave_number1_label = tk.Label(self.top, text='wave number 1(1/cm):', image=wave_number1_image )
        self.wave_number1_label.image = wave_number1_image
        self.wave_number1_label.grid(row=0, column=2)
        self.value_of_wave_number1_label = tk.Label(self.top, text=self.unkonwn)
        self.value_of_wave_number1_label.grid(row=0, column=3)

        # 搭配wave number 2和数值标签
        wave_number2_image = tk.PhotoImage(file=self.current_dir + r'\resource\picture\wave_number2.png')
        self.wave_number2_label = tk.Label(self.top, text='wave number 2(1/cm):', image=wave_number2_image)
        self.wave_number2_label.image = wave_number2_image
        self.wave_number2_label.grid(row=1, column=2)
        self.value_of_wave_number2_label = tk.Label(self.top, text=self.unkonwn)
        self.value_of_wave_number2_label.grid(row=1, column=3)

        # 搭配energy leve和数值标签
        self.energy_level1_label = tk.Label(self.top, text='能级 1:')
        self.value_of_energy_level1_label = tk.Label(self.top, text=self.unkonwn)
        self.energy_level1_label.grid(row=0, column=4)
        self.value_of_energy_level1_label.grid(row=0,column=5)

        # 搭配energy leve和数值标签
        self.energy_level2_label = tk.Label(self.top, text='能级 2:')
        self.value_of_energy_level2_label = tk.Label(self.top, text=self.unkonwn)
        self.energy_level2_label.grid(row=1, column=4)
        self.value_of_energy_level2_label.grid(row=1, column=5)

        # 搭配固定项和数值标签
        fixed_term_image = tk.PhotoImage(file = self.current_dir + r'\resource\picture\fixed_term.png')
        self.fixed_term_label = tk.Label(self.top, text="An'l'(1/cm)", image=fixed_term_image)
        self.fixed_term_label.image = fixed_term_image
        self.fixed_term_label.grid(row=2, column=0)
        self.value_of_fixed_term_label = tk.Label(self.top, text=self.unkonwn)
        self.value_of_fixed_term_label.grid(row=2, column=1)

        # 搭配n 和数值标签
        n_image = tk.PhotoImage(file = self.current_dir + r'\resource\picture\n.png')
        self.n_label = tk.Label(self.top, text="n", image=n_image)
        self.n_label.image = n_image
        self.n_label.grid(row=3, column=0)
        self.value_of_n_label = tk.Label(self.top, text=self.unkonwn)
        self.value_of_n_label.grid(row=3, column=1)

        # 搭配delta_l和数值标签
        delta_l_image = tk.PhotoImage(file = self.current_dir + r'\resource\picture\delta_l.png')  # 一定得是把路径赋给file属性
        self.delta_l_label = tk.Label(self.top, image=delta_l_image) # 这个语句与下一条语句必须搭配使用才能显示图片
        self.delta_l_label.image = delta_l_image
        self.delta_l_label.grid(row=4, column=0)
        self.value_of_delta_l_label = tk.Label(self.top, text=self.unkonwn)
        self.value_of_delta_l_label.grid(row=4, column=1)

        # 搭配波数差delta 和数值标签
        delta_v_image = tk.PhotoImage(file = self.current_dir + r'\resource\picture\delta_v.png')
        self.delta_label = tk.Label(self.top, text='delta(1/cm):', image=delta_v_image)
        self.delta_label.image = delta_v_image
        self.delta_label.grid(row=2, column=2)
        self.value_of_delta_label = tk.Label(self.top, text=self.unkonwn)
        self.value_of_delta_label.grid(row=2, column=3)

        # 显示公式
        formula_image = tk.PhotoImage(file=self.current_dir + r'\resource\picture\formula.png')
        self.formula_label = tk.Label(self.top, image=formula_image)
        self.formula_label.image = formula_image
        self.formula_label.grid(row=3, column=2, rowspan=4, columnspan=4)



        # 开始按钮
        self.start_button = tk.Button(self.top, text="start", command=self.press_button1)
        self.start_button.grid(row =5, column=0)


    def press_button1(self):
        """
        在输入了lambda1和lambda2之后开始计算得出结果
        :return:
        """
        lambda1 = float(self.lambda1_entry.get())
        lambda2 = float(self.lambda2_entry.get())
        wave_number1 = interpolation.convert_to_wave_number(lambda1)
        wave_number2 = interpolation.convert_to_wave_number(lambda2)
        energy_level1 = interpolation.find_energy_level(lambda1)
        energy_level2 = interpolation.find_energy_level(lambda2)

        n = interpolation.find_n(lambda1, lambda2)
        delta = round(abs(wave_number1 - wave_number2), 3)
        print('delta',delta)
        col = interpolation.find_which_col(delta)
        print('col',col)
        alpha = interpolation.find_alpha(delta, col)
        m = interpolation.find_m(col)
        delta_l = interpolation.find_delta_l(n,m,alpha)

        lambda_max = max(lambda1, lambda2)
        wave_number = interpolation.convert_to_wave_number(lambda_max)
        R = interpolation.R
        fixed_term = interpolation.find_fixed_term(wave_number, R, n, delta_l)



        #根据获得的结果更新gui
        self.value_of_fixed_term_label['text']=str(fixed_term)
        self.value_of_n_label['text']=str(n)
        self.value_of_wave_number1_label['text']=str(wave_number1)
        self.value_of_wave_number2_label['text']=str(wave_number2)
        self.value_of_delta_l_label['text']=str(delta_l)
        self.value_of_delta_label['text']=str(delta)
        self.value_of_energy_level1_label['text']=energy_level1
        self.value_of_energy_level2_label['text'] = energy_level2


    def run(self):
        """
        运行gui程序
        :return:
        """
        tk.mainloop()

if __name__ == '__main__':
    g = generate_ui()
    g.run()
import tkinter as tk
import interpolation
import os
from PIL import Image,ImageTk





class tk_generate_ui():
    unkonwn = 'Unknown'
    def __init__(self):
        self.top = tk.Tk()
        self.top.columnconfigure(0, weight=1)
        self.top.columnconfigure(1, weight=1)
        self.top.columnconfigure(2, weight=1)

        # 搭配lambda1 和输入
        self.label1 = tk.Label(self.top, text="λ 1(nm):")
        self.label1.grid(row=0)
        self.entry1 = tk.Entry(self.top)
        self.entry1.grid(row=0, column=1)

        # 搭配lambda2 和输入
        self.label2 = tk.Label(self.top, text="λ 2(nm):")
        self.label2.grid(row=1)
        self.entry2 = tk.Entry(self.top)
        self.entry2.grid(row=1, column=1)


        # 搭配固定项和数值标签
        self.label3 = tk.Label(self.top, text="An'l'(1/cm)")
        self.label3.grid(row=2,column=0)
        self.label4 = tk.Label(self.top, text=self.unkonwn)
        self.label4.grid(row=2, column=1)

        # 搭配n 和数值标签
        self.label5 = tk.Label(self.top, text="n")
        self.label5.grid(row=3, column=0)
        self.label6 = tk.Label(self.top, text=self.unkonwn)
        self.label6.grid(row=3, column=1)

        # 搭配wave number 1和数值标签
        self.label7 = tk.Label(self.top, text='wave number 1(1/cm):')
        self.label7.grid(row=0, column=2)
        self.label8 = tk.Label(self.top, text=self.unkonwn)
        self.label8.grid(row=0, column=3)

        # 搭配wave number 2和数值标签
        self.label9 = tk.Label(self.top, text='wave number 2(1/cm):')
        self.label9.grid(row=1, column=2)
        self.label10 = tk.Label(self.top, text=self.unkonwn)
        self.label10.grid(row=1, column=3)

        # 搭配delta_l和数值标签
        current_dir = os.getcwd()
        photo = tk.PhotoImage(file=current_dir + r'\resource\picture\delta_l.png')
        self.label11 = tk.Label(self.top, image=photo)
        self.label11.image = photo
        self.label11.grid(row=4, column=0)
        self.label12 = tk.Label(self.top, text=self.unkonwn)
        self.label12.grid(row=4, column=1)

        # 搭配波数差delta 和数值标签
        self.label13 = tk.Label(self.top, text='delta(1/cm):')
        self.label13.grid(row=2, column=2)
        self.label14 = tk.Label(self.top, text=self.unkonwn)
        self.label14.grid(row=2, column=3)

        # 开始按钮
        self.button1 = tk.Button(self.top, text="start", command=self.press_button1)
        self.button1.grid(row =5, column=0)


    def press_button1(self):
        """
        在输入了lambda1和lambda2之后开始计算得出结果
        :return:
        """
        lambda1 = float(self.entry1.get())
        lambda2 = float(self.entry2.get())
        wave_number1 = interpolation.convert_to_wave_number(lambda1)
        wave_number2 = interpolation.convert_to_wave_number(lambda2)

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
        self.label4['text']=str(fixed_term)
        self.label6['text']=str(n)
        self.label8['text']=str(wave_number1)
        self.label10['text']=str(wave_number2)
        self.label12['text']=str(delta_l)
        self.label14['text']=str(delta)


    def run(self):
        """
        运行gui程序
        :return:
        """
        tk.mainloop()

if __name__ == '__main__':
    g = tk_generate_ui()
    g.run()
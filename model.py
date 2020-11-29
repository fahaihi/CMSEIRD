"""
describe:This is a infect disease package for any users to remodel a disease model, five parts
         are included in this package, such as SIRD......
authors :SunHui XieHaoNan
data    :2020/11/22
email   :adairmillersh@gmail.com
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import os
import sys
from matplotlib import ticker

data = 200
E0 = 650
I0 = 433
R0 = 123
D0 = 17
S0 = 11210000
II0 = 433
a_I = 15
B_I = 0.313
a_E = 20
B_E = 0.313
i_R = 0.9436
i_D = 0.0579
e_I = 1 / 7
e_R = 0.1
n = 2 / 3
n_d = 1
Td = 5
flag = 0
max_time_I = 0
max_number_I = 0
min_time_S = 0
min_number_S = 11210000
equal_time_D = 0
equal_number_D = 0
def help():
    print("This is a help function for CM-SEIRD, befor you prediction please as follow:")
    print("1:Run model.paramenter() change your paramenter")
    print("2:Run model.sesird() begin your prediction")
def paramenter():
    print("This function is change the paramenter set for CM-SEIRD")
    print("Please input parameter as we requirement")
    global data
    data = int(input("Please input parameter date day："))
    global E0
    E0 = int(input("Please input parameter E0："))
    global I0
    I0 = int(input("Please input parameter I0："))
    global R0
    R0 = int(input("Please input parameter R0："))
    global D0
    D0 = int(input("Please input parameter D0："))
    global S0
    S0 = int(input("Please input parameterS0："))
    global II0
    II0 = int(input("Please input parameterII0："))
    global a_I
    a_I = float(input("Please input parameter a_I："))
    global B_I
    B_I = float(input("Please input parameter B_I："))
    global a_E
    a_E = float(input("Please input parameter a_E："))
    global B_E
    B_E = float(input("Please input parameter B_E："))
    global i_R
    i_R = float(input("Please input parameter i_R："))
    global i_D
    i_D = float(input("Please input parameter i_D："))
    global e_I
    e_I = float(input("Please input parameter e_I："))
    global e_R
    e_R = float(input("Please input parameter e_R："))
    global n
    n = float(input("Please input parameter n："))
    global n_d
    n_d = float(input("Please input parameter n_d："))
    global Td
    Td = float(input("Please input parameter Td："))
    print("Now parameter input over, please begin u work!")
n_dddd = n_d
# [data, a_I, B_I, a_E, B_E, i_R, i_D, e_I, e_R, n, n_d, Td]
def cmseird():
    print("Please input work model")
    print("1:Nd_from_0_to_data")
    print("2:Td_from_0_to_data")
    global flag
    flag = input("Please input work model ：")
    if(flag=='1'):
        E = np.zeros(data)
        I = np.zeros(data)
        R = np.zeros(data)
        D = np.zeros(data)
        S = np.zeros(data)
        II = np.zeros(data)
        TimeI = np.zeros(data)
        TimeS = np.zeros(data)
        TimeD = np.zeros(data)
        T = np.arange(data)
        DataD = np.zeros(data)
        DataS = np.zeros(data)
        DataI = np.zeros(data)
        TT = np.zeros(data)
        n_d1 = float(input("Threshold n_d SUCH AS 1:"))
        for i in range(data):
            TT[i] = (i + 1) * (1/data)
        for td_indx in range(data):
            max_time_I = 0
            max_number_I = 0
            min_time_S = 0
            min_number_S = S0
            equal_time_D = 0
            equal_number_D = 0
            # T = np.arange(200)
            E[0] = E0
            I[0] = I0
            R[0] = R0
            D[0] = D0
            S[0] = S0
            II[0] = II0
            for idx in range(data-1):
                if (idx >= Td):
                    n_d1 = (td_indx + 1) * (1/data)

                S[idx + 1] = S[idx] - a_I * B_I * n * n_d1 * I[idx] * S[idx] / (
                            S[idx] + E[idx] + R[idx] + I[idx] * n) - a_E * B_E * n_d1 * I[idx] * S[idx] / (
                                         S[idx] + E[idx] + R[idx] + I[idx] * n) + i_R * I[idx] + e_R * E[idx]
                E[idx + 1] = E[idx] + a_I * B_I * n * n_d1 * I[idx] * S[idx] / (
                            S[idx] + E[idx] + R[idx] + I[idx] * n) + a_E * B_E * n_d1 * I[idx] * S[idx] / (
                                         S[idx] + E[idx] + R[idx] + I[idx] * n) - e_I * E[idx] - e_R * E[idx]
                I[idx + 1] = I[idx] + e_I * E[idx] - i_R * I[idx] - i_D * I[idx]
                R[idx + 1] = R[idx] + i_R * I[idx] + e_R * E[idx]
                D[idx + 1] = D[idx] + i_D * I[idx]
                II[idx + 1] = II[idx] + I[idx + 1]

            for i in range(data):
                if I[i] > max_number_I:
                    max_number_I = I[i]
                    max_time_I = i
                if S[i] < min_number_S:
                    min_number_S = S[i]
                    min_time_S = i
                if math.floor(D[i]) > equal_number_D:
                    equal_number_D = math.floor(D[i])
                    equal_time_D = i
            TimeI[td_indx] = max_time_I
            TimeS[td_indx] = min_time_S
            TimeD[td_indx] = equal_time_D
            DataD[td_indx] = int(equal_number_D)
            DataI[td_indx] = int(max_number_I)
            DataS[td_indx] = int(min_number_S)
        print("Your work '1:Nd_from_0_to_data' process successfully!")
        print("Whether an image needs to be drawn? : ")
        print("YES:1")
        print("NO:2")
        imageflag = input("Please input your choice:")
        while True:
            if(imageflag == '1'):
                fig1 = plt.figure()
                plt.plot(TT, TimeI, 'r', label='Max infected time')
                plt.xlabel("Measure level")
                plt.ylabel('The time to get the maximum value(day)')
                plt.legend(['Max infected time'])
                plt.show()
                fig1.savefig('./Nd_I_MaxInfectedTime.svg', dpi=400, bbox_inches='tight')
                fig2 = plt.figure()
                plt.plot(TT, DataI, 'r', label='Max infected number')
                plt.xlabel("Measure level")
                plt.ylabel('The maximun number of people')
                ax = plt.gca()
                ax.yaxis.get_major_formatter().set_powerlimits((0, 1))  # 将坐标轴的base number设置为一位。
                plt.legend()
                plt.show()
                fig2.savefig('./Nd_I_MaxInfectedNumber.svg', dpi=400, bbox_inches='tight')
                fig3 = plt.figure()
                plt.plot(TT, DataI / S0, 'r', label="Max infected rate")
                #plt.text(0.23, -0.001, '(0.185,0.028%)', )
                def to_percent(temp, position):
                    return '%1.0f' % (100 * temp) + '%'
                plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
                plt.xlabel("Measure level")
                plt.ylabel('Max/Total(people)')
                plt.legend()
                plt.show()
                fig3.savefig('./Nd_I_MaxInfectedRate.svg', dpi=400, bbox_inches='tight')
                fig4 = plt.figure()
                plt.plot(TT, TimeS, 'r', label='Min susceptible time')
                plt.xlabel("Measure level")
                plt.ylabel('The time to get the minimum value(day)')
                plt.legend()
                fig4.savefig('./Nd_S_MinSusceptibleTime.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig5 = plt.figure()
                plt.plot(TT, DataS, 'r', label='Min susceptible number')
                plt.xlabel("Measure level")
                plt.ylabel('The minimun number of people')
                ax = plt.gca()  # 获取当前图像的坐标轴信息
                ax.yaxis.get_major_formatter().set_powerlimits((0, 1))  # 将坐标轴的base number设置为一位。
                plt.legend()
                fig5.savefig('./Nd_S_MinSusceptibleNumber.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig6 = plt.figure()
                plt.plot(TT, DataS / S0, 'r', label="Min susceptible rate")
                def to_percent(temp, position):
                    return '%1.0f' % (100 * temp) + '%'
                plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
                plt.xlabel("Measure level")
                plt.ylabel('Min/Total(people)')
                plt.legend()
                fig6.savefig('./Nd_S_MinSusceptibleRate.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig7 = plt.figure()
                plt.plot(TT, TimeD, 'r', label='Final death time')
                plt.xlabel("Measure level")
                plt.ylabel('The time to get the maximum value(day)')
                plt.legend()
                fig7.savefig('./Nd_D_FinalDeathTime.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig8 = plt.figure()
                plt.plot(TT, DataD, 'r', label="Final death number")
                ax = plt.gca()  # 获取当前图像的坐标轴信息
                ax.yaxis.get_major_formatter().set_powerlimits((0, 1))  # 将坐标轴的base number设置为一位。
                plt.xlabel("Measure level")
                plt.ylabel('Final death number')
                plt.legend()
                fig8.savefig('./Nd_D_FinalDeathNumber.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig9 = plt.figure()
                plt.plot(TT, DataD /S0, 'r', label="Final death rate")
                # 百分数
                def to_percent(temp, position):
                    return '%1.0f' % (100 * temp) + '%'
                plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
                plt.xlabel("Measure level")
                plt.ylabel('Final Death/Total(people)')
                plt.legend()
                fig9.savefig('./Nd_D_FinalDeathRate.svg', dpi=400, bbox_inches='tight')
                plt.show()
                break
            elif(imageflag == "2"):
                break
            else:
                print("Your input is worng please try again!")
                imageflag = input("Your answer is:")
        print("Do U need to save the data?")
        print("YES:1")
        print("NO:2")
        while True:
            datasaveflag = input("Please input your choice:")
            if (datasaveflag == '1'):
                pd.DataFrame(DataD).to_csv("Nd_from_0_to_data_DataD.csv")
                pd.DataFrame(DataS).to_csv("Nd_from_0_to_data_DataS.csv")
                pd.DataFrame(DataI).to_csv("Nd_from_0_to_data_DataI.csv")
                print("Save data successfully!")
                break
            elif (datasaveflag == '2'):
                break
            else:
                print("Your input is worng please try again!")
                datasaveflag = input("Your answer is:")
    elif(flag == '2'):
        E = np.zeros(data)
        I = np.zeros(data)
        R = np.zeros(data)
        D = np.zeros(data)
        S = np.zeros(data)
        II = np.zeros(data)
        T = np.arange(data)
        TimeI = np.zeros(data)
        DataI = np.zeros(data)
        TimeS = np.zeros(data)
        DataS = np.zeros(data)
        TimeD = np.zeros(data)
        DataD = np.zeros(data)
        new_nd = float(input("Threshold n_d SUCH AS 0.3:"))
        for td_indx in range(data):
            max_time_I = 0
            max_number_I = 0
            min_time_S = 0
            min_number_S = S0
            equal_number_D = 0
            equal_time_D = 0
            T = np.arange(data)
            E[0] = E0
            I[0] = I0
            R[0] = R0
            D[0] = D0
            S[0] = S0
            II[0] = II0
            n_d = n_dddd
            for idx in range(data-1):
                if idx >= td_indx:
                    n_d = new_nd
                S[idx + 1] = S[idx] - a_I * B_I * n * n_d * I[idx] * S[idx] / (
                            S[idx] + E[idx] + R[idx] + I[idx] * n) - a_E * B_E * n_d * I[idx] * S[idx] / (
                                         S[idx] + E[idx] + R[idx] + I[idx] * n) + i_R * I[idx] + e_R * E[idx]
                E[idx + 1] = E[idx] + a_I * B_I * n * n_d * I[idx] * S[idx] / (
                            S[idx] + E[idx] + R[idx] + I[idx] * n) + a_E * B_E * n_d * I[idx] * S[idx] / (
                                         S[idx] + E[idx] + R[idx] + I[idx] * n) - e_I * E[idx] - e_R * E[idx]
                I[idx + 1] = I[idx] + e_I * E[idx] - i_R * I[idx] - i_D * I[idx]
                R[idx + 1] = R[idx] + i_R * I[idx] + e_R * E[idx]
                D[idx + 1] = D[idx] + i_D * I[idx]
                II[idx + 1] = II[idx] + I[idx + 1]
            for i in range(data):
                if I[i] > max_number_I:
                    max_number_I = I[i]
                    max_time_I = i
                if (S[i] < min_number_S):
                    min_number_S = S[i]
                    min_time_S = i
                if math.floor(D[i]) > equal_number_D:
                    equal_number_D = math.floor(D[i])
                    equal_time_D = i

            TimeI[td_indx] = max_time_I
            DataI[td_indx] = int(max_number_I)
            TimeS[td_indx] = min_time_S
            DataS[td_indx] = int(min_number_S)

            TimeD[td_indx] = equal_time_D
            DataD[td_indx] = int(equal_number_D)
        print("Your work 'Td_from_0_to_data.ipynb' process successfully!")
        print("Whether an image needs to be drawn? : ")
        print("YES:1")
        print("NO:2")
        imageflag = input("Please input your choice:")
        while True:
            if(imageflag=='1'):
                fig1 = plt.figure()
                plt.plot(T, TimeI, 'r', label='Max infected time')
                plt.xlabel("Measure start day")
                plt.ylabel('The time to get the maximum value(day)')
                plt.legend(['Max infected time'])
                fig1.savefig('./Td_I_MaxInfectedTime.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig2 = plt.figure()
                plt.plot(T, DataI, 'r', label='Max infected number')
                plt.xlabel("Measure start day")
                plt.ylabel('The maximum number of people')
                ax = plt.gca()  # 获取当前图像的坐标轴信息
                ax.yaxis.get_major_formatter().set_powerlimits((0, 1))  # 将坐标轴的base number设置为一位。
                plt.legend()
                fig2.savefig('./Td_I_MaxInfectedNumber.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig3 = plt.figure()
                plt.plot(T, DataI / S0, 'r', label="Max infected rate")
                # 百分数
                def to_percent(temp, position):
                    return '%1.0f' % (100 * temp) + '%'
                plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
                plt.xlabel("Measure start day")
                plt.ylabel('Max/Total(people)')
                plt.legend()
                fig3.savefig('./Td_I_MaxInfectedRate.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig4 = plt.figure()
                plt.plot(T, TimeS, 'r', label='Min susceptible time')
                plt.xlabel("Measure start day")
                plt.ylabel('The time to get the minimum value(day)')
                plt.legend()
                fig4.savefig('./Td_S_MinSusceptibleTime.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig5 = plt.figure()
                plt.plot(T, DataS, 'r', label='Min susceptible number')
                plt.xlabel("Measure start day")
                plt.ylabel('The minimum number of people')
                ax = plt.gca()  # 获取当前图像的坐标轴信息
                ax.yaxis.get_major_formatter().set_powerlimits((0, 1))  # 将坐标轴的base number设置为一位。
                plt.legend()
                fig5.savefig('./Td_S_MinSusceptibleNumber.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig6 = plt.figure()
                plt.plot(T, DataS / S0, 'r', label="Min susceptible rate")
                # 百分数
                def to_percent(temp, position):
                    return '%1.0f' % (100 * temp) + '%'
                plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
                plt.xlabel("Measure start day")
                plt.ylabel('Min/Total(people)')
                plt.legend()
                fig6.savefig('./Td_S_MinSusceptibleRate.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig7 = plt.figure()
                plt.plot(T, TimeD, 'r', label='Final death time')
                plt.xlabel("Measure start day")
                plt.ylabel('The time to get the maximum value(day)')
                plt.legend()
                fig7.savefig('./Td_D_FinalDeathTime.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig8 = plt.figure()
                plt.plot(T, DataD, 'r', label="Final death number")
                ax = plt.gca()  # 获取当前图像的坐标轴信息
                ax.yaxis.get_major_formatter().set_powerlimits((0, 1))  # 将坐标轴的base number设置为一位。
                plt.xlabel("Measure start day")
                plt.ylabel('Final death number')
                plt.legend()
                fig8.savefig('./Td_D_FinalDeathNumber.svg', dpi=400, bbox_inches='tight')
                plt.show()
                fig9 = plt.figure()
                plt.plot(T, DataD / S0, 'r', label="Final death rate")
                # 百分数
                def to_percent(temp, position):
                    return '%1.0f' % (100 * temp) + '%'
                plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
                plt.xlabel("Measure start day")
                plt.ylabel('Final Death/Total(people)')
                plt.legend()
                fig9.savefig('./Td_D_FinalDeathRate.svg', dpi=400, bbox_inches='tight')
                plt.show()

                print("Do U need to save the data?")
                print("YES:1")
                print("NO:2")
                while True:
                    datasaveflag = input("Please input your choice:")
                    if (datasaveflag == '1'):
                        pd.DataFrame(DataD).to_csv("Td_from_0_to_data_DataD.csv")
                        pd.DataFrame(DataS).to_csv("Td_from_0_to_data_DataS.csv")
                        pd.DataFrame(DataI).to_csv("Td_from_0_to_data_DataI.csv")
                        print("Save data successfully!")
                        break
                    elif (datasaveflag == '2'):
                        break
                    else:
                        print("Your input is worng please try again!")
                        datasaveflag = input("Your answer is:")
                break
            elif(imageflag=='2'):
                break
            else:
                pass
    else:
        print("Your input is wrong, please try again!")

#CM_SEIRD_PARAMENTER()

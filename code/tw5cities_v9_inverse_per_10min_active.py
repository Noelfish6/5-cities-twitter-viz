'''
    The code is used as a practise code of python
    cretated on Tue May 14, 2017
    @author: jimmy shen
'''
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import collections
import math
import re
import assignment2_p1
image_inverse = True

def file_parse(file_name, head_length=0):
    
    line_data=[]
    with open(file_name) as f:
        for line in f:
            line_data.append(line.split())
    #print "before",head_length,line_data[0]
    #del line_data[0:head_length]
    # print line_data[0]
    #line_data_array=np.array(line_data)
#line_data_array = line_data_array.astype(float)
    return line_data
def plot_hist(image,title):
    K=int(max(image.flatten())+1)
    hist, bin_edges = np.histogram(image, bins=K,range=(0.0, K), density=True)
    plt.figure(1)
    #plt.subplot(311)
    plt.plot(hist, '#ca0020')
    plt.title('Normalized hist of '+title + ' for twitter post per 10 mins')
    plt.savefig('/home/tingxu/Documents/jimmy/tw5cities/output/'+title+'histo.png')
    plt.show()

def plot_grey_level_image(data,time_period,y_title,title):
    x=data[:,12].astype(float)
    image_array=np.zeros((time_period,1400))
    for i in range(len(x)):
        day=int(x[i])
        second=int(time_period*(x[i]-math.floor(x[i])))
        if second>=time_period:
            second=time_period-1
        image_array[second,day]+=1
    image_array_active_ratio = np.zeros(image_array.shape)
    image_array_active_ratio.astype(float)
    print "max(image_array.flatten()):",max(image_array.flatten())
    plot_hist(image_array,title)
    for i in range(len(image_array)):
        for j in range(len(image_array[0])):
            if sum(image_array[:,j]) > 1.0:
                   image_array_active_ratio[i,j] = 1000.0*image_array[i,j]/sum(image_array[:,j])
    image_array=(255.0/120.0)*image_array
    #plot_hist(image_array,title+'adjusted')
    binary_image=assignment2_p1.get_binary_image(image_array_active_ratio,threshold=1000.0*0.01,low_threshold_indi=False,title=title)
    if image_inverse:
        image_array=255.0-image_array
        binary_image=255.0-binary_image
    plt.imshow(image_array, cmap='gray')
    plt.title(title)
    plt.ylabel(y_title)
    plt.xlabel("Days since 2011 January 1")
    plt.savefig('/home/tingxu/Documents/jimmy/tw5cities/output/'+title+'.png')
    #binary_image=assignment2_p1.get_binary_image(image_array,threshold=10,low_threshold_indi=False,title=title)
    plt.imshow(binary_image, cmap='gray')
    plt.title(title+"active timeline")
    plt.ylabel(y_title)
    plt.xlabel("Days since 2011 January 1")
    plt.savefig('/home/tingxu/Documents/jimmy/tw5cities/output/'+title+'binary.png')
    plt.show()
def plot_2d(data,i,color_list, label_name):
    x=data[:,12].astype(float)
    y = np.cos(2*np.pi*x)
    # the reason 6 is added is wantting to reverse the order from   1,2,3,4,5 to 5,4,3,2,1 which is 6-i
    y=-0.5+6-i+0.48*y
    #i=1    -0.5+1+0.5(-1.+1)=0.5~1.5
    #i=2    -0.5+2+0.5(-1.+1)= 1.5~2.5

    print y[0:10]
    print data[0:10,12]
    plt.scatter(x, y,alpha=0.3,label= label_name, color=color_list[i-1], s=0.01)


#2011-09-04_12:57:54

def is_leap_year(year):
    """ if year is a leap year return True
        else return False """
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0

def doy(Y,M,D):
    """ given year, month, day return day of year
        Astronomical Algorithms, Jean Meeus, 2d ed, 1998, chap 7 """
    if is_leap_year(Y):
        K = 1
    else:
        K = 2
    N = int((275 * M) / 9.0) - K * int((M + 9) / 12.0) + D - 30
    return N


#2011-09-04_12:57:54
def get_time(str_number):
    new_time = []
    str_number=str_number.split("_")
    new_time.extend(str_number[0].split("-"))
    new_time.extend(str_number[1].split(":"))
    year,month,day,hour,minute,second=int(new_time[0]),int(new_time[1]),int(new_time[2]),int(new_time[3]),int(new_time[4]),int(new_time[5])
    number_of_days=0
#visual tweets in five cities during 2011-2014.
    if year<2011 or year >2014:
        print "error, the visual tweets  in five cities is during 2011-2014"
    elif year == 2011:
        time=doy(year,month,day)-1+(hour*60*60+minute*60+second)/(24*60*60.0)
    else:
        for i in range(2011,year):
            number_of_days+=doy(i,12,31)
        time=number_of_days+doy(year,month,day)-1+(hour*60*60+minute*60+second)/(24*60*60.0)
        number_of_days=0
    return time


def change_the_time_into_some_number (data, index=7):
    data[0].append("time")
    for i in range(1,len(data)):
         data[i].append(get_time(data[i][index]))

def check_valid(data):
    for i in range(len(data)-1):
        if len(data[i]) != len(data[i+1]):
            print "error"


def  visualize_city_one_by_one(data_array,city_name):
    #'b', 'g', 'k', 'm'
    #color_list=['#69D2E7', '#C3FF68', '#FE4365','#CCFF00','#025D8C']
    color_list=['#404040', '#404040', '#404040','#404040','#404040']
    title='all_cities'
    #time_period=60*24
    #every 10 minutes.
    time_period=6*24
    y_title="Every 10 minutes (start from 00:00am to 23:59pm)"
    #every 30 minutes.
    #time_period=2*24
    #y_title="Every 30 minutes (start from 00:00am to 23:59pm)"
    #time_period=60*24
    #y_title="Every minute (start from 00:00am to 23:59pm)"
    plot_grey_level_image(data_array,time_period,y_title,title)
    for i in range(len(city_name)):
        
        title=city_name[i]
        plot_grey_level_image(data_array[data_array[:,0]==city_name[i]],time_period,y_title,title)
    
#plot_2d(data_array[data_array[:,0]==city_name[i]],i+1,color_list,city_name[i])




if __name__=="__main__":

    file_name = "/home/tingxu/Documents/jimmy/tw5cities/tw5cities_after_data_clean.txt"
    data = file_parse(file_name, 0)
    print data[:3]
    
    #remove the first row of the original data
    
    check_valid(data)
    change_the_time_into_some_number (data)
    del data[0]
    print data[:3]
    data_array=np.array(data)
    city_name =list(set(data_array[:,0].tolist()))
    print city_name
    print "data_array[0:10,12]",data_array[0:10,12]
    visualize_city_one_by_one(data_array,city_name)

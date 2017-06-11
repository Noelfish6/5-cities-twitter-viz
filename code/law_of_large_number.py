'''
    The code is used to simulate the toss coin process and finally to simulate the result of the law of large number.
    @author: jimmy shen
'''
import matplotlib.pyplot as plt
import numpy as np


def law_of_large_number_simu(number_of_simulation, step=100):
    """
        
        """
    x=list(range(0,number_of_simulation,step))
    #print(x)
    y=[]
    for i in range(int(number_of_simulation/step)):
        #temp_y=[]
        
        temp_y= np.zeros(1)
        for j in range((i+1)*step):
            if np.random.uniform(0.0, 1.0)<=0.5:
                temp_y+=1
        y.append(temp_y/((i+1)*step))
            #print(y)
    plt.scatter(x, y,alpha=0.08, color='#ca0020', s=0.5)
    
    plt.title('Head frequency by number of fair coin flippings experiments')
    plt.ylabel("Head frequency")
    plt.xlabel("Number of fair coin flippings experiments")
    plt.savefig('/Users/jimmy/Dropbox/data_viz/tw5cities/law_of_large_number.png')
    plt.show()

# y.append()
    

#x=np.random.uniform(0.0, 1.0, size=NUMBER_OF_DATA_POINT)
    

#plt.scatter(x, y,alpha=0.3,label= label_name, color=color_list[i-1], s=0.01)


if __name__=="__main__":
    number_of_simulation=20000
    step=2
    law_of_large_number_simu(number_of_simulation,step)



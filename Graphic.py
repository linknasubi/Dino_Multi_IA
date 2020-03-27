import pyautogui
import time
import numpy as np
import PIL.ImageGrab as ImageGrab
import numpy as np
pyautogui.FAILSAFE = True


def sigmoid(x):
    return (1/(1+np.exp(-x)))


def initial_Values():
    
    vision, w_o, w_h = [], [], []
    
    
    for i in range(5):
    
        vision.append([np.random.randint(0, len(im_matrix), size = spots_number), 
                               np.random.randint(0, len(im_matrix[0]), size = spots_number)])
        
        w_h.append([np.random.rand(len(feature_set), nodes_num)])
    
        w_o.append([np.random.rand(len(hidden_neurons), 1)])
    
    return vision, w_h, w_o


def mutated_Values(vis, wei_h, wei_o):
    vision, w_o, w_h = [[], []], [], []
    gen_vision = []

    
    for i in range (5):
        mut_rate = (np.random.randint(-5,5)/100)
    
        vision[0] = (np.multiply(vis[0], mut_rate))
        vision[1] = (np.multiply(vis[1], mut_rate))
        vision[0] = [int(x) for x in vision[0]]
        vision[1] = [int(x) for x in vision[1]]
        gen_vision.append([(vision[0]),(vision[1])])
#        vision[0] = vision[0].astype(np.int64)
#        vision[1] = vision[1].astype(np.int64)
        
        w_h.append(np.multiply(wei_h, mut_rate))
    
        w_o.append(np.multiply(wei_o, mut_rate))
    
    return gen_vision, w_h, w_o



over = False

time.sleep(2)

start_time = 0
res_config = [1920, 1080]

np.random.seed(7)

box_area_visions = {}
number_of_visions = 6
spots_number = 6


#for i in range (number_of_visions):
#    box_area_vision = (((i+1)*(res_config[0]//2))//(number_of_visions+1), res_config[1]//4, 
#                       ((i+2)*(res_config[0]//2)-10)//(number_of_visions+1), res_config[1]//2)
#    im = ImageGrab.grab(box_area_vision)
#    box_area_visions[i] = im




box_area_vision = (((1)*(res_config[0]//2))//(number_of_visions+1), res_config[1]//4, 
                       ((2)*(res_config[0]//2)-10)//(number_of_visions+1), res_config[1]//2)



game_over_vision = (4*res_config[0]//20, 6*res_config[1]//20, 
                    6*res_config[0]//20, 8*res_config[1]//20)
img_over = ImageGrab.grab(game_over_vision)
arr_over = np.array(img_over)




im = ImageGrab.grab(box_area_vision)
im_matrix = np.array(im)


 

selec_pixels = [np.random.randint(0, len(im_matrix), size = spots_number), 
                np.random.randint(0, len(im_matrix[0]), size = spots_number)]



nodes_num = 6

feature_set = np.array(selec_pixels[0])
hidden_weights = np.random.rand(len(feature_set), nodes_num)
hidden_weights_1 = np.random.rand(nodes_num, nodes_num)
hidden_neurons = np.zeros([nodes_num])
hidden_neurons_1 = np.zeros([nodes_num])
output_weights = np.random.rand(len(hidden_neurons), 1)


vision_values, weights_h, weights_o = initial_Values()
time_values = []




def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')


def appending_values(flag, vision_values, weight_h, weight_o):
    vision = []
    weight_1 = []
    weight_2 = []
    time = []
    vision.append(vision_values)
    weight_1.append(weight_h)
    weight_2.append(weight_o)
    time.append(time.time())

counter, idx_counter, counter_flag = 0, -1, 0
time_flag = True

while True:
    
    over = False
    
    if arr_over[23][100][0] == 83 and arr_over[69][100][0] == 83:
        
        
        print(counter)
        
        game_over_vision = (4*res_config[0]//20, 6*res_config[1]//20, 
                            6*res_config[0]//20, 8*res_config[1]//20)
        img_over = ImageGrab.grab(game_over_vision)
        arr_over = np.array(img_over)
        
        
        
        over=True
        time_flag = True        

        
        if counter == 5:
            print('passou')
            idx_counter = -1

            best_idx = time_values.index(max(time_values))
            
            counter = 0
            
            vision_values, weights_h, weights_o = mutated_Values(vision_values[best_idx],
                                                                 weights_h[best_idx],
                                                                 weights_o[best_idx])
            del time_values[:]
            
              
        if counter_flag == 0:
            time.sleep(0.5)
            print('a')
            jump()
            counter += 1
            idx_counter += 1
            counter_flag = 1
        

        
    if time_flag == True:
        start_time = time.time()
        actual_time = time.time() - start_time
        time_values.append(actual_time)
        
        time_flag = False
    
    
    
    
    
    if over == False:
        counter_flag = 0
   
        time.sleep(0.05)
        
        
        game_over_vision = (4*res_config[0]//20, 6*res_config[1]//20, 
                             6*res_config[0]//20, 8*res_config[1]//20)
        img_over = ImageGrab.grab(game_over_vision)
        arr_over = np.array(img_over)
        
        
       
        
        box_area_vision = (((1)*(res_config[0]//2))//(number_of_visions+1), res_config[1]//4, 
                           ((2)*(res_config[0]//2)-10)//(number_of_visions+1), res_config[1]//2)
    
        im = ImageGrab.grab(box_area_vision)
        im_matrix = np.array(im)
        feature_set = []
        
        
        for i, j in zip(vision_values[idx_counter][0], vision_values[idx_counter][1]):
            feature_set.append(im_matrix[i][j][0])
    
        print(feature_set)
    
        
        
        output_neurons = np.zeros([1])     
        hidden_neurons = sigmoid(np.dot(feature_set, hidden_weights[idx_counter]))
        hidden_neurons_1 = sigmoid(np.dot(hidden_neurons, hidden_weights_1[idx_counter]))
        output_neurons = sigmoid(np.dot(output_weights.T, hidden_neurons_1))
        
    
        

        print(output_neurons)
        
        if output_neurons > 0.8:
            jump()





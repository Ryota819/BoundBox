#################### Configuration File ####################

# Base directory for data formats
#name = 'Guro_GM'
#name = 'Guro_G'
#name = 'Guro_M'
#name = 'Guro_L'
#name = 'Guro_N'
#name = 'WBC'
#name = 'BCCD_GM'
#name = 'BCCD_G'
#name = 'BCCD_M'

#H1_name = 'Guro_GM'
#G_name = 'Guro_G'
#M_name = 'Guro_M'
#N_name = 'Guro_N'
#L_name = 'Guro_L'

name = 'iwasawa_data'
#name = 'kitagawa_data'

data_dir = '/home/mnt/datasets/'
aug_dir = '/home/bumsoo/Data/_train_val/'


# Base directory for data formats
data_base = '/app/test_dir/model_test/tacit/data/' + name 

# Base directory for augmented data formats
resize_base = '/app/test_dir/model_test/tacit/data/resized/'
split_base = '/app/test_dir/model_test/tacit/data/train_val/'
 
# Directory for data formats
resize_dir = resize_base + name
split_dir = split_base + name


# Databases for each formats
aug_base = split_dir
#test_base = '/home/bumsoo/Data/test/WBC_TEST'
test_dir = split_dir + '/val/'
#inf_dir = '/home/bumsoo/Data/_train_val/Guro_WBC/val/'

# model option
batch_size = 8
num_epochs = 100
lr_decay_epoch=2
momentum = 0.9
feature_size = 2

# iwasawa
mean = [0.5227580379258157, 0.5450905843890521, 0.5853761483033867]
std = [0.270646664923136, 0.2747962817680165, 0.28246877727537917]

#kitagawa
#mean = [0.5445120686065779, 0.5626707289320649, 0.5949899302771897]
#std = [0.2736441325979423, 0.2814183767548244, 0.2886356616092051]

'''
# Granulocyte vs Mononuclear
mean_H = [0.75086572277254926, 0.54344990735699861, 0.56189840210810549]
std_H = [0.19795568869316291, 0.29897863665208158, 0.26473830163404605]

# Granulocytes
mean_G = [0.7260078523435356, 0.50995708667892348, 0.53427415115119681]
std_G = [0.20467739828829676, 0.30475251036479978, 0.27280720957235177]

# Mononuclear
mean_M = [0.7594375520640767, 0.55067103657252647, 0.56366851380109106]
std_M = [0.19572272727963994, 0.30284308059727105, 0.26669885653951991]

# NH meanstd
mean_N = [0.72968820508788612, 0.52224113128933247, 0.54099372274735391]
std_N = [0.208528564775461, 0.30056530735626585, 0.27138967466099473]

# LH meanstd
mean_L = [0.7571956979879545, 0.55694333649406613, 0.56854173074367431]
std_L = [0.20890086199641186, 0.31668580372231542, 0.28084878897340337]

if (name == 'Guro_GM'):
    # Granulocytes_vs_Mononuclear
    mean = [0.75086572277254926, 0.54344990735699861, 0.56189840210810549]
    std = [0.19795568869316291, 0.29897863665208158, 0.26473830163404605]
elif (name == 'Guro_G'):
    mean = [0.7260078523435356, 0.50995708667892348, 0.53427415115119681]
    std = [0.20467739828829676, 0.30475251036479978, 0.27280720957235177]
elif (name == 'Guro_M'):
    mean = [0.7594375520640767, 0.55067103657252647, 0.56366851380109106]
    std = [0.19572272727963994, 0.30284308059727105, 0.26669885653951991]
elif (name == 'Guro_L'):
    mean = [0.7571956979879545, 0.55694333649406613, 0.56854173074367431]
    std = [0.20890086199641186, 0.31668580372231542, 0.28084878897340337]
elif (name == 'Guro_N'):
    mean = [0.72968820508788612, 0.52224113128933247, 0.54099372274735391]
    std = [0.208528564775461, 0.30056530735626585, 0.27138967466099473]
elif (name == 'WBC'):
    # WBC meanstd
    mean = [0.7593608074350131, 0.6122998654014106, 0.6142165029355519]
    std = [0.22106204895546486, 0.27805751343124707, 0.2522135438853085]
elif (name == 'BCCD_WBC' or name == 'BCCD_GM'):
    mean = [0.66049439066232607, 0.64131680516457479, 0.67861641316853616]
    std = [0.25870889538041947, 0.26112642565510558, 0.26200774691285844]
elif (name == 'BCCD_G'):
    mean = [0.6573611811732865, 0.6380462082799403, 0.6767932371428185]
    std = [0.25759305343128985, 0.2599911268172555, 0.26104541183046104]
elif (name == 'BCCD_M'):
    mean = [0.6636497050358816, 0.644610476205828, 0.6804524517544022]
    std = [0.2598277668079999, 0.2622647674637204, 0.26297331235868215]
else:
    raise NotImplementedError
'''

import numpy as np
import os
import scikits.statsmodels as sm


### RLM MODEL RESULTS ###

def _shift_intercept(arr):
    """
    A convenience function to make the SAS covariance matrix
    compatible with statsmodels.rlm covariance
    """
    side = np.sqrt(len(arr))
    arr = np.array(arr).reshape(side,side)
    tmp = np.zeros((side,side))
    tmp[:-1,:-1] = arr[1:,1:]
    tmp[-1,-1] = arr[0,0]
    tmp[-1,:-1] = arr[0,1:]
    tmp[:-1,-1] = arr[1:,0]
    return tmp

class Huber(object):
    huber_h1 = [95.8813, 0.19485, -0.44161, -1.13577, 0.1949, 0.01232,
            -0.02474, -0.00484, -0.4416, -0.02474, 0.09177, 0.00001, -1.1358,
            -0.00484, 0.00001, 0.01655]
    h1 = _shift_intercept(huber_h1)

    huber_h2 = [82.6191, 0.07942, -0.23915, -0.95604, 0.0794, 0.01427,
            -0.03013, -0.00344, -0.2392, -0.03013, 0.10391, -0.00166, -0.9560,
            -0.00344, -0.00166, 0.01392]
    h2 = _shift_intercept(huber_h2)

    huber_h3 = [70.1633, -0.04533, -0.00790, -0.78618, -0.0453, 0.01656,
            -0.03608, -0.00203, -0.0079, -0.03608,  0.11610, -0.00333, -0.7862,
            -0.00203, -0.00333,  0.01138]
    h3 = _shift_intercept(huber_h3)

class Hampel(object):
    hampel_h1 = [141.309,  0.28717, -0.65085, -1.67388, 0.287,  0.01816,
            -0.03646, -0.00713, -0.651, -0.03646,  0.13524,  0.00001, -1.674,
            -0.00713, 0.00001,  0.02439]
    h1 = _shift_intercept(hampel_h1)

    hampel_h2 = [135.248,  0.18207, -0.36884, -1.60217, 0.182, 0.02120,
            -0.04563, -0.00567, -0.369, -0.04563,  0.15860, -0.00290, -1.602,
            -0.00567, -0.00290, 0.02329]
    h2 = _shift_intercept(hampel_h2)

    hampel_h3 = [128.921,  0.05409, -0.02445, -1.52732, 0.054,  0.02514,
            -0.05732, -0.00392, -0.024, -0.05732,  0.18871, -0.00652, -1.527,
            -0.00392, -0.00652,  0.02212]
    h3 = _shift_intercept(hampel_h3)

class Bisquare(object):
    bisquare_h1 = [90.3354,  0.18358, -0.41607, -1.07007, 0.1836, 0.01161,
            -0.02331, -0.00456, -0.4161, -0.02331,  0.08646, 0.00001, -1.0701,
            -0.00456, 0.00001,  0.01559]
    h1 = _shift_intercept(bisquare_h1)

    bisquare_h2 = [67.82521, 0.091288, -0.29038, -0.78124, 0.091288,
            0.013849, -0.02914, -0.00352, -0.29038, -0.02914, 0.101088, -0.001,
            -0.78124, -0.00352,   -0.001, 0.011766]
    h2 = _shift_intercept(bisquare_h2)

    bisquare_h3 = [48.8983, 0.000442, -0.15919, -0.53523, 0.000442,
            0.016113, -0.03461, -0.00259, -0.15919, -0.03461, 0.112728,
            -0.00164, -0.53523, -0.00259, -0.00164, 0.008414]
    h3 = _shift_intercept(bisquare_h3)

class Andrews(object):
    andrews_h1 = [87.5357, 0.177891, -0.40318, -1.03691, 0.177891,  0.01125,
            -0.02258, -0.00442, -0.40318, -0.02258, 0.083779, 6.481E-6,
            -1.03691, -0.00442, 6.481E-6,  0.01511]
    h1 = _shift_intercept(andrews_h1)

    andrews_h2 = [66.50472,  0.10489,  -0.3246, -0.76664, 0.10489, 0.012786,
            -0.02651,  -0.0036, -0.3246, -0.02651,  0.09406, -0.00065,
            -0.76664,  -0.0036, -0.00065, 0.011567]
    h2 = _shift_intercept(andrews_h2)

    andrews_h3 = [48.62157, 0.034949, -0.24633, -0.53394, 0.034949, 0.014088,
                -0.02956, -0.00287, -0.24633, -0.02956, 0.100628, -0.00104,
                -0.53394, -0.00287, -0.00104, 0.008441]
    h3 = _shift_intercept(andrews_h3)

    resid = [2.503338458, -2.608934536, 3.5548678338, 6.9333705014,
            -1.768179527, -2.417404513, -1.392991531, -0.392991531,
            -1.704759385,-0.244545418, 0.7659115325, 0.3028635237,
            -3.019999429,-1.434221475,2.1912017882, 0.8543828047,
            -0.366664104,0.4192468573,0.8822948661,1.5378731634,
            -10.44592783]

    sresids = [1.0979293816, -1.144242351, 1.5591155202, 3.040879735,
            -0.775498914, -1.06023995, -0.610946684, -0.172360612,
            -0.747683723, -0.107254214, 0.3359181307, 0.1328317233,
            -1.324529688, -0.629029563, 0.9610305856, 0.3747203984,
            -0.160813769, 0.1838758324, 0.3869622398, 0.6744897502,
            -4.581438458]

    weights = [0.8916509101, 0.8826581922, 0.7888664106, 0.3367252734,
            0.9450252405, 0.8987321912, 0.9656622, 0.9972406688,
            0.948837669, 0.9989310017, 0.9895434667, 0.998360628,
            0.8447116551, 0.9636222149, 0.916330067, 0.9869982597,
            0.9975977354, 0.9968600162, 0.9861384742, 0.9582432444, 0]

    conf_int = [(0.7203,1.1360),(.0819,1.2165),(-.3532,.1287),
                (-60.6305,-23.9555)]

    def __init__(self):
        self.params = [0.9282, 0.6492, -.1123,-42.2930]
        self.bse = [.1061, .2894, .1229, 9.3561]
        self.scale = 2.2801
        self.df_model = 3.
        self.df_resid = 17.
        self.bcov_unscaled = []
        self.h1 = self.h1
        self.h2 = self.h2
        self.h3 = self.h3


### RLM Results with Huber's Proposal 2 ###
### Obtained from SAS ###

class HuberHuber(object):
    def __init__(self):
        self.h1 = [114.4936, 0.232675, -0.52734, -1.35624, 0.232675, 0.014714,
                -0.02954, -0.00578, -0.52734, -0.02954, 0.10958, 8.476E-6,
                -1.35624, -0.00578, 8.476E-6, 0.019764]
        self.h1 = _shift_intercept(self.h1)
        self.h2 = [103.2876, 0.152602, -0.33476, -1.22084, 0.152602, 0.016904,
                -0.03766, -0.00434, -0.33476, -0.03766, 0.132043, -0.00214,
                -1.22084, -0.00434, -0.00214, 0.017739]
        self.h2 = _shift_intercept(self.h2)
        self.h3 = [ 91.7544, 0.064027, -0.11379, -1.08249, 0.064027, 0.019509,
                -0.04702, -0.00278, -0.11379, -0.04702, 0.157872, -0.00462,
                -1.08249, -0.00278, -0.00462, 0.015677]
        self.h3 = _shift_intercept(self.h3)
        self.resid = [2.909155172, -2.225912162, 4.134132661, 6.163172632,
                -1.741815737, -2.789321552, -2.02642336, -1.02642336,
                -2.593402734, 0.698655, 1.914261011, 1.826699492, -2.031210331,
                -0.592975466, 2.306098648, 0.900896645, -1.037551854,
                -0.092080512, -0.004518993, 1.471737448, -8.498372406]
        self.sresids = [0.883018497, -0.675633129, 1.25483702, 1.870713355,
                -0.528694904, -0.84664529, -0.615082113, -0.311551209,
                -0.787177874, 0.212063383, 0.581037374, 0.554459746,
                -0.616535106, -0.179986379, 0.699972205, 0.273449972,
                -0.314929051, -0.027949281, -0.001371654, 0.446717797,
                -2.579518651]
        self.weights = [1, 1, 1, 0.718977066, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 0.52141511]
        self.conf_int = [(0.5612,1.0367),(.3987,1.6963),
                (-.4106,.1405),(-62.0611,-20.1172)]
        self.params = (.7990,1.0475,-0.1351,-41.0892)
        self.bse = (.1213,.3310,.1406,10.7002)
        self.scale = 3.2946
        self.df_model = 3
        self.df_resid = 17


class HampelHuber(object):
    def __init__(self):
        self.h1 = [147.4727, 0.299695, -0.67924, -1.7469, 0.299695, 0.018952,
                -0.03805, -0.00744, -0.67924, -0.03805, 0.141144, 0.000011,
                -1.7469, -0.00744, 0.000011, 0.025456]
        self.h1 = _shift_intercept(self.h1)
        self.h2 = [141.148, 0.190007, -0.38493, -1.67206, 0.190007, 0.02213,
                -0.04762, -0.00592, -0.38493, -0.04762, 0.165518, -0.00303,
                -1.67206, -0.00592, -0.00303, 0.024301]
        self.h2 = _shift_intercept(self.h2)
        self.h3 = [134.5444, 0.05645, -0.02552, -1.59394, 0.05645, 0.026232,
                -0.05982, -0.00409, -0.02552, -0.05982, 0.196946, -0.0068,
                -1.59394, -0.00409, -0.0068, 0.023083]
        self.h3 = _shift_intercept(self.h3)
        self.resid = [3.125725599, -2.022218392, 4.434082972, 5.753880172,
                -1.744479058, -2.995299443, -2.358455878, -1.358455878,
                -3.068281354, 1.150212629, 2.481708553, 2.584584946,
                -1.553899388, -0.177335865, 2.335744732, 0.891912757,
                -1.43012351, -0.394515569, -0.497391962, 1.407968887,
                -7.505098501]
        self.sresids = [0.952186413, -0.616026205, 1.350749906, 1.752798302,
                -0.531418771, -0.912454834, -0.718453867, -0.413824947,
                -0.934687235, 0.350388031, 0.756000196, 0.787339321,
                -0.473362692, -0.054021633, 0.711535395, 0.27170242,
                -0.43565698, -0.120180852, -0.151519976, 0.428908041,
                -2.28627005]
        self.weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 0.874787298]
        self.conf_int = [(0.4619,1.0016),(.5145,1.9872),
                (-.4607,.1648),(-64.0727,-16.4697)]
        self.params = (.7318,1.2508,-0.1479,-40.2712)
        self.bse = (.1377, .3757, .1596, 12.1438)
        self.scale = 3.2827
        self.df_model = 3
        self.df_resid = 17

class BisquareHuber(object):
    def __init__(self):
        self.h1 = [129.9556, 0.264097, -0.59855, -1.5394, 0.264097,
                0.016701, -0.03353, -0.00656, -0.59855, -0.03353,
                0.124379, 9.621E-6, -1.5394, -0.00656, 9.621E-6, 0.022433]
        self.h1 = _shift_intercept(self.h1)
        self.h2 = [109.7685, 0.103038, -0.25926, -1.28355, 0.103038, 0.0214,
                -0.04688, -0.00453, -0.25926, -0.04688, 0.158535, -0.00327,
                -1.28355, -0.00453, -0.00327, 0.018892]
        self.h2 = _shift_intercept(self.h2)
        self.h3 = [91.80527, -0.09171, 0.171716, -1.05244, -0.09171,
                0.027999, -0.06493, -0.00223, 0.171716, -0.06493, 0.203254,
                -0.0071, -1.05244, -0.00223, -0.0071, 0.015584]
        self.h3 = _shift_intercept(self.h3)
        self.resid = [3.034895447, -2.09863887, 4.229870063, 6.18871385,
            -1.715906134, -2.763596142, -2.010080245, -1.010080245,
            -2.590747917, 0.712961901, 1.914770759, 1.82892645, -2.019969464,
            -0.598781979, 2.260467209, 0.859864256, -1.057306197, -0.122565974,
            -0.036721665, 1.471074632, -8.432085298]
        self.sresids = [0.918227061, -0.634956635, 1.279774287, 1.872435025,
            -0.519158394, -0.836143718, -0.608162656, -0.305606249, -0.78384738,                     0.215711191, 0.579326161, 0.553353415, -0.611154703, -0.181165324,
            0.683918836, 0.26015744, -0.319894764, -0.037083121, -0.011110375,
            0.445083055, -2.551181429]
        self.weights = [0.924649089, 0.963600796, 0.856330585, 0.706048833,
            0.975591792, 0.937309703, 0.966582366, 0.991507994, 0.944798311,
            0.995764589, 0.969652425, 0.972293856, 0.966255569, 0.997011618,
            0.957833493, 0.993842376, 0.990697247, 0.9998747, 0.999988752,
            0.982030803, 0.494874977]
        self.conf_int = [(0.5399,1.0465),(.3565,1.7389),
                (-.4271,.1600),(-63.2381,-18.5517)]
        self.params = (.7932, 1.0477, -0.1335, -40.8949)
        self.bse = (.1292, .3527, .1498, 11.3998)
        self.scale = 3.3052
        self.df_model = 3
        self.df_resid = 17


class AndrewsHuber(object):
    def __init__(self):
        self.h1 = [129.9124, 0.264009, -0.59836, -1.53888, 0.264009,
                0.016696, -0.03352, -0.00656, -0.59836, -0.03352, 0.124337,
                9.618E-6, -1.53888, -0.00656, 9.618E-6, 0.022425]
        self.h1 = _shift_intercept(self.h1)
        self.h2 = [109.7595, 0.105022, -0.26535, -1.28332, .105022, 0.021321,
                -0.04664, -0.00456, -0.26535, -0.04664, 0.157885, -0.00321,
                -1.28332, -0.00456, -0.00321, 0.018895]
        self.h2 = _shift_intercept(self.h2)
        self.h3 = [91.82518, -0.08649, 0.155965, -1.05238, -0.08649, 0.027785,
                -0.06427, -0.0023, 0.155965, -0.06427, 0.201544, -0.00693,
                -1.05238, -0.0023, -0.00693, 0.015596]
        self.h3 = _shift_intercept(self.h3)
        self.resid = [3.040515104, -2.093093543, 4.235081748, 6.188729166,
                -1.714119676, -2.762695255, -2.009618953, -1.009618953,
                -2.591649784, 0.715967584, 1.918445405, 1.833412337,
                -2.016815123, -0.595695587, 2.260536347, 0.859710406,
                -1.059386228, -0.1241257, -0.039092633, 1.471556455,
                -8.424624872]
        self.sresids = [0.919639919, -0.633081011, 1.280950793, 1.871854667,
                -0.518455862, -0.835610004, -0.607833129, -0.305371248,
                -0.783875269, 0.216552902, 0.580256606, 0.554537345,
                -0.610009696, -0.180175208, 0.683726076, 0.260029627,
                -0.320423952, -0.037543293, -0.011824031, 0.445089734,
                -2.548127888]
        self.weights = [0.923215335, 0.963157359, 0.854300342, 0.704674258,
                0.975199805, 0.936344742, 0.9660077, 0.991354016, 0.943851708,
                0.995646409, 0.968993767, 0.971658421, 0.965766352, 0.99698502,
                0.957106815, 0.993726436, 0.990483134, 0.999868981, 0.999987004,
                0.981686004, 0.496752113]
        self.conf_int = [(0.5395,1.0460),(.3575,1.7397),
                (-.4271,.1599),(-63.2213,-18.5423)]
        self.params = (.7928, 1.0486, -0.1336, -40.8818)
        self.bse = (.1292, .3526, .1498, 11.3979)
        self.scale = 3.3062
        self.df_model = 3
        self.df_resid = 17

#### Discrete Model Tests ####
# Note that there is a slight refactor of the classes, so that one dataset
# might be used for more than one model

class Anes():
    def __init__(self):
        """
        Results are from Stata 11 (checked vs R nnet package).
        """
        self.nobs = 944

    def mnlogit_basezero(self):
        params = [-.01153598, .29771435, -.024945, .08249144, .00519655,
                -.37340167, -.08875065, .39166864, -.02289784, .18104276,
                .04787398, -2.2509132, -.1059667, .57345051, -.01485121,
                -.00715242, .05757516, -3.6655835, -.0915567, 1.2787718,
                -.00868135, .19982796, .08449838, -7.6138431, -.0932846,
                1.3469616, -.01790407, .21693885, .08095841, -7.0604782,
                -.14088069, 2.0700801, -.00943265, .3219257, .10889408,
                -12.105751]
        self.params = np.reshape(params, (6,-1))
        bse = [.0342823657, .093626795, .0065248584, .0735865799,
                .0176336937, .6298376313, .0391615553, .1082386919,
                .0079144618, .0852893563, .0222809297, .7631899491,
                .0570382292, .1585481337, .0113313133, .1262913234,
                .0336142088, 1.156541492, .0437902764, .1288965854,
                .0084187486, .0941250559, .0261963632, .9575809602,
                .0393516553, .1171860107, .0076110152, .0850070091,
                .0229760791, .8443638283, .042138047, .1434089089,
                .0081338625, .0910979921, .025300888, 1.059954821]
        self.bse = np.reshape(bse, (6,-1))
        self.cov_params = None
        self.llf = -1461.922747312
        self.llnull = -1750.34670999
        self.llr = 576.8479253554
        self.llr_pvalue = 1.8223179e-102
        self.prsquared = .1647810465387
        self.df_model = 30
        self.df_resid = 944 - 36
        self.J = 7
        self.K = 6
        self.aic = 2995.84549462
        self.bic = 3170.45003661
        z =  [-.3364988051, 3.179798597,  -3.823070772, 1.121012042,
            .2946945327, -.5928538661, -2.266269864, 3.618564069,
            -2.893164162, 2.122688754, 2.148652536, -2.949348555,
            -1.857818873, 3.616885888, -1.310634214, -.0566342868,
            1.712822091, -3.169435381, -2.090799808, 9.920912816,
            -1.031191864, 2.123004903, 3.225576554, -7.951122047,
            -2.370538224, 11.49421878, -2.352389066, 2.552011323,
            3.523595639, -8.361890935, -3.34331327, 14.43480847,
            -1.159676452, 3.533839715, 4.303962885, -11.42100649]
        self.z = np.reshape(z, (6,-1))
        pvalues = [0.7364947525, 0.0014737744, 0.0001317999, 0.2622827367,
            0.7682272401, 0.5532789548, 0.0234348654, 0.0002962422,
            0.0038138191, 0.0337799420, 0.0316619538, 0.0031844460,
            0.0631947400, 0.0002981687, 0.1899813744, 0.9548365214,
            0.0867452747, 0.0015273542, 0.0365460134, 3.37654e-23,
            0.3024508550, 0.0337534410, 0.0012571921, 1.84830e-15,
            0.0177622072, 1.41051e-30, 0.0186532528, 0.0107103038,
            0.0004257334, 6.17209e-17, 0.0008278439, 3.12513e-47,
            0.2461805610, 0.0004095694, 0.0000167770, 3.28408e-30]
        self.pvalues = np.reshape(pvalues, (6,-1))
        self.conf_int = [[[-0.0787282, 0.0556562], [0.1142092, 0.4812195],
            [-0.0377335, -0.0121565], [-0.0617356, 0.2267185], [-0.0293649,
            0.0397580], [-1.6078610, 0.8610574]], [[-0.1655059, -0.0119954],
            [0.1795247,	0.6038126], [-0.0384099, -0.0073858], [0.0138787,
            0.3482068], [0.0042042,	0.0915438], [-3.7467380, -0.7550884]],
            [[-0.2177596, 0.0058262], [0.2627019,	0.8841991], [-0.0370602,
            0.0073578], [-0.2546789, 0.2403740], [-0.0083075, 0.1234578],
            [-5.9323630,-1.3988040]],[[-0.1773841, -0.0057293], [1.0261390,
            1.5314040], [-0.0251818, 0.0078191], [0.0153462,	0.3843097],
            [0.0331544,	0.1358423], [-9.4906670, -5.7370190]], [[-0.1704124,
            -0.0161568], [1.1172810,	1.5766420], [-0.0328214, -0.0029868],
            [0.0503282,	0.3835495], [0.0359261,	0.1259907], [-8.7154010,
            -5.4055560]], [[-0.2234697, -0.0582916], [1.7890040, 2.3511560],
            [-0.0253747, 0.0065094], [0.1433769, 0.5004745], [0.0593053,
            0.1584829], [-14.1832200, -10.0282800]]]

class Spector():
    """
    Results are from Stata 11
    """
    def __init__(self):
        self.nobs = 32

    def logit(self):
        self.params = [2.82611297201, .0951576702557, 2.37868772835,
                -13.0213483201]
        self.cov_params = [[1.59502033639, -.036920566629, .427615725153,
                -4.57347950298], [-.036920566629, .0200375937069,
                .0149126464275, -.346255757562], [.427615725153 ,
                .0149126464275, 1.13329715236, -2.35916128427],
                [-4.57347950298, -.346255757562, -2.35916128427,
                24.3179625937]]
        self.bse = [1.26294114526, .141554207662, 1.06456430165, 4.93132462871]
        self.llf = -12.8896334653335
        self.llnull = -20.5917296966173
        self.df_model = 3
        self.df_resid = 32 - 4  #TODO: is this right? not reported in stata
        self.llr = 15.4041924625676
        self.prsquared = .374038332124624
        self.llr_pvalue = .00150187761112892
        self.aic = 33.779266930667
        self.bic = 39.642210541866
        self.z = [2.237723415, 0.6722348408, 2.234423721, -2.640537645]
        self.conf_int = [[.3507938,5.301432],[-.1822835,.3725988],[.29218,
                4.465195],[-22.68657,-3.35613]]
        self.pvalues = [.0252390974, .5014342039, .0254552063, .0082774596]
        self.margeff_nodummy_dydx = [.36258084688424,.01220841099085,
                .30517768382304]
        self.margeff_nodummy_dydxmean = [.53385885781692,.01797548988961,
                .44933926079386]
        self.margeff_nodummy_dydxmedian = [.25009492465091,.00842091261329,
                .2105003352955]

        self.margeff_nodummy_dydxzero = [6.252993785e-06,2.105437138e-07,
                5.263030788e-06]
        self.margeff_nodummy_dyex = [1.1774000792198,.27896245178384,
                .16960002159996]
        self.margeff_nodummy_dyexmean = [1.6641381583512,.39433730945339,
                .19658592659731]
        self.margeff_nodummy_dyexmedian = [.76654095836557,.18947053379898,0]
        self.margeff_nodummy_dyexzero = [0,0,0]
        self.margeff_nodummy_eydx = [1.8546366266779,.06244722072812,
                1.5610138123033]
        self.margeff_nodummy_eydxmean = [2.1116143062702,.0710998816585,
                1.7773072368626]
        self.margeff_nodummy_eydxmedian = [2.5488082240624,.0858205793373,
                2.1452853812126]
        self.margeff_nodummy_eydxzero = [2.8261067189993,.0951574597115,
                2.3786824653103]
        self.margeff_nodummy_eyex = [5.4747106798973,1.3173389907576,
                .44600395466634]
        self.margeff_nodummy_eyexmean = [6.5822977203268,1.5597536538833,
                .77757191612739]
        self.margeff_nodummy_eyexmedian = [7.8120973525952,1.9309630350892,0]
        self.margeff_nodummy_eyexzero = [0,0,0]
        # for below GPA = 2.0, psi = 1
        self.margeff_nodummy_atexog1 = [.1456333017086,.00490359933927,
                .12257689308426]
        # for below GPA at mean, tuce = 21, psi = 0
        self.margeff_nodummy_atexog2 = [.25105129214546,.00845311433473,
                .2113052923675]
        self.margeff_dummy_dydx = [.36258084688424,.01220841099085,
                .35751515254729]
        self.margeff_dummy_dydxmean = [.53385885781692,.01797548988961,
                .4564984096959]
#        self.margeff_dummy_dydxmedian
#        self.margeff_dummy_dydxzero
        self.margeff_dummy_eydx = [1.8546366266779,.06244722072812,
                1.5549034398832]
        self.margeff_dummy_eydxmean = [2.1116143062702,.0710998816585,
                1.6631775707188]
#        self.margeff_dummy_eydxmedian
#        self.margeff_dummy_eydxzero
# Factor variables not allowed in below
#        self.margeff_dummy_dyex
#        self.margeff_dummy_dyexmean
#        self.margeff_dummy_dyexmedian
#        self.margeff_dummy_dyexzero
#        self.margeff_dummy_eyex
#        self.margeff_dummy_eyex
#        self.margeff_dummy_eyex
#        self.margeff_dummy_eyex
        # for below GPA = 2.0, psi = 1
        self.margeff_dummy_atexog1 = [.1456333017086,.00490359933927,
                .0494715429937]
        # for below GPA at mean, tuce = 21, psi = 0
        self.margeff_dummy_atexog2 = [.25105129214546,.00845311433473,
                .44265645632553]

    def probit(self):
        self.params = [1.62581025407, .051728948442, 1.42633236818,
                -7.45232041607]
        self.cov_params =    [[.481472955383, -.01891350017, .105439226234,
            -1.1696681354], [-.01891350017, .00703757594, .002471864882,
            -.101172838897], [.105439226234, .002471864882, .354070126802,
            -.594791776765], [-1.1696681354, -.101172838897, -.594791776765,
            6.46416639958]]
        self.bse = [.693882522754, .083890261293, .595037920474, 2.54247249731]
        self.llf = -12.8188033249334
        self.llnull = -20.5917296966173
        self.df_model = 3
        self.df_resid = 32 - 4
        self.llr = 15.5458527433678
        self.prsquared = .377478069409622
        self.llr_pvalue = .00140489496775855
        self.aic = 33.637606649867
        self.bic = 39.500550261066
        self.z = [ 2.343062695, .6166263836, 2.397044489, -2.931131182]
        self.conf_int = [[.2658255,2.985795],[-.1126929,.2161508],[.2600795,
            2.592585],[-12.43547,-2.469166]]
        self.pvalues = [.0191261688, .537481188, .0165279168, .0033773013]

class RandHIE():
    """
    Results obtained from Stata 11
    """
    def __init__(self):
        self.nobs = 20190

    def poisson(self):
        self.params =   [-.052535114675, -.247086797633, .035290201794,
                -.03457750643, .271713973711, .033941474461, -.012635035534,
                .054056326828, .206115121809, .700352877227]
        self.cov_params = None
        self.bse = [.00288398915279, .01061725196728, .00182833684966,
                .00161284852954, .01223913844387, .00056476496963,
                .00925061122826, .01530987068312, .02627928267502,
                .01116266712362]
        self.llf = -62419.588535018
        self.llnull = -66647.181687959
        self.df_model = 9
        self.df_resid = self.nobs - self.df_model - 1
        self.llr = 8455.186305881856
        self.prsquared = .0634324369893758
        self.llr_pvalue = 0
        self.aic = 124859.17707
        self.bic = 124938.306497
        self.z = [-18.21612769, -23.27219872, 19.30180524, -21.43878101,
                22.20041672, 60.09840604, -1.36585953, 3.53081538, 7.84325525,
                62.74063980]
        self.conf_int = [[ -.0581876, -.0468826],[-0.2678962, -0.2262774],
                [0.0317067, 0.0388737],[-0.0377386, -0.0314164],
                [0.2477257, 0.2957022], [0.0328346, 0.0350484],[-0.0307659,
                    0.0054958], [0.0240495, 0.0840631],[0.1546087, 0.2576216],
                [0.6784745, 0.7222313]]
        self.pvalues = [3.84415e-74, 8.4800e-120, 5.18652e-83, 5.8116e-102,
                3.4028e-109, 0, .1719830562, .0004142808, 4.39014e-15, 0]


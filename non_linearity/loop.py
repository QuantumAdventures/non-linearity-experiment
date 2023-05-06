from multiprocessing import Pool
import numpy as np
from tqdm import tqdm
from scipy import signal as sn
from scipy.optimize import curve_fit
import csv
import matplotlib.pyplot as plt
import pdb
processes = 6
M = 60



radius = 75e-3                     # particle radius         micrometers
presure = 1e-3                     # gas pressure            kg/(micrometer*second^2)
m_gas = 2.325e-26                  # nitrogen gas molecule   kg
T = 300.0                            # temperature             Kelvin
kb = 1.38064852e-11                # Boltzmann cst.          picoJoule/Kelvin
v_gas = np.sqrt(3*kb*T/m_gas)      # meam squared velocity of nitrogen gas        micrometers/seconds
gamma = 15.8*radius**2*presure/(v_gas)
rho = 2200*1e-18                   # silica density          kilogram/(micrometers)^3
massa = rho*4*np.pi*radius**3/3    # mass                    kg
n_m = 1.01                         # medium refractive index
n_p = 1.46                         # particle refractive 
m = (n_p/n_m)                      # relative refractive  
NA = 0.7                           # numerical aperture
c = 3e14                           # speed of light          micrometers/seconds
P = 50e9                           # power                   kilogram*micrometers^2/seconds^3
wl0 = 0.78                         # laser wavelength        micrometers
wl_m = wl0/n_m                     # wavelength              micrometers
w0 = wl_m/(np.pi*NA)               # beam waist              micrometers
zr = np.pi*w0**2/wl_m              # railegh range           micrometers
I0 = 2*P/(np.pi*w0**2)             # intensity               Watts/meter^2
V0 = -(2*np.pi*n_m*radius**3/c)*((m**2-1)/(m**2+2))*I0 
                                   # potential depth         picoJoule 
#spring = -2*V0/(zr**2)             # spring constant         microNewtons/micometers
spring = 1.5348106e-6
print(spring)
t_relaxation = gamma/massa         # relaxation time         seconds
t_period =2*np.pi*np.sqrt(massa/spring)

dt = t_period/400                  # numerical integration with 400 points per period 
reduction = 50                    # one useful state point at avery few integration points
f_integration = 1/dt
f_sampling = f_integration/reduction
print(massa)
f_resonance = 1/t_period




x0 = np.sqrt(kb*T/spring)          # length scale
v0 = np.sqrt(kb*T*spring)/gamma
perturbation_ratio = 0.009
ratio = np.linspace(perturbation_ratio,perturbation_ratio,10)


def electric_force(z,perturbation_ratio):
    elec_number = 20.0
    elec_charge = 1.6e-19                        # electron charge
    # perturbation_ratio = 0.005
    charge = elec_number*elec_charge
    E0 = 2*spring*x0*perturbation_ratio/(charge)
    E = E0*(z/x0)**3
    return charge*E


def simulation(period_m=1000, force_on=0, feedback_filter=False, filter_dict={'order': 2, 'low': 99000, 'high': 101000}):
    max_time = period_m*t_period
    N_time = int(max_time/dt)          # size of simulation
    N_simulation = int(N_time/reduction)
    t = np.linspace(0,max_time,int(N_time/reduction))/t_period # time                    seconds

    # state = np.zeros(shape = (N_time,2))
    state = np.zeros(shape= (N_simulation,2))
    filtered_state = np.zeros(shape= (N_simulation,2))

    w = np.sqrt(2.0 * kb * gamma * T * dt ) * np.random.normal(size = N_time)/massa
    v = 0
    x = 0
    printcounter = 0
    b, a = sn.butter(filter_dict['order'], [filter_dict['low'], filter_dict['high']], fs=f_integration, btype='band', analog=False)
    x_window = np.zeros(b.shape)
    y_window = np.zeros((a.shape[0]-1))
    y_i = 0
    for k in range(N_time-1):
        x_window[1:] = x_window[:-1]
        x_window[0]  = x
        y_i = (b*x_window).sum()-(a[1:]*y_window).sum()
        y_window[1:] = y_window[:-1]
        y_window[0] = y_i

        if np.isnan(y_window).any():
            print(y_window, x_window)
            if np.isnan(y_window).all():
                break
        if feedback_filter:
            v = v - (gamma/massa)*v*dt -(spring/massa)*x*dt - force_on*electric_force(y_i,perturbation_ratio)*dt/massa +w[k] # Numerical integration of velocity    
        else:
            v = v - (gamma/massa)*v*dt -(spring/massa)*x*dt - force_on*electric_force(x,perturbation_ratio)*dt/massa +w[k] # Numerical integration of velocity
        x = x +v*dt                                                                                           # numerical integration of position
#        pdb.set_trace()

        
        if (printcounter == reduction):  # Storing less data than used to integrate.
            state[int(k/reduction),1] = v
            state[int(k/reduction),0] = x
            filtered_state[int(k/reduction),0] = y_i
            printcounter = 0
        printcounter += 1
    
    state[:,0] = state[:,0]
    
    return state[:,0], filtered_state[:,0], t





if __name__ == '__main__':
#    freq, pxx = sn.periodogram(simulation(period_m=80000), f_sampling)
    fig = plt.figure()
 #   plt.semilogy(freq[2:], pxx[2:])
    M = 30
    period_m = 10000
    p_xxs = np.zeros((M, 4001))
    for i in tqdm(range(M)):
        states, filtered_state, t = simulation(period_m=1000)
        freq, pxx = sn.periodogram(states, f_sampling)
        p_xxs[i,:] = pxx
    
    plt.semilogy(freq[2:], p_xxs.mean(axis=0)[2:])

    for i in tqdm(range(M)):
        states, _, t = simulation(period_m=1000, force_on=0.9)
        freq, pxx = sn.periodogram(states, f_sampling)
        p_xxs[i,:] = pxx
    plt.semilogy(freq[2:], p_xxs.mean(axis=0)[2:])

    for i in tqdm(range(M)):
        states, filtered_states, t = simulation(period_m=1000, force_on=0.9, feedback_filter=True)
        freq, pxx = sn.periodogram(states, f_sampling)
        p_xxs[i,:] = pxx
    plt.semilogy(freq[2:], p_xxs.mean(axis=0)[2:])
    plt.xlim([6e4, 2e5])
    plt.legend(['No Filter', 'Feedback from x(t)', r'Feedback from $x_F$(t)'])
    plt.show()

#    for i in tqdm(range(M)):
#        states, filtered_states, t = simulation(period_m=1000, force_on=100)
#        freq, pxx = sn.periodogram(filtered_states, f_sampling)
#        p_xxs[i,:] = pxx

#    plt.semilogy(freq[2:], p_xxs.mean(axis=0)[2:])
  #  freq, pxx = sn.periodogram(simulation(period_m=100), f_sampling)
  #  plt.semilogy(freq[2:], pxx[2:])
  #  plt.legend(['N=80000', 'N=1000', 'N=100'])
#    plt.yscale('log')
#    lowcut = 50000.0
#    highcut = 125000.0
#    b, a = sn.butter(3, [lowcut, highcut], fs=f_sampling, btype='band', analog=False)
    

#    fig = plt.figure()
#    plt.plot(t, states)
#    plt.plot(t, filtered_states)
#    plt.plot(t, sn.lfilter(b, a, states))
#    plt.xlim([0, 100])
#    plt.show()
#    p = Pool(processes)
#    print(processes, M)
#    for i in tqdm(range(M)):
#        data = p.map(psd,range(processes))
#        data = np.array(data)
#        storage[i,:,:] = data

    # storage_reshaped = np.reshape(storage,(500,16,psd_stamps))
#    smooth_data = np.mean(storage,axis = 0)
    

#    psd_mean = np.mean(smooth_data,axis = 0)[8000-400:8000+400]
#    psd_std = np.std(smooth_data,axis = 0)[8000-400:8000+400]
#    freq = frequencies(0)[8000-400:8000+400]




    #p0 = [10000,f_resonance,1000]
    #ans, cov = curve_fit(lorentzian,freq,psd_mean, p0 = p0,sigma = psd_std, absolute_sigma=True)
    
    #center_frequency = ans[1]
    #cf_std = np.sqrt(cov[1,1])
    #myCsvRow = [(perturbation_ratio, center_frequency, cf_std)]
    #with open('file.csv', 'a', newline='') as f:
    #    writer = csv.writer(f)
    #    writer.writerows(myCsvRow)
 
    
    
    

    
    

import pyplot_myconf as mc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)


#   1D plot template    

data = np.loadtxt('./out.dat',skiprows=0)



plt.figure(figsize=(8,6))
exts = ['svg']

label = ['$\mathrm{Re}[E_+(g)]$', '$\mathrm{Im}[E_+(g)]$', '$\mathrm{Re}[E_-(g)]$', '$\mathrm{Im}[E_-(g)]$']
plt.plot(data[:,0],data[:,1], linestyle=mc.ls(0),color=mc.lc(0),label=label[0])
plt.plot(data[:,0],data[:,2], linestyle=mc.ls(1),color=mc.lc(0),label=label[1])
plt.plot(data[:,0],data[:,3], linestyle=mc.ls(0),color=mc.lc(1),label=label[2])
plt.plot(data[:,0],data[:,4], linestyle=mc.ls(1),color=mc.lc(1),label=label[3])

mc.set_myfig(title=None,xlabel='$g$',ylabel='$E_\pm$',yscale='linear', xmin=-3.0,xmax=3.0,xticks=1)
plt.legend(frameon=True)
plt.rcParams["legend.fancybox"] = False # 丸角
plt.rcParams["legend.framealpha"] = 0 # 透明度の指定、0で塗りつぶしなし
plt.rcParams["legend.edgecolor"] = 'black' # edgeの色を変更
mc.fig_output(exts,figname='out')
#plt.show()




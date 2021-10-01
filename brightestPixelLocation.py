from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def load_fits(image):
    hdulist = fits.open(image)
    data = hdulist[0].data
    brightest = np.argmax(data)
    index = np.unravel_index(brightest, data.shape)

    
    plt.imshow(data, cmap=plt.cm.plasma)
    plt.xlabel('x-pixels (RA)')
    plt.ylabel('y-pixels (Dec)')
    plt.colorbar()
    plt.plot(index[1],index[0]-5, color='blue',marker = 'v')
    plt.show()

    return index
    
    
   

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dst as DiscreteSineTransform
from sgnFunction import sgn


# ---------------------------------
# constant parameters of the system
# ---------------------------------
# The inverse temperature; we set its value to one for simplicity
beta = 1
# The scale of the random coupling tensor
J = 50
# Number of particles
numOfParticles = 2 ** 15
# Number of the interacting particles
q = 4


# The speed of convergence of the Fourier series of the two point function
x = 1.0 / 2

# the real space__
theta = [np.pi * k / numOfParticles for k in range(numOfParticles + 1)]

# The number of times of iteration loop
iterationLoop = 100


# -------------------------------------------
# Now let's iterate the Schwinger Dyson eq.
# -------------------------------------------

# The initial two point function is the free one.
twoPointFunction = [0.5 * k for k in sgn(theta)]
object = [1j * k for k in twoPointFunction]
transformedTwoPointFunction = DiscreteSineTransform(object, type=3, norm="ortho")

for iteration in range(iterationLoop):
    progress = float(iteration) / iterationLoop * 100
    if progress % 10 == 0.0:
        print("{}% done".format(progress))

    selfEnergy = [J * J * (k ** (q - 1)) for k in twoPointFunction]
    object = [1j * k for k in selfEnergy]
    transformedSelfEnergy = DiscreteSineTransform(object, type=3, norm="ortho")

    nextTransformedTwoPointFunction = []
    for n in range(len(transformedSelfEnergy)):
        # omega = 2 * np.pi * (n + 0.5)
        omega = n + 0.5
        term1 = x / (- 1j * omega - transformedSelfEnergy[n])
        term2 = (1 - x) * transformedTwoPointFunction[n]
        nextTransformedTwoPointFunction.append(term1 + term2)

    transformedTwoPointFunction = nextTransformedTwoPointFunction[:]
    object = [-1j * k for k in transformedTwoPointFunction]
    twoPointFunction = DiscreteSineTransform(object, type=2, norm="ortho")


plt.plot(theta, [k.real for k in twoPointFunction], 'r')
plt.plot(theta, [k.imag for k in twoPointFunction], 'g')
plt.show()

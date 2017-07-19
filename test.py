import communicator as com
import thread
from matplotlib import pyplot as plt





def run():

    bla = com.Communicator(host = "localhost", port = 9999, server = True)

    bla.run()

run()
input()

#~ lines = plt.plot(1,2,4,8)
#~ plt.plot([1, 4], [2, 8], 'k-', lw=2)
#~ line.draw(plt)   
#~ plt.plot([4,2,2,4])
#~ plt.ylabel("garbage")
#~ plt.show()

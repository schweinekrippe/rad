import communicator as com
import thread


def startServer(a1,a2,a3):
    C = com.Communicator(a1,a2,a3)
    return C

#~ C1 = thread.start_new_thread( startServer,("localhost", 9999, True))

C2 = thread.start_new_thread( startServer,("localhost", 9999, False))

input()

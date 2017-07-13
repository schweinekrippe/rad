import communicator as com
import thread


server = com.Communicator()
#~ client = com.Communicator(server = False)

def runserver():
    server.run()

def runclient():
    client.run()

thread.start_new_thread(runserver, ())
#~ thread.start_new_thread(runclient, ())
input()

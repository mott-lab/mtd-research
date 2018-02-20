import random
import heapq
import logging

# network Node structure
class Node:
    links = []
    ip_addr = '0.0.0.0'
    name = 'h' # name is not used yet, but could be useful to simulate DNS migration

    def __init__(self, name, ip_addr):
        self.ip_addr = ip_addr
        self.name = name

    def add_link(self, link):
        self.links.append(link)

    def set_links(self, links):
        self.links = links

    def set_ip(self, ip_addr):
        self.ip_addr = ip_addr

    def set_name(self, name):
        self.name = name

# event structure
class Event:
    start_time = 0
    payload = 'normal' # other value will be 'evil'

    def __init__(self, start_time, payload):
        self.start_time = start_time
        self.payload = payload

# create network nodes and return a list of them
def initState():
    nodes = []

    h1 = Node('h1', '0.0.0.1')
    h2 = Node('h2', '0.0.0.2')
    h3 = Node('h3', '0.0.0.3')
    h4 = Node('h4', '0.0.0.4')
    h5 = Node('h5', '0.0.0.5')

    h1.set_links([2,3,4,5])
    h2.set_links([1,3,4,5])
    h3.set_links([1,2,4,5])
    h4.set_links([1,2,3,5])
    h5.set_links([1,2,3,4])

    nodes.append(h1)
    nodes.append(h2)
    nodes.append(h3)
    nodes.append(h4)
    nodes.append(h5)

    return nodes

# create event queue and return it as a heap queue
def initSchedule():
    schedule = []
    for i in range(0,100):
        if (i % 12 == 0) & (i != 0):        # create an evil event every 12 packets, but not the first one
            event = Event(i, 'evil')
        else:
            event = Event(i, 'normal')
        heapq.heappush(schedule, event)

    return schedule

def main():
    logger = logging.getLogger('net-sim')
    ch = logging.StreamHandler()    # handler for console output
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)

    # start section
    end = False
    states = initState()
    schedule = initSchedule()
    time = 0
    stop_time = len(schedule)

    random.seed(a=1)

    logger.info('INITIAL STATE INFO: ')
    for node in states:
        logger.info(node.name + ': ' + node.ip_addr)

    # loop section
    while end is False:

        event = schedule[0] # top of schedule heap

        if event.payload == 'evil':
            # logic to select host to migrate goes here; right now: random
            h = random.randint(0,4)
            # logic to negotiate new IP address goes here; right now: random
            new_ip = ''
            for i in range(0,4):
                ip_char = random.randint(0,255)
                new_ip += str(ip_char)
                if i < 3:
                    new_ip += '.'

            states[h].set_ip(new_ip) # make the IP address migration
            log_msg = 'AT T=' + str(event.start_time) + ': ' 'Node ' + str(h) + ' IP address set to: ' + new_ip
            logger.warn(log_msg) # separate log_msg for now b/c maybe output it to a file or somewhere else

        prev_time = heapq.heappop(schedule).start_time # pop current event
        if prev_time == stop_time-1:
            end = True
        else:
            next_time = schedule[0].start_time # load next event
            logger.debug('Set next_time to ' + str(next_time))

    # end section
    print 'Event queue finished.'

if __name__ == '__main__':
    main()

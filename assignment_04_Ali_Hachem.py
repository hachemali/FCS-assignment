class Task:
    def __init__(self,__task_id,__descritpion,__priority,__completed):
        self.__task_id=__task_id
        self.__description=__descritpion
        self.__priority=__priority
        self.__completed=__completed
        self.__next=None

    def getTaskId(self):
        return self.__task_id
    
    def setTaskId(self,task_id):
        self.__task_id=task_id
    
    def getDescription(self):
        return self.__description
    
    def setDescription(self,description):
        self.__description=description

    def getPriority(self):
        return self.__priority
    
    def setPriority(self,priority):
        self.__priority=priority

    def getStatus(self):
        return self.__completed
    
    def setStatus(self,status):
        self.__completed=status

    def getNext(self):
        return self.__next
    
    def setNext(self,next):
        self.__next=next

class PriorityQueue:
    def __init__(self):
        self.__header=None
    
    def isEmpty(self):
        return self.__header==None
    
    def enqueue(self,new_Task:Task):
        if (self.isEmpty()):
            self.__header=new_Task
        else:
            current=self.__header
            previous=current
            priority=new_Task.getPriority()
            while(priority<current.getPriority() and current is not None):
                previous=current
                current=current.getNext()
            new_Task.setNext(current)
            previous.setNext(new_Task)
    
    def dequeue(self):
        if (self.isEmpty()):
            return -99
        else:
            current= self.__header
            self.__header=current.getNext()
            current.setNext(None)
            task_id=current.getTaskId()
            current=None
            return task_id
        

    
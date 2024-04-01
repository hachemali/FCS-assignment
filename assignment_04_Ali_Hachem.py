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
            while(current is not None and priority<=current.getPriority() ):
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
        
class Stack:
    def __init__(self):
        self.__header=None

    def push(self,completed_task:Task):
        if self.__header is None:
            self.__header=completed_task
        else:
            completed_task.setNext(self.__header)
            self.__header=completed_task

    def pop(self):
        if self.__header is None:
            return None
        else:
            current=self.__header
            self.__header=current.getNext()
            current.setNext(None) 
            return current

class TaskManager:
    def __init__(self):
       self.task_queue=PriorityQueue()
       self.task_history=Stack()

    def addNewTask(self,new_task:Task):
        self.task_queue.enqueue(new_task)

    def getTask(self,task_id):
        if self.task_queue.__header is None:
            return None
        current=self.task_queue.__header
        if current.getTaskId()==task_id:
            return current
        else:
         while (current is not None and current.getTaskId()!=task_id):
            current=current.getNext()
        return current 
     
    def markCompleted(self):
        if self.task_queue.isEmpty():
            return 
        else:
            current=self.task_queue.__header
            current.setStatus(True)
            self.task_history.push(current)
            self.task_queue.dequeue()
        
    def displayInOrder(self):
        if (self.task_queue.isEmpty()):
            print("empty")

        current = self.task_queue.__header

        while (current is not None):
            print(current.getTaskId(),current.getDescription(), end="")
            current =  current.getNext()

        
    
    def displayNotCompleted(self):
         
        if (self.task_queue.isEmpty()):
            print("empty")

        current = self.task_queue.__header

        while (current is not None):
            if not current.getStatus():
             print(current.getTaskId(),current.getDescription(), end="")
             current =  current.getNext()

    def displayLastCompleted(self):
        if (self.task_history.isEmpty()):
            print ("There is no completed tasks")
        else:
            current=self.task_history.__header
            print(current.getTaskId(),current.getDescription(), end="")
            


       

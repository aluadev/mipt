import threading
import time
from tqdm import tqdm

# train model - stub
def _trainModel():
    time.sleep(3)
    return

# assume we loop 10 times
epochs = 10

# without multithreading
# use with for tqdm to properly shut tqdm down if exception appears
with tqdm(range(epochs)) as epochLoop:
    for _ in epochLoop:
    # trainModel
        _trainModel()

class TrainModel (threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data
    def run(self):
        # return model loss
        self._return = _trainModel()    
    def join(self):
        threading.Thread.join(self)
        return self._return


# with multithreading
# use with for tqdm to properly shut tqdm down if exception appears
with tqdm(range(epochs)) as epochLoop:
    for _ in epochLoop:
        
    # trainModel
        trainThread1 = TrainModel(None)
        trainThread1.start()
        
        trainThread2 = TrainModel(None)
        trainThread2.start()
        
        trainThread3 = TrainModel(None)
        trainThread3.start()
        
        trainThread4 = TrainModel(None)
        trainThread4.start()
    
        trainThread5 = TrainModel(None)
        trainThread5.start()
    # only continue if all threads are done
        modelLoss1 = trainThread1.join()
        modelLoss2 = trainThread2.join()
        modelLoss3 = trainThread3.join()
        modelLoss4 = trainThread4.join()
        modelLoss5 = trainThread5.join()

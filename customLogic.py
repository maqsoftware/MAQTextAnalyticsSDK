
class BatchSetup():

    def __init__(self,data):
        self.data = data
    
    def makeBody(self):
        dataList = []
        dataInput = dict()
        for idx,data in enumerate(self.data):
            dataDict = dict()
            dataDict['id'] = str(idx)
            dataDict['text'] = data
            dataList.append(dataDict)
        dataInput['data'] = dataList
        return dataInput

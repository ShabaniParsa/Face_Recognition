import yaml
import pickle as pkl
import time

cfg = yaml.load(open('config.yaml','r'),Loader=yaml.FullLoader)



def GSADI(name:str,lname:str,id:int,mode:int):
    '''
    G.Give
    S.Student
    A.Add
    D.Data
    I.Info
    '''
    tm = time.localtime()
    year = tm[0]
    month = tm[1]
    day = tm[2]
    hour = tm[3]
    minute = tm[4]
    second = tm[5]
    return {'name':name,'lname':lname,'id':id,'year':year,'month':month,'day':day,'hour':hour,'minute':minute,'second':second,'mode':mode}



class DataBase():
    def __init__(self,):
        global cfg
        self.PKL_PATH = cfg['PATH']['STUDENT_DB_PATH']
        with open(self.PKL_PATH,'rb') as f:
            database = pkl.load(f)
        self.PKL_INF = database
    def get(self):
        with open(self.PKL_PATH,'rb') as f:
            database = pkl.load(f)
        self.PKL_INF = database
        return self.PKL_INF
    def delete(self,id):
        with open(self.PKL_PATH,'rb') as f:
            database = pkl.load(f)
        self.PKL_INF = database
        match_itm = None
        for itm in self.PKL_INF:
            if self.PKL_INF[itm]['id'] == id:
                match_itm = itm
        if match_itm == None:
            raise ValueError('Icant found your id in database.')
        del self.PKL_INF[match_itm]
        with open(self.PKL_PATH,'wb') as f:
            pkl.dump(self.PKL_INF,f)
    def add(self,info):
        self.PKL_INF.setdefault(len(self.PKL_INF),info)
        with open(self.PKL_PATH,'wb') as f:
            pkl.dump(self.PKL_INF,f)
    def getMode(self,id):
        ids = [self.PKL_INF[itm]['id'] for itm in self.PKL_INF]
        if id in ids:
            return ids.count(id) % 2 == 0
        elif ids.count(id) == 0:
            return True
        else:
            raise ValueError('Icant found your id in database.')
    def reset(self):
        with open(self.PKL_PATH,'wb') as f:
            pkl.dump({},f)
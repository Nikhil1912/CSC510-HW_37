from Utils import ProcessCsv

# Holds rows and their summaries in Cols.
class Data:
    def __init__(self, src):
        self.cols = None            #Summaries of data
        self.rows = {}              #Kept data

        if src:
            ProcessCsv.csv(src, self.add)       #If string name do IO on csv file and send pass the add row func
        else:
            for _, row in src:                  #Else given rows so no processing just add
                self.add(row)

    def add(self, xs):
        # Filler code this is TODO
        self.cols = xs



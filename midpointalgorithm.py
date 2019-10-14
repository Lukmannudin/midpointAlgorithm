import matplotlib.pyplot as plt

class Midpoint():
    def __init__(self):
        self.r = 0.0
        self.midCircleCoordinate = []
    
    def setCircleRadius(self, r):
        self.r = r
    
    def setMidCircleCoordinate(self, xc, yc):
       self.midCircleCoordinate = [xc,yc]

    def showCircleCoordinate(self):
        p0 = (5/4)-self.r
        pk = p0
        xk = self.midCircleCoordinate[0]
        yk = self.r

        results = {'k':[], 'Pk':[],'x':[xk],'y':[yk], '2xk':[], '2yk':[]}

        # for x in range(1,20):
        x=0
        while(xk<yk):
            if (pk<0):
                xk = xk + 1
                yk = yk
                pk = pk + (2*xk) + 1
                twotimesxk = 2 * xk
                twotimesyk = 2 * yk
            else:
                xk = xk + 1
                yk = yk - 1
                pk = pk + (2*xk)+1-(2*yk)
                twotimesxk = (2*xk) + 2
                twotimesyk = (2*yk) - 2

            results['k'].append(x)
            results['Pk'].append(pk)
            results['x'].append(xk)
            results['y'].append(yk)
            results['2xk'].append(twotimesxk)
            results['2yk'].append(twotimesyk)
            x = x+1
        
        rangeArray = len(results['k'])

        for x in reversed(range(rangeArray)):
            results['k'].append(len(results['k']))
            results['Pk'].append(results['Pk'][x])
            results['x'].append(results['y'][x])
            results['y'].append(results['x'][x])
            results['2xk'].append(results['2yk'][x])
            results['2yk'].append(results['2xk'][x])
        
        rangeArray = len(results['k'])       

        for x in reversed(range(rangeArray)):
            results['k'].append(len(results['k']))
            results['x'].append(results['x'][x])
            results['y'].append(results['y'][x] * -1)

        for x in range(rangeArray):
            results['k'].append(len(results['k']))
            results['x'].append(results['x'][x] * -1)
            results['y'].append(results['y'][x] * -1)
        
        for x in reversed(range(rangeArray)):
            results['k'].append(len(results['k']))
            results['x'].append(results['x'][x] * -1)
            results['y'].append(results['y'][x])


        for x in results['x']:
            print(results['x'][x], results['y'][x])

        plt.plot(results['x'],results['y'])
        plt.grid(True)
        plt.show()

mid = Midpoint()
mid.setCircleRadius(1000)
mid.setMidCircleCoordinate(0,0)
mid.showCircleCoordinate()


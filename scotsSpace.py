def scotsSpace(v0, runwayLength, cD, timeChange):
    # accuracy of result
    
    # change in time
    tC = timeChange
    # initial velocity
    v = v0
    #starting disance
    x = 0
    #lower range of binary search
    bMin = 0
    #upper range of binary search
    bNoDrag = (v0 ** 2) / (2 * runwayLength)
    bMax = bNoDrag 
    #initial testcase
    bMid = bNoDrag / 2
    iteration = 0
    #set tolerance to 0.000001
    while bMax - bMid >= 0.000001:
       print('Search #', iteration)
       print('Braking coeffecient candidate: ', bMid)
       print('distance traveled', x)
        #initial conditions are set every iteration
       v = v0
       x = 0
       while v > 0:
            print(x)
            #eulers method to simulate distance
            xOld = x
            vOld = v
            aOld = (bMid * -1) - (cD * (vOld ** 2))
            v = vOld + (aOld * tC)
            x = xOld + (vOld * tC)
       
       if x < runwayLength: 
            #if passenger carrier did not reach runwayLength, search range is set to current values of [bMin, bMid]
         bMax = bMid
         bMid = (bMax + bMin) / 2
         
       if x >= runwayLength:
            # if passenger carrier traveled farther than runwayLength, search range is et to current valules of [bMid, bMax]
         bMin = bMid
         bMid = (bMax + bMin) / 2
       iteration = iteration + 1
        # returns optimal braking coeffecient
    return bMid

velocity = float(input('Enter initial velocity: '))
r_length = float(input('Enter runway length: '))
dragco = float(input('Enter drag coeffecient: '))
timechange = float(input('Enter Time change: '))
print('Optimal braking coeffecient:', scotsSpace(velocity, r_length, dragco, timechange))

        
            
            


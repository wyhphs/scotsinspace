![alt text](https://cdn.mos.cms.futurecdn.net/BiH44Z2Wd9PS55wXBuQK8H.jpg)

# SCOTS IN SPACE

open source code published by GMT

## Basic Overview
It’s been 10 years since the first settlement was established on Mars. The Martians want to
encourage their burgeoning tourism industry, so they are installing a runway for a new re-usable
passenger space shuttle. The aerospace engineers have not finalized the design of the shuttle
because the design of the landing gear depends on the length of the runway...and the runway length
has not been finalized because the civil engineers don’t know the distance the shuttle needs to
come to a safe and complete stop!

This program creates a landing scenario program that calculates a passenger
shuttle’s optimal braking coefficient given different system parameters (initial velocity, air braking coefficient, and braking distance).

## Simulating the Shuttle's Motion
To helpthe engineers finalize their designs for the shuttle and the runway length, the program
simulates the distance necessary for the shuttle to stop when given a number of conditions:

● Δt - time increments

● v0 - The initial velocity of the shuttle at the start of the runway.

● b - The braking coefficient (i.e. how hard do we apply the brakes).

● cd- The atmospheric drag coefficient. This is an empirically determined value that depends
on the shape of the shuttle, the drag created by its flaps, and the thickness of the
Marsian atmosphere.The aerospace engineers will test the shuttle design in a wind
tunnel and let you know the proper value (i.e. it's a program input).

![image](https://user-images.githubusercontent.com/119697227/205563444-d893dd22-db8c-4580-a8f0-c24882bd67a5.png)

Both the braking coefficient and the atmospheric drag contribute to the shuttle's acceleration(here
"deceleration", since its negative). Because air resistance increases the faster the shuttle is moving,
the contribution of the drag force depends on the shuttle's currentvelocity, v(t),whichvaries with
time t. The following equation determines a(t), the acceleration of the shuttle at time t:

![image](https://user-images.githubusercontent.com/119697227/205564130-98591f46-0779-4a77-9411-daf81d42ee49.png)

The drag force and consequently
the acceleration, depends on the current velocity.An analytical solution does not exist,requiring
Python and numerical methods to simulate the shuttle's motion approximately.

## Numerical Methods

For this project, Euler’s Method was used to
simulate the motion of the shuttle.The basic approach is to pick a small unit of time(e.g.Δt=
0.00001 seconds) and during that small time, assume constant acceleration and constant velocity
(any object essentially moves in astraight line if you observe fora small period of time).

Update equations are then written for the shuttle's new velocity and new position after a single
Δt has elapsed, based on old acceleration, velocity, and position. The value of the shuttle's previous
acceleration (aold) depends on the shuttle's previous state as described in Equation 1 above.

![image](https://user-images.githubusercontent.com/119697227/205564853-5239b073-5c46-4d5d-a200-98e7f3a8cf75.png)

## Finding the Optimal Brake Coeffecient

The ultimate goal is to determine the optimal braking coefficient,b<sub>optimal</sub>,the minimum braking
coefficient that will safely stop thes huttle before the runway ends.The minimum value is required
since this will ensure the lowest G-forces passengers will endure.Another way to think about it is
when b<sub>optimal</sub> is applied, the shuttle will come to a stop precisely at the end of the runway.

### Binary Search

Instead of a linear search, a more efficient algorithm called a binary search is used. In a
binary search, you systematically guess at the midpoint of the search range and use selection to
test whether the desired value is "higher or lower" than the midpoint. This divides the search space
in half, and may be used iteratively, until you have found the desired value. For example, let's say a
friend asks you to guess a secret number between 0 and 20. Here's the binary search strategy:

![image](https://user-images.githubusercontent.com/119697227/205565654-aee82ab7-d200-4120-9462-4370261eed3b.png)

#### Search Bounds

For the upper bound, we consider the case of no atmospheric air drag. This case would require the greatest braking, since air drag cannot help slow down the shuttle.
b<sub>nodrag</sub> can be solved analytically. 


![image](https://user-images.githubusercontent.com/119697227/205566314-ac06209f-85a8-4c70-b4a8-01d3e7d29f3a.png)

To start the binary search, we will set our initial lower bound  b<sub>min</sub> to 0 and our initial upper bound to b<sub>max</sub> to b<sub>nodrag</sub>
Now, begin the process of repeatedly narrowing the search range. Pick a candidate braking
coefficient using a b value midway between bsub>min</sub> and b<sub>max</sub>. Let's call this midpoint b<sub>mid</sub>. Using this
candidate b value, compute the simulated stopping distance for the shuttle. Comparing this
distance to runwayLength will tell you whether your guess was too high or too low. That is, you know
whether the solution for b<sub>optimal</sub> falls in the range (b<sub>min</sub>, b<sub>mid</sub>) or in the range ( b<sub>mid</sub>, b<sub>max</sub>). Adjust your
lower and upper bounds accordingly and repeat this calculation over and over, each time narrowing
the possible b range until its size is less than some tolerance. That is, stop when:

![image](https://user-images.githubusercontent.com/119697227/205567040-e1aaedda-e1c3-4fd4-8e0a-0ee7a285745a.png)

We have set our tolerance to 0.000001 for six digits of accuracy.

When using a binary search, you say that your algorithm has converged on a solution when the size
of the search space (e.g. the difference between the upper bound and the lower bound) is less than
some specified tolerance. Because of the way we've been narrowing in on the solution, the midpoint
of this range should be quite close to b<sub>optimal</sub>!


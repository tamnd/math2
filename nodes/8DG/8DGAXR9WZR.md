---
tag: 8DGAXR9WZR
kind: concept
name: Karmarkar's algorithm
msc: [90C05, 90C51, 68Q25]
sources:
  - url: https://en.wikipedia.org/wiki/Karmarkar's_algorithm
same_as:
  wikidata: Q2246305
  wikipedia: Karmarkar's algorithm
---

## Summary

Karmarkar's algorithm is a polynomial-time method for [[linear programming|VNMXB0J2KA]], published by Narendra Karmarkar in 1984.
Instead of walking along edges like the [[simplex algorithm|MH272QHWPM]], it moves through the interior of the feasible region.
At each step a projective transformation puts the current point at the centre of a simplex.
Then the method takes a step against the projected gradient of the objective.
It started the field of interior-point methods, which are polynomial like the [[ellipsoid method|TJR5MQHNYE]] and also fast in practice.

## Explanations

### L1 human

Picture the feasible region as a room; the simplex method walks along the walls, from corner to corner.
Karmarkar's method walks through the middle of the room instead.
Near a wall it is hard to take a long step, so before each step it redraws the room so that the current point sits right in the centre.
From the centre it can take a long step downhill, and then it redraws again.
The number of steps grows only polynomially with the size of the problem.

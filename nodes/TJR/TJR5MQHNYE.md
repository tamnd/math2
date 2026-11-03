---
tag: TJR5MQHNYE
kind: concept
name: Ellipsoid method
msc: [90C25, 90C05, 68Q25]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Ellipsoid_method
same_as:
  wikidata: Q378574
  wikipedia: Ellipsoid method
---

## Summary

The ellipsoid method is an iterative [[algorithm|9DMSG5HAQX]] for finding a point in a [[convex set|02AS45T3H9]] of $\R^n$, and hence for convex optimization.
It keeps an ellipsoid that contains the set.
At each step it cuts the ellipsoid in half through its center and replaces it by the smallest ellipsoid containing the correct half.
The volume shrinks by a fixed factor at each step.
So the number of steps is polynomial in $n$ and in the input size.
Applied to [[linear programming|VNMXB0J2KA]], it gave the first polynomial-time algorithm, a result of Khachiyan known as Khachiyan's theorem.

## Explanations

### L1 human

Imagine hunting for a hidden region inside a large egg-shaped search area.
Ask whether the center of the egg lies in the region; if not, an answer tells you which half of the egg the region must lie in.
Draw a new, smaller egg around that half and ask again about its center.
Each new egg has at most a fixed fraction of the volume of the old one.
So after enough steps either the center is in the region or the egg is too small to hold it.
In the plane, one step can shrink the unit disk to an ellipse whose area is about $77\%$ of that of the disk.

---
tag: 4SQYNP0B4Y
kind: concept
name: Nilpotency class
msc: [20F18, 20F14, 20D15]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_group
---

## Summary

The nilpotency class of a nilpotent group is the length of its shortest central series.
It measures how far the group is from being abelian: the trivial group has class $0$ and a nontrivial abelian group has class $1$.
It equals the number of steps that the lower central series, or the upper central series, needs to reach its end.

## Explanations

### L1 human

In an abelian group, all elements commute.
In a nilpotent group, the failure to commute dies out after a fixed number of steps: commutators of commutators of commutators, and so on, become trivial.
The class is that number of steps.
For example, in the quaternion group $Q_8$ every commutator is $\pm 1$, and $\pm 1$ commutes with everything, so $Q_8$ has class $2$.

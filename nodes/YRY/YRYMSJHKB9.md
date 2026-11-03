---
tag: YRYMSJHKB9
kind: example
name: Michell structures
msc: [74P05, 74P15]
illustrates: [E5ZHQSHB97]
sources:
  - url: https://en.wikipedia.org/wiki/Michell_structures
same_as:
  wikidata: Q60790440
  wikipedia: Michell structures
---

## Example

A *Michell structure* is a [[truss|E5ZHQSHB97]], or a limit of trusses with ever more members, of least volume of material.
It must carry given loads to given supports.
Here each member may carry stress of absolute value at most $\sigma > 0$.
A member of length $L$ carrying an axial force $N$ then needs volume $\abs{N} L / \sigma$.
So the task is to minimise $\sum_i \abs{N_i} L_i$ over all trusses in a design region that balance the loads.

Michell's criterion (1904) gives a sufficient condition for optimality.
Suppose there is a continuous virtual displacement field $u$ on the design region, zero at the supports, and a number $\varepsilon_0 > 0$, such that:

1. the axial strain of $u$ along each tension member is $+\varepsilon_0$ and along each compression member is $-\varepsilon_0$;
2. the linear strain of $u$ in every direction at every point of the region has absolute value at most $\varepsilon_0$.

Then the truss has the least volume among all trusses in the region that carry the same loads.
The check uses virtual work.
For any admissible truss, the work $W$ of the loads on $u$ equals $\sum_i N_i \Delta_i$, where $\Delta_i$ is the elongation of member $i$ under $u$.
Clause 2 gives $\abs{\Delta_i} \le \varepsilon_0 L_i$, so $\sum_i \abs{N_i} L_i \ge W / \varepsilon_0$.
Clause 1 gives equality for the given truss.

Simplest instance: a force $P$ at a point $A$, pulling directly away from a fixed support point $O$.
The single straight bar $OA$ is optimal.
The uniform dilatation $u(x) = \varepsilon_0 (x - O)$ proves it, since its strain is $\varepsilon_0$ in every direction.

Michell also found the optimal cantilever for a point load carried to a circular support.
Its members form two families of logarithmic spirals that cross at right angles.

## Explanations

### L1 human

Michell asked how to build the lightest frame of bars that holds a given load.
The answer often looks like a net of curved bars that meet at right angles, some pulled and some pushed.
To prove that such a net is best, one imagines stretching the whole region a little in a special way.
If every bar of the net is stretched or squeezed by the largest allowed amount, and no direction anywhere is stretched more, then no other frame can use less material.
Modern topology optimisation programs often produce shapes close to these Michell nets.

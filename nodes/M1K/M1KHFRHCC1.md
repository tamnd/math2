---
tag: M1KHFRHCC1
kind: counterexample
name: Stokes' paradox
msc: [76D07, 35Q35]
uses: [13CB7V2YM4, QMTKCY36JE, DF0M8YNQ3D, 5632SYFZNF]
sources:
  - url: https://en.wikipedia.org/wiki/Stokes'_paradox
same_as:
  wikidata: Q17106061
  wikipedia: Stokes' paradox
---

## Counterexample

Let $D = \set{x \in \R^2 : \abs{x} \le a}$ be a disk of radius $a > 0$, the cross-section of an infinite circular cylinder, and let $U \ne 0$ be a speed.
Consider the two-dimensional steady [[Stokes equations|13CB7V2YM4]] $\mu \Delta u = \nabla p$, $\nabla \cdot u = 0$ in $\R^2 \setminus D$.
They have no smooth solution $(u, p)$ with
$$u = 0 \text{ on } \abs{x} = a \qquad \text{and} \qquad u(x) \to (U, 0) \text{ as } \abs{x} \to \infty.$$
So slow uniform flow past a cylinder has no Stokes solution in the plane.
For a sphere in three dimensions, the same problem is solvable and gives [[Stokes' law|WW2DTGE881]].

Why: a body that feels a nonzero force $F$ produces at large distances a two-dimensional [[Stokeslet|QMTKCY36JE]], whose velocity grows like $\abs{F} \log \abs{x}$.
One cannot match such a flow both to the [[no-slip condition|DF0M8YNQ3D]] on the cylinder and to a finite uniform stream at infinity.

## Remarks

The paradox shows that the Stokes approximation fails far from the body in two dimensions, however small the Reynolds number.
At a distance of order $\nu / U$ the neglected inertial terms become as large as the viscous ones.
Oseen's linearisation, the [[Oseen equations|5632SYFZNF]], keeps a part of the inertia and does have a solution.
Its drag per unit length depends on the logarithm of the Reynolds number; Lamb computed it in 1911.
Matched asymptotic expansions later explained the structure systematically.

## Explanations

### L1 human

The slow-flow equations work perfectly for a small ball in honey.
For a long rod in honey, the same equations have no answer at all.
The reason is that the disturbance from a rod fades far too slowly, so it never settles into the steady stream far away.
The fix is to keep a little of the fluid's inertia far from the rod.

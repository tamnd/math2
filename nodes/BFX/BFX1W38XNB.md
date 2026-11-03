---
tag: BFX1W38XNB
kind: definition
name: Shear and moment diagram
msc: [74K10, 70C20]
defines: KQPKN2D1R9
uses: [Q6XAPXMGH0, GDM0J9ZCBT]
sources:
  - url: https://en.wikipedia.org/wiki/Shear_and_moment_diagram
---

## Definition

Let a beam occupy $0 \le x \le L$ and carry a distributed transverse load $q(x)$, point forces and point couples, together with its support reactions, in equilibrium.
Let $V(x)$ be the shear force and $M(x)$ the [[bending moment|Q6XAPXMGH0]] at the section $x$.
The *shear diagram* is the graph of $V$ on $[0, L]$, and the *moment diagram* is the graph of $M$ on $[0, L]$.
Between point loads they satisfy
$$\frac{dV}{dx} = -q, \qquad \frac{dM}{dx} = V.$$
At a point force $P$ in the direction of $q$, the function $V$ jumps by $-P$.
At a point couple, $M$ jumps by the value of the couple, with the sign given by the convention.

## Remarks

Example: a simply supported beam with a uniform load $q$ has reactions $qL/2$ at both ends.
Its diagrams are $V(x) = q(L/2 - x)$ and $M(x) = qx(L - x)/2$.
Check: $V' = -q$, $M' = q(L - 2x)/2 = V$, and $M(0) = M(L) = 0$ at the hinged ends.
The moment is largest, $qL^2/8$, at mid-span, where $V = 0$.

Non-example: the deflection curve $w(x)$ of the beam is not a moment diagram.
It depends on the stiffness, while $M$ of a statically determinate beam does not.

A local extremum of $M$ in a span occurs where $V$ changes sign.

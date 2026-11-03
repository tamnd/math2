---
tag: V8RK0F7B5B
kind: statement
role: theorem
name: Parallel axis theorem
msc: ["70E15", "70E17"]
uses: [08ANASGBXV, 0HNK6KT05K, WVGTEH6P10]
about: [08ANASGBXV]
sources:
  - url: https://en.wikipedia.org/wiki/Parallel_axis_theorem
same_as:
  wikidata: Q828284
  wikipedia: Parallel axis theorem
---

## Statement

Let a body of total mass $M > 0$ have [[centre of mass|0HNK6KT05K]] $C$.
Let $\ell_C$ be a line through $C$, and let $\ell$ be a line parallel to $\ell_C$ at distance $d$ from it.
Let $I_C$ and $I_\ell$ be the [[moments of inertia|08ANASGBXV]] of the body about $\ell_C$ and $\ell$.
Then
$$I_\ell = I_C + M d^2.$$

## Remarks

Put $C$ at the origin and let both lines be parallel to the $z$-axis, with $\ell$ through the point $(a, b, 0)$ and $d^2 = a^2 + b^2$.
Then $I_\ell = \int \rho\,\big((x - a)^2 + (y - b)^2\big)\,dV$.
Expanding the squares gives $I_C - 2a \int \rho x \, dV - 2b \int \rho y \, dV + M d^2$, and the two middle integrals vanish because $C$ is the origin.
The hypothesis that $\ell_C$ passes through the centre of mass is needed: for two arbitrary parallel lines the cross terms do not vanish.
In terms of the [[inertia tensor|WVGTEH6P10]], the same computation gives $I_O = I_C + M\big(\abs{c}^2 \mathrm{Id} - c\,c^T\big)$, where $c$ is the vector from $O$ to $C$.

Example: a uniform rod of mass $M$ and length $L$ has moment of inertia $M L^2 / 12$ about the perpendicular line through its midpoint.
About the parallel line through one end, at distance $d = L/2$, the theorem gives $M L^2/12 + M L^2/4 = M L^2 / 3$.

## Explanations

### L1 human

Spinning a body about an axis that misses its centre of mass is harder than spinning it about the parallel axis through the centre of mass.
The extra amount is exactly what a single point carrying all the mass at the centre of mass would add.
So one only needs the moments of inertia about axes through the centre of mass; all the others follow.

### L2 human

The theorem shows that among all parallel axes, the one through the centre of mass has the smallest moment of inertia.
It is used constantly to compute moments of inertia of composite bodies: compute each part about its own centre of mass, then shift.
The tensor form shifts the whole inertia tensor from the centre of mass to any other point.
The same computation splits the kinetic energy of a rigid body into two parts.
One is the energy of the motion of the centre of mass, the other the energy of the rotation about it.

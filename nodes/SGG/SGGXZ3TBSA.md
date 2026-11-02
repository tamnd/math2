---
tag: SGGXZ3TBSA
kind: object
name: Free loop space
msc: [58D15, 55P35, "58E10"]
instance_of: [BW12J14X0Z]
uses: [F45VQ47GPV, 060W5CBZP6, 2JFF5F3EGF, RG15F0TWPW, WWX7H5W1RP]
sources:
  - url: https://en.wikipedia.org/wiki/Free_loop
---

## Description

Let $M$ be a smooth manifold and $S^1 = \R / \Z$ the [[circle|060W5CBZP6]].
The *free loop space* of $M$ is
$$L M = C^\infty(S^1, M),$$
the set of all smooth loops in $M$, with no condition on a base point.
Since $S^1$ is compact, it is a manifold of smooth mappings, which is a Fréchet manifold.
Its tangent space at a loop $\gamma$ is the space of smooth vector fields along $\gamma$, that is, [[sections|WWX7H5W1RP]] of $\gamma^* TM$.

## Remarks


The circle acts on $L M$ by rotating the parameter, $(\theta \cdot \gamma)(t) = \gamma(t + \theta)$, and the fixed points of this action are the constant loops, a copy of $M$.
Evaluation at $0$ is a map $L M \to M$, $\gamma \mapsto \gamma(0)$, whose fibre over $x$ is the smooth based [[loop space|2JFF5F3EGF]] $\Omega_x M$.
For $M = S^1$, a loop has a degree in $\Z$, and the connected components of $L S^1$ correspond to the integers.

In topology one also uses the space $\mathrm{Map}(S^1, X)$ of continuous loops in a space $X$ with the [[compact-open topology|RG15F0TWPW]].
For a manifold $M$, the inclusion of smooth loops into continuous loops is a homotopy equivalence.


## Explanations

### L1 human

A point of the free loop space is a whole closed curve in $M$, which may sit anywhere and need not pass through a chosen point.
Moving a little in this space means wiggling the curve.
Constant curves, which sit still at one point, form a copy of $M$ inside the loop space.
The free loop space is where one looks for closed geodesics, which are the critical points of the energy of a loop.

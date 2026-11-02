---
tag: 4DEGC6JADR
kind: statement
role: theorem
name: Center manifold theorem
msc: [37D10, 34C45]
uses: [F35WJP8VHG, 07BNRFQ0PJ, 0G4X36AE0X, 047NDTEPCV, WWZTW11664, 02903SSA48]
about: [X45STCVFZR]
sources:
  - url: https://en.wikipedia.org/wiki/Center_manifold
---

## Statement

Let $U$ be an open subset of $\R^n$, let $k$ be an integer with $1 \le k < \infty$, and let $f \colon U \to \R^n$ be of class $C^k$.
Let $x_0 \in U$ be an [[equilibrium point|0G4X36AE0X]] of the [[autonomous system|07BNRFQ0PJ]] $x' = f(x)$.
Let $E^c$ be the sum of the generalised eigenspaces of the [[Jacobian matrix|047NDTEPCV]] $Df(x_0)$ for the eigenvalues with real part $0$.
Then $x_0$ has a [[local center manifold|F35WJP8VHG]] $W^c$ of class $C^k$.
That is, $W^c$ is an embedded $C^k$ submanifold of a neighbourhood of $x_0$ that contains $x_0$.
Its tangent space at $x_0$ is $E^c$, and it is locally [[invariant|WWZTW11664]] under the [[flow|02903SSA48]] of $f$.

## Remarks

The usual proof first cuts $f$ off outside a small ball, so that the nonlinear part is globally small in $C^1$.
For the modified equation, a global center manifold is the graph of a map $E^c \to E^s \oplus E^u$.
This map is found as a fixed point of a contraction on a space of functions with controlled growth; this is the Lyapunov–Perron method.
The center manifold need not be unique.
For $x' = x^2$, $y' = -y$, every curve made of $y = c e^{1/x}$ for $x < 0$ and $y = 0$ for $x \ge 0$ is a center manifold of the origin.
The finiteness of $k$ matters.
For a $C^\infty$ system there is a $C^k$ center manifold for each finite $k$, but in general no $C^\infty$ one, and the neighbourhood may shrink as $k$ grows.
If no eigenvalue of $Df(x_0)$ has positive real part, the stability of $x_0$ is the same as for the restriction of the equation to $W^c$.

## Explanations

### L1 human

At a rest point, the linear part of the equation splits the directions into contracting, expanding and neutral ones.
In the contracting and expanding directions the linear part already tells what happens.
The theorem says that the neutral directions bend into a curved invariant surface through the rest point.
All the delicate behaviour happens on this surface, which has fewer dimensions than the whole space.

### L2 human

The theorem is the main tool for studying non-hyperbolic equilibria, where the [[Hartman–Grobman theorem|0S8WX8A4V9]] gives no information.
One computes a Taylor expansion of the center manifold as a graph over $E^c$ by matching coefficients in the invariance equation.
Then one studies the reduced equation on $E^c$, which in a bifurcation is often one- or two-dimensional.
This reduction underlies the normal forms of the saddle-node and Hopf bifurcations.
It complements the [[stable manifold theorem|WF22KK7C3R]], which treats the contracting and expanding directions.

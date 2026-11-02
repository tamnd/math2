---
tag: FVGW1381TZ
kind: statement
role: theorem
name: Gage–Hamilton–Grayson theorem
msc: ["53E10", 53A04]
uses: [DVGFRRYK10, 7JQS6VKFEZ, 02AS45T3H9, 060W5CBZP6]
about: [DVGFRRYK10]
sources:
  - url: https://en.wikipedia.org/wiki/Curve-shortening_flow
---

## Statement

Let $\gamma_0$ be a smooth embedded closed plane curve that encloses area $A_0$.
Then the [[curve-shortening flow|DVGFRRYK10]] with initial curve $\gamma_0$ has a unique smooth solution $(\gamma_t)_{0 \le t < T}$ with $T = A_0 / (2\pi)$, and:

1. each $\gamma_t$ is embedded;
2. there is $t_0 < T$ such that $\gamma_t$ bounds a strictly [[convex|02AS45T3H9]] region for all $t \in [t_0, T)$;
3. as $t \to T$, the curves $\gamma_t$ converge to a point $p$. Rescale $\gamma_t$ by the dilation about $p$ that makes the enclosed area equal to $\pi$. These rescaled curves converge smoothly to the unit [[circle|060W5CBZP6]] centered at $p$.

## Remarks

Gage and Hamilton proved in 1986 that convex curves stay convex and shrink to a round point.
Grayson proved in 1987 that every embedded curve becomes convex before it becomes singular, which reduces the general case to the convex one.
The value of $T$ comes from the identity $A'(t) = -\int_{\gamma_t} \kappa \, ds = -2\pi$ for embedded curves, since the total [[curvature|7JQS6VKFEZ]] of a simple closed curve is $2\pi$.
Embeddedness is needed: an immersed figure-eight curve, or a curve with a small loop, can develop a singularity before it shrinks to a point.

Example: a circle of radius $r_0$ encloses area $\pi r_0^2$ and vanishes at time $r_0^2 / 2 = A_0 / (2\pi)$, in agreement with the formula.

## Explanations

### L1 human

Let a simple closed curve in the plane move by curvature, so sharply bent parts move fastest.
However twisted the curve is at the start, it never crosses itself, it becomes convex, and then it shrinks to a point while looking more and more like a circle.
The time it lives is exactly its area divided by $2\pi$.

### L2 human

The theorem is a model for later results on geometric flows, such as Huisken's theorem on convex hypersurfaces under mean curvature flow and Hamilton's work on Ricci flow.
Grayson's step is the hard part, because it must rule out singularities for nonconvex curves.
Later proofs by Huisken and by Andrews and Bryan compare distances along the curve with distances in the plane.
The flow can also be used to prove geometric inequalities and the existence of closed geodesics on surfaces.

---
tag: 5SDA7ZXT95
kind: statement
role: theorem
name: Milnor conjecture on slice genus of torus knots
msc: [57K10, 57K40]
uses: [NS60VV786W, PW9D9QKAD4]
about: [NS60VV786W]
sources:
  - url: https://en.wikipedia.org/wiki/Torus_knot
---

## Statement

Let $p, q \ge 2$ be coprime integers and let $T(p, q)$ be the [[torus knot|NS60VV786W]] of type $(p, q)$.
For a knot $K \subset S^3 = \partial B^4$, consider the compact oriented surfaces smoothly and properly embedded in $B^4$ with boundary $K$.
The *slice genus* $g_4(K)$ is the least genus of such a surface.
Then
$$g_4(T(p, q)) = u(T(p, q)) = \frac{(p-1)(q-1)}{2},$$
where $u$ is the [[unknotting number|PW9D9QKAD4]].

## Remarks

For any knot, $g_4(K) \le u(K)$: each crossing change can be realized by adding a handle to a surface in $B^4$.
An explicit unknotting shows $u(T(p, q)) \le (p-1)(q-1)/2$.
The hard part is the lower bound $g_4(T(p, q)) \ge (p-1)(q-1)/2$.
Kronheimer and Mrowka proved it in 1993 using gauge theory.
Rasmussen later gave a combinatorial proof with his invariant from [[Khovanov homology|XB24W24B20]].
Example: for the [[trefoil knot|VYTYSVHN4A]] $T(2, 3)$, the formula gives $g_4 = u = 1$.
Milnor asked the question in his study of singular points of complex plane curves, where torus knots appear as links of singularities.

## Explanations

### L1 human

A torus knot is wound on a doughnut, going $p$ times one way and $q$ times the other.
The theorem gives the exact number of crossing changes needed to untie it: $(p-1)(q-1)/2$.
It also says that no surface in the four-dimensional ball bounded by it can have fewer handles than this.
Both quantities are easy to bound from one side and very hard to bound from the other.

### L2 human

The upper bounds are elementary, but lower bounds on the slice genus need deep tools.
Kronheimer and Mrowka obtained the bound from gauge theory, through lower bounds on the genus of embedded surfaces in $4$-manifolds.
Rasmussen's $s$-invariant, the Ozsváth–Szabó $\tau$-invariant from [[knot Floer homology|5P608WRETM]], and the signature give bounds of the form $g_4(K) \ge \abs{s(K)}/2$ and $g_4(K) \ge \abs{\tau(K)}$.
For torus knots, the $s$- and $\tau$-invariants are large enough to give the exact value.

---
tag: S4XMYJ3V42
kind: statement
role: theorem
name: Rankine–Hugoniot conditions
msc: [35L67, 35L65, 76L05]
uses: [8RA7AMWSAF, SJZX81A783]
about: [8RA7AMWSAF]
sources:
  - url: https://en.wikipedia.org/wiki/Rankine–Hugoniot_conditions
same_as:
  wikidata: Q1192131
  wikipedia: Rankine–Hugoniot conditions
---

## Statement

Let $F \colon \R^m \to \R^m$ be a $C^1$ function and consider the system of [[conservation laws|8RA7AMWSAF]] $u_t + F(u)_x = 0$ in one space dimension.
Let $V \subseteq \R \times (0, \infty)$ be open, and let $C = \set{(s(t), t) : t \in I} \subseteq V$ be a curve with $s$ of class $C^1$.
Assume that $C$ splits $V$ into a left part $V_l$ and a right part $V_r$.
Let $u \colon V \to \R^m$ be bounded and of class $C^1$ on $V_l$ and on $V_r$.
Assume that $u$ has one-sided limits $u_l(t)$ from $V_l$ and $u_r(t)$ from $V_r$ at $(s(t), t)$, continuous in $t$.
Then $u$ is a [[weak solution|SJZX81A783]] in $V$ if and only if $u$ solves the equation classically in $V_l$ and in $V_r$, and
$$F(u_l(t)) - F(u_r(t)) = s'(t)\, \big( u_l(t) - u_r(t) \big) \qquad \text{for all } t \in I.$$

## Remarks

Write $[\,\cdot\,]$ for the jump across the curve; then the condition is $[F(u)] = \sigma [u]$ with shock speed $\sigma = s'$.
The proof tests the weak formulation with a test function supported near a point of $C$.
On each side $u$ is a classical solution, so integrating by parts on $V_l$ and on $V_r$ leaves only boundary integrals over $C$.
These combine to $\int_C \big( [F(u)] - s' [u] \big) \varphi \, dt = 0$ for all test functions, which gives the jump condition.

Example: for the scalar [[Burgers' equation|NEGHXN8RE1]], $F(u) = u^2/2$, the condition gives $s' = \dfrac{u_l^2/2 - u_r^2/2}{u_l - u_r} = \dfrac{u_l + u_r}{2}$.
So a jump from $u_l = 2$ to $u_r = 0$ moves at speed $1$.

The conditions are necessary but do not select a unique solution.
A jump from $0$ to $1$ for Burgers' equation also satisfies them and gives a weak solution, but not the physical one.
An entropy condition is needed in addition.
In several space dimensions the same argument gives $\sum_j [F_j(u)]\, \nu_{x_j} = - \nu_t [u]$, where $(\nu_x, \nu_t)$ is a normal to the surface of discontinuity.

## Explanations

### L1 human

When a conserved quantity jumps across a moving front, the front cannot move at any speed it likes.
The amount that piles up at the front per unit time must match the difference of the fluxes on the two sides.
This balance fixes the speed of the front: it equals the jump of the flux divided by the jump of the quantity.
In gas dynamics these are the jump relations for mass, momentum and energy across a shock.

### L2 human

The theorem shows that piecewise smooth weak solutions are exactly the piecewise classical solutions whose jumps obey the Rankine–Hugoniot relations.
It is used to construct explicit solutions, for example of the [[Riemann problem|GJWKX22VVE]], and to check proposed shock solutions.
Since it allows non-physical jumps, it is always combined with an entropy condition such as the Lax condition, which leads to the notion of [[entropy solution|1A01A3EJRX]].
For a system, the set of states $u_r$ that can be joined to a given $u_l$ is the Hugoniot locus.
For a strictly hyperbolic system, near $u_l$ it consists of $m$ curves through $u_l$.

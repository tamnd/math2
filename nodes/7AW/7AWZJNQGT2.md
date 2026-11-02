---
tag: 7AWZJNQGT2
kind: statement
role: theorem
name: Oka–Weil theorem
msc: ["32E30", "32E20"]
uses: [AD3474PVHR, 507C34W0ZT, 07GNX8GCYP, 08VZ57PT26]
about: [AD3474PVHR, 507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Oka%E2%80%93Weil_theorem
same_as:
  wikidata: Q105742287
  wikipedia: Oka–Weil theorem
---

## Statement

Let $K \subseteq \C^n$ be a compact [[polynomially convex set|AD3474PVHR]].
Let $f$ be a [[holomorphic function|507C34W0ZT]] on an open set containing $K$.
Then for every $\varepsilon > 0$ there is a [[polynomial|07GNX8GCYP]] $p$ in $z_1, \dots, z_n$ with $\abs{f(z) - p(z)} < \varepsilon$ for all $z \in K$.
That is, $f$ is a [[uniform limit|08VZ57PT26]] of polynomials on $K$.

## Remarks

The proof first finds polynomials $p_1, \dots, p_N$ such that the polynomial polyhedron $P = \set{z : \abs{z_j} \le R, \ \abs{p_k(z)} \le 1}$ contains $K$ and lies in the open set where $f$ is defined; this uses polynomial convexity of $K$.
The map $z \mapsto (z, p_1(z), \dots, p_N(z))$ embeds a neighbourhood of $P$ as a closed complex submanifold of a polydisc in $\C^{n+N}$.
Oka's extension theorem extends $f$ from this submanifold to a holomorphic function on the polydisc, and the Taylor series of the extension gives polynomials converging to $f$ uniformly on $K$.

Example: for $n = 1$ the theorem is the polynomial case of [[Runge's theorem|6DG4CTGXJD]]: if $\C \setminus K$ is connected, every function holomorphic near $K$ is a uniform limit of polynomials on $K$.

Polynomial convexity cannot be dropped.
On the unit circle $K$, which is not polynomially convex, the function $1/z$ is not a uniform limit of polynomials: polynomials $p$ satisfy $\int_K p(z) \, dz = 0$, while $\int_K z^{-1} \, dz = 2\pi i$.

## Explanations

### L1 human

On a compact set that equals its own polynomial hull, every holomorphic function can be approximated as closely as one likes by polynomials.
This is the several-variable version of Runge's approximation theorem.
The condition on the set rules out holes that would trap functions such as $1/z$.

### L2 human

The theorem is a basic approximation result of several complex variables.
It generalises to holomorphically convex compact subsets of Stein manifolds and of domains of holomorphy, with polynomials replaced by holomorphic functions on the whole domain.
The method of its proof, embedding a polynomial polyhedron into a polydisc, reduces global questions to questions on polydiscs.
It is also used to show that convex domains and balls are Runge domains.

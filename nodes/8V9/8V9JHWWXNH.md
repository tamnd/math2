---
tag: 8V9JHWWXNH
kind: statement
role: theorem
name: Carleson embedding theorem
msc: [30H10, 42B35]
uses: [SQHGJ9C0QE, PNNNFJVF6W, 8G5ABXRK85, DYR1QFNGNJ]
about: [SQHGJ9C0QE, PNNNFJVF6W]
sources:
  - url: https://en.wikipedia.org/wiki/Carleson_measure
---

## Statement

Let $\mathbb{D}$ be the open [[unit disc|8G5ABXRK85]], let $0 < p < \infty$, and let $H^p$ be the [[Hardy space|PNNNFJVF6W]] of $\mathbb{D}$ with norm $\norm{\cdot}_{H^p}$.
Let $\mu$ be a positive [[Borel measure|DYR1QFNGNJ]] on $\mathbb{D}$.
For an arc $I$ of the unit circle, let $\ell(I)$ be its length and $S(I)$ its Carleson box.
Then the following are equivalent:

1. $\mu$ is a [[Carleson measure|SQHGJ9C0QE]], that is, $\mu(S(I)) \le C \ell(I)$ for some $C$ and every arc $I$.
2. There is a constant $C_p$ such that
$$\int_{\mathbb{D}} \abs{f}^p \, d\mu \le C_p \norm{f}_{H^p}^p \quad \text{for all } f \in H^p.$$

## Remarks

To show that 1 implies 2, let $f^*$ be the nontangential maximal function of $f$ on the circle.
For $\lambda > 0$, the open set $\set{f^* > \lambda}$ of the circle is a union of disjoint arcs $I_k$.
Up to a fixed change of aperture, the set $\set{z \in \mathbb{D} : \abs{f(z)} > \lambda}$ is covered by the Carleson boxes over the enlarged arcs $3 I_k$.
Hence $\mu(\set{\abs{f} > \lambda}) \le C \abs{\set{f^* > \lambda}}$, and integrating in $\lambda$ gives $\int \abs{f}^p \, d\mu \le C \norm{f^*}_{L^p}^p \le C' \norm{f}_{H^p}^p$.
To show that 2 implies 1, test the inequality on $f(z) = \left( (1 - \abs{a}^2)/(1 - \bar a z)^2 \right)^{1/p}$ for $a \in \mathbb{D}$, which has $H^p$ norm $1$ and is large on the Carleson box near $a/\abs{a}$ of size $1 - \abs{a}$.

The theorem is due to Carleson, who used it in his solution of the interpolation problem for bounded holomorphic functions and in his proof of the corona theorem.
The condition does not depend on $p$, so a measure that works for one $p$ works for all $p$.

Example: area measure on $\mathbb{D}$ is a Carleson measure, so $\int_{\mathbb{D}} \abs{f}^p \, dA \le C_p \norm{f}_{H^p}^p$, a weak form of the fact that $H^p$ is contained in the Bergman space $A^p$.

## Explanations

### L1 human

A Carleson measure spreads its mass near the boundary circle in a controlled way.
A box of side $\ell$ touching the circle carries at most a constant times $\ell$ of mass.
The theorem says that exactly these measures can be used to measure the size of Hardy space functions inside the disc.
So the boundary behaviour of $f$ controls its size against such measures.

### L2 human

The theorem turns a statement about holomorphic functions into a geometric condition on boxes, which is often easy to check.
Let $(z_k)$ be a sequence of points of $\mathbb{D}$.
The measure $\sum (1 - \abs{z_k}) \delta_{z_k}$ is a Carleson measure exactly when the map $f \mapsto ((1 - \abs{z_k})^{1/p} f(z_k))_k$ is bounded from $H^p$ to $\ell^p$.
This is a key step in interpolation problems.
In the upper half-space of $\R^{n+1}$ the analogous theorem holds for Poisson integrals of $L^p$ functions, $1 < p < \infty$.
Carleson measures are also linked with BMO.
A function $b$ is in BMO exactly when $t \abs{\nabla u(x, t)}^2 \, dx \, dt$ is a Carleson measure, where $u$ is the Poisson integral of $b$.

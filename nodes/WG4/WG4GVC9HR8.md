---
tag: WG4GVC9HR8
kind: statement
role: theorem
name: Unique solvability of Volterra equations of the second kind
msc: [45D05]
uses: [ATPSAHYG7C, 3QDDSSH4FB, ARTJV1XCRX]
about: [ATPSAHYG7C]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Statement

Let $a < b$, let $\Delta = \set{(t, s) : a \le s \le t \le b}$, let $K \colon \Delta \to \C$ be continuous, let $f \colon [a, b] \to \C$ be continuous, and let $\lambda \in \C$.
Then the [[Volterra equation of the second kind|ATPSAHYG7C]]
$$x(t) = f(t) + \lambda \int_a^t K(t, s) \, x(s) \, ds, \quad t \in [a, b],$$
has exactly one continuous solution $x \colon [a, b] \to \C$.
It is $x(t) = f(t) + \lambda \int_a^t R(t, s; \lambda) \, f(s) \, ds$, where $R$ is the [[resolvent kernel|ARTJV1XCRX]] of $K$.

## Remarks

Existence is given by the [[convergence of the Neumann series for Volterra kernels|3QDDSSH4FB]].
For uniqueness, let $y$ be the difference of two continuous solutions; then $y(t) = \lambda \int_a^t K(t, s) \, y(s) \, ds$.
With $M = \max \abs{K}$ and $C = \max \abs{y}$, induction gives $\abs{y(t)} \le C \frac{(\abs{\lambda} M (t - a))^n}{n!}$ for every $n$, so $y = 0$.
In particular, the homogeneous equation has only the zero solution, so a continuous Volterra kernel has no [[characteristic values|DC7HMHVREP]].
Example: $x(t) = \cos t - \int_0^t x(s) \, ds$ has the unique solution $x(t) = \tfrac12 (\cos t - \sin t + e^{-t})$; it solves $x' = -\sin t - x$ with $x(0) = 1$.
The continuity of $K$ can be weakened to boundedness with measurability, or to a weak singularity such as $\abs{K(t, s)} \le C (t - s)^{-\alpha}$ with $0 \le \alpha < 1$, with the same conclusion.
For the equation of the first kind the statement fails: $\int_0^t x(s) \, ds = 1$ has no continuous solution, because the left side vanishes at $t = 0$.

## Explanations

### L1 human

A linear Volterra equation of the second kind with a continuous kernel can always be solved, and in only one way.
This holds for every value of the parameter $\lambda$, with no exceptions.
The reason is that the solution is built forward in time, each value being determined by the earlier ones.

### L2 human

For a Fredholm equation of the second kind, the [[Fredholm alternative|4HH8C9V8JQ]] says that solvability fails exactly at the characteristic values of the kernel.
A Volterra kernel has none, because the Volterra integral operator is quasinilpotent: its spectrum is $\set{0}$.
The theorem covers the integral form of every linear initial value problem $y^{(n)} + a_{n-1}(t) y^{(n-1)} + \cdots + a_0(t) y = g(t)$ with continuous coefficients, and thus gives global existence and uniqueness for those.

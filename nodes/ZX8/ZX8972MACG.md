---
tag: ZX8972MACG
kind: definition
name: A priori estimate
msc: [35B45, 35A01]
defines: 7CT1JTB4JJ
uses: [GC5BDZ6QBC, 06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/A_priori_estimate
---

## Definition

Let $X$ and $Y$ be normed spaces of functions, for example [[Banach spaces|06GZ956657]], and let $\mathcal{F}$ be a class of data $f \in Y$.
Consider a [[partial differential equation|GC5BDZ6QBC]] or boundary value problem $A(u) = f$.
Let $C \colon [0, \infty) \to [0, \infty)$ be a function, often linear, that does not depend on $u$.
An *a priori estimate* for this problem is an inequality $\norm{u}_X \le C(\norm{f}_Y)$.
It must hold for every solution $u \in X$ of $A(u) = f$ with $f \in \mathcal{F}$.
The estimate assumes that $u$ is a solution in $X$; it asserts nothing about the existence of $u$.

## Remarks

Example: let $\Omega \subseteq \R^n$ be bounded and open, $f \in L^2(\Omega)$, and let $u \in H^1_0(\Omega)$ be a weak solution of $-\Delta u = f$.
Testing with $u$ gives $\int_\Omega \abs{\nabla u}^2 = \int_\Omega f u \le \norm{f}_{L^2} \norm{u}_{L^2}$.
By the [[Poincaré inequality|JS2CCR3RNS]], $\norm{u}_{L^2} \le C_P \norm{\nabla u}_{L^2}$, hence $\norm{\nabla u}_{L^2} \le C_P \norm{f}_{L^2}$.
The constant depends only on $\Omega$.

Non-example: a bound $\norm{u}_X \le C(u)$ with a constant that depends on the particular solution is not an a priori estimate.
It gives no uniform control over a family of solutions.

The [[Schauder estimates|HSEKZMAH1V]] and [[Calderón–Zygmund estimates|RYQJH4RYB4]] are a priori estimates in Hölder and $L^p$ norms.
Combined with the Leray–Schauder fixed point method or the method of continuity, a priori estimates yield existence.

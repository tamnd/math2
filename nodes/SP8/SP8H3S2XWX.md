---
tag: SP8H3S2XWX
kind: definition
name: Hasse principle
msc: [11D09, "11E12", 11G05]
defines: EMAR4X3W8D
uses: [BT6T702C28, 08B1RTW7VZ]
sources:
  - url: https://en.wikipedia.org/wiki/Hasse_principle
---

## Definition

For a prime $p$, let $\Q_p$ be the field of [[p-adic numbers|BT6T702C28]], and let $\Q_\infty = \R$.
Let $\mathcal{C}$ be a class of systems of polynomial equations with coefficients in $\Q$.
For a system of homogeneous equations, a solution means a solution other than the zero solution.
Let $V$ be the set of all primes together with the symbol $\infty$.
The class $\mathcal{C}$ *satisfies the Hasse principle* if each system in $\mathcal{C}$ with a solution in $\Q_v$ for every $v \in V$ has a solution in $\Q$.

## Remarks

The converse always holds, since $\Q$ is a subfield of each $\Q_v$.
The same definition makes sense over any number field, with its completions in place of the $\Q_v$.

Example: the class of homogeneous quadratic equations $Q(x_1, \dots, x_n) = 0$, with $Q$ a quadratic form over $\Q$, satisfies the Hasse principle; this is the [[Hasse–Minkowski theorem|R8HCWA981S]].

Non-example: the class of homogeneous cubic equations in three variables does not.
Selmer's equation $3x^3 + 4y^3 + 5z^3 = 0$ has nonzero solutions in $\R$ and in every $\Q_p$, but it has no nonzero solution in $\Q$.

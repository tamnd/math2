---
tag: BWT2AAEK9R
kind: definition
name: q-difference equation
msc: [39A13, 05A30]
defines: FQPYGXJJN0
uses: [PMJT3FZE0Y, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_calculus
---

## Definition

Let $q \in \C$ with $q \ne 0$ and $q \ne 1$, let $n \ge 1$, and let $U \subseteq \C$ be a set with $qU \subseteq U$.
Let $F$ be a given [[function|0EPAT51DXQ]] of $n + 2$ complex variables.
A *$q$-difference equation of order $n$* for an unknown function $y \colon U \to \C$ is a condition
$$F\big(x, y(x), y(qx), \dots, y(q^n x)\big) = 0 \quad \text{for all } x \in U.$$
It is *linear* if it has the form
$$a_n(x) y(q^n x) + \cdots + a_1(x) y(qx) + a_0(x) y(x) = b(x)$$
with given functions $a_0, \dots, a_n, b$ on $U$.

## Remarks

Example: let $0 < \abs{q} < 1$ and $e_q(x) = \sum_{k \ge 0} x^k / [k]_q!$ for $\abs{x} < 1/\abs{1 - q}$, where $[k]_q = (1 - q^k)/(1 - q)$ and $[k]_q! = [1]_q \cdots [k]_q$.
Since the [[q-derivative|PMJT3FZE0Y]] satisfies $D_q x^k = [k]_q x^{k-1}$, one gets $D_q e_q = e_q$.
Written out, this is the first-order linear $q$-difference equation $e_q(qx) = \big(1 + (q - 1)x\big) e_q(x)$.

Non-example: $y(x + 1) = x\, y(x)$, satisfied by the gamma function, relates $y$ at $x$ and at the translate $x + 1$.
It involves no dilate $q^j x$, so it is an ordinary difference equation and not a $q$-difference equation.

The $q$-derivative $D_q y(x) = \big(y(qx) - y(x)\big)/\big((q - 1)x\big)$ lets one rewrite any $q$-difference equation in terms of $D_q, D_q^2, \dots$, as a $q$-analog of a differential equation.
Many authors assume $\abs{q} \ne 1$, or at least that $q$ is not a root of unity.

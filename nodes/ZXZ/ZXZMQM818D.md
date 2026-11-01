---
tag: ZXZMQM818D
kind: statement
role: proposition
name: Transitivity of integrality
msc: [13B21]
uses: [1EHN4KPSFS, B7X0KFY1S1, 05QY1VEBYD]
about: [B7X0KFY1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_element
---

## Statement

Let $A \subseteq B \subseteq C$ be commutative rings.
If $B$ is [[integral|B7X0KFY1S1]] over $A$ and $C$ is integral over $B$, then $C$ is integral over $A$.

## Remarks

Let $c \in C$ and take a monic relation $c^n + b_{n-1} c^{n-1} + \cdots + b_0 = 0$ with $b_i \in B$.
Each $b_i$ is [[integral|1EHN4KPSFS]] over $A$, so $A' = A[b_0, \ldots, b_{n-1}]$ is a [[finitely generated|05QY1VEBYD]] $A$-module.
The relation shows that $A'[c]$ is a finitely generated $A'$-module, so $A'[c]$ is a finitely generated $A$-module.
Hence $c$ is integral over $A$ by the module criterion for integrality.

Example: $\sqrt[4]{2}$ is integral over $\Z[\sqrt{2}]$, as a root of $x^2 - \sqrt{2}$, and $\Z[\sqrt{2}]$ is integral over $\Z$.
So $\sqrt[4]{2}$ is integral over $\Z$; indeed it is a root of $x^4 - 2$.

## Explanations

### L1 human

If each step of a tower of rings only adds roots of monic equations, then the whole tower does too.
This mirrors the fact that an algebraic extension of an algebraic extension of fields is algebraic.

### L2 human

The proof does not build the monic polynomial over $A$ directly; it passes through finite generation of modules.
The same argument shows that the elements of $B$ integral over $A$ form a subring, the [[integral closure|G0V86SJBQW]] of $A$ in $B$.
Transitivity then shows that the integral closure is integrally closed in $B$.

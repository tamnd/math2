---
tag: J6MTQSZVEM
kind: definition
name: Outer regular measure
msc: [28C15]
defines: 33C1KEK3SC
uses: [DYR1QFNGNJ, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Radon_measure
---

## Definition

Let $X$ be a topological space and let $\mu$ be a [[Borel measure|DYR1QFNGNJ]] on $X$.
A Borel set $A \subseteq X$ is *outer regular* for $\mu$ if
$$\mu(A) = \inf \set{\mu(U) : U \supseteq A, \ U \text{ open}}.$$
The measure $\mu$ is *outer regular* if every Borel set is outer regular for $\mu$.

## Remarks

Every [[open set|02BH3MCBQB]] is outer regular, by taking $U = A$.

Example: Lebesgue measure $\lambda$ on the Borel sets of $\R$ is outer regular.
For a Borel set $A$ and $\varepsilon > 0$, the outer measure construction gives intervals $I_k$ covering $A$ with $\sum_k \lambda(I_k) < \lambda(A) + \varepsilon$.
Enlarging each $I_k$ slightly to an open interval gives an open $U \supseteq A$ with $\lambda(U) < \lambda(A) + 2\varepsilon$.

Non-example: counting measure $\mu$ on $\R$ is not outer regular.
The set $\{0\}$ has $\mu(\{0\}) = 1$, but every open set containing $0$ is infinite and has measure $\infty$.

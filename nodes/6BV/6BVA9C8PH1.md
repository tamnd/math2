---
tag: 6BVA9C8PH1
kind: definition
name: Goppa code
msc: [94B05, 11T71]
defines: KJCJSAPV1P
uses: [E85KREWV60, 0ZXZ82FTX2, 0SDC934R52, 0076HWHGHQ, M2X88AXM17]
sources:
  - url: https://en.wikipedia.org/wiki/Binary_Goppa_code
---

## Definition

Let $q$ be a prime power and $m \ge 1$, and let $g \in \F_{q^m}[x]$ be a polynomial of degree $t \ge 1$ over the [[finite field|0ZXZ82FTX2]] $\F_{q^m}$.
Let $L = (\alpha_1, \dots, \alpha_n)$ be distinct elements of $\F_{q^m}$ with $g(\alpha_i) \ne 0$ for all $i$.
For each $i$, let $\frac{1}{x - \alpha_i}$ denote the inverse of $x - \alpha_i$ in the [[quotient ring|0076HWHGHQ]] $\F_{q^m}[x]/(g)$, which exists because $g(\alpha_i) \ne 0$.
The *Goppa code* $\Gamma(L, g)$ is
$$\Gamma(L, g) = \set{c \in \F_q^n : \sum_{i=1}^{n} \frac{c_i}{x - \alpha_i} \equiv 0 \pmod{g(x)}}.$$
It is a *binary Goppa code* when $q = 2$.

## Remarks

The condition is $\F_q$-linear in $c$, so $\Gamma(L, g)$ is a [[linear code|E85KREWV60]] of length $n$.
Writing the condition in a basis of $\F_{q^m}[x]/(g)$ over $\F_q$ gives $mt$ linear equations, so the dimension is at least $n - mt$.
The [[minimum distance|M2X88AXM17]] is at least $t + 1$.
If $q = 2$ and $g$ has no repeated roots in an algebraic closure, then $\Gamma(L, g) = \Gamma(L, g^2)$, and the minimum distance is at least $2t + 1$.

Example: $q = 2$, $m = 3$, $g(x) = x^2 + x + 1$ and $L$ the list of all $8$ elements of $\F_8$.
The roots of $g$ are the primitive cube roots of unity, which lie in $\F_4$ and not in $\F_8$, so $g(\alpha) \ne 0$ for all $\alpha \in \F_8$.
Since $g$ is squarefree, $\Gamma(L, g)$ is a binary code of length $8$, dimension at least $8 - 6 = 2$ and minimum distance at least $5$.

Non-example: if some $\alpha_i$ is a root of $g$, then $x - \alpha_i$ has no inverse modulo $g$, and the defining sum is not defined.

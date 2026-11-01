---
tag: CEK4HKMPB4
kind: definition
name: Formally smooth map
msc: [13B40, 13D10, 14B25]
defines: 8KPDNVKX7B
uses: [0310REJJY8, DPBJ04JMH8, 096Z9MP2ME, 0076HWHGHQ, 0VTH8KPCG2, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Formally_smooth_map
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $A$ be a commutative [[$R$-algebra|DPBJ04JMH8]].
Then $A$ is *formally smooth* over $R$, and the structure map $R \to A$ is a *formally smooth map*, if the following holds.
Let $C$ be a commutative $R$-algebra and let $J \subseteq C$ be an [[ideal|096Z9MP2ME]] with $J^2 = 0$.
Let $\pi \colon C \to C/J$ be the [[quotient map|0076HWHGHQ]], and let $u \colon A \to C/J$ be an $R$-algebra [[homomorphism|0VTH8KPCG2]].
The condition is that for every such $C$, $J$ and $u$ there is an $R$-algebra homomorphism $v \colon A \to C$ with $\pi \circ v = u$.

## Remarks

The lift $v$ need not be unique.
If the lift always exists and is unique, $A$ is *formally étale* over $R$; if it is always unique, $A$ is *formally unramified* over $R$.

Example: let $A = R[x_i : i \in I]$ be a [[polynomial ring|0SDC934R52]] in any set of variables.
Given $u \colon A \to C/J$, choose for each $i$ an element $c_i \in C$ with $\pi(c_i) = u(x_i)$, and let $v$ be the $R$-algebra map with $v(x_i) = c_i$.
Then $\pi \circ v$ and $u$ agree on the variables, so they are equal.

Non-example: let $k$ be a field and $A = k[x]/(x^2)$.
Take $C = k[x]/(x^3)$ and $J = (x^2)/(x^3)$, so $J^2 = 0$ and $C/J = A$, and let $u$ be the identity of $A$.
A lift $v$ would send $x$ to $x + a x^2$ for some $a \in k$, and then $v(x)^2 = x^2 \ne 0$ in $C$, while $v(x^2) = v(0) = 0$.
So no lift exists, and $A$ is not formally smooth over $k$.

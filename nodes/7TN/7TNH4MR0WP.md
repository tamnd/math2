---
tag: 7TNH4MR0WP
kind: definition
name: Distributive property
msc: [08A02]
defines: 63JGSKKF7J
uses: [0M418FE7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Distributive_property
---

## Definition

Let $S$ be a set with two [[binary operations|0M418FE7BB]] $\ast$ and $+$.

1. The operation $\ast$ is *left distributive* over $+$ if $a \ast (b + c) = (a \ast b) + (a \ast c)$ for all $a, b, c \in S$.
2. The operation $\ast$ is *right distributive* over $+$ if $(b + c) \ast a = (b \ast a) + (c \ast a)$ for all $a, b, c \in S$.
3. The operation $\ast$ is *distributive* over $+$ if it is both left and right distributive over $+$.

## Remarks

Example: matrix multiplication on the set of $n \times n$ real matrices is distributive over matrix addition, since $A(B + C) = AB + AC$ and $(B + C)A = BA + CA$ by the entrywise formulas.

Non-example: on the set $\R_{>0}$ of positive reals, take ordinary multiplication $\cdot$ in place of $+$, and let $a \ast b = a^b$.
Then $\ast$ is right distributive over $\cdot$, since $(bc)^a = b^a c^a$.
It is not left distributive, since $2^{1 \cdot 1} = 2$ while $2^1 \cdot 2^1 = 4$.

If $\ast$ is commutative, left and right distributivity are equivalent.
In a ring, multiplication is distributive over addition; in a Boolean algebra, each of $\wedge$ and $\vee$ is distributive over the other.

---
tag: 2XYEC53KNK
kind: definition
name: Bialgebra
msc: [16T10]
defines: Q9HHVN606G
uses: [3CTW1P4HBP, A06RA8KB0T, 0BF2DE2SYK, MNP2HBWB5Q]
sources:
  - url: https://en.wikipedia.org/wiki/Bialgebra
---

## Definition

Let $K$ be a field.
A *bialgebra* over $K$ is a vector space $B$ over $K$ with linear maps $m \colon B \otimes B \to B$, $\eta \colon K \to B$, $\Delta \colon B \to B \otimes B$ and $\varepsilon \colon B \to K$ such that:

1. $(B, m, \eta)$ is an [[associative algebra|3CTW1P4HBP]] with multiplication $m$ and unit $\eta(1)$.
2. $(B, \Delta, \varepsilon)$ is a [[coalgebra|A06RA8KB0T]].
3. $\Delta$ and $\varepsilon$ are algebra homomorphisms, where $B \otimes B$ has the product $(a \otimes b)(c \otimes d) = ac \otimes bd$.

## Remarks

Clause 3 means $\Delta(ab) = \Delta(a)\Delta(b)$, $\Delta(1) = 1 \otimes 1$, $\varepsilon(ab) = \varepsilon(a)\varepsilon(b)$ and $\varepsilon(1) = 1$.
It is equivalent to asking that $m$ and $\eta$ be coalgebra homomorphisms.
Example: the [[group algebra|MNP2HBWB5Q]] $KG$ of a group $G$, with $\Delta(g) = g \otimes g$ and $\varepsilon(g) = 1$ for $g \in G$.
The check of clause 3 on the basis: $\Delta(gh) = gh \otimes gh = (g \otimes g)(h \otimes h) = \Delta(g)\Delta(h)$ and $\varepsilon(gh) = 1 = \varepsilon(g)\varepsilon(h)$.
Non-example: on $K[x]$, the coalgebra with $\Delta(x^n) = \sum_{k=0}^{n} x^k \otimes x^{n-k}$ and $\varepsilon(x^n) = \delta_{n,0}$ fails clause 3.
Indeed $\Delta(x)^2 = (x \otimes 1 + 1 \otimes x)^2 = x^2 \otimes 1 + 2\, x \otimes x + 1 \otimes x^2$, while $\Delta(x^2) = x^2 \otimes 1 + x \otimes x + 1 \otimes x^2$, and $2 \ne 1$ in every field.
With $\Delta(x^n) = \sum_{k} \binom{n}{k} x^k \otimes x^{n-k}$ instead, $K[x]$ is a bialgebra.

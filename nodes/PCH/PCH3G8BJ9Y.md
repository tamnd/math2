---
tag: PCH3G8BJ9Y
kind: definition
name: Multiplicative set
msc: [13B30, 13A99]
defines: AN9SKEZ3VY
uses: [0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplicatively_closed_set
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] with identity $1$.
A subset $S \subseteq R$ is a *multiplicative set* (or *multiplicatively closed set*) if:

1. $1 \in S$;
2. $st \in S$ for all $s, t \in S$.

## Remarks

Example: let $\mathfrak p$ be a [[prime ideal|00MHHZ9SNE]] of $R$ and $S = R \setminus \mathfrak p$.
Then $1 \in S$ because $\mathfrak p$ is a proper ideal.
If $s, t \notin \mathfrak p$, then $st \notin \mathfrak p$ by the definition of a prime ideal, so $st \in S$.

Other examples are the powers $\set{1, f, f^2, \ldots}$ of an element $f \in R$, the [[units|0XVEZDE9J8]] of $R$, and the set of elements of $R$ that are not [[zero divisors|0NNRDW10RZ]].

Non-example: in $\Z$, the set $S = R \setminus 6\Z$ is not multiplicative.
It contains $2$ and $3$ but not $2 \cdot 3 = 6$.
The ideal $6\Z$ is not prime.

Some authors also require $0 \notin S$.
If $0 \in S$, the [[localization|4C1AE84N5N]] $S^{-1}R$ is the zero ring.

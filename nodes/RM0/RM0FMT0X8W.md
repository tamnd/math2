---
tag: RM0FMT0X8W
kind: definition
name: Local homomorphism
msc: [13H99, 13B10]
defines: P8YTMGEN9R
uses: [MZ02BKPHJA, 0VTH8KPCG2, 0XVEZDE9J8]
sources:
  - url: https://en.wikipedia.org/wiki/Local_ring
---

## Definition

Let $(R, \mathfrak m)$ and $(S, \mathfrak n)$ be [[local rings|MZ02BKPHJA]].
A [[ring homomorphism|0VTH8KPCG2]] $f \colon R \to S$ is a *local homomorphism* if $f(\mathfrak m) \subseteq \mathfrak n$.

## Remarks

Equivalent forms:

1. $f^{-1}(\mathfrak n) = \mathfrak m$;
2. for every $a \in R$, if $f(a)$ is a [[unit|0XVEZDE9J8]] of $S$, then $a$ is a unit of $R$.

Indeed $f^{-1}(\mathfrak n)$ is a proper ideal containing $\mathfrak m$ when $f(\mathfrak m) \subseteq \mathfrak n$, so it equals $\mathfrak m$.
A local homomorphism induces a field homomorphism $R/\mathfrak m \to S/\mathfrak n$ of [[residue fields|NJ3APQ8BHH]].

Example: the quotient map $\Z_{(p)} \to \Z/p\Z$ is local, since it sends $p\Z_{(p)}$ to $0$, the maximal ideal of the field $\Z/p\Z$.
For a prime ideal $\mathfrak q \subseteq \mathfrak p$ of a ring $R$, the natural map $R_{\mathfrak p} \to R_{\mathfrak q}$ is local only when $\mathfrak q = \mathfrak p$.

Non-example: the inclusion $\Z_{(p)} \to \Q$ is a ring homomorphism between local rings, but it is not local.
It sends $p \in p\Z_{(p)}$ to $p$, which is a unit of $\Q$ and so not in the maximal ideal $(0)$ of $\Q$.

---
tag: V3ZBMRKC08
kind: statement
role: theorem
name: Regular local rings are domains
msc: [13H05]
uses: [63XXTF6B5M, 0QVD7WBFGN, 8HFAEGFQT1, 1Q1AH2V41S, 0SDC934R52]
about: [63XXTF6B5M, 0QVD7WBFGN]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_local_ring
---

## Statement

Let $(R, \mathfrak m)$ be a [[regular local ring|63XXTF6B5M]].
Then $R$ is an [[integral domain|0QVD7WBFGN]].

## Remarks

Proof idea: let $d = \dim R$ and $k = R/\mathfrak m$.
A regular system of parameters $x_1, \ldots, x_d$ gives a surjection $k[X_1, \ldots, X_d] \to \operatorname{gr}_{\mathfrak m} R = \bigoplus_n \mathfrak m^n / \mathfrak m^{n+1}$ onto the [[associated graded ring|8HFAEGFQT1]].
Comparing dimensions shows that this surjection is an isomorphism, so $\operatorname{gr}_{\mathfrak m} R$ is a [[polynomial ring|0SDC934R52]], hence a domain.
By the [[Krull intersection theorem|1Q1AH2V41S]], $\bigcap_n \mathfrak m^n = 0$, so each nonzero $a \in R$ has an order $n$ with $a \in \mathfrak m^n \setminus \mathfrak m^{n+1}$.
The leading forms of two nonzero elements multiply to a nonzero form, so their product is nonzero.

Example: $k[\![x, y]\!]$ and $\Z_{(p)}[x]_{(p, x)}$ are regular local rings, hence domains.

The hypothesis $\dim R = \operatorname{edim} R$ cannot be dropped.
The Noetherian local ring $R = k[x, y]_{(x, y)}/(xy)$ has dimension $1$ and [[embedding dimension|DP3KSCRKFP]] $2$, and it is not a domain, since $x \cdot y = 0$ with $x, y \ne 0$.

## Explanations

### L1 human

A regular local ring describes a smooth point.
Near a smooth point a space cannot be made of two pieces that cross, so the ring has no zero divisors.
The example $xy = 0$, two lines crossing at the origin, is not smooth at the crossing point, and there $x \cdot y = 0$.

### L2 human

The statement is the first step in the theory of regular local rings.
The stronger theorem that [[regular local rings are UFDs|1HD3EK5392]] uses it together with homological tools such as [[Serre's theorem on regular local rings|93RQRG9R1P]].
It also implies that a regular local ring of dimension $1$ is a [[discrete valuation ring|MGM3CNJW9V]].

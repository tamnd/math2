---
tag: E7XJ3X8RG4
kind: statement
role: proposition
name: Characterizations of discrete valuation rings
msc: [13F30, 13H05]
uses: [MGM3CNJW9V, 0670T59HGE, MZ02BKPHJA, 0QVD7WBFGN, MVGBS3J1P7, H20P600HQS, 0SVYSP8HCG, NJ3APQ8BHH, 63XXTF6B5M]
about: [MGM3CNJW9V]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_valuation_ring
---

## Statement

Let $R$ be a [[Noetherian|0670T59HGE]] [[local|MZ02BKPHJA]] [[integral domain|0QVD7WBFGN]] of [[Krull dimension|MVGBS3J1P7]] $1$, with maximal ideal $\mathfrak{m}$ and [[residue field|NJ3APQ8BHH]] $k = R/\mathfrak{m}$.
The following conditions are equivalent:

1. $R$ is a [[discrete valuation ring|MGM3CNJW9V]].
2. $R$ is [[integrally closed|H20P600HQS]] in its field of fractions.
3. $\mathfrak{m}$ is a [[principal ideal|0SVYSP8HCG]].
4. $\dim_k \mathfrak{m}/\mathfrak{m}^2 = 1$.
5. Every nonzero ideal of $R$ is a power $\mathfrak{m}^n$ with $n \ge 0$.
6. There is $x \in R$ such that every nonzero ideal of $R$ is $(x^n)$ for some $n \ge 0$.

## Remarks

The key step is that 2 implies 3.
Take $a \in \mathfrak{m}$ nonzero; since $\mathfrak{m}$ is the only nonzero prime, some power $\mathfrak{m}^n$ lies in $(a)$; with $n$ minimal one can pick $b \in \mathfrak{m}^{n-1}$ with $b \notin (a)$.
For $y = a/b$, the element $y^{-1}$ is not in $R$, so by integral closedness it is not integral, and then $y^{-1}\mathfrak{m} \not\subseteq \mathfrak{m}$; this forces $y^{-1}\mathfrak{m} = R$, so $\mathfrak{m} = (y)$.
The other implications use Nakayama's lemma and the fact that $\bigcap_n \mathfrak{m}^n = 0$.

Condition 4 says that $R$ is a [[regular local ring|63XXTF6B5M]] of dimension $1$.
Example: the local ring of $k[x, y]/(y - x^2)$ at the origin is a discrete valuation ring, with $\mathfrak{m} = (x)$, since $y = x^2$ there.
The local ring of $k[x, y]/(y^2 - x^3)$ at the origin is not: its maximal ideal $(x, y)$ needs two generators, and $t = y/x$ satisfies $t^2 = x$, so it is not integrally closed.

The hypotheses matter.
Without dimension $1$, the ring $k[\![x, y]\!]$ is a Noetherian integrally closed local domain, but not a discrete valuation ring.
Without the Noetherian condition, a valuation ring with value group $\Q$ is an integrally closed local domain of dimension $1$, but its maximal ideal is not principal.

## Explanations

### L1 human

Discrete valuation rings can be recognised in several ways.
Among the "one-dimensional" local rings, they are exactly the ones without singularity.
"Without singularity" can mean that no fraction is missing which should be there.
It can also mean that the maximal ideal has a single generator, or that all ideals are powers of one ideal.
The theorem says that all these meanings agree.

### L2 human

This result is the local step in the theory of [[Dedekind domains|7NPY2CN5KB]].
A Noetherian domain of dimension $1$ is a Dedekind domain exactly when its localizations at nonzero primes are discrete valuation rings.
In geometry, it says that a point on a curve is nonsingular exactly when the local ring there is integrally closed, which is why normalization resolves the singularities of curves.
Condition 4 links the theory with [[regular local rings|63XXTF6B5M]], which generalise discrete valuation rings to higher dimension.

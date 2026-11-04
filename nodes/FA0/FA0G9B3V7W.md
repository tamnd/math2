---
tag: FA0G9B3V7W
kind: proof
name: Proof of the Dirichlet convolution formula over ordered pairs
msc: [11A25]
proves: 0SAR26CKPS
uses: [0KH1N66QWW, 0FCWA16FZE, 0H2EPRZC0D]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_convolution
    locator: Definition
---

## Proof

1. Let $f$ and $g$ be [[arithmetic functions|0H2EPRZC0D]] and $n$ a positive integer. Let $D$ be the set of [[positive divisors|0FCWA16FZE]] of $n$, and $P$ the set of ordered pairs $(a, b)$ of positive integers with $ab = n$.
2. By the definition of the [[Dirichlet convolution|0KH1N66QWW]], $(f * g)(n) = \sum_{d \in D} f(d) \, g(n/d)$.
3. For $d \in D$, the number $n/d$ is a positive integer and $d \cdot (n/d) = n$. So $\beta(d) = (d, n/d)$ defines a map $\beta : D \to P$.
4. For $(a, b) \in P$, the equation $n = ab$ shows $a \in D$, and $n/a = b$. So $\beta(a) = (a, b)$, and $\beta$ is surjective.
5. If $\beta(d) = \beta(d')$, then the first coordinates give $d = d'$. So $\beta$ is injective, hence a bijection.
6. Reindexing the finite sum of step 2 along $\beta$ gives $(f * g)(n) = \sum_{(a, b) \in P} f(a) \, g(b)$.

## Idea

A divisor $d$ of $n$ and the pair $(d, n/d)$ carry the same information. So summing over divisors is the same as summing over the ordered factorizations $n = ab$.

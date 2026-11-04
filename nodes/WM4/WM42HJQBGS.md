---
tag: WM42HJQBGS
kind: proof
name: Proof of the factor theorem
msc: [13F20]
proves: 0K3MWA7DMC
uses: [0GYGHKX834, 0TEDQH56RW, 00EHX6FWC0, 0125QVNCFQ, 04GNK7K4VP]
sources:
  - url: https://proofwiki.org/wiki/Polynomial_Factor_Theorem
---

## Proof

Let $R$ be a [[commutative ring|0GYGHKX834]], let $f \in R[x]$ and let $c \in R$.

1. Suppose that $x - c$ [[divides|04GNK7K4VP]] $f$ in $R[x]$. Then $f = (x - c) h$ for some $h \in R[x]$.
2. The [[evaluation homomorphism|0125QVNCFQ]] at $c$ is a ring homomorphism. So $f(c) = (c - c) h(c) = 0 \cdot h(c) = 0$.
3. Thus $c$ is a [[root|00EHX6FWC0]] of $f$.
4. Conversely, suppose that $f(c) = 0$. By the [[remainder theorem|0TEDQH56RW]], there is $q \in R[x]$ with $f = (x - c) q + f(c)$.
5. Since $f(c) = 0$, this gives $f = (x - c) q$. So $x - c$ divides $f$ in $R[x]$.

## Idea

The remainder of $f$ on division by $x - c$ is the number $f(c)$. So $x - c$ goes into $f$ exactly when this remainder is zero, that is, when $c$ is a root.

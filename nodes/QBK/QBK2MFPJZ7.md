---
tag: QBK2MFPJZ7
kind: definition
name: Double complex
msc: [18G35]
defines: N80ABTQHEQ
uses: [B2VP96NJSK, WQ82C0M3QB, BZEJKTQ76T, 0NZ8JA25WK]
sources:
  - url: https://en.wikipedia.org/wiki/Double_complex
---

## Definition

Let $\mathcal{A}$ be an [[additive category|B2VP96NJSK]], for example the category of [[modules|0NZ8JA25WK]] over a ring.
A *double complex* in $\mathcal{A}$ consists of objects $C_{p,q}$ for all integers $p, q$ and morphisms
$$d^h_{p,q} \colon C_{p,q} \to C_{p-1,q}, \qquad d^v_{p,q} \colon C_{p,q} \to C_{p,q-1},$$
called the horizontal and vertical differentials, such that:

1. $d^h \circ d^h = 0$;
2. $d^v \circ d^v = 0$;
3. $d^h \circ d^v + d^v \circ d^h = 0$.

Suppose that the needed direct sums exist, for example for modules.
Then the *total complex* is the [[chain complex|WQ82C0M3QB]] with
$$\mathrm{Tot}(C)_n = \bigoplus_{p + q = n} C_{p,q}, \qquad d = d^h + d^v.$$

## Remarks

The three conditions give $d^2 = (d^h)^2 + d^h d^v + d^v d^h + (d^v)^2 = 0$, so the total complex is a complex.
The sums are finite, and exist in any additive category, when only finitely many $C_{p,q}$ with $p + q = n$ are nonzero for each $n$.
Some texts ask instead that the squares commute, $d^h d^v = d^v d^h$, and put the sign into the total complex as $d = d^h + (-1)^p d^v$; the two conventions are equivalent.
Using products instead of direct sums gives a second total complex, which differs when infinitely many terms are nonzero on a diagonal.

Example: for chain complexes $(P_\bullet, d^P)$ and $(Q_\bullet, d^Q)$ of modules over a commutative ring, set $C_{p,q} = P_p \otimes Q_q$, $d^h = d^P \otimes 1$ and $d^v = (-1)^p \, 1 \otimes d^Q$ on $C_{p,q}$.
For $x \in P_p$ and $y \in Q_q$, $d^h d^v (x \otimes y) = (-1)^p\, d^P x \otimes d^Q y$ and $d^v d^h (x \otimes y) = (-1)^{p-1}\, d^P x \otimes d^Q y$, so condition 3 holds.

Non-example: the same data without the sign, $d^v = 1 \otimes d^Q$, fails condition 3 in general, since then $d^h d^v + d^v d^h = 2\, d^P \otimes d^Q$; over $\Z$ with $P = Q = (\Z \xrightarrow{1} \Z)$ this is $2 \ne 0$.

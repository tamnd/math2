---
tag: WSQ8GH8XWZ
kind: definition
name: Henselian ring
msc: [13J15]
defines: RNXPV3KC5J
uses: [MZ02BKPHJA, NJ3APQ8BHH, 0SDC934R52, 0C3QBCR46M]
sources:
  - url: https://en.wikipedia.org/wiki/Henselian_ring
---

## Definition

Let $(R, \mathfrak m)$ be a [[local ring|MZ02BKPHJA]] with [[residue field|NJ3APQ8BHH]] $k = R/\mathfrak m$.
For $f \in R[x]$, write $\bar f \in k[x]$ for the polynomial obtained by reducing the coefficients modulo $\mathfrak m$.
The ring $R$ is *Henselian* if the following holds for every [[monic polynomial|0C3QBCR46M]] $f \in R[x]$.
If $\bar f = g_0 h_0$ with $g_0, h_0 \in k[x]$ monic and coprime, then there are monic $g, h \in R[x]$ with $f = gh$, $\bar g = g_0$ and $\bar h = h_0$.

## Remarks

An equivalent condition: for every monic $f \in R[x]$ and every $a_0 \in k$ with $\bar f(a_0) = 0$ and $\bar f'(a_0) \ne 0$, there is $a \in R$ with $f(a) = 0$ and $a \equiv a_0 \pmod{\mathfrak m}$.
That is, simple roots modulo $\mathfrak m$ lift to roots.

Example: every complete Noetherian local ring is Henselian, by the general form of [[Hensel's lemma|010QVB71T2]]; this includes the $p$-adic integers $\Z_p$ and $k[\![t]\!]$ for a field $k$.
Every field is Henselian, since $\mathfrak m = 0$ and $\bar f = f$.

Non-example: $R = \Z_{(5)}$ is not Henselian.
For $f = x^2 + 1$, one has $\bar f = (x - 2)(x - 3)$ in $\Z/5\Z[x]$, and the factors $x - 2$ and $x - 3$ are coprime because $2 \ne 3$.
A lift would give a root $a \in \Z_{(5)} \subseteq \Q$ of $x^2 + 1$, but $-1$ has no rational square root.

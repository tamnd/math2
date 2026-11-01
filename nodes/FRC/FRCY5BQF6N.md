---
tag: FRCY5BQF6N
kind: statement
role: theorem
name: Kunz's theorem
msc: [13A35, 13H05]
uses: [0670T59HGE, 0F6ES3BRYP, 0T3WVTD675, 73RYYEVDKA, 4C1AE84N5N, 00MHHZ9SNE, 63XXTF6B5M]
about: [0T3WVTD675, 63XXTF6B5M]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_endomorphism
---

## Statement

Let $p$ be a prime and let $R$ be a [[Noetherian ring|0670T59HGE]] of [[characteristic|0F6ES3BRYP]] $p$.
Let $F \colon R \to R$, $F(r) = r^p$, be the [[Frobenius endomorphism|0T3WVTD675]], and view $R$ as an $R$-module through $F$.
Then the following are equivalent:

1. $R$ is a [[flat|73RYYEVDKA]] $R$-module through $F$.
2. $R$ is regular, that is, for every [[prime ideal|00MHHZ9SNE]] $\mathfrak p$ of $R$, the [[localization|4C1AE84N5N]] $R_{\mathfrak p}$ is a [[regular local ring|63XXTF6B5M]].

## Remarks

Both conditions are local, so one may assume that $R$ is local with maximal ideal $\mathfrak m$.
If $R$ is regular, $F$ is a local homomorphism from a regular local ring to a Cohen–Macaulay ring with $\dim R/\mathfrak m^{[p]} = 0$, and such a map is flat ("miracle flatness").
The converse is the deeper direction, and it was the main new point of Kunz's work.

Example: for $R = \F_p[x]$, the image of $F$ is $\F_p[x^p]$.
The ring $R$ is a free module over it with basis $1, x, \ldots, x^{p-1}$, so $F$ is flat, as the theorem predicts for this regular ring.
For $R = \F_p[x, y]/(xy)$, which is not regular at $(x, y)$, the Frobenius map is not flat.

## Explanations

### L1 human

In characteristic $p$, taking $p$-th powers is a ring homomorphism.
Kunz's theorem says that this map is as nice as possible, namely flat, exactly when the ring has no singular points.
So a purely algebraic property of one canonical map detects regularity, the algebraic form of having no singular points.

### L2 human

The theorem is the starting point of the use of Frobenius to study singularities in prime characteristic.
It shows, for instance, that in a regular ring every ideal is tightly closed: from $c x^q \in I^{[q]}$ and flatness one gets $c \in (I^{[q]} : x^q) = (I : x)^{[q]}$, which forces $x \in I$.
Weakening flatness of Frobenius leads to the classes of F-regular, F-rational, F-pure and F-injective rings, see [[tight closure|KJ9MMP99G6]].

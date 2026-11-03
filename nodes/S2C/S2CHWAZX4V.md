---
tag: S2CHWAZX4V
kind: conjecture
name: Birch–Tate conjecture
msc: ["11R70", "11R42", "19F27"]
uses: [4HXFKW55WJ, KXS5DQDFYD, MWBDFS2KJ5, NN77VYSGXR]
about: [4HXFKW55WJ, KXS5DQDFYD]
sources:
  - url: https://en.wikipedia.org/wiki/Birch–Tate_conjecture
same_as:
  wikidata: Q4915794
  wikipedia: Birch–Tate conjecture
history:
  posed_by: Bryan Birch and John Tate
  first_stated: "1970"
---

## Statement

Let $F$ be a totally real [[number field|MWBDFS2KJ5]] with $r_1$ real embeddings and ring of integers $\mathcal{O}_F$, and let $\zeta_F$ be its [[Dedekind zeta function|KXS5DQDFYD]].
Let $w_2(F)$ be the largest integer $N$ such that the Galois group of the [[cyclotomic extension|NN77VYSGXR]] $F(\mu_N)/F$ has exponent dividing $2$.
Then
$$\zeta_F(-1) = (-1)^{r_1} \, \frac{\abs{K_2(\mathcal{O}_F)}}{w_2(F)},$$
where $K_2(\mathcal{O}_F)$ is the second [[K-group|4HXFKW55WJ]] of $\mathcal{O}_F$, a finite group.

## Remarks

Example: for $F = \Q$, $r_1 = 1$, $K_2(\Z) \cong \Z/2$ and $w_2(\Q) = 24$, since $(\Z/24\Z)^\times$ has exponent $2$ and $24$ is the largest such modulus.
The formula gives $-2/24 = -1/12 = \zeta(-1)$, which is correct.

The finiteness of $K_2(\mathcal{O}_F)$ is a theorem of Garland.
The odd part of the conjecture follows from the main conjecture of Iwasawa theory for totally real fields, proved by Wiles.
The deduction also uses work of Tate relating $K_2$ to Galois cohomology.
The conjecture is the case $n = 2$ of [[Lichtenbaum's conjecture on special values|33AYS9Q2PB]].

## Explanations

### L1 human

The value of the Dedekind zeta function of a totally real field at $-1$ is a rational number.
The conjecture says that, up to sign, this number is the size of the group $K_2$ of the ring of integers divided by a simple number $w_2(F)$.
The number $w_2(F)$ comes from roots of unity.
For the rational numbers it recovers $\zeta(-1) = -1/12$ from $\abs{K_2(\Z)} = 2$ and $w_2(\Q) = 24$.
It is an analogue of the class number formula one step higher in K-theory.

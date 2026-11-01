---
tag: BRXX5Y929C
kind: definition
name: Embedding dimension
msc: [13H05, 13H99]
defines: DP3KSCRKFP
uses: [MZ02BKPHJA, 0670T59HGE, Z1CGB483J6, 03GSZ8RTZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_local_ring
---

## Definition

Let $(R, \mathfrak m)$ be a [[Noetherian|0670T59HGE]] [[local ring|MZ02BKPHJA]] with residue field $k = R/\mathfrak m$.
The *embedding dimension* of $R$ is the [[dimension|03GSZ8RTZJ]] of its [[cotangent space|Z1CGB483J6]]:
$$\operatorname{edim} R = \dim_k \mathfrak m / \mathfrak m^2.$$

## Remarks

Since $\mathfrak m$ is finitely generated, [[Nakayama's lemma|15JHBYR6KH]] shows that $\operatorname{edim} R$ is the minimal number of generators of the ideal $\mathfrak m$.
The [[dimension theorem for local rings|KW3HY77V6D]] gives $\dim R \le \operatorname{edim} R$, where $\dim R$ is the [[Krull dimension|MVGBS3J1P7]].
When equality holds, $R$ is a [[regular local ring|63XXTF6B5M]].

Example: for a field $k$, the ring $k[\![x_1, \ldots, x_n]\!]$ has $\mathfrak m = (x_1, \ldots, x_n)$, and the classes of the $x_i$ form a basis of $\mathfrak m/\mathfrak m^2$, so $\operatorname{edim} = n$.
For the cusp $R = k[x, y]_{(x,y)}/(y^2 - x^3)$, one has $\operatorname{edim} R = 2$ but $\dim R = 1$.

Non-example: without the Noetherian hypothesis, $\dim_k \mathfrak m / \mathfrak m^2$ need not count generators of $\mathfrak m$.
In a valuation ring with value group $\Q$, every element of positive value $q$ is a product of two elements of value $q/2$.
So $\mathfrak m = \mathfrak m^2$ and $\mathfrak m / \mathfrak m^2 = 0$, although $\mathfrak m \ne 0$; here $\mathfrak m$ is not finitely generated.

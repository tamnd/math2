---
tag: MHF34RK5ZT
kind: definition
name: Chain map
msc: [18G35]
defines: HTK9WQZJ1G
uses: [WQ82C0M3QB, B2VP96NJSK, 859F0TFVA3]
sources:
  - url: https://en.wikipedia.org/wiki/Chain_complex
---

## Definition

Let $\mathcal{A}$ be an [[additive category|B2VP96NJSK]] and let $(C_\bullet, d^C)$ and $(D_\bullet, d^D)$ be [[chain complexes|WQ82C0M3QB]] in $\mathcal{A}$.
A *chain map* $f \colon C_\bullet \to D_\bullet$ is a family of [[morphisms|859F0TFVA3]] $f_n \colon C_n \to D_n$, one for each integer $n$, such that
$$d^D_n \circ f_n = f_{n-1} \circ d^C_n \quad \text{for all } n \in \Z.$$

## Remarks

Chain maps are composed degreewise, and the identity chain map has $f_n = 1_{C_n}$.
With these, chain complexes in $\mathcal{A}$ form a category, often written $\mathrm{Ch}(\mathcal{A})$.
A chain map sends $\ker d^C_n$ into $\ker d^D_n$ and $\im d^C_{n+1}$ into $\im d^D_{n+1}$.

Example: let $C_\bullet = D_\bullet$ be the complex with $C_1 = C_0 = \Z$, $d_1$ multiplication by $3$, and $C_n = 0$ otherwise.
Then $f_1 = f_0 = $ multiplication by $2$ is a chain map, since $3 \cdot 2x = 2 \cdot 3x$ for $x \in \Z$.

Non-example: in the same complex, take $f_1 = 1_{\Z}$ and $f_0 = 0$.
Then $d_1 \circ f_1$ is multiplication by $3$ but $f_0 \circ d_1 = 0$, so the square in degree $1$ does not commute.

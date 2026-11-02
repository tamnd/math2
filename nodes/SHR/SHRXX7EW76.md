---
tag: SHRXX7EW76
kind: definition
name: Chain homotopy
msc: [18G35, 55U15]
defines: 4EBHAWJJ8C
uses: [WQ82C0M3QB, HTK9WQZJ1G, B2VP96NJSK, 2J4JJJYP22]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_category_of_chain_complexes
---

## Definition

Let $\mathcal{A}$ be an [[additive category|B2VP96NJSK]], let $(C_\bullet, d^C)$ and $(D_\bullet, d^D)$ be [[chain complexes|WQ82C0M3QB]] in $\mathcal{A}$, and let $f, g \colon C_\bullet \to D_\bullet$ be [[chain maps|HTK9WQZJ1G]].
A *chain homotopy* from $f$ to $g$ is a family of morphisms $h_n \colon C_n \to D_{n+1}$, one for each integer $n$, such that
$$f_n - g_n = d^D_{n+1} \circ h_n + h_{n-1} \circ d^C_n \quad \text{for all } n \in \Z.$$
The maps $f$ and $g$ are *chain homotopic*, written $f \simeq g$, if such a family exists.

## Remarks

Chain homotopy is an equivalence relation compatible with composition.
A chain map $f$ is a *chain homotopy equivalence* if there is a chain map $g \colon D_\bullet \to C_\bullet$ with $g \circ f \simeq 1_C$ and $f \circ g \simeq 1_D$.
A complex is *contractible* if its identity is chain homotopic to the zero map.
In an abelian category, chain homotopic maps induce the same morphisms on [[homology|2J4JJJYP22]]: a cycle $z$ is sent by $f - g$ to $d^D h(z)$, which is a boundary.

Example: let $C_\bullet = D_\bullet$ have $C_1 = C_0 = \Z$, $d_1 = 1_{\Z}$, and $C_n = 0$ otherwise; let $f$ be the identity and $g = 0$.
Take $h_0 = 1_{\Z} \colon C_0 \to D_1$ and all other $h_n = 0$.
In degree $0$, $d_1 h_0 + h_{-1} d_0 = 1 + 0 = 1 = f_0 - g_0$; in degree $1$, $d_2 h_1 + h_0 d_1 = 0 + 1 = 1 = f_1 - g_1$.

Non-example: let $C_\bullet = D_\bullet$ be $\Z$ in degree $0$ and $0$ elsewhere.
In degree $0$, the map $h_0$ lands in $D_1 = 0$ and $d^C_0$ lands in $C_{-1} = 0$, so $d_1 h_0 + h_{-1} d_0 = 0$, while $f_0 - g_0 = 1$.
So the identity is not chain homotopic to $0$; indeed it induces the identity of $H_0 = \Z$.

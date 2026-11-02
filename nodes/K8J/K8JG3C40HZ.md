---
tag: K8JG3C40HZ
kind: definition
name: Homotopy category of chain complexes
msc: [18G80, 18G35]
defines: 9Y5Y92R4D5
uses: [B2VP96NJSK, WQ82C0M3QB, HTK9WQZJ1G, 4EBHAWJJ8C, A2DE66937D]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_category_of_chain_complexes
---

## Definition

Let $\mathcal{A}$ be an [[additive category|B2VP96NJSK]].
The *homotopy category of chain complexes* $K(\mathcal{A})$ is the [[category|A2DE66937D]] defined as follows.

1. Its objects are the [[chain complexes|WQ82C0M3QB]] in $\mathcal{A}$.
2. For complexes $C$ and $D$, the morphisms $C \to D$ are the [[chain maps|HTK9WQZJ1G]] $C \to D$ modulo [[chain homotopy|4EBHAWJJ8C]]. Here $f \sim g$ if there are morphisms $s_n \colon C_n \to D_{n+1}$ with $f_n - g_n = d_{n+1} s_n + s_{n-1} d_n$ for all $n$.
3. Composition is induced by the composition of chain maps.

## Remarks

Chain homotopy is an equivalence relation compatible with sums and composition, so $K(\mathcal{A})$ is again additive and composition is well defined.
Example: in $K$ of abelian groups, the complex $C = (0 \to \Z \xrightarrow{\id} \Z \to 0)$, in degrees $1$ and $0$, is isomorphic to $0$, since $s_0 = \id \colon C_0 \to C_1$ gives $\id_C = d s + s d$.
Non-example: the complex $\cdots \to \Z/4\Z \xrightarrow{\cdot 2} \Z/4\Z \xrightarrow{\cdot 2} \Z/4\Z \to \cdots$ is exact, but it is not isomorphic to $0$ in $K$: a contraction would split each short exact sequence $0 \to 2\Z/4\Z \to \Z/4\Z \to 2\Z/4\Z \to 0$, and $\Z/4\Z \not\cong \Z/2\Z \oplus \Z/2\Z$.
If $\mathcal{A}$ is abelian, homology is a functor on $K(\mathcal{A})$.
Bounded variants $K^b(\mathcal{A})$, $K^+(\mathcal{A})$ and $K^-(\mathcal{A})$ use only complexes that are zero in all but finitely many degrees, in low degrees, or in high degrees.

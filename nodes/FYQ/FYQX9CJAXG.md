---
tag: FYQX9CJAXG
kind: definition
name: Ext functor
msc: [13D07, 18G15]
defines: 4P7GBWJ4RR
uses: [0B1261B5ED, 0NZ8JA25WK, HK2AA1YSQ2, BFFA03GE3V]
sources:
  - url: https://en.wikipedia.org/wiki/Ext_functor
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] and let $M$ and $N$ be [[$R$-modules|0NZ8JA25WK]].
Choose a [[projective resolution|HK2AA1YSQ2]] $\cdots \to P_1 \xrightarrow{d_1} P_0 \to M \to 0$ of $M$.
Applying $\Hom_R(-, N)$ to $P_\bullet$ gives a cochain complex
$$0 \to \Hom_R(P_0, N) \xrightarrow{d_1^*} \Hom_R(P_1, N) \xrightarrow{d_2^*} \Hom_R(P_2, N) \to \cdots,$$
where $d_i^*(f) = f \circ d_i$.
For $n \ge 0$, the $n$-th *Ext group* is its cohomology
$$\operatorname{Ext}^n_R(M, N) = \ker d_{n+1}^* / \im d_n^*,$$
with $d_0^* = 0$.

## Remarks

Up to a canonical isomorphism, $\operatorname{Ext}^n_R(M, N)$ does not depend on the choice of the resolution.
One has $\operatorname{Ext}^0_R(M, N) \cong \Hom_R(M, N)$, and the same groups are obtained from an injective resolution of $N$.
If $R$ is commutative, the Ext groups are $R$-modules.
Example: from $0 \to \Z \xrightarrow{\cdot n} \Z \to \Z/n\Z \to 0$ with $n \ge 1$, the complex is $\Z \xrightarrow{\cdot n} \Z$, so $\operatorname{Ext}^0_\Z(\Z/n\Z, \Z) = 0$ and $\operatorname{Ext}^1_\Z(\Z/n\Z, \Z) \cong \Z/n\Z$.
Non-example: the sequence $0 \to \Z/n\Z \xrightarrow{\id} \Z/n\Z \to 0$ is exact but $\Z/n\Z$ is not projective over $\Z$ for $n \ge 2$; using it would give $\operatorname{Ext}^1 = 0$, which is wrong.
A module $M$ is projective if and only if $\operatorname{Ext}^1_R(M, N) = 0$ for all $R$-modules $N$.

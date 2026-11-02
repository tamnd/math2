---
tag: JZAKGD68TY
kind: definition
name: Picard group
msc: [14C22, 14C20]
defines: 3Z9DCWYXQZ
uses: [KNDXDE7K8M, 7JCF2TE3V5, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Picard_group
---

## Definition

Let $(X, \mathcal{O}_X)$ be a [[ringed space|KNDXDE7K8M]].
The *Picard group* $\operatorname{Pic}(X)$ is the set of isomorphism classes of [[invertible sheaves|7JCF2TE3V5]] on $X$, with the operation
$$[\mathcal{L}] \cdot [\mathcal{M}] = [\mathcal{L} \otimes_{\mathcal{O}_X} \mathcal{M}].$$
It is an [[abelian group|082GHNPJ53]] with identity $[\mathcal{O}_X]$ and inverse $[\mathcal{L}]^{-1} = [\mathcal{L}^\vee]$, where $\mathcal{L}^\vee = \mathcal{H}om(\mathcal{L}, \mathcal{O}_X)$.

## Remarks

For a field $k$ and $r \ge 1$, $\operatorname{Pic}(\mathbb{P}^r_k) \cong \Z$, with $n \mapsto [\mathcal{O}(n)]$.
For $X = \operatorname{Spec} A$, $\operatorname{Pic}(X)$ is the [[Picard group of the ring|DZW58R6T2Q]] $A$.
If $A$ is a principal ideal domain, every invertible sheaf on $\operatorname{Spec} A$ is trivial, so $\operatorname{Pic}(\operatorname{Spec} A) = 0$.
There is a natural isomorphism $\operatorname{Pic}(X) \cong H^1(X, \mathcal{O}_X^\times)$ with the first cohomology of the sheaf of units.

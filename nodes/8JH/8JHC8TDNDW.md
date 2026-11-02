---
tag: 8JHC8TDNDW
kind: definition
name: Invertible sheaf
msc: [14C20, 14F06]
defines: 7JCF2TE3V5
uses: [KNDXDE7K8M, S33B2H3MYD]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_sheaf
---

## Definition

Let $(X, \mathcal{O}_X)$ be a [[ringed space|KNDXDE7K8M]].
An *invertible sheaf* on $X$ is a [[sheaf of $\mathcal{O}_X$-modules|S33B2H3MYD]] $\mathcal{L}$ with the following property.
Every point of $X$ has an open neighbourhood $U$ such that $\mathcal{L}|_U \cong \mathcal{O}_X|_U$ as $\mathcal{O}_U$-modules.

## Remarks

The structure sheaf $\mathcal{O}_X$ is invertible, with $U = X$ for every point.
On $X = \mathbb{A}^2_k = \operatorname{Spec} k[x, y]$ over a field $k$, the ideal sheaf $\mathcal{I}$ of the origin, given by the ideal $(x, y)$, is not invertible.
Its stalk at the origin is the maximal ideal of $k[x, y]_{(x, y)}$, which needs two generators, so it is not free of rank $1$.
In other words, an invertible sheaf is a locally free sheaf of rank $1$.
For invertible sheaves $\mathcal{L}$ and $\mathcal{M}$, the tensor product $\mathcal{L} \otimes_{\mathcal{O}_X} \mathcal{M}$ is invertible.
The dual $\mathcal{L}^\vee = \mathcal{H}om(\mathcal{L}, \mathcal{O}_X)$ satisfies $\mathcal{L} \otimes \mathcal{L}^\vee \cong \mathcal{O}_X$, which explains the name.

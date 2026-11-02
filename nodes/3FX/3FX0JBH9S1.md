---
tag: 3FX0JBH9S1
kind: definition
name: Vector bundle
msc: [14F06]
defines: P4DZM975BV
uses: [5A35TYZD02, S33B2H3MYD, KPKND0K7W6]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_sheaf
---

## Definition

Let $X$ be a [[scheme|5A35TYZD02]] and $n \ge 0$ an integer.
A *vector bundle of rank $n$* on $X$ is a [[sheaf of $\mathcal{O}_X$-modules|S33B2H3MYD]] $\mathcal{E}$ with the following property.
Every point of $X$ has an open neighbourhood $U$ such that $\mathcal{E}|_U \cong \mathcal{O}_U^{\oplus n}$ as $\mathcal{O}_U$-modules.
It is also called a *locally free sheaf of rank $n$*.

## Remarks

The free sheaf $\mathcal{O}_X^{\oplus n}$ is a vector bundle of rank $n$, with $U = X$ for every point.
On $\mathbb{A}^1_k = \operatorname{Spec} k[t]$ over a field $k$, the skyscraper sheaf $\widetilde{M}$ with $M = k[t]/(t)$ is not a vector bundle.
Its stalk at the origin is $k$, which is killed by $t$ and so is not a free module over the local ring $k[t]_{(t)}$; its stalks elsewhere are $0$.
A vector bundle is a [[quasi-coherent sheaf|KPKND0K7W6]], and it is coherent when $X$ is locally Noetherian.
To $\mathcal{E}$ corresponds the geometric vector bundle $\mathbb{V}(\mathcal{E}^\vee) = \operatorname{Spec}_X \operatorname{Sym}(\mathcal{E}^\vee)$, whose sheaf of sections is $\mathcal{E}$.
Hartshorne writes $\mathbb{V}(\mathcal{E}) = \operatorname{Spec}_X \operatorname{Sym}(\mathcal{E})$, whose sheaf of sections is $\mathcal{E}^\vee$, so the placement of the dual differs between sources.

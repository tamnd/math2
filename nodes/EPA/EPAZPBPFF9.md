---
tag: EPAZPBPFF9
kind: definition
name: Simplicial set
msc: [18N50, 55U10]
defines: WW81ARB8K9
uses: [FRFYHJGAN3, AND2WHZC8P, WK0A32TZHB]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_set
---

## Definition

Let $\Delta$ be the [[simplex category|FRFYHJGAN3]].
A *simplicial set* is a functor $X \colon \Delta^{\mathrm{op}} \to \mathbf{Set}$, that is, a [[presheaf|AND2WHZC8P]] on $\Delta$.
The elements of $X_n = X([n])$ are the $n$-simplices of $X$.
A map of simplicial sets is a natural transformation.
Thus a simplicial set is a [[simplicial object|WK0A32TZHB]] in the category of sets.

## Remarks

Concretely, a simplicial set is a family of sets $X_n$ with face maps $d_i \colon X_n \to X_{n-1}$ and degeneracy maps $s_i \colon X_n \to X_{n+1}$, $0 \le i \le n$, that satisfy the simplicial identities.
An $n$-simplex is degenerate when it lies in the image of some $s_i$.
Example: the standard $n$-simplex $\Delta^n = \Hom_{\Delta}(-, [n])$ is a representable functor, so it is a simplicial set; its nondegenerate $m$-simplices are the injective order-preserving maps $[m] \to [n]$.
Non-example: a family of sets $X_n$ with only face maps and no degeneracy maps is not a simplicial set; such data form a semi-simplicial set.
The category of simplicial sets is often written $\mathbf{sSet}$.

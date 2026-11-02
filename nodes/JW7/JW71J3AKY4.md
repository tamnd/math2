---
tag: JW71J3AKY4
kind: conjecture
name: Zimmer's conjecture
msc: ["37C85", "57S20", "22E40"]
uses: [BTYF5Y5PFY, 0V9PMN0RBH, F45VQ47GPV, 0KZZ70ZHXP]
about: [BRKPE99MFC]
sources:
  - url: https://en.wikipedia.org/wiki/Zimmer's_conjecture
history:
  posed_by: "Robert Zimmer"
  first_stated: "1986"
---

## Statement

Let $n \ge 3$ and let $\Gamma$ be a [[lattice|BTYF5Y5PFY]] in the [[special linear group|0V9PMN0RBH]] $\mathrm{SL}_n(\R)$, for example $\Gamma = \mathrm{SL}_n(\Z)$.
Let $M$ be a compact [[smooth manifold|F45VQ47GPV]] with $\dim M < n - 1$, and let $\mathrm{Diff}(M)$ be its group of [[diffeomorphisms|0KZZ70ZHXP]].
Then every group homomorphism $\rho \colon \Gamma \to \mathrm{Diff}(M)$ has finite image.

## Remarks

This is the case of $\mathrm{SL}_n(\R)$ of a more general conjecture of Zimmer for lattices in higher-rank simple Lie groups, with a dimension bound depending on the group.
Zimmer stated conjectures of this kind in his 1986 address to the International Congress of Mathematicians, in several versions, some of them only for actions preserving a volume form.
The bound $n - 1$ is sharp: $\mathrm{SL}_n(\Z)$ acts with infinite image on the real projective space of dimension $n - 1$.
Aaron Brown, David Fisher and Sebastián Hurtado proved it, with $C^2$ regularity, for cocompact lattices in $\mathrm{SL}_n(\R)$.
In a paper published in Inventiones Mathematicae in 2020 they proved it for actions by $C^2$ diffeomorphisms of finite-index subgroups of $\mathrm{SL}_n(\Z)$ with $n > 3$.
The general conjecture for lattices in other higher-rank groups is still studied.

## Explanations

### L1 human

The group $\mathrm{SL}_n(\Z)$ of integer matrices with determinant $1$ is a very rigid infinite group when $n \ge 3$.
The conjecture says it cannot act in an interesting way by smooth symmetries on a compact space whose dimension is too small.
Any such action must factor through a finite group.
So a big rigid group needs room to move, and a low-dimensional manifold does not give it enough.

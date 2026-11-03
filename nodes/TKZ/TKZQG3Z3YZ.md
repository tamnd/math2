---
tag: TKZQG3Z3YZ
kind: example
name: Su–Schrieffer–Heeger model
msc: [82D20, 81V70, 47B36]
illustrates: [X66S7EJ1R7]
uses: [57Z8F1Q74B, 0NQSV2EWDR, QP0TK2M29V]
sources:
  - url: https://en.wikipedia.org/wiki/Su%E2%80%93Schrieffer%E2%80%93Heeger_model
same_as:
  wikidata: Q113012911
  wikipedia: Su–Schrieffer–Heeger model
---

## Example

The *Su–Schrieffer–Heeger (SSH) model* is a [[tight-binding|57Z8F1Q74B]] chain with two sites $A$ and $B$ in each unit cell and alternating hopping amplitudes.
Let $v, w \ge 0$ be the hopping inside a cell and between neighbouring cells.
On $\ell^2(\Z; \C^2)$, with $\psi(n) = (\psi_A(n), \psi_B(n))$, the Hamiltonian is
$$(H\psi)_A(n) = v\,\psi_B(n) + w\,\psi_B(n-1), \qquad (H\psi)_B(n) = v\,\psi_A(n) + w\,\psi_A(n+1).$$
Its Bloch Hamiltonian is
$$H(k) = \begin{pmatrix} 0 & h(k) \\ \overline{h(k)} & 0 \end{pmatrix}, \qquad h(k) = v + w e^{-ik}, \quad k \in [-\pi, \pi],$$
so the [[band structure|QP0TK2M29V]] is $E_\pm(k) = \pm\abs{v + w e^{-ik}}$.

Check of the gap: $\abs{v + we^{-ik}}$ ranges over $[\abs{v - w}, v + w]$, so the bands are separated by a gap around $0$ exactly when $v \ne w$.

Check of the topology: $H(k)$ anticommutes with $\sigma_z = \operatorname{diag}(1, -1)$ (chiral symmetry), so when $v \ne w$ the loop $k \mapsto h(k)$ avoids $0$ and has a [[winding number|0NQSV2EWDR]] around $0$.
The circle $v + w e^{-ik}$ has centre $v$ and radius $w$, so the winding number has absolute value $1$ if $w > v$ and is $0$ if $w < v$.

Check of the edge states: take the half-infinite chain $n \ge 1$ with $v = 0$ and $w > 0$.
The site $A$ of the first cell has no partner, since its only bond would go to cell $0$.
So $\psi = \delta_{A,1}$ satisfies $H\psi = 0$, a zero-energy state at the end, as predicted by the nonzero winding number.

## Explanations

### L1 human

The SSH model is a chain of atoms in which the bonds are alternately strong and weak, as in the polyacetylene molecule studied by Su, Schrieffer and Heeger in 1979.
Both ways of alternating give an insulator in the bulk.
They differ in how the chain ends: if the chain ends on a weak bond, a lone atom is left with a state of zero energy at the edge.
The difference is measured by a winding number, which makes the SSH model the simplest example of a [[topological insulator|X66S7EJ1R7]].

---
tag: YZNR1T43KK
kind: example
name: t–J model
msc: [82B20, 82D55, 82D03]
instance_of: [PAEME5EQRM]
uses: [PAEME5EQRM, 3B76W03AN7, 5QG15H8P5J]
sources:
  - url: https://en.wikipedia.org/wiki/T-J_model
same_as:
  wikidata: Q1049381
  wikipedia: T-J model
---

## Example

Let $\Lambda$ be a finite graph with edge set $E$, with fermion operators $c_{j\sigma}$ and $n_j = n_{j\uparrow} + n_{j\downarrow}$.
Let $P$ be the projection onto states with no doubly occupied site.
Let $\mathbf{S}_j = \tfrac12 \sum_{\alpha, \beta} c_{j\alpha}^\dagger \boldsymbol{\sigma}_{\alpha\beta} c_{j\beta}$ be the spin at site $j$, where $\boldsymbol{\sigma}$ is the vector of Pauli matrices.
For $t > 0$ and $J > 0$, the *t–J model* acts on the range of $P$ with Hamiltonian
$$H = -t \sum_{\set{i, j} \in E} \sum_{\sigma} P\big(c_{i\sigma}^\dagger c_{j\sigma} + c_{j\sigma}^\dagger c_{i\sigma}\big)P + J \sum_{\set{i, j} \in E} \Big(\mathbf{S}_i \cdot \mathbf{S}_j - \tfrac14 n_i n_j\Big).$$
Check on two sites with two electrons: the hopping term has no allowed move, so $H = J(\mathbf{S}_1 \cdot \mathbf{S}_2 - \tfrac14)$.
This gives $-J$ for the singlet and $0$ for the triplet.
This agrees with the [[Hubbard model|3B76W03AN7]] on two sites for large $U$, where the singlet lies at about $-4t^2/U$, when $J = 4t^2/U$.

## Remarks

The model is the large-$U$ limit of the Hubbard model, obtained by eliminating doubly occupied states to second order in $t/U$, with $J = 4t^2/U$.
The derivation also produces three-site terms that are usually dropped.
At half filling, with one electron per site, the hopping term vanishes and the model is the antiferromagnetic [[quantum Heisenberg model|5QG15H8P5J]].
Away from half filling it describes holes moving in an antiferromagnetic background.
Zhang and Rice argued in 1988 that the low-energy physics of the copper-oxide planes of cuprate superconductors reduces to this model.
In one dimension it is exactly solvable by the Bethe ansatz at the supersymmetric point $J = 2t$.

## Explanations

### L1 human

The t–J model describes electrons on a lattice that are forbidden from sharing a site.
Electrons can hop to empty neighbouring sites, which gives the term with $t$, and neighbouring spins prefer to point opposite ways, which gives the term with $J$.
When every site is filled, nothing can hop and only the magnetism remains.
Removing some electrons creates holes whose motion fights the magnetic order, and this competition is thought to underlie high-temperature superconductivity.

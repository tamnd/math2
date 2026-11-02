---
tag: WWX8HCN260
kind: statement
role: theorem
name: Wang sequence
msc: [55R20, 55T10]
uses: [PB9JXQ2KC3, T62369RFH6, M0Q5CFJ7ZH, JB7ZBFBA9C, AHW4B5480K, D3BN7MBKTR, 2JFF5F3EGF]
about: [PB9JXQ2KC3, M0Q5CFJ7ZH]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_sequence
---

## Statement

Let $n \ge 2$ and let $p \colon E \to S^n$ be a [[Serre fibration|PB9JXQ2KC3]] over the [[sphere|T62369RFH6]] $S^n$, with fibre $F = p^{-1}(x_0)$ over a point $x_0 \in S^n$.
Then there is a long [[exact sequence|JB7ZBFBA9C]] in integral [[singular homology|M0Q5CFJ7ZH]]
$$\cdots \to H_k(F) \xrightarrow{\ i_*\ } H_k(E) \to H_{k-n}(F) \to H_{k-1}(F) \xrightarrow{\ i_*\ } H_{k-1}(E) \to \cdots,$$
where $i \colon F \to E$ is the inclusion of the fibre.

## Remarks

The base $S^n$ is simply connected because $n \ge 2$, so the [[Serre spectral sequence|AHW4B5480K]] has $E^2_{s,t} = H_s(S^n; H_t(F))$.
This is nonzero only for $s = 0$ and $s = n$, so the only possible differential is $d^n \colon E^n_{n,t} \to E^n_{0,t+n-1}$.
Unfolding this two-column spectral sequence gives the long exact sequence, and the map $H_{k-n}(F) \to H_{k-1}(F)$ is this differential.
A dual sequence holds in cohomology.

Example: the [[path space fibration|D3BN7MBKTR]] $\Omega S^n \to P S^n \to S^n$ has contractible total space, where $\Omega S^n$ is the [[loop space|2JFF5F3EGF]].
Exactness then gives isomorphisms $H_{k-n}(\Omega S^n) \cong H_{k-1}(\Omega S^n)$ for $k \ge 2$.
Since $H_0(\Omega S^n) = \Z$, one gets $H_j(\Omega S^n) \cong \Z$ when $j$ is a multiple of $n - 1$ and $H_j(\Omega S^n) = 0$ otherwise.

## Explanations

### L1 human

A fibration over a sphere is a space that looks locally like a product of a piece of sphere with a fixed fibre, but may be twisted globally.
The Wang sequence links the homology of the total space with the homology of the fibre.
All the twisting is concentrated in a single map from the homology of the fibre to itself, which lowers the degree by $n - 1$.

### L2 human

The Wang sequence is the fibration analogue of the Mayer–Vietoris sequence, obtained by cutting the sphere into two discs.
It is the base-sphere counterpart of the Gysin sequence, which treats fibrations whose fibre is a sphere.
Its classical use is the computation of the homology of loop spaces of spheres, as in the example above.

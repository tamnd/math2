---
tag: 7FFZVT5MEV
kind: definition
name: Cosmological perturbation theory
msc: [83F05, 83C25]
defines: XMH5RQCJYT
uses: [ECJMS4VDTF, 3MCZ97SW6V, REDZ92MKXX, PJWK0PKN6Q, 0KZZ70ZHXP]
sources:
  - url: https://en.wikipedia.org/wiki/Cosmological_perturbation_theory
---

## Definition

Let $a(\eta) > 0$ be the scale factor of a spatially flat [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]] in conformal time $\eta$.
The background metric is
$$\bar g = a(\eta)^2 \left( -d\eta^2 + \delta_{ij}\, dx^i dx^j \right),$$
with indices $i, j \in \set{1, 2, 3}$.
Let $\bar T$ be a background [[stress–energy tensor|REDZ92MKXX]] that solves the [[Einstein field equations|3MCZ97SW6V]] with $\bar g$.
*Linear cosmological perturbation theory* studies metrics $g = \bar g + \delta g$ and stress–energy tensors $T = \bar T + \delta T$ with small $\delta g$ and $\delta T$.
It requires the Einstein field equations to hold to first order in $\delta g$ and $\delta T$.
The perturbed metric is written as
$$ds^2 = a^2 \left[ -(1 + 2A)\, d\eta^2 + 2 B_i\, dx^i d\eta + \left( \delta_{ij} + h_{ij} \right) dx^i dx^j \right],$$
where $A$, $B_i$ and $h_{ij} = h_{ji}$ are functions of $(\eta, x)$ treated to first order.
They are split into scalar, vector and tensor parts with respect to rotations of the spatial slices:

1. $B_i = \partial_i B + S_i$ with $\partial_i S_i = 0$.
2. $h_{ij} = -2\psi\, \delta_{ij} + 2\, \partial_i \partial_j E + \partial_i F_j + \partial_j F_i + h^{T}_{ij}$, with summation over repeated indices.
   The conditions are $\partial_i F_i = 0$, $h^{T}_{ii} = 0$ and $\partial_i h^{T}_{ij} = 0$.

Here $A, B, \psi, E$ are scalar perturbations, $S_i, F_i$ are vector perturbations, and $h^{T}_{ij}$ is the tensor perturbation.
A change of coordinates $x^\mu \mapsto x^\mu + \xi^\mu$ with small $\xi$ changes $\delta g$ by the [[Lie derivative|PJWK0PKN6Q]] $\mathcal{L}_\xi \bar g$, up to a sign fixed by convention.
It changes $\delta T$ by $\mathcal{L}_\xi \bar T$ in the same way.
This freedom is called the *gauge freedom*.

## Remarks

At first order the scalar, vector and tensor parts satisfy separate equations, so each part can be studied on its own.
The count of functions is $4$ scalars, $2 + 2$ components of the two divergence-free vectors, and $2$ components of $h^T_{ij}$, which gives the $10$ components of a symmetric $4 \times 4$ metric perturbation.
Example: the *Newtonian gauge* sets $B = E = 0$; with no vector and tensor parts, the metric becomes $a^2[-(1 + 2\Psi)\, d\eta^2 + (1 - 2\Phi)\, \delta_{ij} dx^i dx^j]$, where $\Psi = A$ and $\Phi = \psi$ play the role of Newtonian potentials.
Non-example: for a small vector field $\xi$, the perturbation $\delta g = \mathcal{L}_\xi \bar g$ is not physical, since a [[diffeomorphism|0KZZ70ZHXP]] removes it.
This is why one uses gauge-invariant combinations, such as the Bardeen potentials.
Second-order and higher perturbation theory keep the higher terms in $\delta g$ and $\delta T$.

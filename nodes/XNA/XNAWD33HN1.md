---
tag: XNAWD33HN1
kind: example
name: Torus as a group
msc: [22B05, "22E15"]
instance_of: [ZR09S9R3AW]
uses: [04EAFVFTF7, 03NM7DZXXC, FMW57WNPDB]
sources:
  - url: https://en.wikipedia.org/wiki/Torus
---

## Example

Let $n \ge 1$ and let $\mathbb{T} = \set{z \in \C : \abs{z} = 1}$ be the [[circle group|04EAFVFTF7]].
The *$n$-torus* is the product group $\mathbb{T}^n$ with coordinatewise multiplication and the product topology.
It is a [[locally compact abelian group|ZR09S9R3AW]].
It is abelian because $\mathbb{T}$ is, Hausdorff as a subspace of $\C^n$, and compact as a closed bounded subset of $\C^n$.
The map $(t_1, \dots, t_n) \mapsto (e^{2\pi i t_1}, \dots, e^{2\pi i t_n})$ is a continuous surjective homomorphism $\R^n \to \mathbb{T}^n$ with kernel $\Z^n$, and it induces an isomorphism of topological groups $\R^n / \Z^n \cong \mathbb{T}^n$.

## Remarks

As a topological space, $\mathbb{T}^2$ is the [[torus|03NM7DZXXC]] surface; the group structure is the extra data.
The torus $\mathbb{T}^n$ is a compact connected abelian Lie group of dimension $n$, and every compact connected abelian Lie group is isomorphic to some $\mathbb{T}^n$.
Its [[Pontryagin dual|FMW57WNPDB]] is $\Z^n$: the continuous characters are $(z_1, \dots, z_n) \mapsto z_1^{k_1} \cdots z_n^{k_n}$ with $(k_1, \dots, k_n) \in \Z^n$.
Fourier analysis on $\mathbb{T}^n$ is the theory of multiple Fourier series.

## Explanations

### L1 human

The $n$-torus is a list of $n$ angles, where one adds angles in each slot and forgets full turns.
For $n = 2$ the two angles locate a point on the surface of a doughnut: one goes around the hole, the other around the tube.
Adding angles slides points along the surface, so the doughnut surface becomes a group.

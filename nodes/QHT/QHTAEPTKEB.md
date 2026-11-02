---
tag: QHTAEPTKEB
kind: object
name: Hurwitz quaternions
msc: [11R52, 16H10]
instance_of: [E5DH1CSW1N]
uses: [0GE4DVQKR8, ZWXW0T3EAC, 1ZBX4TKVZ9, 0KYYSMEVHH]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz_quaternion
same_as:
  wikidata: Q1327941
  wikipedia: Hurwitz quaternion
---

## Description

Let $\mathbb{H}$ be the [[quaternions|0GE4DVQKR8]], with basis $1, i, j, k$ over $\R$ and $i^2 = j^2 = k^2 = ijk = -1$.
The *Hurwitz quaternions* are the elements
$$a + bi + cj + dk \in \mathbb{H}$$
such that either $a, b, c, d$ are all in $\Z$ or all in $\Z + \tfrac{1}{2}$.
They form a ring, written $\mathcal{H}$ here.
Equivalently, $\mathcal{H}$ is the $\Z$-span of $i$, $j$, $k$ and $\omega = \tfrac{1}{2}(1 + i + j + k)$.

## Remarks

The ring $\mathcal{H}$ is a maximal [[order|1ZBX4TKVZ9]] in the rational [[quaternion algebra|ZWXW0T3EAC]] $(-1, -1)_{\Q}$.
It contains the Lipschitz quaternions, those with $a, b, c, d \in \Z$, as a subring of index $2$; the Lipschitz quaternions are an order but not a maximal one.
The reduced norm $a^2 + b^2 + c^2 + d^2$ takes integer values on $\mathcal{H}$; for example $\omega$ has norm $4 \cdot \tfrac14 = 1$.
The units of $\mathcal{H}$ are the $24$ elements $\pm 1, \pm i, \pm j, \pm k$ and $\tfrac12(\pm 1 \pm i \pm j \pm k)$; they form the binary tetrahedral group.
Hurwitz quaternions admit division with remainder on each side, so every one-sided ideal of $\mathcal{H}$ is principal.
This is a standard route to [[Lagrange's four-square theorem|0KYYSMEVHH]].

## Explanations

### L1 human

The Hurwitz quaternions are the quaternion analogue of the integers.
One allows all four coordinates to be integers, or all four to be halves of odd integers.
Adding the half-integer points makes the set a better ring than the plain integer quaternions: one can divide with a small remainder, as for whole numbers.
The quaternion $\tfrac12(1 + i + j + k)$ is a typical new element, and it is even a unit, with norm $1$.

---
tag: X12FS2JAP0
kind: object
name: Symplectic group
msc: [20G20, 51A50]
instance_of: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_group
same_as:
  wikidata: Q936434
  wikipedia: Symplectic group
---

## Description

Let $\mathbb{K}$ be a [[field|04C5ZBG1WT]], let $n \ge 1$, and let
$$\Omega = \begin{pmatrix} 0 & I_n \\ -I_n & 0 \end{pmatrix},$$
a $2n \times 2n$ [[block matrix|0ASDFEQS6P]], where $I_n$ is the $n \times n$ identity matrix.
The *symplectic group* is
$$\operatorname{Sp}(2n, \mathbb{K}) = \set{M \in \operatorname{GL}(2n, \mathbb{K}) : M^T \Omega M = \Omega}.$$
It is a [[group|G5S1M9]] under matrix multiplication, a subgroup of the [[general linear group|0FCHE902D7]].
Check: $I^T \Omega I = \Omega$; if $M^T \Omega M = \Omega$ and $N^T \Omega N = \Omega$, then $(MN)^T \Omega (MN) = N^T (M^T \Omega M) N = \Omega$; and multiplying $M^T \Omega M = \Omega$ by $(M^T)^{-1}$ on the left and $M^{-1}$ on the right gives $(M^{-1})^T \Omega M^{-1} = \Omega$.

## Remarks

The group $\operatorname{Sp}(2n, \mathbb{K})$ is the group of linear maps of $\mathbb{K}^{2n}$ that preserve the standard symplectic form $\omega(x, y) = x^T \Omega y$; see [[symplectic vector space|PQ7JJY0VPH]].
Every symplectic matrix has determinant $1$, so $\operatorname{Sp}(2n, \mathbb{K})$ lies in the [[special linear group|0V9PMN0RBH]].
For $n = 1$, every $2 \times 2$ matrix $M$ satisfies $M^T \Omega M = (\det M)\, \Omega$, so $\operatorname{Sp}(2, \mathbb{K}) = \operatorname{SL}(2, \mathbb{K})$.
For $\mathbb{K} = \R$ it is a connected noncompact Lie group of dimension $n(2n + 1)$.
The notation $\operatorname{Sp}(n)$ is also used for the compact symplectic group, the quaternionic unitary group, which is a different group.

## Explanations

### L1 human

Symplectic matrices are the linear changes of coordinates that preserve a certain signed area between pairs of position and momentum coordinates.
They are the linear maps allowed in Hamiltonian mechanics, because they keep the form of Hamilton's equations.
In the plane, preserving signed area is the same as having determinant $1$.
In higher dimensions the condition is stronger than determinant $1$.

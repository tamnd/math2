---
tag: Y64E6EXGY5
kind: example
name: A Jordan matrix that is not in Weyr form
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: research
not_instance_of:
  - target: 9XEA4VR8WP
    note: its Weyr structure is (2, 2), but its upper left 2 × 2 block is J₂(0) and not the zero matrix
uses: [9XEA4VR8WP, 0PBFS92AJP]
sources:
  - url: https://en.wikipedia.org/wiki/Weyr_canonical_form
    locator: Relation between Weyr and Jordan forms
---

## Example

Over a field $F$, let
$$J = J_2(0) \oplus J_2(0) = E_{12} + E_{34} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix},$$
a matrix in [[Jordan form|0PBFS92AJP]].
We show that $J$ is not a [[Weyr matrix|9XEA4VR8WP]], and we find its Weyr form.

1. The matrix $J$ has rank $2$ and $J^2 = 0$. So the kernels of $J$ and $J^2$ have dimensions $2$ and $4$, and the only possible Weyr structure is $(2, 2)$.
2. A basic Weyr matrix of structure $(2, 2)$ with eigenvalue $0$ has the zero block in rows and columns $1, 2$. In $J$ this block is $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \ne 0$.
3. So $J$ is not a Weyr matrix.
4. Order the basis by height, eigenvectors first: $f_1 = e_1$, $f_2 = e_3$, $f_3 = e_2$, $f_4 = e_4$. Then $J f_3 = f_1$ and $J f_4 = f_2$, while $J f_1 = J f_2 = 0$.
5. So in the basis $f_1, \dots, f_4$ the matrix of $J$ is $E_{13} + E_{24} = \begin{pmatrix} 0 & I_2 \\ 0 & 0 \end{pmatrix}$, the [[basic Weyr matrix of structure (2, 2)|1MN49GY0GV]].
6. The matrix $X = E_{31} + E_{42}$ commutes with $J$. Using $E_{ij} E_{kl} = E_{il}$ when $j = k$ and $0$ otherwise, we get
$$J X = E_{34} E_{42} = E_{32}, \qquad X J = E_{31} E_{12} = E_{32}.$$
7. The matrix $X$ has entries in the lower left $2 \times 2$ block, so in the Jordan basis the centralizer of $J$ is not block upper triangular.

## Remarks

The failure is the order of the basis, not the map.
The Jordan form keeps each chain together, $e_1, e_2$ and then $e_3, e_4$, while the Weyr form puts both eigenvectors $e_1, e_3$ first.
For $J_2(0) \oplus J_2(0)$ the two forms differ by the swap of the middle basis vectors $e_2$ and $e_3$.

When does a Jordan matrix already have Weyr form?
A single block $J_n(\lambda)$ and a scalar matrix $\lambda I_n$ have it.
As soon as one eigenvalue has two or more blocks and one of them has size at least $2$, the two forms differ.
For instance $J_2(0) \oplus J_1(0)$ has Weyr form $E_{13}$, not $E_{12}$.

## Explanations

### L1 human

Picture two ladders with two rungs each.
The Jordan form lists the rungs ladder by ladder: bottom, top, bottom, top.
The Weyr form lists them floor by floor: both bottoms first, then both tops.
This matrix uses the first order, so it is in Jordan form but not in Weyr form.

### L2 human

The quickest test is the first group of basis vectors.
In a Weyr matrix with eigenvalue $\lambda$, the first $n_1$ basis vectors are eigenvectors, because $W_{11} = \lambda I_{n_1}$.
Here $n_1 = 2$, but the second basis vector $e_2$ is not an eigenvector, since $J e_2 = e_1 \ne 0$.
That one line already shows that $J$ is not in Weyr form.

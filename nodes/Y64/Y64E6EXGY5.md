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

Let $J = J_2(0) \oplus J_2(0) = E_{12} + E_{34} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$.

1. $J$ is nilpotent with $J^2 = 0$ and $\operatorname{rank} J = 2$. So $\dim \ker J = 2$ and $\dim \ker J^2 = 4$, and the only possible Weyr structure is $(2, 2)$.
2. For structure $(2, 2)$, the block $W_{11}$ in rows and columns $1, 2$ must be $0 \cdot I_2$. In $J$ this block is $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \ne 0$.
3. So $J$ is not a Weyr matrix.
4. The basis $e_1, e_3, e_2, e_4$ orders the vectors by height: first the eigenvectors $e_1, e_3$, then $e_2, e_4$. In this basis $J$ becomes $\begin{pmatrix} 0 & I_2 \\ 0 & 0 \end{pmatrix}$, the Weyr form.
5. The matrix $X = E_{31} + E_{42}$ commutes with $J$: $JX = E_{34} E_{42} = E_{32}$ and $XJ = E_{31} E_{12} = E_{32}$. It is not block upper triangular for the blocks $\{1, 2\}$, $\{3, 4\}$.

## Remarks

A Jordan matrix is a Weyr matrix only when each eigenvalue has a single Jordan block or only blocks of size $1$.
For $J_2(0) \oplus J_2(0)$ the two forms differ by the permutation of the middle basis vectors.

## Explanations

### L1 human

This matrix is in Jordan form, but not in Weyr form.
Weyr wants all the eigenvectors first and all the vectors one level up afterwards.
The Jordan form instead keeps each chain together.

### L2 human

The test is the block of the eigenvectors.
In a Weyr matrix, $A - \lambda I$ is zero on the first group of basis vectors.
Here the first group $e_1, e_2$ contains $e_2$, which is not an eigenvector.

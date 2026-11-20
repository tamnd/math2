---
tag: VZN1T7QCWE
kind: example
name: A 2 × 2 matrix times a vector with 3 entries is not defined
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
not_instance_of:
  - target: 0PDVQEP0ZC
    note: the matrix has 2 columns and the vector has 3 entries, so the sum over j in the definition has no common range
uses: [0CCQV3884B]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Definition
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $x = (1, 2, 3)^{\mathsf{T}}$.

1. The [[definition|0CCQV3884B]] of $(Ax)_i = \sum_j a_{ij} x_j$ needs one entry $x_j$ for each column $j$ of $A$.
2. $A$ has 2 columns, and $x$ has 3 entries.
3. The term for $j = 3$ would need $a_{13}$, which does not exist.
4. If we drop $x_3$, we get $(1 + 4, 3 + 8)^{\mathsf{T}} = (5, 11)^{\mathsf{T}}$, but this is the product with the different vector $(1, 2)^{\mathsf{T}}$.
5. So $Ax$ is not defined.

## Remarks

The product $x^{\mathsf{T}} B$ is defined for a $3 \times k$ matrix $B$, but not for $A$.
A size check before each product catches many errors: an $m \times n$ matrix accepts only vectors with $n$ entries.

## Explanations

### L1 human

Each row of the matrix must be as long as the vector.
Here the rows have 2 entries and the vector has 3, so they do not fit.

### L2 human

As a map, $A$ goes from $\mathbb{R}^2$ to $\mathbb{R}^2$.
A vector of $\mathbb{R}^3$ is not in its domain.

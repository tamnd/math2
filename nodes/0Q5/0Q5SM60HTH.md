---
tag: 0Q5SM60HTH
kind: definition
name: Permutation matrix
msc: [15A99, 05A05]
defines: 08SP3DF8NB
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Permutation_matrix
    locator: lead section
inventory: [8DZKY09KVR]
---

## Definition

Let $n \ge 1$ and let $\sigma$ be a permutation of $\{1, \dots, n\}$.
The *permutation matrix* of $\sigma$ is the $n \times n$ matrix $P_\sigma$ with entries
$$(P_\sigma)_{ij} = \begin{cases} 1 & \text{if } i = \sigma(j), \\ 0 & \text{otherwise.} \end{cases}$$
A *permutation matrix* is a matrix of the form $P_\sigma$.

## Remarks

The matrix $P_\sigma$ sends the standard basis vector $e_j$ to $e_{\sigma(j)}$.
With this convention, $P_\sigma P_\tau = P_{\sigma \tau}$; some authors use the transposed convention.
Each permutation matrix is invertible with $P_\sigma^{-1} = P_\sigma^T$, and $\det P_\sigma = \sgn \sigma$.
The matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is the permutation matrix that exchanges two coordinates.

## Explanations

### L1 human

A permutation matrix is the identity matrix with its columns shuffled.
Multiplying a vector by it shuffles the entries of the vector in the same way.
Each row and each column has exactly one $1$.

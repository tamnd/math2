---
tag: 07HFRH2AWY
kind: example
name: Circulant matrix
msc: [15B05]
instance_of: [0JXZKX526R]
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Circulant_matrix
    locator: Definition
same_as:
  wikidata: Q245457
  wikipedia: Circulant matrix
---

## Example

Let $F$ be a field and let $c_0, c_1, \dots, c_{n-1} \in F$.
The *circulant matrix* with first column $(c_0, c_1, \dots, c_{n-1})^T$ is the $n \times n$ matrix $C$ with entries $C_{ij} = c_{(i - j) \bmod n}$, for $0 \le i, j \le n - 1$.
Each column is the previous column shifted down by one place, with the last entry moved to the top.
For $n = 3$:
$$C = \begin{pmatrix} c_0 & c_2 & c_1 \\ c_1 & c_0 & c_2 \\ c_2 & c_1 & c_0 \end{pmatrix}.$$

## Remarks

Some authors define circulant matrices by their first row; the two conventions give transposed matrices.
Over $\C$, the vectors $(1, \omega^k, \omega^{2k}, \dots, \omega^{(n-1)k})$ with $\omega = e^{2\pi i/n}$ are eigenvectors of every $n \times n$ circulant matrix.
The product of two circulant matrices of the same order is circulant, and circulant matrices commute with each other.

## Explanations

### L1 human

In a circulant matrix, each column is the column before it, rotated down by one step.
All the information is in the first column.
The discrete Fourier transform diagonalises all of these matrices at the same time.

---
tag: ~949caecd
kind: example
name: The entrywise square is not a polynomial in the matrix
msc: ["15A24"]
topics: [6R1D6QPY3S]
audience: ug1
not_instance_of:
  - target: 0E3MV6E6MG
    note: The entrywise square of A does not commute with A, so it is not a polynomial in A
uses: [0BNEXSKNRV]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_product_(matrices)
    locator: Definition
---

## Example

Let $A = \begin{pmatrix} 0 & 1 \\ 2 & 0 \end{pmatrix}$.
Squaring each entry gives $B = \begin{pmatrix} 0 & 1 \\ 4 & 0 \end{pmatrix}$.

1. Every [[value q(A)|0BNEXSKNRV]] of a polynomial $q$ is a combination of powers of $A$. So $q(A)A = Aq(A)$.
2. $AB = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 4 & 0 \cdot 1 + 1 \cdot 0 \\ 2 \cdot 0 + 0 \cdot 4 & 2 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 4 & 0 \\ 0 & 2 \end{pmatrix}$.
3. $BA = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 2 & 0 \cdot 1 + 1 \cdot 0 \\ 4 \cdot 0 + 0 \cdot 2 & 4 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 4 \end{pmatrix}$.
4. So $AB \ne BA$. By step 1, $B$ is not $q(A)$ for any polynomial $q$.
5. The true square is $A^2 = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 2I$, which differs from $B$.

## Remarks

- In $q(A)$, the power $A^k$ is the matrix product, not the entrywise power.
- The entrywise product is the Hadamard product. It does not fit the rule $q(A)v = q(\lambda)v$ for eigenvectors.

## Explanations

### L1 human

The square of a matrix means $A$ times $A$.
Squaring each entry gives a different matrix.
Here the entrywise square does not even commute with $A$.

### L2 human

The typical lesson is that $A^2$ is a matrix product.
A trap is to compute $p(A)$ by applying $p$ to each entry of $A$.

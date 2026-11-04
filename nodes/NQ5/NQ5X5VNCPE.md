---
tag: NQ5X5VNCPE
kind: proof
name: Proof of the formula for the determinant of a 2 by 2 matrix
msc: [15A15]
proves: 0ZN2J42SK7
uses: [016PE4VZ8Q, 0FWVRHBRWM, 0SK90238BH]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Two by two matrices
---

## Proof

1. Write the matrix as $A = (a_{ij})$ with $a_{11} = a$, $a_{12} = b$, $a_{21} = c$ and $a_{22} = d$.
2. By the [[Leibniz formula|016PE4VZ8Q]], $\det A = \sum_{\sigma \in S_2} \sgn(\sigma)\, a_{1, \sigma(1)} a_{2, \sigma(2)}$.
3. The group $S_2$ has two elements: the identity $\iota$ and the [[transposition|0FWVRHBRWM]] $\tau$ that exchanges $1$ and $2$.
4. By the [[definition of the sign|0SK90238BH]], $\sgn(\iota) = (-1)^0 = 1$ and $\sgn(\tau) = (-1)^1 = -1$.
5. The term of $\iota$ is $a_{11} a_{22} = ad$. The term of $\tau$ is $-a_{12} a_{21} = -bc$.
6. So $\det A = ad - bc$.

## Idea

For $n = 2$ there are only two permutations. The identity gives the product of the main diagonal, and the swap gives minus the product of the other diagonal.

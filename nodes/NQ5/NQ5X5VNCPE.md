---
tag: NQ5X5VNCPE
kind: proof
name: Proof of the formula for the determinant of a 2 × 2 matrix
msc: ["15A15"]
topics: [DTBK11SR77]
audience: school
proves: 0ZN2J42SK7
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [016PE4VZ8Q, 0FWVRHBRWM, 0SK90238BH, 8XWC7RKNN1, 0EB9N0S33C, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Two by two matrices
---

## Proof

**Part 1.**

1. Write $A = (a_{ij})$ with $a_{11} = a$, $a_{12} = b$, $a_{21} = c$ and $a_{22} = d$.
2. By the [[Leibniz formula|016PE4VZ8Q]], $\det A = \sum_{\sigma \in S_2} \sgn(\sigma)\, a_{1 \sigma(1)} a_{2 \sigma(2)}$.
3. The group $S_2$ has two elements: the identity $\iota$ and the [[transposition|0FWVRHBRWM]] $\tau$ that exchanges $1$ and $2$.
4. By the [[definition of the sign|0SK90238BH]], $\sgn(\iota) = (-1)^0 = 1$ and $\sgn(\tau) = (-1)^1 = -1$.
5. The term of $\iota$ is $a_{11} a_{22} = ad$. The term of $\tau$ is $-a_{12} a_{21} = -bc$.
6. So $\det A = ad - bc$.

**Part 2.** Let $K$ be a field and write $\delta = ad - bc$ and $B = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.

7. By the [[matrix product|032Q9FB8MT]], $AB = BA = \delta I_2$. The calculation is in the example on the [[inverse of a 2 × 2 matrix|8XWC7RKNN1]].
8. Let $\delta \neq 0$. Then $A (\delta^{-1} B) = (\delta^{-1} B) A = I_2$ by step 7, so $A$ is [[invertible|0EB9N0S33C]] with $A^{-1} = \delta^{-1} B$.
9. Let $\delta = 0$ and suppose that $A$ has an inverse $A^{-1}$. By step 7, $AB = 0$.
10. Multiply $AB = 0$ on the left by $A^{-1}$. This gives $B = 0$, so $a = b = c = d = 0$.
11. Then $A = 0$, and $0 \cdot A^{-1} = 0 \neq I_2$. This contradicts step 9, so $A$ is not invertible.

**Part 3.** Let $\delta \neq 0$.

12. The system is $A \binom{x}{y} = \binom{e}{f}$.
13. By step 8, multiplication by $A^{-1}$ shows that the only solution is $\binom{x}{y} = A^{-1} \binom{e}{f} = \delta^{-1} \binom{de - bf}{-ce + af}$.
14. This is the formula of part 3.

## Idea

For $n = 2$ there are only two permutations.
The identity gives the product of the main diagonal, and the swap gives minus the product of the other diagonal.
The inverse and the solution of the system then follow from the product $AB = \delta I_2$.

## Variants

Part 1 also follows from the defining properties alone.
Write the rows as $(a, b) = a e_1 + b e_2$ and $(c, d) = c e_1 + d e_2$ and expand by multilinearity.
The terms with two equal rows vanish, and $\det(e_2, e_1) = -1$, so $\det A = ad \det I_2 + bc \det(e_2, e_1) = ad - bc$.

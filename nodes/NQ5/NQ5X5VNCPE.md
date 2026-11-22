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

We read part 1 off the Leibniz formula, and we get parts 2 and 3 from one matrix product.

*Part 1: the formula.*

1. Write $A = (a_{ij})$ with $a_{11} = a$, $a_{12} = b$, $a_{21} = c$ and $a_{22} = d$.
2. By the [[Leibniz formula|016PE4VZ8Q]],
$$\det A = \sum_{\sigma \in S_2} \operatorname{sgn}(\sigma)\, a_{1 \sigma(1)} a_{2 \sigma(2)}.$$
3. The group $S_2$ has two elements: the identity $\iota$ and the [[transposition|0FWVRHBRWM]] $\tau$ that exchanges $1$ and $2$.
4. By the [[definition of the sign|0SK90238BH]], $\operatorname{sgn}(\iota) = 1$ and $\operatorname{sgn}(\tau) = -1$.
5. The term of $\iota$ is $a_{11} a_{22} = ad$.
   The term of $\tau$ is $-a_{12} a_{21} = -bc$.
6. So $\det A = ad - bc$.

*Part 2: the inverse.* Let $K$ be a field, and write $\delta = ad - bc$ and $B = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.

7. By the definition of the [[matrix product|032Q9FB8MT]],
$$AB = \begin{pmatrix} ad - bc & -ab + ba \\ cd - dc & -cb + da \end{pmatrix} = \delta I_2,$$
and in the same way $BA = \delta I_2$, as in the example on the [[inverse of a 2 × 2 matrix|8XWC7RKNN1]].
8. Let $\delta \neq 0$.
   Then $A (\delta^{-1} B) = (\delta^{-1} B) A = I_2$ by step 7, so $A$ is [[invertible|0EB9N0S33C]] with $A^{-1} = \delta^{-1} B$.
9. Let $\delta = 0$, and suppose that $A$ has an inverse $A^{-1}$.
   By step 7, $AB = 0$.
10. Multiply $AB = 0$ on the left by $A^{-1}$.
    This gives $B = 0$, so $a = b = c = d = 0$ and $A = 0$.
11. But then $A A^{-1} = 0 \neq I_2$, which contradicts the choice of $A^{-1}$.
    So $A$ is not invertible when $\delta = 0$.

*Part 3: the system.* Let $\delta \neq 0$.

12. The system is $A \binom{x}{y} = \binom{e}{f}$.
13. Multiplying on the left by $A^{-1}$ shows that every solution equals $A^{-1} \binom{e}{f}$, and this vector is a solution because $A A^{-1} = I_2$.
14. By step 8, this unique solution is
$$\binom{x}{y} = \frac{1}{\delta} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \binom{e}{f} = \frac{1}{\delta} \binom{de - bf}{af - ce},$$
which is the formula of part 3.

## Idea

For $n = 2$ there are only two permutations.
The identity gives the product of the main diagonal, and the swap gives minus the product of the other diagonal.
Everything else comes from one product: the matrix $B$ with swapped diagonal and negated corners satisfies $AB = BA = (ad - bc) I_2$.
When $ad - bc$ can be inverted, $B$ divided by it is the inverse, and the inverse solves the system.

## Variants

Part 1 also follows from the defining properties of the determinant, without the Leibniz formula.
Write the rows as $(a, b) = a e_1 + b e_2$ and $(c, d) = c e_1 + d e_2$, and expand by linearity in each row.
Of the four terms, the two with a repeated row vanish, and $\det(e_2, e_1) = -1$, so
$$\det A = ad \det(e_1, e_2) + bc \det(e_2, e_1) = ad - bc.$$
Part 2 can also be proved by row reduction, which turns $A$ into $I_2$ exactly when $ad - bc \neq 0$.

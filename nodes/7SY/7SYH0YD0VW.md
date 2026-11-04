---
tag: 7SYH0YD0VW
kind: proof
name: Proof that the constant coefficient of the characteristic polynomial is a signed determinant
msc: [15A15, 15A18]
proves: 0T0X8GTYYS
uses: [039HF58KQ5, 016PE4VZ8Q, 0125QVNCFQ, 01EXSMK864, 0Q9EZS90GY]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
---

## Proof

We evaluate the characteristic polynomial at $t = 0$.

1. Let $A = (a_{ij})$ be an $n \times n$ matrix over $K$. Let $p_A(t) = \det(t I_n - A)$ be its [[characteristic polynomial|039HF58KQ5]] in the [[polynomial ring|0Q9EZS90GY]] $K[t]$.
2. Write $p_A(t) = c_0 + c_1 t + \cdots + c_n t^n$ with $c_k \in K$. Then $p_A(0) = c_0$, the constant coefficient.
3. Let $\operatorname{ev}_0 \colon K[t] \to K$ be the [[evaluation homomorphism|0125QVNCFQ]] at $0$. It maps each entry of $t I_n - A$ to the same entry of $-A$.
4. By the [[Leibniz formula|016PE4VZ8Q]], $p_A(t)$ is a sum of products of entries of $t I_n - A$, with signs $\pm 1$.
5. A ring homomorphism preserves sums, products and signs. So by step 4 and the Leibniz formula for $-A$, $p_A(0) = \operatorname{ev}_0(p_A) = \det(-A)$.
6. By the rule for the [[determinant of a scalar multiple|01EXSMK864]] with $c = -1$, $\det(-A) = (-1)^n \det A$.
7. By steps 2, 5 and 6, the constant coefficient of $p_A$ is $p_A(0) = (-1)^n \det A$.

## Idea

The constant coefficient of a polynomial is its value at $0$. Putting $t = 0$ in $\det(t I - A)$ gives $\det(-A)$, and the factor $-1$ comes out of each of the $n$ rows.

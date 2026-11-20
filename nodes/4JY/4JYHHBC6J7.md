---
tag: 4JYHHBC6J7
kind: proof
name: Proof that row rank equals column rank for real matrices by orthogonality
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug2
proves: 0TZAG60ZYT
uses: [0EP73HK4C4, 0F0RPPJ2TT, 0PDVQEP0ZC, 05HQYM0R4G, 08ZDRN6H41, 0W809K6AW0, 0VTQTPQGAV]
methods: [S3QADD13E9]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Proof using orthogonality
---

## Proof

This proof is for a real $m \times n$ matrix $A$.
Let $d = \dim \operatorname{Row}(A)$ and $r = \dim \operatorname{Col}(A)$.

1. Let $x_1, \dots, x_d$ be a [[basis|0VTQTPQGAV]] of the [[row space|0EP73HK4C4]] $\operatorname{Row}(A) \subseteq \R^n$.
2. Claim: $Ax_1, \dots, Ax_d$ are linearly independent. Let $c_1 Ax_1 + \dots + c_d Ax_d = 0$, and put $v = c_1 x_1 + \dots + c_d x_d$.
3. Then $v \in \operatorname{Row}(A)$, and $Av = 0$ by linearity of the [[matrix-vector product|0PDVQEP0ZC]].
4. Entry $i$ of $Av$ is the [[dot product|05HQYM0R4G]] of row $i$ of $A$ with $v$. So $v$ is orthogonal to every row of $A$.
5. The dot product is linear, so $v$ is orthogonal to every combination of the rows. Since $v \in \operatorname{Row}(A)$, this gives $v \cdot v = 0$.
6. $v \cdot v = v_1^2 + \dots + v_n^2$, a sum of real squares. It is $0$ only if $v = 0$.
7. So $c_1 x_1 + \dots + c_d x_d = 0$. The $x_i$ are independent, so all $c_i = 0$. This proves the claim.
8. Each $Ax_i$ is a combination of the columns of $A$, so it lies in the [[column space|0F0RPPJ2TT]] $\operatorname{Col}(A)$.
9. So $\operatorname{Col}(A)$ contains $d$ independent vectors. The [[Steinitz exchange lemma|08ZDRN6H41]] gives $d \le r$.
10. Apply steps 1 to 9 to the real matrix $A^\top$, the [[transpose|0W809K6AW0]]. Its rows are the columns of $A$, and its columns are the rows of $A$. This gives $r \le d$.
11. By steps 9 and 10, $d = r$.

## Idea

The matrix $A$ is injective on its row space, because a row space vector killed by $A$ is orthogonal to itself.
So the row space has an isomorphic copy inside the column space.
Transposing gives the reverse inequality.

## Variants

- Over $\C$, the same proof works with the conjugate transpose and the Hermitian product. It shows $\dim \operatorname{Row}(\overline{A}) = \dim \operatorname{Col}(A)$, and conjugation keeps dimensions.
- Over a field such as $\mathbb{F}_2$, step 6 fails. The row $(1, 1)$ of $\begin{pmatrix} 1 & 1 \end{pmatrix}$ satisfies $(1, 1) \cdot (1, 1) = 0$. The [[proof by row reduction|WK6YWCWJD0]] works over every field.

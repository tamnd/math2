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

We show that $A$ maps a basis of its row space to independent vectors of its column space, and then we apply the same argument to the transpose.
Let $A$ be a real $m \times n$ matrix, and let $d = \dim \operatorname{Row}(A)$ and $r = \dim \operatorname{Col}(A)$.

1. Let $x_1, \dots, x_d$ be a [[basis|0VTQTPQGAV]] of the [[row space|0EP73HK4C4]] $\operatorname{Row}(A) \subseteq \mathbb{R}^n$, with rows read as vectors of $\mathbb{R}^n$.
2. We claim that $Ax_1, \dots, Ax_d$ are linearly independent.
Suppose that $c_1 Ax_1 + \dots + c_d Ax_d = 0$, and put $v = c_1 x_1 + \dots + c_d x_d$.
3. The vector $v$ lies in $\operatorname{Row}(A)$, because it is a combination of the $x_i$.
Also $Av = 0$, by the linearity of the [[matrix-vector product|0PDVQEP0ZC]].
4. Entry $i$ of $Av$ is the [[dot product|05HQYM0R4G]] of row $i$ of $A$ with $v$, so $v$ is orthogonal to every row of $A$.
5. The dot product is linear in each factor, so $v$ is orthogonal to every combination of the rows.
Since $v$ is itself such a combination, $v \cdot v = 0$.
6. The number $v \cdot v = v_1^2 + \dots + v_n^2$ is a sum of real squares, so it is $0$ only when every $v_j$ is $0$.
Hence $v = 0$.
7. So $c_1 x_1 + \dots + c_d x_d = 0$, and the $x_i$ are independent, so every $c_i$ is $0$.
This proves the claim.
8. Each $Ax_i$ is a combination of the columns of $A$, with the entries of $x_i$ as coefficients, so it lies in the [[column space|0F0RPPJ2TT]] $\operatorname{Col}(A)$.
9. So $\operatorname{Col}(A)$ contains $d$ independent vectors, and the [[Steinitz exchange lemma|08ZDRN6H41]] gives $d \le r$.
10. The [[transpose|0W809K6AW0]] $A^{\mathsf{T}}$ is again a real matrix, its rows are the columns of $A$, and its columns are the rows of $A$.
Steps 1 to 9 applied to $A^{\mathsf{T}}$ give $r \le d$.
11. Steps 9 and 10 give $d = r$, so the row rank of $A$ equals its column rank.

## Idea

The matrix $A$ cannot kill a nonzero vector of its own row space.
Such a vector would be orthogonal to every row, hence orthogonal to itself, and over $\mathbb{R}$ only the zero vector is orthogonal to itself.
So $A$ carries the row space into the column space without collapsing it, which gives one inequality.
The transpose swaps the roles of rows and columns and gives the other one.

## Variants

The argument uses only one property of $\mathbb{R}$: a sum of squares is zero only when each term is zero.
So it works over every ordered field, such as $\mathbb{Q}$.
Over $\mathbb{F}_2$ it breaks at step 6, since $(1, 1) \cdot (1, 1) = 1 + 1 = 0$ although $(1, 1) \ne 0$.

Over $\mathbb{C}$ we can repair it with the Hermitian product $\langle u, v \rangle = \sum_j u_j \overline{v_j}$.
Then $Av = 0$ says that $v$ is orthogonal to the conjugates of the rows, so the same steps give $\dim \operatorname{Row}(\overline{A}) \le \dim \operatorname{Col}(A)$, and conjugation does not change dimensions.
The [[proof by row reduction|WK6YWCWJD0]] and the [[proof by a factorization|S1C1ATEFW1]] avoid all of this and work over every field.
The same idea, in the language of orthogonal complements, gives the theorem that the [[orthogonal complement of the column space is the left null space|J4SZVFBHS5]].

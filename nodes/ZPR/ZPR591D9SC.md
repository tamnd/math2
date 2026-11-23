---
tag: ZPR591D9SC
kind: example
name: De Morgan and contraposition as matrix identities
aliases: [de-morgan-law-in-vector-logic, contraposition-in-vector-logic]
msc: ["03B50", "15A69"]
topics: [WZP584JQ06]
audience: grad
instance_of: [DJ41X602BJ]
uses: [DJ41X602BJ, 0N7ENQRCXN, 09PKJKA6J0, 08SP3DF8NB]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_logic
    locator: Dyadic operators; De Morgan's law; Law of contraposition
---

## Example

Work in [[vector logic|DJ41X602BJ]] with $q = 2$, $s = (1, 0)^T$ and $n = (0, 1)^T$.
The inputs $s \otimes s, s \otimes n, n \otimes s, n \otimes n$ are the standard basis vectors $e_1, e_2, e_3, e_4$ of $\mathbb{R}^4$.
We check the matrix form of [[De Morgan's law|09PKJKA6J0]] $p \land q \equiv \neg (\neg p \lor \neg q)$, and the matrix form of $p \to q \equiv \neg p \lor q$.

1. The matrices are $N = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $C = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 1 & 1 \end{pmatrix}$, $D = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$ and $L = \begin{pmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 0 & 0 \end{pmatrix}$.
2. By the mixed product rule, $(N \otimes N)(u \otimes v) = Nu \otimes Nv$, so $N \otimes N$ sends $e_1, e_2, e_3, e_4$ to $e_4, e_3, e_2, e_1$.
3. The $j$-th column of $D (N \otimes N)$ is $D$ applied to the image of $e_j$, so $D (N \otimes N)$ lists the columns of $D$ in reverse order: $D (N \otimes N) = \begin{pmatrix} 0 & 1 & 1 & 1 \\ 1 & 0 & 0 & 0 \end{pmatrix}$.
4. Multiplying by $N$ swaps the two rows: $N D (N \otimes N) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 1 & 1 \end{pmatrix} = C$.
5. In the same way, $N \otimes I$ sends $e_1, e_2, e_3, e_4$ to $e_3, e_4, e_1, e_2$, since $N$ acts on the first factor only.
6. So $D (N \otimes I)$ has the columns of $D$ in the order $3, 4, 1, 2$: $D (N \otimes I) = \begin{pmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 0 & 0 \end{pmatrix} = L$.

So $C = N D (N \otimes N)$ and $L = D (N \otimes I)$ hold as equations between matrices.

## Remarks

The contraposition law $p \to q \equiv \neg q \to \neg p$ follows from these identities.
For logical vectors $u$ and $v$ we compute:
$$L (u \otimes v) = D (Nu \otimes v) = D (Nu \otimes NNv) = D (NNv \otimes Nu) = D (N \otimes I)(Nv \otimes Nu) = L (Nv \otimes Nu).$$
The third equality uses $D (a \otimes b) = D (b \otimes a)$, since disjunction is commutative.
In matrix form this is $D K = D$, where $K$ is the [[permutation matrix|08SP3DF8NB]] that swaps $e_2$ and $e_3$, and it holds because columns 2 and 3 of $D$ are both $s$.

The identities do not depend on the basis.
Take $s = \tfrac{1}{\sqrt2}(1, 1)^T$ and $n = \tfrac{1}{\sqrt2}(1, -1)^T$, so that $N = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.
Then conjunction and disjunction have these matrices:
$$\sqrt2\, C = \begin{pmatrix} 2 & 0 & 0 & 0 \\ -1 & 1 & 1 & 1 \end{pmatrix}, \quad \sqrt2\, D = \begin{pmatrix} 2 & 0 & 0 & 0 \\ 1 & 1 & 1 & -1 \end{pmatrix}.$$
Here $N \otimes N$ is the diagonal matrix with entries $1, -1, -1, 1$, so $D (N \otimes N)$ changes the signs of columns 2 and 3 of $D$, and $N$ then changes the sign of the second row.
The result is $C$ again.
For $q = 3$ with orthonormal $s$ and $n$, both sides of each identity vanish on the vectors orthogonal to all four $a \otimes b$, so the identities hold there too.

The dual law $D = N C (N \otimes N)$ follows by multiplying $C = N D (N \otimes N)$ by $N$ on the left and by $N \otimes N$ on the right, since $N^2 = I$.

## Explanations

### L1 human

De Morgan's law says that "$p$ and $q$" means the same as "not (not $p$ or not $q$)".
In vector logic each side is a matrix.
Multiply the matrices on the right side, and the result is the matrix for "and".
So the law is one equation between two tables of numbers.

### L2 human

Write the four inputs as $e_1, e_2, e_3, e_4$, and find where $N \otimes N$ sends each of them: it reverses the order.
Reorder the columns of $D$ in the same way, swap the two rows, which is the effect of $N$, and compare with $C$.
This proves a logical equivalence once, as a matrix identity, for all inputs at the same time.
Watch out: $N \otimes N$ is a $4 \times 4$ matrix, while $N$ is $2 \times 2$, so keep the sizes apart when you multiply.

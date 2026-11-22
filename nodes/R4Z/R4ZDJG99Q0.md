---
tag: R4ZDJG99Q0
kind: example
name: The identity and diag(1, 2) are not congruent over the rationals
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: ug1
not_instance_of:
  - target: WJWNYSQKK8
    note: over Q, a congruence would give det diag(1, 2) = (det P)^2 det I, so 2 would be the square of a rational number, which is false
uses: [NZJDNC6EP6, D3E2Y85S6H]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
    locator: lead section
---

## Example

Let $A = I_2$ and $A' = \operatorname{diag}(1, 2)$, as matrices over $\mathbb{Q}$.
We show that they are not [[congruent|NZJDNC6EP6]] over $\mathbb{Q}$, and that they are congruent over $\mathbb{R}$.

1. Suppose that $A' = P^{\mathsf{T}} A P$ for an invertible matrix $P$ with rational entries.
2. By part 5 of the [[invariance statement|D3E2Y85S6H]], the determinants satisfy
$$2 = \det A' = (\det P)^2 \det A = (\det P)^2.$$
3. The number $\det P$ is rational, because it is a sum of products of the rational entries of $P$.
4. No rational number has square $2$, since $\sqrt{2}$ is irrational. This contradicts step 2.
5. So no such $P$ exists, and $A$ and $A'$ are not congruent over $\mathbb{Q}$.
6. Over $\mathbb{R}$, take $P = \operatorname{diag}(1, \sqrt{2})$. Then
$$P^{\mathsf{T}} I_2 P = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{2} \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{2} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix},$$
so the two matrices are congruent over $\mathbb{R}$.

## Remarks

The example shows that congruence depends on the field.
Both matrices are symmetric, of rank $2$ and positive definite, so the invariants that classify forms over $\mathbb{R}$, rank and signature, cannot separate them.
Over $\mathbb{Q}$ a finer invariant does: the determinant modulo nonzero squares, the discriminant, which is the class of $1$ for $A$ and the class of $2$ for $A'$.

In the language of forms, $x_1^2 + x_2^2$ cannot be turned into $x_1^2 + 2x_2^2$ by any invertible rational substitution.
The difference is not about the size of values: both forms take only positive values on nonzero vectors.

What happens when the number $2$ changes?
If we replace $2$ by $4$, the matrices become congruent over $\mathbb{Q}$, with $P = \operatorname{diag}(1, 2)$.
If we replace $2$ by $5$, or by any rational number that is not a square, the same argument shows that they are not congruent over $\mathbb{Q}$.
Watch out: the test works in one direction only.
Equal square classes of determinants do not prove congruence, as $\operatorname{diag}(1, 1)$ and $\operatorname{diag}(-1, -1)$ show over $\mathbb{Q}$: both have determinant $1$, but the first takes only positive values on nonzero vectors and the second only negative values.

## Explanations

### L1 human

Over the real numbers we can stretch the second axis by $\sqrt{2}$, and then the form $x^2 + y^2$ turns into $x^2 + 2y^2$.
Over the rational numbers we are not allowed to use $\sqrt{2}$.
The determinant shows that no other rational change of coordinates works either.
Any change of coordinates multiplies the determinant by a square, and $2$ is not the square of a fraction.

### L2 human

The determinant test is a quick way to show that two forms are not equivalent.
Compute $\det A = 1$ and $\det A' = 2$, and then the ratio $2 / 1 = 2$.
Ask whether the ratio is a square in the field.
In $\mathbb{Q}$ it is not, so the matrices are not congruent, while in $\mathbb{R}$ it is, so the test says nothing there.
The typical use is a fast proof that two forms are not equivalent over $\mathbb{Q}$ or over a finite field.
Over $\mathbb{F}_3$, for example, $2$ is not a square either, since $1^2 = 2^2 = 1$, so $I_2$ and $\operatorname{diag}(1, 2)$ are not congruent over $\mathbb{F}_3$ for the same reason.

---
tag: VND7J04NCS
kind: example
name: The determinant of the Gram matrix is not itself an invariant
msc: ["11E04", 15A63]
topics: [6TSCEW8QMK]
audience: ug2
not_instance_of:
  - target: MZFRXECCMC
    note: the forms x^2 and 4x^2 are equivalent but have Gram determinants 1 and 4, so the discriminant is the determinant modulo squares and not the determinant itself
uses: [MZFRXECCMC, WYQGZK8GFT]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
---

## Example

The number $\det A$ is not an invariant of a quadratic form, because two equivalent forms can have Gram matrices with different determinants.
Let $Q_1 = x^2$ and $Q_2 = 4x^2$ on the one-dimensional space $\mathbb{Q}$.

1. The two forms are equivalent. The invertible substitution $x \mapsto 2x$ gives $Q_1(2x) = (2x)^2 = 4x^2 = Q_2(x)$.
2. The Gram matrices are the $1 \times 1$ matrices $(1)$ and $(4)$, with determinants $1$ and $4$.
3. So the number $\det A$ changes under an equivalence, and it is not an invariant of the form.
4. The quotient $4 / 1 = 2^2$ is a square, so the two determinants lie in the same square class, as [[the invariance theorem|WYQGZK8GFT]] predicts. The [[discriminant|MZFRXECCMC]] is this class, not the number.

## Remarks

### Every square can appear

The example works in every dimension.
Replace one basis vector $e$ by $c e$ with $c \ne 0$, and the matrix entry $Q(e)$ becomes $c^2 Q(e)$, while the rest of the row and column is scaled by $c$.
So $\det A$ is multiplied by $c^2$, and every nonzero square of $F$ can appear as a factor.
For $x^2 + y^2$ and $c = 3$ we get $x^2 + 9y^2$, with determinant $9$ in place of $1$.

### Over the integers the number survives

Over $\mathbb{Z}$ the situation is different.
An integer matrix with an integer inverse has $\det P = \pm 1$, so $\det(P)^2 = 1$.
So for forms with integer coefficients and integral changes of variables, the number $\det A$ itself is an invariant.
The forms $x^2$ and $4x^2$ are not equivalent over $\mathbb{Z}$, since $x \mapsto 2x$ has no integer inverse.

## Explanations

### L1 human

Doubling the variable turns $x^2$ into $4x^2$.
The determinant of the matrix changes from $1$ to $4$, although the form is the same up to a change of variables.
So only the determinant up to squares can be a property of the form.

### L2 human

Watch out: do not write $\operatorname{disc} Q = 4$ and $\operatorname{disc} Q = 1$ as if they were different answers.
Over $\mathbb{Q}$, both numbers name the class of squares, so they are the same discriminant.
To compare two discriminants, divide one determinant by the other and test whether the quotient is a square in the field.
Here $4/1 = 2^2$, so the test passes.

---
tag: ~57f2aaae
kind: example
name: The determinant of the Gram matrix is not itself an invariant
msc: ["11E04", 15A63]
topics: [6TSCEW8QMK]
audience: ug2
not_instance_of:
  - target: ~492cb8aa
    note: the forms x^2 and 4x^2 are equivalent but have Gram determinants 1 and 4, so the discriminant is the determinant modulo squares and not the determinant itself
uses: [~492cb8aa, ~98c127ee]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
---

## Example

Let $Q_1 = x^2$ and $Q_2 = 4x^2$ on $\Q$.

1. The substitution $x \mapsto 2x$ gives $Q_1(2x) = 4x^2 = Q_2(x)$. So $Q_1$ and $Q_2$ are equivalent.
2. Their $1 \times 1$ matrices are $(1)$ and $(4)$, with determinants $1$ and $4$.
3. So the number $\det A$ changes under equivalence, and it is not an invariant.
4. The quotient $4 / 1 = 2^2$ is a square, so the two determinants lie in the same square class, as [[the invariance theorem|~98c127ee]] says.

## Remarks

The [[discriminant|~492cb8aa]] is the class of $\det A$ modulo squares, not the number $\det A$.
In dimension $n$, scaling one basis vector by $c$ multiplies $\det A$ by $c^2$, so every nonzero square can appear as a factor.
Over $\Z$ the situation is different: an invertible integer matrix has $\det P = \pm 1$, so $\det A$ itself is an invariant of integral equivalence.

## Explanations

### L1 human

Doubling the variable multiplies the form by $4$.
The determinant changes from $1$ to $4$, but the form is the same up to a change of variables.
So only the determinant up to squares can be an invariant.

### L2 human

A trap: do not write "$\operatorname{disc} Q = 4$" and "$\operatorname{disc} Q = 1$" as if they were different.
Both describe the class of squares.

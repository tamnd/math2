---
tag: 5JPJW2GJR6
kind: example
name: A map on the real plane that is linear in one slot only
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
not_instance_of:
  - target: 0SQZMXB6GP
    note: "B(x, y) = x_1 y_1 + x_2 is linear in x for fixed y, but B(x, 0) = x_2 is not 0, so B is not linear in y"
uses: [0P799D6AMN]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: lead section
---

## Example

On $\mathbb{R}^2$ let
$$B(x, y) = x_1 y_1 + x_2.$$
We check the two conditions of a [[bilinear form|0P799D6AMN]], one slot at a time.

1. Fix $y$. Then $x \mapsto y_1 x_1 + x_2$ is a linear combination of the coordinates of $x$, so $B$ is linear in the first slot.
2. Fix $x = (0, 1)$. Then the first term is $0 \cdot y_1 = 0$, so $B(x, y) = 1$ for every $y$.
3. A linear map sends $0$ to $0$, but step 2 gives $B(x, 0) = 1$. So $y \mapsto B(x, y)$ is not linear.
4. Scaling fails too. For $x = (0, 1)$ and any $y$:
$$B(x, 2y) = 1, \qquad 2 B(x, y) = 2.$$
5. So $B$ is linear in the first slot and not in the second slot, and $B$ is not a bilinear form.

## Remarks

The example shows that linearity in one slot does not give linearity in the other slot.
The cause is the term $x_2$, which contains no coordinate of $y$.
Every term of a bilinear form written as a polynomial must contain exactly one coordinate of $x$ and one coordinate of $y$.

Small changes repair the map.
If we remove the term $x_2$, we get $x_1 y_1$, which is bilinear but [[degenerate|01NHFZF2SK]], since $e_2$ pairs to $0$ with every vector.
If we change $x_2$ to $x_2 y_2$, we get the [[dot product|0S52TNNTH9]].
If we instead swap the roles of the slots, the map $x_1 y_1 + y_2$ is linear in $y$ and not in $x$, by the same argument.

## Explanations

### L1 human

A bilinear rule must double its answer when you double either input.
Here the second input never touches the term $x_2$.
With $x = (0, 1)$ the rule gives $1$ for every second input, even for the zero vector.
So doubling the second input leaves the answer at $1$, and the rule is not bilinear.

### L2 human

Here is a fast test for a formula that is a polynomial in the coordinates.
Write the formula as a sum of monomials, and check that each monomial has degree $1$ in the coordinates of $x$ and degree $1$ in the coordinates of $y$.
For $x_1 y_1 + x_2$, the monomial $x_1 y_1$ passes, but $x_2$ has degree $0$ in $y$, so the test fails.
The test also rejects $x_1^2 y_1$, which has degree $2$ in $x$.
Watch out: checking one slot is never enough, because the failure here is only in the second slot.

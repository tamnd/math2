---
tag: 1V7NMPCSK9
kind: example
name: A skew-symmetric form over the field with two elements that is not alternating
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
not_instance_of:
  - target: 0DGDS5XY84
    note: over F_2 the form x_1 y_1 + x_2 y_2 is skew-symmetric because -1 = 1, but B(e_1, e_1) = 1 is not 0
  - target: PQ7JJY0VPH
    note: the form is nondegenerate but not alternating, since B(e_1, e_1) = 1, so it is not a symplectic form
uses: [08ZQAKBKHF, 1ZB13N78XW]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Symmetric, skew-symmetric, and alternating forms
---

## Example

Let $\mathbb{F}_2 = \{0, 1\}$ be the field with two elements, in which $1 + 1 = 0$.
On $V = \mathbb{F}_2^2$ let
$$B(x, y) = x_1 y_1 + x_2 y_2,$$
the dot product, with matrix $I_2$.
We check that $B$ is skew-symmetric and nondegenerate but not alternating.

1. $B$ is bilinear, because each term $x_k y_k$ is linear in $x$ and in $y$.
2. $B$ is symmetric, since $x_1 y_1 + x_2 y_2 = y_1 x_1 + y_2 x_2$.
3. In $\mathbb{F}_2$ we have $1 + 1 = 0$, so $-1 = 1$ and $-c = c$ for every $c$. So $-B(y, x) = B(y, x) = B(x, y)$, and $B$ is skew-symmetric.
4. $B(e_1, e_1) = 1 \cdot 1 = 1 \ne 0$, so $B$ is not [[alternating|08ZQAKBKHF]].
5. The four vectors of $V$ give these values of $B(v, v)$:
$$B\bigl((0, 0), (0, 0)\bigr) = 0, \quad B\bigl((1, 0), (1, 0)\bigr) = 1, \quad B\bigl((0, 1), (0, 1)\bigr) = 1, \quad B\bigl((1, 1), (1, 1)\bigr) = 1 + 1 = 0.$$
6. $\det I_2 = 1 \ne 0$, so $B$ is nondegenerate, but it is not a symplectic form, because a symplectic form must be alternating.

## Remarks

The example shows that in [[characteristic|1ZB13N78XW]] $2$ the word "skew-symmetric" is weaker than "alternating".
The matrix $I_2$ passes the test $I_2^{\mathsf{T}} = -I_2$, but it fails the second test, a zero diagonal.

Step 5 hides a small surprise.
Over $\mathbb{F}_2$ we have $c^2 = c$, so $B(v, v) = v_1^2 + v_2^2 = v_1 + v_2$, and the map $v \mapsto B(v, v)$ is linear here.
Its kernel is the line spanned by $(1, 1)$, the only nonzero isotropic vector.

What changes with the field?
Over $\mathbb{F}_3$ the same formula gives a symmetric form that is not skew-symmetric, since $B(e_1, e_1) = 1$ but $-B(e_1, e_1) = 2$.
The one-dimensional [[form xy on the field with two elements|QFAWSF1A04]] shows the same effect in the smallest space.

## Explanations

### L1 human

In the number system with only $0$ and $1$, where $1 + 1 = 0$, minus one is the same as one.
So "changes sign when we swap" means the same as "does not change when we swap".
The dot product does not change when we swap, so in this system it also "changes sign".
But the arrow $(1, 0)$ paired with itself gives $1$, so the form is not alternating.

### L2 human

We test the form with the two parts of the matrix criterion.
First, $A = I_2$ and $A^{\mathsf{T}} = I_2 = -I_2$ over $\mathbb{F}_2$, so the first part holds.
Second, the diagonal entries of $A$ are $1$, so the second part fails.
So the form is skew-symmetric but not alternating.
This matters in coding theory and in the theory of symplectic groups over $\mathbb{F}_2$, where all computations take place in characteristic $2$.
Watch out: over $\mathbb{F}_2$ the test $A^{\mathsf{T}} = -A$ says nothing beyond symmetry, so you must check the diagonal separately.

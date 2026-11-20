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

Let $V = \mathbb{F}_2^2$, where $\mathbb{F}_2 = \{0, 1\}$ is the field with two elements.
Let $B(x, y) = x_1 y_1 + x_2 y_2$, with the identity matrix $I_2$.

1. $B$ is bilinear, because it is the dot product on $\mathbb{F}_2^2$.
2. $B$ is symmetric, since $x_1 y_1 + x_2 y_2 = y_1 x_1 + y_2 x_2$.
3. In $\mathbb{F}_2$, $1 + 1 = 0$, so $-1 = 1$ and $-B(y, x) = B(y, x) = B(x, y)$. So $B$ is skew-symmetric.
4. $B(e_1, e_1) = 1 \neq 0$. So $B$ is not [[alternating|08ZQAKBKHF]].
5. The values $B(v, v)$ for the four vectors $(0, 0), (1, 0), (0, 1), (1, 1)$ are $0, 1, 1, 0$.

## Remarks

The example shows that "skew-symmetric" is weaker than "alternating" in [[characteristic|1ZB13N78XW]] $2$.
The matrix $I_2$ satisfies $I_2^T = -I_2$ over $\mathbb{F}_2$, but its diagonal is not zero.
The vector $(1, 1)$ is isotropic, since $B((1, 1), (1, 1)) = 1 + 1 = 0$.
In fact $B(v, v) = (v_1 + v_2)^2$ over $\mathbb{F}_2$, so $v \mapsto B(v, v)$ is linear here.
Over $\mathbb{F}_3$ the same formula gives a form that is symmetric but not skew-symmetric, since $1 \neq -1$ there.
The one-dimensional [[form $xy$ on $\mathbb{F}_2$|QFAWSF1A04]] shows the same effect.

## Explanations

### L1 human

In the number system with only $0$ and $1$, where $1 + 1 = 0$, minus one equals one.
So "changes sign when we swap" is the same as "does not change when we swap".
The ordinary dot product does not change when we swap, so it also "changes sign".
But a vector paired with itself can give $1$, so the form is not alternating.

### L2 human

We test the form with the two conditions of the matrix criterion.

1. $A = I_2$ and $A^T = I_2 = -I_2$ over $\mathbb{F}_2$. The first condition holds.
2. The diagonal entries of $A$ are $1$. The second condition fails.
3. So the form is skew-symmetric but not alternating.

The typical use of this example is a warning when we work over $\mathbb{F}_2$, for example in coding theory.
A trap: over $\mathbb{F}_2$ the test $A^T = -A$ says nothing beyond symmetry, so we must check the diagonal separately.

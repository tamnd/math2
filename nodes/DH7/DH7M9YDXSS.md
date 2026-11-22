---
tag: DH7M9YDXSS
kind: example
name: The sum of two squares is anisotropic over the field with three elements
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
not_instance_of:
  - target: MZHFGPV1YT
    note: x^2 + y^2 is zero over F_3 only at (0, 0), because -1 = 2 is not a square in F_3, so the form has no isotropic vector
  - target: 1X5PZSK44P
    note: a hyperbolic plane contains isotropic vectors, and this form over F_3 has none
uses: [0744CN4MDA]
sources:
  - url: https://en.wikipedia.org/wiki/Isotropic_quadratic_form
    locator: lead section
---

## Example

On $V = \mathbb{F}_3^2$ let $B$ be the [[symmetric bilinear form|0744CN4MDA]]
$$B(x, y) = x_1 y_1 + x_2 y_2,$$
whose matrix is the identity.
We show that no nonzero vector $v$ has $B(v, v) = 0$, so the form is not [[isotropic|MZHFGPV1YT]].
The value on the diagonal is $B(v, v) = v_1^2 + v_2^2$, and all arithmetic is modulo $3$.

1. The squares in $\mathbb{F}_3 = \{0, 1, 2\}$ are $0^2 = 0$, $1^2 = 1$ and $2^2 = 4 = 1$. So each $v_i^2$ is $0$ or $1$.
2. If exactly one coordinate of $v$ is nonzero, then $B(v, v) = 0 + 1 = 1$.
3. If both coordinates are nonzero, then $B(v, v) = 1 + 1 = 2$.
4. These cases cover all $8$ nonzero vectors, and neither value is $0$. So $B(v, v) \neq 0$ for every $v \neq 0$, and $B$ is anisotropic.

A second way to see it avoids the case split.
If $v_1^2 + v_2^2 = 0$ with $v_2 \neq 0$, divide by $v_2^2$:
$$\left( \frac{v_1}{v_2} \right)^2 = -1 = 2.$$
But $2$ is not a square in $\mathbb{F}_3$, so $v_2 = 0$, and then $v_1^2 = 0$ gives $v_1 = 0$.

Since a [[hyperbolic plane|1X5PZSK44P]] contains the isotropic vectors of a hyperbolic pair, this plane is not hyperbolic either.

## Remarks

The example shows that "anisotropic" does not need an order on the field.
Over $\mathbb{R}$ the sum of two squares is anisotropic because squares are positive, but $\mathbb{F}_3$ has no positive elements at all.
Here the reason is arithmetic: $-1$ is not a square.

Change the field and the answer can change.
Over $\mathbb{F}_5$ we have $2^2 = 4 = -1$, so
$$B((1, 2), (1, 2)) = 1 + 4 = 5 = 0,$$
and the same formula gives a hyperbolic plane, as [[the hyperbolic pair over the field with five elements|QG9SC0MYDX]] shows.
For an odd prime power $q$, the form $x_1 y_1 + x_2 y_2$ over $\mathbb{F}_q$ is isotropic exactly when $-1$ is a square in $\mathbb{F}_q$, and that happens exactly when $q \equiv 1 \pmod 4$.
So it is anisotropic over $\mathbb{F}_3$, $\mathbb{F}_7$ and $\mathbb{F}_{11}$, and isotropic over $\mathbb{F}_5$, $\mathbb{F}_9$ and $\mathbb{F}_{13}$.

Change the dimension and the answer changes too.
Adding a third square gives an isotropic form over $\mathbb{F}_3$, since $1 + 1 + 1 = 0$, as for [[the sum of three squares|5VMQ97B0XH]].
In fact every symmetric form over a finite field in three or more variables is isotropic, so an anisotropic form over a finite field has dimension at most $2$.

## Explanations

### L1 human

In the field with three elements, every nonzero number squares to $1$.
So $x^2 + y^2$ is $1$ when one of $x, y$ is zero and the other is not, and it is $1 + 1 = 2$ when both are nonzero.
It is never $0$ unless both $x$ and $y$ are $0$.
So the form has no isotropic vector, just as the dot product of the real plane has none.

### L2 human

Here is a test that works over every field: when is $a x^2 + b y^2$ isotropic, for nonzero $a$ and $b$?
If $a x^2 + b y^2 = 0$ with $y \neq 0$, divide by $a y^2$:
$$\left( \frac{x}{y} \right)^2 = -\frac{b}{a}.$$
If $y = 0$, then $a x^2 = 0$ forces $x = 0$.
So the form is isotropic exactly when $-b/a$ is a square in the field.
For $a = b = 1$ over $\mathbb{F}_3$, the number $-1 = 2$ is not a square, so the form is anisotropic.
For $a = 1$ and $b = 2$ over $\mathbb{F}_3$, the number $-2 = 1$ is a square, and indeed $1^2 + 2 \cdot 1^2 = 3 = 0$.
This test is how one finds the anisotropic part of a form over a small field.
Watch out: compute $-b/a$ in the field, not in the integers, since $-1$ and $2$ are the same element of $\mathbb{F}_3$.

---
tag: 2A38WWPDES
kind: example
name: The bilinear dot product on the complex plane is not sesquilinear
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
instance_of: [0AXZNE5XNH]
not_instance_of:
  - target: 054YEQ0Y8M
    note: B(x, y) = x_1 y_1 + x_2 y_2 on C^2 is linear in y, so B(e_1, i e_1) = i, while a sesquilinear form gives -i h(e_1, e_1)
uses: [0W44K2VNBD, 0P799D6AMN, 3W8AFC4A9P]
sources:
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Informal introduction
---

## Example

On $\C^2$ let $B(x, y) = x_1 y_1 + x_2 y_2$, without conjugation.

1. $B$ is linear in each slot, so it is a symmetric [[bilinear form|0P799D6AMN]] over $\C$.
2. For a [[sesquilinear form|0W44K2VNBD]] $h$, $h(x, iy) = \bar i\, h(x, y) = -i\, h(x, y)$.
3. For $B$, $B(e_1, i e_1) = 1 \cdot i = i$, and $-i\, B(e_1, e_1) = -i$.
4. Since $i \neq -i$, $B$ is not sesquilinear.
5. $B$ also has the nonzero vector $v = (1, i)$ with $B(v, v) = 1 + i^2 = 0$, and $B(iv, iv) = -B(v, v)$ for every $v$.

## Remarks

A map that is both bilinear and sesquilinear satisfies $a\, h(x, y) = \bar a\, h(x, y)$ for all $a$, so $h(x, y) = 0$.
Only the zero form is both.
The sesquilinear version of this form is $\sum_i x_i \bar y_i$, the standard inner product of $\C^2$.
The example [[the bilinear dot product on $\C^2$ is not an inner product|3W8AFC4A9P]] treats the same form from the side of inner products.

## Explanations

### L1 human

The real dot product formula, used on complex vectors, gives a bilinear form.
It does not conjugate the second vector.
So it is not sesquilinear, and it cannot measure lengths: $(1, i)$ has "length" zero.

### L2 human

To test whether a form on $\C^n$ is sesquilinear, compute $h(x, iy)$ for one pair with $h(x, y) \neq 0$.
A sesquilinear form gives $-i\, h(x, y)$; a bilinear form gives $i\, h(x, y)$.
A trap: over $\R$ the two notions agree, since $\bar a = a$ for real $a$; the difference appears only over $\C$.

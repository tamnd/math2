---
tag: QFAWSF1A04
kind: example
name: An antisymmetric bilinear form that is not alternating
msc: ["15A69"]
topics: [DTBK11SR77]
audience: ug2
instance_of: [0443XNARDV]
not_instance_of:
  - target: 0K6CH0MT0F
    note: the form f(x, y) = xy on the field with two elements changes sign under an exchange, but f(1, 1) = 1 is not 0
uses: [0MSWYWHYF5, 0SDMPMCN43, 1ZB13N78XW, VJZVSTWYYW]
sources:
  - url: https://en.wikipedia.org/wiki/Alternating_multilinear_map
    locator: Properties
---

## Example

Let $\mathbb{F}_2 = \set{0, 1}$ be the field with two elements, and view it as a vector space of dimension $1$ over itself.
Let $f \colon \mathbb{F}_2 \times \mathbb{F}_2 \to \mathbb{F}_2$ be $f(x, y) = xy$.

1. Bilinear: $f(x + x', y) = xy + x'y$ and $f(cx, y) = c\,xy$ by the distributive and associative laws, and the same holds in $y$.
2. Antisymmetric: $f(y, x) = yx = xy$. In $\mathbb{F}_2$ we have $-1 = 1$, so $xy = -xy$ and $f(y, x) = -f(x, y)$.
3. Not alternating: $f(1, 1) = 1 \neq 0$.
4. So $f$ satisfies the sign rule but is not an [[alternating multilinear map|0MSWYWHYF5]].

## Remarks

The example shows that part 4 of the [[antisymmetry theorem|VJZVSTWYYW]] needs its condition on $2$.
In $\mathbb{F}_2$ the element $2 = 0$ is a zero divisor, so the step from $y = -y$ to $y = 0$ fails.
Over a field whose [[characteristic|1ZB13N78XW]] is not $2$, the same formula $f(x, y) = xy$ is not antisymmetric, since $f(1, 1) = 1 \neq -1$.
The [[dot product|0S52TNNTH9]] on $\mathbb{R}^2$ is another non-example: $e_1 \cdot e_1 = 1$, and it is symmetric, not antisymmetric.

## Explanations

### L1 human

In arithmetic with only $0$ and $1$, where $1 + 1 = 0$, the numbers $1$ and $-1$ are the same.
So every rule that is symmetric also counts as "changing sign" under a swap.
The rule $x \cdot y$ is such a rule, but it is not zero when $x = y = 1$.

### L2 human

To test the alternating property, put equal inputs and check for zero; the sign rule alone is not a test.
A trap: many books define the determinant by the sign rule, and that definition breaks down in characteristic $2$.

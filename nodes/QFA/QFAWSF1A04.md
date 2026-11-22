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

Let $\mathbb{F}_2 = \{0, 1\}$ be the field with two elements, viewed as a vector space of dimension $1$ over itself.
Let $f \colon \mathbb{F}_2 \times \mathbb{F}_2 \to \mathbb{F}_2$ be $f(x, y) = xy$.
We check that $f$ is bilinear and satisfies the sign rule, but is not alternating.

1. Bilinear.
   By the distributive and associative laws, $f(x + x', y) = xy + x'y$ and $f(cx, y) = c\,xy$ for all $x, x', y, c \in \mathbb{F}_2$, and the same holds in $y$.
2. The sign rule.
   Multiplication in a field is commutative, so $f(y, x) = yx = xy$.
   In $\mathbb{F}_2$ we have $1 + 1 = 0$, so $-1 = 1$ and $xy = -xy$.
   Together, $f(y, x) = -f(x, y)$ for all $x, y$.
3. Not alternating: $f(1, 1) = 1 \cdot 1 = 1 \neq 0$.
4. So $f$ is a [[multilinear map|0SDMPMCN43]] with the sign rule that is not an [[alternating multilinear map|0MSWYWHYF5]].

## Remarks

The example shows why part 4 of the [[antisymmetry lemma|VJZVSTWYYW]] needs its condition on $2$.
The usual argument puts equal arguments in two places, gets $y = -y$ from the sign rule, and concludes $y = 0$.
In $\mathbb{F}_2$ the equation $y = -y$ holds for every $y$, because $2 = 0$, so the last step fails.

The same failure spoils the definition of the determinant by the sign rule.
On $\mathbb{F}_2^2$, both $\det(u, v) = u_1 v_2 - u_2 v_1$ and $g(u, v) = u_1 v_2 - u_2 v_1 + u_1 v_1$ are bilinear, satisfy the sign rule and take the value $1$ on $(e_1, e_2)$.
The first is alternating, but $g(e_1, e_1) = 1$, so only the vanishing condition picks out the determinant.

Now change the field.
Over a field whose [[characteristic|1ZB13N78XW]] is not $2$, the same formula $f(x, y) = xy$ does not even satisfy the sign rule, since $f(1, 1) = 1$ but $-f(1, 1) = -1 \neq 1$.

## Explanations

### L1 human

In arithmetic with only $0$ and $1$, where $1 + 1 = 0$, the numbers $1$ and $-1$ are the same.
So every rule that stays the same under a swap also counts as "changing sign" under the swap.
The rule $x \cdot y$ is such a rule, but it is not zero when $x = y = 1$.

### L2 human

To test whether a bilinear form is alternating, put equal inputs in and check for zero.
The sign rule alone is not a test, because in characteristic $2$ it says no more than symmetry.
Watch out for books that define alternating forms by the sign rule: their theorems silently assume that $2$ is invertible.

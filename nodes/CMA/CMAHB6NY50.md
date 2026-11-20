---
tag: CMAHB6NY50
kind: example
name: Evaluation and integration on polynomials
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug1
instance_of: [07YQ1C78G0]
uses: [0RT96J4D3H, 0JGZCDT5DN, 02MAKWDKGT, 04TMP0XGMJ, 0R8X9XA83A]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_form
    locator: Examples
  - book: isbn:9783031410253
    locator: Section 3F
---

## Example

Let $V = P_2(\R)$ be the [[space of real polynomials|0JGZCDT5DN]] of degree at most $2$, with the basis $1, x, x^2$.
Define two maps $V \to \R$:
$$\operatorname{ev}_2(p) = p(2), \qquad I(p) = \int_0^1 p(t)\,dt.$$
We check that both are [[linear forms|0RT96J4D3H]], and we compute them in coordinates.

1. Additivity of $\operatorname{ev}_2$: $(p + q)(2) = p(2) + q(2)$, by the definition of the sum of polynomials and of [[polynomial evaluation|02MAKWDKGT]].
2. Homogeneity of $\operatorname{ev}_2$: $(cp)(2) = c\,p(2)$ for every $c \in \R$, by the same definitions.
3. Additivity and homogeneity of $I$: the [[definite integral|04TMP0XGMJ]] satisfies $\int_0^1 (p + q) = \int_0^1 p + \int_0^1 q$ and $\int_0^1 cp = c \int_0^1 p$.
4. Values of $\operatorname{ev}_2$ on the basis: $\operatorname{ev}_2(1) = 1$, $\operatorname{ev}_2(x) = 2$ and $\operatorname{ev}_2(x^2) = 4$.
5. Values of $I$ on the basis: $\int_0^1 1\,dt = 1$, $\int_0^1 t\,dt = \tfrac12$ and $\int_0^1 t^2\,dt = \tfrac13$.
6. A linear map is [[determined by its values on a basis|0R8X9XA83A]]. So $\operatorname{ev}_2(a + bx + cx^2) = a + 2b + 4c$ and $I(a + bx + cx^2) = a + \tfrac12 b + \tfrac13 c$.
7. In coordinates, $\operatorname{ev}_2$ is the row vector $(1, 2, 4)$, and $I$ is the row vector $(1, \tfrac12, \tfrac13)$.
8. Check with $p = 1 - 3x + 2x^2$. Directly, $p(2) = 1 - 6 + 8 = 3$, and the row vector gives $1 \cdot 1 + 2 \cdot (-3) + 4 \cdot 2 = 3$.
9. Also $\int_0^1 (1 - 3t + 2t^2)\,dt = 1 - \tfrac32 + \tfrac23 = \tfrac16$, and the row vector gives $1 - \tfrac32 + \tfrac23 = \tfrac16$.

## Remarks

- The kernel of $\operatorname{ev}_2$ is the set of polynomials with a root at $2$, that is, $\set{(x - 2)(a + bx) : a, b \in \R}$. It has dimension $2$.
- The kernel of $I$ also has dimension $2$. A basis is $x - \tfrac12$ and $x^2 - \tfrac13$, since $\int_0^1 (t - \tfrac12)\,dt = 0$ and $\int_0^1 (t^2 - \tfrac13)\,dt = 0$.
- The two row vectors are not proportional, so the two forms are not multiples of each other, and their kernels differ.
- Evaluation at a point $a$ gives the row vector $(1, a, a^2)$. Integration over $[0, c]$ gives $(c, \tfrac{c^2}{2}, \tfrac{c^3}{3})$.
- The derivative at a point, $p \mapsto p'(a)$, is a third linear form, with row vector $(0, 1, 2a)$.

## Explanations

### L1 human

A polynomial can be turned into a single number in many ways.
We can put $x = 2$ into it, or we can take the area under its graph from $0$ to $1$.
Both rules respect sums and scaling, so both are linear forms.
For $p = 1 - 3x + 2x^2$, the first rule gives $3$ and the second gives $\tfrac16$.

### L2 human

A linear form on a space with a basis is a row of numbers, its values on the basis.

1. Write each polynomial as $a + bx + cx^2$, that is, as the column $(a, b, c)$.
2. The form $\operatorname{ev}_2$ is the row $(1, 2, 4)$, and the form $I$ is the row $(1, \tfrac12, \tfrac13)$.
3. The value of a form on a polynomial is the product of the row and the column.

The typical use is a test: a quadrature rule such as $I(p) \approx \tfrac16 p(0) + \tfrac46 p(\tfrac12) + \tfrac16 p(1)$ is exact on $P_2$ exactly when both sides have the same row.
Here the right side has row $\tfrac16(1, 0, 0) + \tfrac46(1, \tfrac12, \tfrac14) + \tfrac16(1, 1, 1) = (1, \tfrac12, \tfrac13)$, so Simpson's rule is exact on $P_2$.
A trap: the row of a form depends on the basis; in the basis $1, x - 2, (x - 2)^2$ the form $\operatorname{ev}_2$ becomes $(1, 0, 0)$.

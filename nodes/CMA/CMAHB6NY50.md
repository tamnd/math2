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

Let $V = P_2(\mathbb{R})$ be the [[space of real polynomials|0JGZCDT5DN]] of degree at most $2$, with the basis $1, x, x^2$.
Define two maps $V \to \mathbb{R}$ by
$$\operatorname{ev}_2(p) = p(2), \qquad I(p) = \int_0^1 p(t) \, dt.$$
We check that both are [[linear forms|0RT96J4D3H]], and then we write each one as a row of three numbers.

First, $\operatorname{ev}_2$ is linear.
By the definition of the sum of polynomials and of [[polynomial evaluation|02MAKWDKGT]], $(p + q)(2) = p(2) + q(2)$.
In the same way $(cp)(2) = c \, p(2)$ for every $c \in \mathbb{R}$.

Second, $I$ is linear, because the [[definite integral|04TMP0XGMJ]] respects sums and constant factors:
$$\int_0^1 (p + q) = \int_0^1 p + \int_0^1 q, \qquad \int_0^1 cp = c \int_0^1 p.$$

Third, we evaluate both forms on the basis.
Putting $x = 2$ into $1, x, x^2$ gives $1, 2, 4$.
Integrating the same three polynomials over $[0, 1]$ gives
$$\int_0^1 1 \, dt = 1, \qquad \int_0^1 t \, dt = \tfrac12, \qquad \int_0^1 t^2 \, dt = \tfrac13.$$
A linear map is [[fixed by its values on a basis|0R8X9XA83A]], so
$$\operatorname{ev}_2(a + bx + cx^2) = a + 2b + 4c, \qquad I(a + bx + cx^2) = a + \tfrac12 b + \tfrac13 c.$$
In coordinates, $\operatorname{ev}_2$ is the row $(1, 2, 4)$ and $I$ is the row $(1, \tfrac12, \tfrac13)$.

Check with $p = 1 - 3x + 2x^2$.
Directly, $p(2) = 1 - 6 + 8 = 3$, and the row gives $1 \cdot 1 + 2 \cdot (-3) + 4 \cdot 2 = 3$.
Directly, $\int_0^1 (1 - 3t + 2t^2) \, dt = 1 - \tfrac32 + \tfrac23 = \tfrac16$, and the row gives the same sum $1 - \tfrac32 + \tfrac23 = \tfrac16$.

## Remarks

The two kernels are planes inside the three-dimensional space $V$.
The kernel of $\operatorname{ev}_2$ is the set of polynomials with a root at $2$, that is, $\{(x - 2)(a + bx) : a, b \in \mathbb{R}\}$, of dimension $2$.
The kernel of $I$ has the basis $x - \tfrac12$ and $x^2 - \tfrac13$, since $\int_0^1 (t - \tfrac12) \, dt = \tfrac12 - \tfrac12 = 0$ and $\int_0^1 (t^2 - \tfrac13) \, dt = \tfrac13 - \tfrac13 = 0$.
The rows $(1, 2, 4)$ and $(1, \tfrac12, \tfrac13)$ are not proportional, so neither form is a multiple of the other, and the two kernels differ.

What happens when we move the point or the interval?
Evaluation at a point $a$ has the row $(1, a, a^2)$, and integration over $[0, c]$ has the row $(c, \tfrac{c^2}{2}, \tfrac{c^3}{3})$.
The derivative at a point, $p \mapsto p'(a)$, is a third kind of linear form, with the row $(0, 1, 2a)$.

## Explanations

### L1 human

A polynomial can be turned into a single number in many ways.
You can put $x = 2$ into it, or you can take the area under its graph from $0$ to $1$.
Both rules respect adding and scaling, so both are linear forms.
For $p = 1 - 3x + 2x^2$ the first rule gives $3$ and the second gives $\tfrac16$.

### L2 human

Here is a typical use: testing a rule for approximate integration.
Simpson's rule says
$$\int_0^1 p(t) \, dt \approx \tfrac16 p(0) + \tfrac46 p(\tfrac12) + \tfrac16 p(1).$$
Both sides are linear forms on $P_2(\mathbb{R})$, so they agree on all of $P_2$ exactly when their rows agree.
The left side has the row $(1, \tfrac12, \tfrac13)$.
Evaluation at $0$, $\tfrac12$ and $1$ has the rows $(1, 0, 0)$, $(1, \tfrac12, \tfrac14)$ and $(1, 1, 1)$, so the right side has the row
$$\tfrac16 (1, 0, 0) + \tfrac46 (1, \tfrac12, \tfrac14) + \tfrac16 (1, 1, 1) = (1, \tfrac12, \tfrac13).$$
The rows agree, so Simpson's rule is exact for every polynomial of degree at most $2$.
Three numbers on each side replaced a check over infinitely many polynomials.
Watch out: the row of a form depends on the basis, and in the basis $1, x - 2, (x - 2)^2$ the form $\operatorname{ev}_2$ has the row $(1, 0, 0)$.

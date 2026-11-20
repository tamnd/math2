---
tag: J8RDPQXN1Z
kind: example
name: Evaluation at nodes is the dual basis of the Lagrange basis
msc: ["15A04", "41A05"]
topics: [9K7FFF26QR]
audience: ug1
instance_of: [0ZD2CF6ZS0]
uses: [0W6M3PSD08, 0JGZCDT5DN, TEQNAME853, 0GJ7T0NK49, 04TMP0XGMJ, 096V7H13H9]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_basis
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Lagrange_polynomial
    locator: A perspective from linear algebra
---

## Example

Let $V = P_2(\R)$ be the [[space of real polynomials|0JGZCDT5DN]] of degree at most $2$.
Take the nodes $0, 1, 2$, and the [[Lagrange basis polynomials|TEQNAME853]]
$$L_0(x) = \tfrac{1}{2}(x - 1)(x - 2), \quad L_1(x) = -x(x - 2), \quad L_2(x) = \tfrac{1}{2} x (x - 1).$$
Let $\mathrm{ev}_a(p) = p(a)$ be [[evaluation at $a$|0GJ7T0NK49]].
We show that $\mathrm{ev}_0, \mathrm{ev}_1, \mathrm{ev}_2$ is the [[dual basis|0W6M3PSD08]] of $L_0, L_1, L_2$.

1. Values of $L_0$: $L_0(0) = \frac{1}{2}(-1)(-2) = 1$, $L_0(1) = 0$ and $L_0(2) = 0$.
2. Values of $L_1$: $L_1(0) = 0$, $L_1(1) = -1 \cdot (-1) = 1$ and $L_1(2) = 0$.
3. Values of $L_2$: $L_2(0) = 0$, $L_2(1) = 0$ and $L_2(2) = \frac{1}{2} \cdot 2 \cdot 1 = 1$.
4. So $\mathrm{ev}_j(L_i) = \delta_{ij}$ for all $i, j \in \set{0, 1, 2}$.
5. The $L_i$ are independent. If $a_0 L_0 + a_1 L_1 + a_2 L_2 = 0$, then evaluation at $j$ gives $a_j = 0$, by step 4.
6. Three independent vectors in a space of dimension $3$ form a basis, by the [[right-size criterion for a basis|096V7H13H9]]. So $L_0, L_1, L_2$ is a basis.
7. By step 4 and the definition, $\mathrm{ev}_0, \mathrm{ev}_1, \mathrm{ev}_2$ is its dual basis.
8. Expansion of a vector: $p = p(0) L_0 + p(1) L_1 + p(2) L_2$. For $p = x^2$, this is $0 \cdot L_0 + 1 \cdot L_1 + 4 \cdot L_2 = (-x^2 + 2x) + (2x^2 - 2x) = x^2$.
9. Expansion of a form: let $I(p) = \int_0^2 p(t)\,dt$, a [[definite integral|04TMP0XGMJ]]. Then $I = I(L_0)\,\mathrm{ev}_0 + I(L_1)\,\mathrm{ev}_1 + I(L_2)\,\mathrm{ev}_2$.
10. Compute: $I(L_0) = \frac{1}{2}\int_0^2 (t^2 - 3t + 2)\,dt = \frac{1}{2}(\frac{8}{3} - 6 + 4) = \frac{1}{3}$.
11. Also $I(L_1) = \int_0^2 (-t^2 + 2t)\,dt = -\frac{8}{3} + 4 = \frac{4}{3}$, and $I(L_2) = \frac{1}{2}\int_0^2 (t^2 - t)\,dt = \frac{1}{2}(\frac{8}{3} - 2) = \frac{1}{3}$.
12. So $I(p) = \frac{1}{3} p(0) + \frac{4}{3} p(1) + \frac{1}{3} p(2)$ for every $p \in P_2(\R)$. This is Simpson's rule on $[0, 2]$.
13. Check with $p = x^2$: $\frac{1}{3} \cdot 0 + \frac{4}{3} \cdot 1 + \frac{1}{3} \cdot 4 = \frac{8}{3} = \int_0^2 t^2\,dt$.

## Remarks

- The same works for any $n + 1$ distinct nodes $a_0, \dots, a_n$ in $P_n(F)$. The evaluations at the nodes are the dual basis of the Lagrange basis.
- Step 12 shows that each linear form on $P_2(\R)$ is fixed by its values on $L_0, L_1, L_2$. The values for the integral are the weights of a quadrature rule.
- The forms $\mathrm{ev}_0, \mathrm{ev}_1, \mathrm{ev}_2$ were studied as linear forms in the example on [[evaluation and integration on polynomials|CMAHB6NY50]].

## Explanations

### L1 human

The polynomial $L_0$ is $1$ at the point $0$ and $0$ at the points $1$ and $2$.
The polynomials $L_1$ and $L_2$ do the same for the points $1$ and $2$.
So "evaluate at $0$", "evaluate at $1$" and "evaluate at $2$" are exactly the coordinate rules for the basis $L_0, L_1, L_2$.

### L2 human

The dual basis turns a question about forms into a computation of a few numbers.

1. To write a form in the basis $\mathrm{ev}_0, \mathrm{ev}_1, \mathrm{ev}_2$, compute its values on $L_0, L_1, L_2$.
2. For the integral over $[0, 2]$, these values are $\frac{1}{3}, \frac{4}{3}, \frac{1}{3}$.
3. So the integral of a quadratic polynomial over $[0, 2]$ is a weighted sum of its three values.

The typical use is the derivation of interpolation and quadrature formulas.
A trap: Simpson's rule is exact for polynomials of degree at most $2$ by this argument; for other functions it is only an approximation.

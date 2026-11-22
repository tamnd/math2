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
Take the nodes $0, 1, 2$ and the [[Lagrange basis polynomials|TEQNAME853]]
$$L_0(x) = \tfrac{1}{2}(x - 1)(x - 2), \qquad L_1(x) = -x(x - 2), \qquad L_2(x) = \tfrac{1}{2} x (x - 1).$$
Let $\mathrm{ev}_a(p) = p(a)$ be [[evaluation at $a$|0GJ7T0NK49]], a linear form on $V$.
We show that $\mathrm{ev}_0, \mathrm{ev}_1, \mathrm{ev}_2$ is the [[dual basis|0W6M3PSD08]] of $L_0, L_1, L_2$, and then we use it to derive a quadrature rule.

1. Each $L_i$ vanishes at the two nodes other than $i$, because of its two linear factors. At its own node, $L_0(0) = \tfrac{1}{2}(-1)(-2) = 1$, $L_1(1) = -1 \cdot (-1) = 1$ and $L_2(2) = \tfrac{1}{2} \cdot 2 \cdot 1 = 1$.
2. So $\mathrm{ev}_i(L_j) = \delta_{ij}$ for all $i, j \in \{0, 1, 2\}$.
3. The $L_j$ are independent. If $a_0 L_0 + a_1 L_1 + a_2 L_2 = 0$, then applying $\mathrm{ev}_i$ and step 2 give $a_i = 0$ for each $i$.
4. Three independent vectors in a space of dimension $3$ form a basis, by the [[right-size criterion for a basis|096V7H13H9]]. So $L_0, L_1, L_2$ is a basis of $V$.
5. By step 2 and the definition of the dual basis, $\mathrm{ev}_0, \mathrm{ev}_1, \mathrm{ev}_2$ is the dual basis of $L_0, L_1, L_2$.

The expansion of a vector in the basis uses the dual basis as coefficients:
$$p = p(0)\, L_0 + p(1)\, L_1 + p(2)\, L_2.$$
For $p = x^2$ the values are $0, 1, 4$, and indeed
$$0 \cdot L_0 + 1 \cdot L_1 + 4 \cdot L_2 = (-x^2 + 2x) + (2x^2 - 2x) = x^2.$$

The expansion of a form uses its values on the basis.
Let $I(p) = \int_0^2 p(t)\,dt$, a [[definite integral|04TMP0XGMJ]] and a linear form on $V$.
Then $I = I(L_0)\, \mathrm{ev}_0 + I(L_1)\, \mathrm{ev}_1 + I(L_2)\, \mathrm{ev}_2$, and the three values are
$$I(L_0) = \tfrac{1}{2} \int_0^2 (t^2 - 3t + 2)\,dt = \tfrac{1}{2}\big(\tfrac{8}{3} - 6 + 4\big) = \tfrac{1}{3},$$
$$I(L_1) = \int_0^2 (-t^2 + 2t)\,dt = -\tfrac{8}{3} + 4 = \tfrac{4}{3}, \qquad I(L_2) = \tfrac{1}{2} \int_0^2 (t^2 - t)\,dt = \tfrac{1}{2}\big(\tfrac{8}{3} - 2\big) = \tfrac{1}{3}.$$
So for every $p$ in $P_2(\R)$,
$$\int_0^2 p(t)\,dt = \tfrac{1}{3} p(0) + \tfrac{4}{3} p(1) + \tfrac{1}{3} p(2),$$
which is Simpson's rule on $[0, 2]$.
Check with $p = x^2$: the right side is $0 + \tfrac{4}{3} + \tfrac{4}{3} = \tfrac{8}{3}$, which is $\int_0^2 t^2\,dt$.

## Remarks

The example shows a dual basis that we meet in practice without the name.
The same holds for any $n + 1$ distinct nodes $a_0, \dots, a_n$ in $P_n(F)$: the evaluations at the nodes are the dual basis of the Lagrange basis for these nodes.
The weights of a quadrature rule are then the values of the integral on the Lagrange polynomials.

If we change the nodes, the dual basis changes with them.
For the nodes $-1, 0, 1$, the same computation gives $\int_{-1}^1 p(t)\,dt = \tfrac{1}{3} p(-1) + \tfrac{4}{3} p(0) + \tfrac{1}{3} p(1)$, as the shift $t \mapsto t - 1$ of the interval suggests.
If two nodes coincide, the evaluations are no longer independent, and they are not a dual basis of anything.
The forms $\mathrm{ev}_a$ and $I$ are studied as linear forms in the example on [[evaluation and integration on polynomials|CMAHB6NY50]].

## Explanations

### L1 human

The polynomial $L_0$ is $1$ at the point $0$ and $0$ at the points $1$ and $2$.
The polynomials $L_1$ and $L_2$ do the same for the points $1$ and $2$.
So "evaluate at $0$", "evaluate at $1$" and "evaluate at $2$" are exactly the rules that give the coordinates in the basis $L_0, L_1, L_2$.
For $x^2$, the three values are $0$, $1$ and $4$, and those are its coordinates.

### L2 human

The dual basis turns a question about a form into the computation of a few numbers.
To write a form in the basis $\mathrm{ev}_0, \mathrm{ev}_1, \mathrm{ev}_2$, compute its values on $L_0, L_1, L_2$.
For the derivative at $1$, $D(p) = p'(1)$, we get $L_0'(x) = x - \tfrac{3}{2}$, $L_1'(x) = -2x + 2$ and $L_2'(x) = x - \tfrac{1}{2}$, so the values are $-\tfrac{1}{2}$, $0$ and $\tfrac{1}{2}$.
This gives the central difference formula
$$p'(1) = \tfrac{1}{2}\big(p(2) - p(0)\big),$$
exact for every $p$ of degree at most $2$.
Check with $p = x^2$: $p'(1) = 2$ and $\tfrac{1}{2}(4 - 0) = 2$.
The typical use is the derivation of interpolation, differentiation and quadrature formulas.
Watch out: such a formula is exact only on $P_2(\R)$; for other functions it is an approximation.

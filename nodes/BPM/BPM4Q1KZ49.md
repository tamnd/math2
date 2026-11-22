---
tag: BPM4Q1KZ49
kind: example
name: The dual of differentiation on polynomials
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug2
instance_of: [0AZ5ARP287]
uses: [0C2TQMW5A1, 0JGZCDT5DN, 0W6M3PSD08, 0YYMY95FWS, 0ZPB3180AY]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 3F
---

## Example

Let $V = P_2(\R)$ be the [[space of real polynomials|0JGZCDT5DN]] of degree at most $2$, and let $D \colon V \to V$ be differentiation, $D(p) = p'$.
We compute the [[dual map|0C2TQMW5A1]] $D^* \colon V^* \to V^*$ on two familiar forms, and then in a basis.
Throughout, write $p = a_0 + a_1 x + a_2 x^2$, so that $p' = a_1 + 2a_2 x$.

1. Let $\mathrm{ev}_1(p) = p(1)$, the value at $1$. By the definition of the dual map, $D^*(\mathrm{ev}_1)(p) = \mathrm{ev}_1(p') = p'(1)$. So $D^*$ turns "value at $1$" into "slope at $1$".
2. Let $I(p) = \int_0^1 p(t) \, dt$. By the fundamental theorem of calculus, $D^*(I)(p) = \int_0^1 p'(t) \, dt = p(1) - p(0)$. So $D^*(I) = \mathrm{ev}_1 - \mathrm{ev}_0$.
3. Take the basis $1, x, x^2$ of $V$. Then $D(1) = 0$, $D(x) = 1$ and $D(x^2) = 2x$.
4. Column $j$ of the [[matrix of D|0YYMY95FWS]] holds the coordinates of $D$ of basis vector $j$, so the matrix is $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$.
5. Let $\varphi_0, \varphi_1, \varphi_2$ be the [[dual basis|0W6M3PSD08]], so that $\varphi_k(p) = a_k$ reads off the coefficient of $x^k$.
6. The constant term of $p'$ is $a_1$, so $D^*(\varphi_0)(p) = \varphi_0(p') = a_1$, and $D^*(\varphi_0) = \varphi_1$.
7. The coefficient of $x$ in $p'$ is $2a_2$, so $D^*(\varphi_1)(p) = 2a_2$, and $D^*(\varphi_1) = 2\varphi_2$.
8. The polynomial $p'$ has no $x^2$ term, so $D^*(\varphi_2) = 0$.
9. Column $k$ of the matrix of $D^*$ in the dual basis holds the coordinates of $D^*(\varphi_k)$, so the matrix is $\begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 2 & 0 \end{pmatrix}$. It is $A^{\mathsf{T}}$, as the theorem on the [[matrix of the dual map|0ZPB3180AY]] predicts.
10. Check of step 1 in coordinates: $\mathrm{ev}_1(p) = a_0 + a_1 + a_2$, so $\mathrm{ev}_1 = \varphi_0 + \varphi_1 + \varphi_2$. By steps 6 to 8, $D^*(\mathrm{ev}_1) = \varphi_1 + 2\varphi_2$, which sends $p$ to $a_1 + 2a_2 = p'(1)$.
11. Check of step 2 in coordinates: $I(p) = a_0 + \tfrac{1}{2} a_1 + \tfrac{1}{3} a_2$, so $D^*(I) = \varphi_1 + \tfrac{1}{2} \cdot 2\varphi_2 = \varphi_1 + \varphi_2$. Also $\mathrm{ev}_1 - \mathrm{ev}_0 = (\varphi_0 + \varphi_1 + \varphi_2) - \varphi_0 = \varphi_1 + \varphi_2$.

## Remarks

The example shows the dual map on a space of functions, where forms are measurements such as values and integrals.
The general rule "apply $D$ first, then measure" gives the answers in steps 1 and 2 with no basis at all, and the basis is needed only to compare with the transpose.

The example also shows how $D$ and $D^*$ trade injectivity and surjectivity.
The map $D$ is not injective, since $D(1) = 0$, and $D^*$ is not surjective: its image is spanned by $\varphi_1$ and $\varphi_2$, which are exactly the forms that vanish on $\ker D = \R \cdot 1$.
The map $D$ is not surjective, since $x^2$ is not the derivative of any polynomial of degree at most $2$, and $D^*$ is not injective: $D^*(\varphi_2) = 0$, and $\varphi_2$ vanishes on $\im D = P_1(\R)$.
Both facts are cases of the theorem on the [[kernel and image of the dual map|7FA499AW3T]].

If you replace $P_2(\R)$ by $P_n(\R)$, the same steps give $D^*(\varphi_k) = (k + 1)\varphi_{k+1}$ for $k < n$ and $D^*(\varphi_n) = 0$.

## Explanations

### L1 human

The dual of differentiation turns a measurement of polynomials into a new measurement: first differentiate, then measure.
For the measurement "value at $1$", the new measurement is "slope at $1$".
For $p = x^2$, the value at $1$ is $1$, and the slope at $1$ is $2$.
For the measurement "area under the graph from $0$ to $1$", the new measurement is "value at $1$ minus value at $0$".

### L2 human

To compute $D^*(\varphi)$ for a form $\varphi$, apply $\varphi$ to $p'$ and simplify.
Take $\varphi(p) = p(2) - p(0)$, for instance.
With $p' = a_1 + 2a_2 x$ we get
$$D^*(\varphi)(p) = p'(2) - p'(0) = (a_1 + 4a_2) - a_1 = 4a_2,$$
so $D^*(\varphi) = 4\varphi_2$.
Check with $p = x^2$: the slope is $4$ at $2$ and $0$ at $0$, and $4 - 0 = 4 = 4 \cdot 1$.
Watch out: $D^*$ goes in the opposite direction to $D$, but it is not integration, since it acts on forms and not on polynomials.

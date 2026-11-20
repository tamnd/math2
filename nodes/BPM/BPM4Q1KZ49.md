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
We compute the [[dual map|0C2TQMW5A1]] $D^* \colon V^* \to V^*$ on two forms and in a basis.

1. Let $\mathrm{ev}_1(p) = p(1)$. Then $D^*(\mathrm{ev}_1)(p) = \mathrm{ev}_1(D p) = p'(1)$. So $D^*(\mathrm{ev}_1)$ is the form "derivative at $1$".
2. Let $I(p) = \int_0^1 p(t)\,dt$. Then $D^*(I)(p) = \int_0^1 p'(t)\,dt = p(1) - p(0)$. So $D^*(I) = \mathrm{ev}_1 - \mathrm{ev}_0$.
3. Take the basis $1, x, x^2$ of $V$. Then $D(1) = 0$, $D(x) = 1$ and $D(x^2) = 2x$.
4. So the [[matrix of $D$|0YYMY95FWS]] is $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$, with column $j$ the coordinates of $D$ of basis vector $j$.
5. Let $\varphi_0, \varphi_1, \varphi_2$ be the [[dual basis|0W6M3PSD08]], so $\varphi_k(a_0 + a_1 x + a_2 x^2) = a_k$.
6. $D^*(\varphi_0)(p) = \varphi_0(p')$, the constant term of $p' = a_1 + 2a_2 x$. So $D^*(\varphi_0) = \varphi_1$.
7. $D^*(\varphi_1)(p) = \varphi_1(p') = 2a_2$. So $D^*(\varphi_1) = 2\varphi_2$.
8. $D^*(\varphi_2)(p) = \varphi_2(p') = 0$, since $p'$ has degree at most $1$. So $D^*(\varphi_2) = 0$.
9. The matrix of $D^*$ in the dual basis has columns $(0, 1, 0)^{\mathsf{T}}$, $(0, 0, 2)^{\mathsf{T}}$ and $(0, 0, 0)^{\mathsf{T}}$. This is $A^{\mathsf{T}}$, as the theorem on the [[matrix of the dual map|0ZPB3180AY]] says.
10. Check of step 1 in coordinates: $\mathrm{ev}_1 = \varphi_0 + \varphi_1 + \varphi_2$. By steps 6 to 8, $D^*(\mathrm{ev}_1) = \varphi_1 + 2\varphi_2$, which sends $p$ to $a_1 + 2a_2 = p'(1)$.

## Remarks

- $D$ is not injective, since $D(1) = 0$. Accordingly $D^*$ is not surjective: its image is spanned by $\varphi_1$ and $\varphi_2$, the forms that vanish on the kernel $\R \cdot 1$ of $D$.
- $D$ is not surjective, since $x^2$ is not a derivative in $P_2(\R)$. Accordingly $D^*$ is not injective: $D^*(\varphi_2) = 0$, and $\varphi_2$ vanishes on the image $P_1(\R)$ of $D$.
- These two remarks are cases of the theorem on the [[kernel and image of the dual map|7FA499AW3T]].

## Explanations

### L1 human

The dual of differentiation turns a measurement of polynomials into a new measurement: "first differentiate, then measure".
For the measurement "value at $1$", the new measurement is "slope at $1$".
For the measurement "integral from $0$ to $1$", the new measurement is "value at $1$ minus value at $0$", by the fundamental theorem of calculus.

### L2 human

To compute $D^*(\varphi)$, apply $\varphi$ to $p'$ and simplify.

1. Write $p = a_0 + a_1 x + a_2 x^2$ and $p' = a_1 + 2a_2 x$.
2. Apply $\varphi$ to $p'$.
3. Express the result as a form in $a_0, a_1, a_2$.

The typical use is to see the transpose of a matrix as a concrete operation on forms.
A trap: $D^*$ is not "integration", although it goes in the opposite direction to $D$.

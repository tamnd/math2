---
tag: JNME2MD8GM
kind: example
name: The Hilbert matrix as the Gram matrix of monomials
msc: ["15A63", "15B05"]
topics: [1D4JTZ9VS3]
audience: ug1
instance_of: [00SPJSDT3Z]
uses: [0HX8HZ1WTQ, W6NJ22XGWT, A1Y41YZFB6]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Examples
---

## Example

On the real polynomials of degree at most $2$, use the [[integral inner product|W6NJ22XGWT]] $\ip{p}{q} = \int_0^1 p(x) q(x)\, dx$.
We compute the [[Gram matrix|0HX8HZ1WTQ]] of $v_1 = 1$, $v_2 = x$ and $v_3 = x^2$.

1. The entries are $\ip{x^{i-1}}{x^{j-1}} = \int_0^1 x^{i + j - 2}\, dx = \frac{1}{i + j - 1}$.
2. So $G = \begin{pmatrix} 1 & \frac12 & \frac13 \\ \frac12 & \frac13 & \frac14 \\ \frac13 & \frac14 & \frac15 \end{pmatrix}$. This is the [[Hilbert matrix|2DTWB6F5TA]] $H_3$.
3. Expansion along the first row gives $\det G = \frac{1}{240} - \frac12 \cdot \frac{1}{60} + \frac13 \cdot \frac{1}{72}$.
4. Over the denominator $2160$, this is $\frac{9 - 18 + 10}{2160} = \frac{1}{2160}$.
5. The [[Gram-Schmidt process|A1Y41YZFB6]] gives $u_1 = 1$, $u_2 = x - \frac12$ and $u_3 = x^2 - x + \frac16$.
6. Their squared norms are $1$, $\int_0^1 (x - \frac12)^2\, dx = \frac{1}{12}$ and $\int_0^1 (x^2 - x + \frac16)^2\, dx = \frac{1}{180}$.
7. The product is $1 \cdot \frac{1}{12} \cdot \frac{1}{180} = \frac{1}{2160} = \det G$.

## Remarks

The determinant is positive, so $1, x, x^2$ are independent, as expected.
It is very small, so the three functions are close to dependent on $[0, 1]$: the volume that they span is $\frac{1}{\sqrt{2160}} \approx 0.0215$.
For $1, x, \dots, x^{n-1}$ the Gram matrix is $H_n$, and its determinant decreases very fast with $n$.
This is why the normal equations for polynomial fits in the monomial basis are badly conditioned.

## Explanations

### L1 human

The functions $1$, $x$ and $x^2$ on $[0, 1]$ look quite similar: all three increase or stay flat.
Their Gram matrix has a tiny determinant, $\frac{1}{2160}$.
A tiny Gram determinant means the vectors almost lie in a smaller space.

### L2 human

The step that needs care is step 6.
Expand $(x^2 - x + \frac16)^2 = x^4 - 2x^3 + \frac43 x^2 - \frac13 x + \frac1{36}$.
Integrate over $[0, 1]$: $\frac15 - \frac12 + \frac49 - \frac16 + \frac1{36} = \frac{36 - 90 + 80 - 30 + 5}{180} = \frac{1}{180}$.
A trap: the inner product is over $[0, 1]$.
Over $[-1, 1]$ the matrix is different, and $x$ is orthogonal to $1$.

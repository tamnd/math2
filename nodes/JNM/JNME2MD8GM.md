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

On the real polynomials of degree at most $2$, use the [[integral inner product|W6NJ22XGWT]]
$$\ip{p}{q} = \int_0^1 p(x)\, q(x) \, dx.$$
We compute the [[Gram matrix|0HX8HZ1WTQ]] of $v_1 = 1$, $v_2 = x$ and $v_3 = x^2$, find its determinant, and check the determinant against the Gram-Schmidt process.

1. The entries are integrals of powers of $x$:
$$G_{ij} = \ip{x^{i-1}}{x^{j-1}} = \int_0^1 x^{i + j - 2} \, dx = \frac{1}{i + j - 1}.$$
2. So the Gram matrix is the $3 \times 3$ [[Hilbert matrix|2DTWB6F5TA]]
$$H_3 = \begin{pmatrix} 1 & \frac12 & \frac13 \\ \frac12 & \frac13 & \frac14 \\ \frac13 & \frac14 & \frac15 \end{pmatrix}.$$
3. Expand along the first row. The three $2 \times 2$ minors are $\frac{1}{15} - \frac{1}{16} = \frac{1}{240}$, $\frac{1}{10} - \frac{1}{12} = \frac{1}{60}$ and $\frac18 - \frac19 = \frac{1}{72}$, so
$$\det H_3 = 1 \cdot \frac{1}{240} - \frac12 \cdot \frac{1}{60} + \frac13 \cdot \frac{1}{72} = \frac{9 - 18 + 10}{2160} = \frac{1}{2160}.$$
4. The [[Gram-Schmidt process|A1Y41YZFB6]] gives $u_1 = 1$ and $u_2 = x - \ip{x}{1} \cdot 1 = x - \frac12$. Then $\ip{x^2}{1} = \frac13$, $\ip{x^2}{u_2} = \frac14 - \frac16 = \frac{1}{12}$ and $\ip{u_2}{u_2} = \frac{1}{12}$, so $u_3 = x^2 - \frac13 - (x - \frac12) = x^2 - x + \frac16$.
5. The squared norms are $\norm{u_1}^2 = 1$ and $\norm{u_2}^2 = \int_0^1 (x - \frac12)^2 \, dx = \frac{1}{12}$.
6. For $u_3$, expand $(x^2 - x + \frac16)^2 = x^4 - 2x^3 + \frac43 x^2 - \frac13 x + \frac{1}{36}$ and integrate term by term:
$$\norm{u_3}^2 = \frac15 - \frac12 + \frac49 - \frac16 + \frac{1}{36} = \frac{36 - 90 + 80 - 30 + 5}{180} = \frac{1}{180}.$$
7. The product is $1 \cdot \frac{1}{12} \cdot \frac{1}{180} = \frac{1}{2160}$, which equals $\det H_3$, as the [[squared volume theorem|FWA0AKJA2R]] predicts.

## Remarks

The determinant is positive, so $1$, $x$ and $x^2$ are independent, which you knew already.
What is new is its size: the three functions span a box of volume $\frac{1}{\sqrt{2160}} \approx 0.0215$, although each has length at most $1$.
On $[0, 1]$ the graphs of $x$ and $x^2$ are close to each other, so the monomials are nearly dependent.

For $1, x, \dots, x^{n-1}$ the Gram matrix is the Hilbert matrix $H_n$ with the entries $\frac{1}{i + j - 1}$.
Its determinant falls very fast: $\det H_2 = \frac13 - \frac14 = \frac{1}{12}$, $\det H_3 = \frac{1}{2160}$ and $\det H_4 = \frac{1}{6048000}$.
This is why fitting a polynomial by least squares in the monomial basis gives normal equations that are badly conditioned, and why one uses orthogonal polynomials instead.

If the interval changes, the matrix changes.
On $[-1, 1]$ the inner products of $1$ with $x$ and of $x$ with $x^2$ are $0$, because the integrands are odd, and Gram-Schmidt there gives the [[Legendre polynomials|JPDVZM20EX]] up to scaling.

## Explanations

### L1 human

The functions $1$, $x$ and $x^2$ on the interval from $0$ to $1$ are all small and all increase or stay flat.
Seen as vectors, they point in nearly the same direction.
Their Gram matrix has the tiny determinant $\frac{1}{2160}$, and a tiny Gram determinant means that the vectors almost lie in a smaller space.

### L2 human

The step that needs care is step 6, the norm of $u_3 = x^2 - x + \frac16$.
Square it term by term: $x^4$, then $2 \cdot x^2 \cdot (-x) = -2x^3$, then $x^2 + 2 \cdot x^2 \cdot \frac16 = \frac43 x^2$, then $2 \cdot (-x) \cdot \frac16 = -\frac13 x$, then $\frac{1}{36}$.
The integral of $x^m$ over $[0, 1]$ is $\frac{1}{m + 1}$, and the common denominator of $5$, $2$, $9$, $6$ and $36$ is $180$.
Check: $u_3$ is orthogonal to $1$, since $\frac13 - \frac12 + \frac16 = 0$.
Watch out: the polynomials $u_j$ depend on the interval, and on $[0, 1]$ they are shifted Legendre polynomials, not the Legendre polynomials themselves.

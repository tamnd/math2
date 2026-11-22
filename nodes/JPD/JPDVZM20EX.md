---
tag: JPDVZM20EX
kind: example
name: Legendre polynomials from the Gram-Schmidt process
msc: ["15A63", "33C45", "42C05"]
topics: [1D4JTZ9VS3]
audience: ug1
instance_of: [0VT6P0GNQR, 0RW9TNNT87]
uses: [A1Y41YZFB6, 4JVVDAQ9XX, 0VGSYBWHV2]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_polynomials
    locator: Definition by construction as an orthogonal system
  - url: https://en.wikipedia.org/wiki/Legendre_polynomials
    locator: Orthogonality and normalization
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: Description
---

## Example

On $\mathcal{P}_3(\mathbb{R})$, the real polynomials of degree at most $3$, take the [[inner product|0VGSYBWHV2]]
$$\ip{p}{q} = \int_{-1}^{1} p(x) q(x)\, dx,$$
and apply the [[Gram-Schmidt process|A1Y41YZFB6]] to $1, x, x^2, x^3$.
Every integral below comes from one rule: $\int_{-1}^1 x^m\, dx = \frac{2}{m + 1}$ for even $m$, and $0$ for odd $m$ because the integrand is odd.

1. Keep the first vector: $u_0 = 1$, with $\ip{u_0}{u_0} = \int_{-1}^1 1\, dx = 2$.
2. Since $\ip{x}{1} = 0$, nothing is subtracted, so $u_1 = x$, with $\ip{u_1}{u_1} = \int_{-1}^1 x^2\, dx = \tfrac23$.
3. For $x^2$ we have $\ip{x^2}{1} = \tfrac23$ and $\ip{x^2}{x} = 0$, so $u_2 = x^2 - \frac{2/3}{2} \cdot 1 = x^2 - \tfrac13$.
4. Its squared norm is $\int_{-1}^1 \left(x^4 - \tfrac23 x^2 + \tfrac19\right) dx = \tfrac25 - \tfrac49 + \tfrac29 = \tfrac{8}{45}$.
5. For $x^3$ we have $\ip{x^3}{1} = 0$, $\ip{x^3}{x} = \tfrac25$, and $\ip{x^3}{u_2} = 0$ because $x^3 u_2$ is odd, so $u_3 = x^3 - \frac{2/5}{2/3} x = x^3 - \tfrac35 x$.
6. Its squared norm is $\int_{-1}^1 \left(x^6 - \tfrac65 x^4 + \tfrac{9}{25} x^2\right) dx = \tfrac27 - \tfrac{12}{25} + \tfrac{6}{25} = \tfrac{8}{175}$.
7. Check two orthogonality relations that the parity argument does not cover: $\ip{u_2}{u_0} = \tfrac23 - \tfrac23 = 0$ and $\ip{u_3}{u_1} = \tfrac25 - \tfrac35 \cdot \tfrac23 = 0$.
8. The [[Legendre polynomials|4JVVDAQ9XX]] are the multiples with $P_n(1) = 1$: $P_0 = 1$, $P_1 = x$, $P_2 = \tfrac32 u_2 = \tfrac12(3x^2 - 1)$ and $P_3 = \tfrac52 u_3 = \tfrac12(5x^3 - 3x)$.
9. Their squared norms are $2$, $\tfrac23$, $\tfrac94 \cdot \tfrac{8}{45} = \tfrac25$ and $\tfrac{25}{4} \cdot \tfrac{8}{175} = \tfrac27$, so $\norm{P_n}^2 = \frac{2}{2n + 1}$ for $n \leq 3$.
10. The orthonormal output is $e_n = \sqrt{\tfrac{2n + 1}{2}}\, P_n$, that is,

$$e_0 = \tfrac{1}{\sqrt2}, \qquad e_1 = \sqrt{\tfrac32}\, x, \qquad e_2 = \sqrt{\tfrac52} \cdot \tfrac12(3x^2 - 1), \qquad e_3 = \sqrt{\tfrac72} \cdot \tfrac12(5x^3 - 3x).$$

So the process turns the monomials into an orthonormal basis of $\mathcal{P}_3(\mathbb{R})$, and the vectors that it produces are multiples of the first four Legendre polynomials.

## Remarks

Three normalizations of the same polynomials are in use: the monic $u_n$ that the process produces before normalizing, the Legendre $P_n$ with $P_n(1) = 1$, and the orthonormal $e_n$.
All three families are orthogonal, but only the $e_n$ have norm $1$.

The process keeps parity: $u_n$ is even for even $n$ and odd for odd $n$.
The reason is that an even and an odd polynomial are always orthogonal on $[-1, 1]$, so $x^n$ only loses components of its own parity.
That is why half of the inner products in the steps above vanish without any work.

Change the interval or the weight and the output changes.
On $[0, 1]$ the same process gives the shifted Legendre polynomials; for example $u_1 = x - \frac{\ip{x}{1}}{\ip{1}{1}} = x - \tfrac12$.
With the weight $\frac{1}{\sqrt{1 - x^2}}$ in the integral on $[-1, 1]$, the process gives multiples of the Chebyshev polynomials instead.

## Explanations

### L1 human

Polynomials can be at right angles to each other, if we measure them with an integral.
Two polynomials count as perpendicular when the integral of their product from $-1$ to $1$ is zero.
Starting from $1, x, x^2, x^3$, the Gram-Schmidt process produces polynomials that are perpendicular in this sense.
For example $x^2 - \tfrac13$ is perpendicular to $1$, because the area under it from $-1$ to $1$ is $\tfrac23 - \tfrac23 = 0$.
These polynomials are the Legendre polynomials, up to a scale factor.

### L2 human

Here is a typical use: find the straight line $a + bx$ closest to $x^3$ on $[-1, 1]$ in the sense of this inner product.
The closest line is the projection of $x^3$ onto $\operatorname{span}(e_0, e_1)$, so we need two inner products:
$$\ip{x^3}{e_0} = \tfrac{1}{\sqrt2} \int_{-1}^1 x^3\, dx = 0, \qquad \ip{x^3}{e_1} = \sqrt{\tfrac32} \int_{-1}^1 x^4\, dx = \sqrt{\tfrac32} \cdot \tfrac25.$$
The projection is
$$\ip{x^3}{e_1}\, e_1 = \tfrac32 \cdot \tfrac25\, x = \tfrac35 x.$$
The error is $x^3 - \tfrac35 x = u_3$, which is orthogonal to every line, and its squared norm is $\tfrac{8}{175}$ by step 6.
This is mean-square approximation of functions by polynomials, the continuous form of least squares.
Watch out: the Legendre polynomials $P_n$ are orthogonal but not orthonormal, since $\norm{P_n}^2 = \frac{2}{2n + 1}$, so a projection with $P_n$ needs the division by $\norm{P_n}^2$.

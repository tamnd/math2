---
tag: 3XJYJHMPKY
kind: definition
name: Zernike polynomials
msc: [33C45, 78A10]
defines: 7YW5WB3BY4
uses: [07GNX8GCYP]
sources:
  - url: https://en.wikipedia.org/wiki/Zernike_polynomials
---

## Definition

Let $n$ and $m$ be integers with $0 \le m \le n$ and $n - m$ even.
The *radial polynomial* $R_n^m$ on $[0, 1]$ is
$$R_n^m(\rho) = \sum_{k=0}^{(n - m)/2} \frac{(-1)^k \, (n - k)!}{k! \, \left( \frac{n + m}{2} - k \right)! \, \left( \frac{n - m}{2} - k \right)!} \, \rho^{n - 2k}.$$
The *Zernike polynomials* are the functions on the closed unit disk, written in polar coordinates $(\rho, \varphi)$ with $0 \le \rho \le 1$, given by
$$Z_n^m(\rho, \varphi) = R_n^m(\rho) \cos(m\varphi),$$
and, for $m > 0$,
$$Z_n^{-m}(\rho, \varphi) = R_n^m(\rho) \sin(m\varphi).$$

## Remarks

Each $Z_n^{\pm m}$ is a [[polynomial in the two variables|07GNX8GCYP]] $x = \rho \cos \varphi$ and $y = \rho \sin \varphi$, of degree $n$.
Examples: $Z_0^0 = 1$, $Z_1^1 = \rho \cos \varphi = x$ and $Z_2^0 = 2\rho^2 - 1 = 2x^2 + 2y^2 - 1$.
Check for $R_2^0$: the term $k = 0$ is $\frac{2!}{0! \, 1! \, 1!} \rho^2 = 2\rho^2$ and the term $k = 1$ is $-\frac{1!}{1! \, 0! \, 0!} = -1$.
Orthogonality: $\int_0^1 R_n^m(\rho) R_{n'}^m(\rho) \, \rho \, d\rho = \frac{\delta_{n n'}}{2(n + 1)}$; for example $\int_0^1 (2\rho^2 - 1) \rho \, d\rho = \frac12 - \frac12 = 0$.
The normalisation is $R_n^m(1) = 1$.
The radial parts are Jacobi polynomials: $R_n^m(\rho) = (-1)^{(n - m)/2} \rho^m P_{(n - m)/2}^{(m, 0)}(1 - 2\rho^2)$.
Non-example: $n = 1$, $m = 0$ is excluded because $n - m$ is odd.
The natural candidate $\rho = \sqrt{x^2 + y^2}$ is rotation invariant but is not a polynomial in $x$ and $y$.

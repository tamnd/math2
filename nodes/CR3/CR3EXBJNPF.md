---
tag: CR3EXBJNPF
kind: example
name: Adjoint of differentiation on polynomials of degree at most 2
msc: ["15A04", "47A05"]
topics: [3YM9EK6VMB]
audience: ug1
instance_of: [0R9NMSM1ZP]
not_instance_of:
  - target: 0C8BR8XRTR
    note: differentiation D on this space satisfies DD^*(1) = 3 but D^*D(1) = 0, so D is not normal
illustrates: [0DBTE6HVBD]
uses: [0ST8QF9T3T, 0DBTE6HVBD, 0JGZCDT5DN, JPDVZM20EX, 0FWJ0VW561, 0ENZN5G4CV]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_polynomials
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Example

Let $V = \mathcal{P}_2(\mathbb{R})$ be the [[space of real polynomials|0JGZCDT5DN]] of degree at most $2$, with the inner product
$$\ip{p}{q} = \int_{-1}^{1} p(x) q(x) \, dx.$$
Let $D \colon V \to V$ be differentiation, $D(p) = p'$.
We compute the [[adjoint|0ST8QF9T3T]] $D^*$ and show that $D^* D \neq D D^*$.

1. We take an orthonormal basis. Let $e_0 = \tfrac{1}{\sqrt 2}$, $e_1 = \sqrt{\tfrac{3}{2}}\, x$ and $e_2 = \sqrt{\tfrac{5}{8}}\, (3x^2 - 1)$, the normalized [[Legendre polynomials|JPDVZM20EX]] of degree $0$, $1$ and $2$.
2. Each has norm $1$:
$$\int_{-1}^{1} \tfrac12 \, dx = 1, \qquad \int_{-1}^{1} \tfrac32 x^2 \, dx = \tfrac32 \cdot \tfrac23 = 1, \qquad \int_{-1}^{1} \tfrac58 (9x^4 - 6x^2 + 1) \, dx = \tfrac58 \left(\tfrac{18}{5} - 4 + 2\right) = 1.$$
3. They are orthogonal. The products $e_0 e_1$ and $e_1 e_2$ are odd functions, so their integrals over $[-1, 1]$ are $0$, and $\int_{-1}^{1} (3x^2 - 1) \, dx = 2 - 2 = 0$ gives $\ip{e_0}{e_2} = 0$. So $(e_0, e_1, e_2)$ is an [[orthonormal basis|0FWJ0VW561]].
4. We find the matrix of $D$. We have $D e_0 = 0$ and $D e_1 = \sqrt{\tfrac32} = \sqrt 3\, e_0$. Also $D e_2 = 6\sqrt{\tfrac58}\, x = \sqrt{15}\, e_1$, because $6 \sqrt{5/8} \big/ \sqrt{3/2} = 6 \sqrt{5/12} = \sqrt{15}$.
5. So the matrix of $D$ in this basis is
$$\begin{pmatrix} 0 & \sqrt3 & 0 \\ 0 & 0 & \sqrt{15} \\ 0 & 0 & 0 \end{pmatrix}.$$
6. The basis is orthonormal and the matrix is real, so by the [[matrix of the adjoint|0DBTE6HVBD]] the matrix of $D^*$ is the transpose. Hence $D^* e_0 = \sqrt 3\, e_1$, $D^* e_1 = \sqrt{15}\, e_2$ and $D^* e_2 = 0$.
7. We go back to the monomials. Since $1 = \sqrt2\, e_0$, we get $D^*(1) = \sqrt6\, e_1 = \sqrt6 \sqrt{\tfrac32}\, x = 3x$.
8. Since $x = \sqrt{\tfrac23}\, e_1$, we get $D^*(x) = \sqrt{\tfrac23} \sqrt{15}\, e_2 = \sqrt{10} \sqrt{\tfrac58}\, (3x^2 - 1) = \tfrac52 (3x^2 - 1)$.
9. Since $x^2 = \tfrac13 (3x^2 - 1) + \tfrac13 = \tfrac13 \sqrt{\tfrac85}\, e_2 + \tfrac{\sqrt2}{3}\, e_0$, we get $D^*(x^2) = \tfrac{\sqrt2}{3} \sqrt3\, e_1 = \tfrac{\sqrt6}{3} \sqrt{\tfrac32}\, x = x$.
10. We check the defining identity for $p = x^2$ and $q = x$:
$$\ip{Dp}{q} = \int_{-1}^{1} 2x^2 \, dx = \tfrac43, \qquad \ip{p}{D^* q} = \int_{-1}^{1} x^2 \cdot \tfrac52 (3x^2 - 1) \, dx = \tfrac52 \left(\tfrac65 - \tfrac23\right) = \tfrac43.$$
11. Last, $D$ is not normal. We have $D D^*(1) = D(3x) = 3$, but $D^* D(1) = D^*(0) = 0$. So $D D^* \neq D^* D$, and $D$ is not [[normal|0ENZN5G4CV]].

## Remarks

The example shows how to find an adjoint on a function space: choose an orthonormal basis, transpose, and translate back.
The answer looks strange at first, since $D$ lowers the degree while $D^*$ raises it.

Integration by parts explains part of the picture:
$$\ip{p'}{q} = p(1) q(1) - p(-1) q(-1) - \ip{p}{q'}.$$
If the boundary term were always $0$, the adjoint would be $-D$.
On $\mathcal{P}_2$ the boundary term is not $0$, and $D^*$ is not $-D$: for example $D^*(1) = 3x$, while $-D(1) = 0$.
The boundary term is $0$ when $p$ or $q$ is zero at both ends, and this is why $-D$ appears as the adjoint of $D$ in the theory of differential equations.

The adjoint also depends on the interval.
With $\int_0^1 p q \, dx$ in place of $\int_{-1}^{1} p q \, dx$, the orthonormal basis changes, and the same map $D$ gets a different adjoint.

Both $D$ and $D^*$ are nilpotent, and a nonzero nilpotent operator is never normal.
The [[complex spectral theorem|04CW1P44VD]] gives the reason for matrices viewed over $\mathbb{C}$: a normal matrix with only the eigenvalue $0$ is diagonal with zeros in some orthonormal basis, so it is $0$.

## Explanations

### L1 human

Differentiation sends $x^2$ to $2x$, $x$ to $1$ and $1$ to $0$.
On polynomials, an integral from $-1$ to $1$ plays the part of the dot product.
The adjoint of differentiation is a new map that gives the same integrals when it acts on the other polynomial.
It sends $1$ to $3x$, so it raises the degree, while differentiation lowers it.

### L2 human

The method works for any operator on a space with an inner product: find an orthonormal basis, write the matrix, take the conjugate transpose, translate back, and check one pair of vectors.
Here the basis was the normalized Legendre polynomials, and the check with $p = x^2$ and $q = x$ gave $\tfrac43$ on both sides.
The same method computes adjoints of differential operators, which is a standard step in the study of boundary value problems.
Watch out: the transpose of the matrix in the monomial basis $1, x, x^2$ is not the matrix of $D^*$, because that basis is not orthonormal.
In the monomial basis the matrix of $D$ is
$$\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix},$$
and the first column of its transpose is $(0, 1, 0)$, which would send $1$ to $x$, while the correct value is $D^*(1) = 3x$.

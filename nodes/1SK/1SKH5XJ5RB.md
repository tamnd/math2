---
tag: 1SKH5XJ5RB
kind: example
name: Eigenvalues of the derivative
msc: ["15A18", "34L10"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0BQAA2BK3Q, 0N6960W0BV, 0G0RFPG8HR, 0J5EMJRRFM]
illustrates: [0QEM68Y0DE]
uses: [0ZND7NQ970, 0B5H4208Z9, 0AYEPBQMAW, 0BZ81AJNWF, 0K1KKMFHYH]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Derivative operator example
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Example

Let $V = C^\infty(\mathbb{R})$ be the real vector space of smooth functions $\mathbb{R} \to \mathbb{R}$, and let $D \colon V \to V$ be the derivative, $Df = f'$.
We find the eigenvalues of $D$ on $V$, and then on the small space $P_2$ of polynomials of degree at most $2$.

*On all smooth functions.*

1. $D$ is linear, because $(af + bg)' = af' + bg'$ for real numbers $a, b$.
2. Let $\lambda \in \mathbb{R}$ and $f(x) = e^{\lambda x}$, which is not the zero function.
   The chain rule gives $Df = \lambda e^{\lambda x} = \lambda f$.
3. So every real $\lambda$ is an [[eigenvalue|0ZND7NQ970]] of $D$, with the [[eigenvector|0B5H4208Z9]] $e^{\lambda x}$.
4. Conversely, suppose $f' = \lambda f$, and put $g(x) = f(x) e^{-\lambda x}$.
   The product rule gives $g' = (f' - \lambda f) e^{-\lambda x} = 0$, so $g$ is a constant $c$, by the mean value theorem.
5. So $f = c e^{\lambda x}$, and the [[eigenspace|0AYEPBQMAW]] $E_\lambda$ is the line spanned by $e^{\lambda x}$.

*On polynomials of degree at most 2.*

6. The derivative of a polynomial of degree at most $2$ is again such a polynomial, so $D$ restricts to $P_2$.
   We use the basis $1, x, x^2$.
7. We have $D1 = 0$, $Dx = 1$ and $Dx^2 = 2x$, and these images give the columns of the matrix
$$[D] = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}.$$
8. The matrix $tI - [D]$ is upper triangular with diagonal entries $t, t, t$.
   By the [[determinant of a triangular matrix|0K1KKMFHYH]], the [[characteristic polynomial|0BZ81AJNWF]] is $p_D(t) = t^3$.
9. So the only eigenvalue of $D$ on $P_2$ is $0$, and its eigenvectors are the nonzero constants.
   Check another way: $D^3 p = p''' = 0$ for every $p \in P_2$, so $D$ is nilpotent, and a nilpotent map can only have the eigenvalue $0$.

## Remarks

The two answers look opposite, but they agree.
The eigenvectors $e^{\lambda x}$ with $\lambda \ne 0$ are not polynomials, so none of them lies in $P_2$, and only $\lambda = 0$ survives.
On $P_2$ the eigenvalue $0$ is a triple root of $p_D$, but its eigenspace is only the line of constants.
So its algebraic multiplicity is $3$ and its geometric multiplicity is $1$.
On $P_n$, the polynomials of degree at most $n$, the same argument gives $p_D(t) = t^{n+1}$.

On the whole space $C^\infty(\mathbb{R})$ the derivative has eigenvalues but no characteristic polynomial, because the space is infinite-dimensional.
The square $D^2$ has more eigenvectors than $D$: for example $D^2 \sin = -\sin$ and $D^2 \cos = -\cos$, so $-1$ is an eigenvalue of $D^2$, while $\sin$ is not an eigenvector of $D$.
If we allow complex-valued functions, then $e^{\lambda x}$ with $\lambda \in \mathbb{C}$ makes every complex number an eigenvalue of $D$.

## Explanations

### L1 human

The function $e^{2x}$ has derivative $2e^{2x}$, which is $2$ times the function itself.
So differentiation only stretches it by $2$, and $e^{2x}$ is an eigenvector of the derivative with eigenvalue $2$.
The same works for every number in place of $2$.
This is why exponential functions solve equations such as $y' = 3y$.

### L2 human

The typical use is to solve the equation $y' = \lambda y$, and systems $y' = Ay$ built from such equations.
Steps 4 and 5 say that the solutions of $y' = \lambda y$ are exactly the functions $c e^{\lambda x}$.
On a finite-dimensional space of polynomials the picture changes: differentiation lowers the degree, so it is nilpotent, and $0$ is its only eigenvalue.
Watch out: a polynomial such as $x^2$ is never an eigenvector, because $Dx^2 = 2x$ is not a multiple of $x^2$.

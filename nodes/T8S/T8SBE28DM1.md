---
tag: T8SBE28DM1
kind: concept
name: Monodromy of the hypergeometric equation
msc: ["33C05", "34M35"]
specializes: [C8HD62AB6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function
---

## Summary

The monodromy of the [[hypergeometric differential equation|W8VE25R5A7]] records how a basis of solutions changes under analytic continuation along closed loops.
The loops go around the singular points $0$, $1$ and $\infty$.
It is a representation of the [[fundamental group|S1XK3HXHFX]] of the thrice-punctured sphere, a free group on two generators, into $\mathrm{GL}_2(\C)$.
It is the special case of [[monodromy|C8HD62AB6Q]] that Riemann used to study the hypergeometric function.
It decides, for example, when all solutions are algebraic functions.

## Explanations

### L1 human

Solutions of the hypergeometric equation are not single-valued: following a solution once around the point $1$ can bring it back as a different solution.
Since the solutions form a two-dimensional space, each loop acts on it by a $2 \times 2$ matrix.
Collecting these matrices for all loops gives the monodromy group.
For example, when $a = b = 1$ and $c = 2$ the solutions are spanned by $1/z$ and $\log(1 - z)/z$, and going around $z = 1$ adds a multiple of $2\pi i / z$ to the second one.
Riemann showed that this matrix data, together with the local exponents, nearly determines the equation and its solutions.

### L2 human

The local monodromy around each singular point has eigenvalues $e^{2\pi i \rho}$, where $\rho$ runs over the two exponents at that point.
The monodromy is irreducible exactly when none of $a$, $b$, $c - a$, $c - b$ is an integer.
In the irreducible case, the representation is determined up to conjugacy by the three pairs of local eigenvalues, a fact known as rigidity.
Finite monodromy groups give algebraic solutions, and these are classified by [[Schwarz's list|W0MJ51242N]].

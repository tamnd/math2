---
tag: XQ8DYKW4SH
kind: statement
role: theorem
name: Fredholm's theorem
msc: [45B05, 47A53]
uses: [WWMWX7AD4V, DEYYNVCV9J, W6CYS54QXS, XEZXGBT42J, DC7HMHVREP, 4HH8C9V8JQ, M2NEP1K5AE, 8HWGKWD6ZM, JEPDM5B5FC]
about: [DEYYNVCV9J]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm%27s_theorem
same_as:
  wikidata: Q3984069
  wikipedia: Fredholm's theorem
---

## Statement

Let $a < b$ and let $K \in L^2([a, b] \times [a, b])$ be a [[square-integrable kernel|WWMWX7AD4V]].
Let $K^*(x, y) = \overline{K(y, x)}$ be the adjoint kernel, and let $\mu \in \C$.
Consider, in $L^2[a, b]$, the [[Fredholm equation of the second kind|DEYYNVCV9J]] and its [[adjoint equation|XEZXGBT42J]]
$$\varphi(x) - \mu \int_a^b K(x, y) \varphi(y) \, dy = f(x), \qquad \psi(x) - \overline{\mu} \int_a^b K^*(x, y) \psi(y) \, dy = g(x).$$
Then:

1. Either the first equation has exactly one solution $\varphi \in L^2[a, b]$ for every $f \in L^2[a, b]$, or the [[homogeneous equation|W6CYS54QXS]] with $f = 0$ has a nonzero solution.
2. The homogeneous equation ($f = 0$) and the homogeneous adjoint equation ($g = 0$) have the same finite number of linearly independent solutions.
3. Assume the homogeneous equation has a nonzero solution. Then the first equation is solvable if and only if $\int_a^b f \overline{\psi} = 0$ for every solution $\psi$ of the homogeneous adjoint equation.
4. The set of [[characteristic values|DC7HMHVREP]] of $K$ has no accumulation point in $\C$. These are the $\mu$ for which the homogeneous equation has a nonzero solution.

## Remarks

Let $T$ be the integral operator with kernel $K$; it is a [[compact operator|M2NEP1K5AE]] on $L^2[a, b]$, and its adjoint is the integral operator with kernel $K^*$.
For $\mu = 0$ the statements are trivial, and for $\mu \ne 0$ they are statements about $I - \mu T$ with $\mu T$ compact.
One proof approximates $K$ in $L^2$ by a degenerate kernel $K_0$ with $\abs{\mu} \norm{K - K_0} < 1$, with operator $T_0$.
Then $I - \mu (T - T_0)$ is invertible by a Neumann series, and the equation reduces to a finite linear system.
The [[Fredholm alternative|4HH8C9V8JQ]] for matrices applies to that system.

Example: on $[0, 1]$ with $K(x, y) = xy$ and $\mu = 3$, the homogeneous equation has the solution $\varphi(x) = x$, and $K^* = K$.
The equation $\varphi(x) - 3 \int_0^1 x y \varphi(y) \, dy = f(x)$ is solvable exactly when $\int_0^1 f(x) \, x \, dx = 0$; for instance $f = 1$ fails this, and indeed integrating $\varphi - 3x \int_0^1 y \varphi = 1$ against $x$ gives the contradiction $0 = 1/2$.

The square-integrability of $K$ matters because it makes $T$ compact.
For the identity operator on $L^2[a, b]$, which is bounded but not compact and not given by a square-integrable kernel, the equation $\varphi - \varphi = 0$ has infinitely many independent solutions, against part 2.

## Explanations

### L1 human

An integral equation of the second kind behaves like a square system of linear equations.
Either it always has exactly one solution, or its homogeneous version has nonzero solutions.
In the second case, a right-hand side is allowed exactly when it is perpendicular to all solutions of the adjoint homogeneous equation, just as for matrices.

### L2 human

These are Fredholm's results, obtained first with his determinants for continuous kernels and later extended to square-integrable kernels.
In the language of operators, they say that $I - \mu T$ is a [[Fredholm operator|8HWGKWD6ZM]] of index $0$ when $T$ is compact.
They also say that its image is the orthogonal complement of the kernel of its adjoint.
Part 4 is the statement that the nonzero spectrum of a compact operator is discrete, as in the [[spectral theory of compact operators|JEPDM5B5FC]].
They are the reason why boundary value problems that reduce to integral equations of the second kind have a solvability theory as clean as linear algebra.

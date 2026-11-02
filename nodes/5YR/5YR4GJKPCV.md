---
tag: 5YR4GJKPCV
kind: statement
role: theorem
name: Hille–Yosida theorem
msc: [47D06, 34G10]
uses: [0BDTTM24DP, VM7B38PA87, BCJHNHKQFG, J5YNNKSB9P, EVF180QJXY, XPWE94BV6N, 60HSWZBTK9]
about: [EVF180QJXY, 60HSWZBTK9]
sources:
  - url: https://en.wikipedia.org/wiki/Hille–Yosida_theorem
same_as:
  wikidata: Q974405
  wikipedia: Hille–Yosida theorem
---

## Statement

Let $X$ be a real or complex [[Banach space|0BDTTM24DP]].
Let $A \colon D(A) \to X$ be a linear operator with domain $D(A) \subseteq X$.
Then $A$ is the [[generator|60HSWZBTK9]] of a [[strongly continuous|EVF180QJXY]] [[contraction semigroup|XPWE94BV6N]] $(T(t))_{t \ge 0}$ on $X$ if and only if the following two conditions hold.

1. $A$ is a [[closed operator|VM7B38PA87]] and is [[densely defined|BCJHNHKQFG]].
2. Every real $\lambda > 0$ lies in the [[resolvent set|J5YNNKSB9P]] of $A$, and $\norm{(\lambda I - A)^{-1}} \le \dfrac{1}{\lambda}$.

## Remarks

The necessity comes from the resolvent formula $(\lambda I - A)^{-1} x = \int_0^\infty e^{-\lambda t} T(t) x \, dt$, whose norm is at most $\norm{x} / \lambda$ when $\norm{T(t)} \le 1$.
For the converse, one forms the Yosida approximations $A_\lambda = \lambda A (\lambda I - A)^{-1} = \lambda^2 (\lambda I - A)^{-1} - \lambda I$.
They are bounded operators, the exponentials $e^{t A_\lambda}$ are contractions, and they converge strongly as $\lambda \to \infty$ to a semigroup with generator $A$.
The general form concerns semigroups with $\norm{T(t)} \le M e^{\omega t}$ for constants $M \ge 1$ and $\omega \in \R$.
The operator $A$ generates such a semigroup if and only if it is closed and densely defined, $(\omega, \infty)$ lies in its resolvent set, and $\norm{(\lambda I - A)^{-n}} \le M (\lambda - \omega)^{-n}$ for all $\lambda > \omega$ and $n \ge 1$.
Example: on $X = \C$, the operator $A x = a x$ with $\operatorname{Re} a \le 0$ satisfies $\abs{(\lambda - a)^{-1}} \le 1/\lambda$ for $\lambda > 0$, and it generates the contractions $T(t) = e^{a t}$.
If $a > 0$ is real, then $\lambda = a$ is not in the resolvent set, and indeed $e^{a t} > 1$ for $t > 0$, so no contraction semigroup has this generator.
The [[Lumer–Phillips theorem|Z2N8MPD8DH]] replaces condition 2 by dissipativity and a range condition, which are often easier to check.

## Explanations

### L1 human

Many evolution equations have the form $u'(t) = A u(t)$, where $A$ is an unbounded operator such as a second derivative.
One wants a solution map $T(t)$ that sends the initial state to the state at time $t$.
The theorem says exactly which operators $A$ give such a family of maps that never increases the norm.
The test only uses the inverse of $\lambda I - A$, which is often easy to study.

### L2 human

The theorem turns an abstract Cauchy problem $u' = A u$, $u(0) = u_0$, in a [[Banach space|0BDTTM24DP]] into a question about the resolvent of $A$.
For a [[densely defined|BCJHNHKQFG]] closed operator, the resolvent bound is checked by solving the stationary equation $\lambda u - A u = f$ with an a priori estimate $\lambda \norm{u} \le \norm{f}$.
This is how one shows that the heat equation and many parabolic equations are well posed.
The semigroup is then the abstract replacement for the matrix exponential $e^{tA}$ of a system of linear ordinary differential equations.
The [[Lumer–Phillips theorem|Z2N8MPD8DH]] is the form used most often in Hilbert spaces.

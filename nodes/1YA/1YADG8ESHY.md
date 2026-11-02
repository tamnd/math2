---
tag: 1YADG8ESHY
kind: statement
role: theorem
name: Favard's theorem
msc: [42C05, 44A60]
uses: [DYR1QFNGNJ, 0FYX44GP92]
about: [0FYX44GP92]
sources:
  - url: https://en.wikipedia.org/wiki/Favard%27s_theorem
same_as:
  wikidata: Q5438430
  wikipedia: Favard's theorem
---

## Statement

Let $(a_n)_{n \ge 0}$ be real numbers and let $(b_n)_{n \ge 1}$ be positive real numbers.
Define polynomials by $p_{-1} = 0$, $p_0 = 1$ and the [[recurrence|0FYX44GP92]]
$$p_{n+1}(x) = (x - a_n)\, p_n(x) - b_n\, p_{n-1}(x) \qquad (n \ge 0).$$
Then there is a positive [[Borel measure|DYR1QFNGNJ]] $\mu$ on $\R$ with infinite support and all moments finite such that
$$\int_\R p_m(x)\, p_n(x)\, d\mu(x) = 0 \quad \text{for } m \ne n.$$

## Remarks

The proof defines a linear functional $L$ on polynomials by $L(1) = 1$ and $L(p_n) = 0$ for $n \ge 1$, which is possible since $p_n$ is monic of degree $n$.
The recurrence gives $L(p_m p_n) = 0$ for $m \ne n$ and $L(p_n^2) = b_1 b_2 \cdots b_n > 0$, so $L$ is positive on nonzero squares of polynomials.
Then $L(f) \ge 0$ for every polynomial $f \ge 0$ on $\R$, since such $f$ is a sum of two squares, and the Hamburger moment problem gives a measure $\mu$ with $L(f) = \int f\, d\mu$.
The measure need not be unique.
It is unique when the moment problem is determinate, for instance when $(a_n)$ and $(b_n)$ are bounded, and then $\mu$ has compact support.
Example: $a_n = 0$ and $b_n = \frac{1}{4}$ give the monic Chebyshev polynomials of the second kind, and $\mu$ is the semicircle measure $\frac{2}{\pi} \sqrt{1 - x^2}\, dx$ on $[-1, 1]$.
The hypothesis $b_n > 0$ is needed.
For orthogonal polynomials of a positive measure with infinite support, $b_n = \frac{\int p_n^2\, d\mu}{\int p_{n-1}^2\, d\mu} > 0$, so a recurrence with some $b_n \le 0$ cannot come from such a measure.

## Explanations

### L1 human

Orthogonal polynomials always satisfy a three-term recurrence.
Favard's theorem says the converse: any polynomials built by such a recurrence, with positive coefficients in the right place, are orthogonal for some weight.
So one can produce orthogonal polynomials just by choosing two sequences of numbers.

### L2 human

The theorem identifies orthogonal polynomial sequences on the real line with pairs of sequences $(a_n)$, $(b_n)$ with $b_n > 0$, that is, with Jacobi matrices.
In operator language, $\mu$ is a spectral measure of the Jacobi operator with diagonal $a_n$ and off-diagonal $\sqrt{b_n}$.
It reverses the [[three-term recurrence|YRYWCP9TYV]], and its proof reduces to the Hamburger moment problem.
It is used to show that families defined by recurrences, such as many in the Askey scheme, are orthogonal before the weight is known.

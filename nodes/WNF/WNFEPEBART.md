---
tag: WNFEPEBART
kind: statement
role: theorem
name: Antithetic variates
msc: [65C05]
uses: [A01GEGWKVB, 0AREFQ9Z65, 0477R9PYAE, 0KBFAWYRTE, S8X2N1DW8P]
about: [A01GEGWKVB]
sources:
  - url: https://en.wikipedia.org/wiki/Antithetic_variates
same_as:
  wikidata: Q3554719
  wikipedia: Antithetic variates
---

## Statement

Let $f \colon (0, 1) \to \R$ be monotone (non-decreasing or non-increasing) with $\int_0^1 f(u)^2\, du < \infty$, and let $U$ have the [[uniform distribution|0AREFQ9Z65]] on $(0, 1)$.
Let $Z = \frac12 \bigl( f(U) + f(1 - U) \bigr)$.
Then:

1. $\mathbb E Z = \mathbb E f(U) = \int_0^1 f(u)\, du$;
2. $\operatorname{Cov}\bigl(f(U), f(1 - U)\bigr) \le 0$;
3. $\operatorname{Var} Z \le \frac12 \operatorname{Var} f(U)$.

Both $n$ copies of $Z$ and $2n$ copies of $f(U)$ need $2n$ evaluations of $f$.
The average of $n$ independent copies of $Z$ is at least as accurate as that of $2n$ independent copies of $f(U)$.

## Remarks

Clause 1 holds because $1 - U$ is uniform on $(0, 1)$ too.
For clause 2, if $f$ is non-decreasing then $u \mapsto f(1 - u)$ is non-increasing, and for a non-decreasing $a$ and a non-increasing $b$ one has $\mathbb E[a(U) b(U)] \le \mathbb E a(U)\, \mathbb E b(U)$, the integral form of [[Chebyshev's sum inequality|S8X2N1DW8P]].
This in turn follows from $\mathbb E\bigl[(a(U) - a(V))(b(U) - b(V))\bigr] \le 0$ for an independent copy $V$ of $U$, since the two factors have opposite signs.
Clause 3: $\operatorname{Var} Z = \frac14 \bigl( 2 \operatorname{Var} f(U) + 2 \operatorname{Cov}(f(U), f(1-U)) \bigr) \le \frac12 \operatorname{Var} f(U)$, using $\operatorname{Var} f(1 - U) = \operatorname{Var} f(U)$.
Example: for $f(u) = e^u$, $\operatorname{Var} f(U) \approx 0.2420$ while $\operatorname{Var} Z \approx 0.0039$, a gain of a factor of about $30$ over $2$ independent samples.
Monotonicity is needed: for $f(u) = (u - \frac12)^2$ one has $f(1 - u) = f(u)$, so $Z = f(U)$ and $\operatorname{Var} Z = \operatorname{Var} f(U)$, twice the variance of the average of two independent samples.

## Explanations

### L1 human

The idea is to sample in pairs that are opposite to each other: $U$ and $1 - U$.
If one value of the function is too high, its partner tends to be too low, and the errors partly cancel in the average.
For a function that always increases or always decreases, the method is guaranteed not to hurt and often helps a lot.

### L2 human

Antithetic variates is one of the simplest [[variance reduction|A01GEGWKVB]] techniques, with no extra modelling and almost no extra cost.
The same idea applies to normal inputs with the pair $Z$ and $-Z$, and to simulations driven by many uniforms, replacing each $U_j$ by $1 - U_j$.
In the multivariate case the guarantee holds when the output is a monotone function of each input separately, but for general outputs the method can increase the variance.
Combined with inverse transform sampling, which is monotone, it yields negatively correlated pairs from any distribution.

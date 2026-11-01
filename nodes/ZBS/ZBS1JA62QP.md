---
tag: ZBS1JA62QP
kind: statement
role: theorem
name: Bernstein's theorem on monotone functions
msc: [26A48, 44A10]
uses: [QQSPWH4NG9, 0V49JEZW06, 0J0FCWV32D]
about: [QQSPWH4NG9]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%27s_theorem_on_monotone_functions
same_as:
  wikidata: Q3527015
  wikipedia: Bernstein's theorem on monotone functions
---

## Statement

Let $f \colon (0, \infty) \to \R$.
Call $f$ completely monotone if $f$ is infinitely differentiable and $(-1)^k f^{(k)}(x) \ge 0$ for all integers $k \ge 0$ and all $x > 0$.
Then $f$ is completely monotone if and only if there is a positive Borel measure $\mu$ on $[0, \infty)$ with the following property.
For every $x > 0$ the integral below converges and
$$f(x) = \int_{[0, \infty)} e^{-tx} \, d\mu(t).$$

## Remarks

So the completely monotone functions are exactly the [[Laplace transforms|0V49JEZW06]] of positive measures.
The "if" direction is direct: differentiating under the integral sign gives $(-1)^k f^{(k)}(x) = \int t^k e^{-tx} \, d\mu(t) \ge 0$.
The "only if" direction is the hard part; one proof approximates $f$ by sums built from its derivatives and uses a compactness argument for measures.
Example: $f(x) = 1/x$ is completely monotone on $(0, \infty)$, and $1/x = \int_0^\infty e^{-tx} \, dt$, so $\mu$ is Lebesgue measure on $[0, \infty)$.
By $x \mapsto -x$, the theorem also describes [[absolutely monotonic functions|QQSPWH4NG9]] on $(-\infty, 0)$ as integrals $\int e^{tx} \, d\mu(t)$.

## Explanations

### L1 human

A function whose derivatives alternate in sign forever looks very special.
Bernstein's theorem says that these functions are exactly the mixtures, with nonnegative weights, of decaying [[exponential functions|0J0FCWV32D]] $e^{-tx}$.

### L2 human

The theorem links a condition on derivatives with a positivity condition on a measure.
It is used in probability, where completely monotone functions are Laplace transforms of distributions on $[0, \infty)$, and in the theory of positive definite functions.
If $f$ is also continuous on $[0, \infty)$, then $\mu$ is finite and $\mu([0, \infty)) = f(0)$.

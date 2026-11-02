---
tag: V5EPT2PX9Z
kind: statement
role: theorem
name: Abel's summation formula
msc: [40A05, 11A25]
uses: [06SKCHDQT5, 0QM4TXT3DR, 08Y1BBQTK9]
sources:
  - url: https://en.wikipedia.org/wiki/Abel%27s_summation_formula
same_as:
  wikidata: Q1659643
  wikipedia: Abel's summation formula
---

## Statement

Let $(a_n)_{n \ge 1}$ be a sequence of complex numbers, and for real $t$ put $A(t) = \sum_{1 \le n \le t} a_n$.
Let $x \ge 1$ be a real number, and let $\varphi$ be a [[continuously differentiable|06SKCHDQT5]] complex-valued function on $[1, x]$.
Then
$$\sum_{1 \le n \le x} a_n \varphi(n) = A(x) \varphi(x) - \int_1^x A(t) \varphi'(t) \, dt.$$

## Remarks

The function $A$ is constant on each interval $[k, k+1)$, so the integral splits as $\sum_k A(k) (\varphi(k+1) - \varphi(k))$ plus a last piece up to $x$.
Rearranging this finite sum gives the left side; this is summation by parts.
The formula is the discrete analogue of [[integration by parts|08Y1BBQTK9]], and it is integration by parts for the Riemann–Stieltjes integral $\int \varphi \, dA$.
Example: with $a_n = 1$ and $\varphi(t) = 1/t$, one has $A(t) = \floor{t}$, and
$$\sum_{1 \le n \le x} \frac{1}{n} = \frac{\floor{x}}{x} + \int_1^x \frac{\floor{t}}{t^2} \, dt.$$
Writing $\floor{t} = t - \{t\}$ shows that the harmonic numbers minus the logarithm converge.

## Explanations

### L1 human

Abel's summation formula turns a weighted sum $\sum a_n \varphi(n)$ into an integral of the partial sums $A(t)$.
It is useful when the partial sums of $a_n$ are well understood but the terms themselves are irregular.
It plays the role of integration by parts for sums.

### L2 human

In analytic number theory one often knows a counting function $A(x)$, such as the number of primes up to $x$, and wants sums like $\sum_{p \le x} 1/p$.
Abel's formula transfers estimates for $A$ into estimates for such weighted sums.
It also extends the [[Riemann zeta function|1XWBY4N0VT]] to a meromorphic function on $\operatorname{Re}(s) > 0$ with a single pole at $s = 1$, by taking $a_n = 1$ and $\varphi(t) = t^{-s}$.
The [[Dirichlet's test|0V9ME8GQE7]] and [[Abel's test|0CN97GADE5]] for series rest on the same summation by parts.

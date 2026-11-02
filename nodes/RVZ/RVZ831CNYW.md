---
tag: RVZ831CNYW
kind: statement
role: theorem
name: Carleman's condition
msc: [44A60, "26E10"]
uses: [H0GY2J14CA, TBNCFXTMMW, Y9KH8P9JC0, 01XAHPADBA]
about: [H0GY2J14CA]
sources:
  - url: https://en.wikipedia.org/wiki/Carleman%27s_condition
same_as:
  wikidata: Q5041151
  wikipedia: Carleman's condition
---

## Statement

1. Let $\mu$ be a positive Borel measure on $\R$ with finite [[moments|01XAHPADBA]] $m_n = \int x^n \, d\mu(x)$ and with $m_{2n} > 0$ for all $n \ge 1$. If
$$\sum_{n=1}^{\infty} m_{2n}^{-1/(2n)} = \infty,$$
then the [[Hamburger moment problem|TBNCFXTMMW]] for $(m_n)$ is [[determinate|H0GY2J14CA]]: $\mu$ is the only positive measure on $\R$ with these moments.
2. Let $\mu$ be a positive Borel measure on $[0, \infty)$ with finite moments $m_n$ and with $m_n > 0$ for all $n \ge 1$. If
$$\sum_{n=1}^{\infty} m_{n}^{-1/(2n)} = \infty,$$
then the [[Stieltjes moment problem|Y9KH8P9JC0]] for $(m_n)$ is determinate: $\mu$ is the only positive measure on $[0, \infty)$ with these moments.

## Remarks

The proof goes through quasi-analytic functions.
The condition puts the Fourier–Stieltjes transform of the difference of two solutions in a quasi-analytic class.
That transform has all its derivatives zero at $0$, so it vanishes identically.
Example: for the standard normal distribution, $m_{2n} = (2n - 1)!! \le (2n)^n$, so $m_{2n}^{-1/(2n)} \ge (2n)^{-1/2}$ and the series diverges; the normal law is determined by its moments.
Example: if $\mu$ has bounded support in $[-R, R]$, then $m_{2n} \le m_0 R^{2n}$, so every term is at least $m_0^{-1/(2n)}/R$, and the series diverges.
The condition is sufficient but not necessary for determinacy.
The hypothesis $m_{2n} > 0$ only excludes the measures concentrated at $0$, which are determinate anyway.

## Explanations

### L1 human

The moments of a distribution may fail to identify it, but only if they grow very fast.
Carleman's condition is a precise way of saying that they do not grow too fast.
When it holds, two distributions with the same moments are the same distribution.

### L2 human

It is the test used in practice to check that a law is determined by its moments, for instance before applying the method of moments to prove convergence in distribution.
A simpler sufficient condition is that the moment generating function is finite near $0$, and that condition implies Carleman's.
In the other direction, Krein's condition gives indeterminacy for densities with very heavy tails, such as the log-normal density.

---
tag: K7TYSAWGPC
kind: definition
name: Wiman–Valiron theory
msc: ["30D20", "30D15"]
defines: BWZ1H4FAQG
uses: [0419794R0T, 0225QPWRRE]
sources:
  - url: https://en.wikipedia.org/wiki/Wiman%E2%80%93Valiron_theory
---

## Definition

Let $f(z) = \sum_{n \ge 0} a_n z^n$ be a transcendental [[entire function|0419794R0T]], that is, an entire function that is not a polynomial.
Wiman–Valiron theory studies $f$ through the following functions of $r > 0$:

1. the *maximum term* $\mu(r) = \max_{n \ge 0} \abs{a_n} r^n$;
2. the *central index* $\nu(r)$, the largest integer $n$ with $\abs{a_n} r^n = \mu(r)$.

## Remarks

The maximum exists because $\abs{a_n} r^n \to 0$ as $n \to \infty$ for every $r$, by convergence of the [[Taylor series|0225QPWRRE]].
The function $\nu(r)$ is nondecreasing, and $\nu(r) \to \infty$ because $f$ is not a polynomial.
Example: for $f = e^z$, $a_n = 1/n!$ and the ratio of consecutive terms is $r/(n+1)$, so $\nu(r) = \lfloor r \rfloor$ and $\mu(r) = r^{\nu(r)}/\nu(r)!$.
Non-example: for a polynomial of degree $d$, $\nu(r) = d$ for all large $r$, so it stays bounded; this is why the theory requires $f$ transcendental.
The Cauchy estimates give $\mu(r) \le M(r)$, where $M(r) = \max_{\abs{z} = r} \abs{f(z)}$.
The main result states that, for $r$ outside a set $E$ with $\int_E dr/r < \infty$ and $z_r$ with $\abs{z_r} = r$ and $\abs{f(z_r)} = M(r)$, one has $f^{(k)}(z_r) = \left(\nu(r)/z_r\right)^k f(z_r)\,(1 + o(1))$ as $r \to \infty$, for each fixed $k$.

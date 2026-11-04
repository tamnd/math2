---
tag: W8BV2CKYHP
kind: proof
name: Proof of the monotonicity of the integral
msc: [26A42]
proves: 0MBWQKM8QR
uses: [0N1JQXZXHC, 0QM4TXT3DR, 0HBY48G8G1, 04GM4NYXJB, 0A3GWZ86AY]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorem 1.27 and Definition 1.85
---

## Proof

We compare Riemann sums for the same tagged partition.

1. Let $a < b$, and let $f, g \colon [a, b] \to \mathbb{R}$ be [[Riemann integrable|0N1JQXZXHC]] with $f \le g$ on $[a, b]$. Let $I_f$ and $I_g$ be their [[integrals|0QM4TXT3DR]].
2. For each tagged partition $(P, t)$ with $P = (x_0, \dots, x_n)$, we have $f(t_i)(x_i - x_{i-1}) \le g(t_i)(x_i - x_{i-1})$ for each $i$. Adding gives $S(f, P, t) \le S(g, P, t)$ for the [[Riemann sums|0HBY48G8G1]].
3. Let $\varepsilon > 0$. Take $\delta_f > 0$ such that the Riemann sums of $f$ for tagged partitions of [[mesh|04GM4NYXJB]] less than $\delta_f$ are within $\varepsilon$ of $I_f$.
   Take $\delta_g > 0$ in the same way for $g$ and $I_g$. Let $\delta = \min(\delta_f, \delta_g)$.
4. By the [[Archimedean property|0A3GWZ86AY]], take $n$ with $n \delta > b - a$. The points $x_i = a + i(b - a)/n$ with tags $t_i = x_i$ give a tagged partition $(P, t)$ of mesh less than $\delta$.
5. By steps 2 and 3, $I_f - \varepsilon < S(f, P, t) \le S(g, P, t) < I_g + \varepsilon$. So $I_f < I_g + 2 \varepsilon$.
6. This holds for each $\varepsilon > 0$. Hence $I_f \le I_g$, that is, $\int_a^b f(x) \, dx \le \int_a^b g(x) \, dx$.

## Idea

For the same tagged partition, each Riemann sum of $f$ is at most the Riemann sum of $g$. Inequalities that hold for every approximation survive in the limit.

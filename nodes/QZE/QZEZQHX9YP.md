---
tag: QZEZQHX9YP
kind: proof
name: Proof of the triangle inequality for integrals
msc: [26A42]
proves: 0NR82KMYKD
uses: [0N1JQXZXHC, 0HBY48G8G1, 0A3GWZ86AY, 0QRQVH0CRW, 0C9S13WKMF, 00S7C68D51, 017DH8WXTE, 080RWVVSB6, 0MBWQKM8QR]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorem 1.31
---

## Proof

We first show that $|f|$ is integrable by Riemann's criterion, and then compare integrals.

1. Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be [[Riemann integrable|0N1JQXZXHC]] with integral $I$. We first show that $f$ is bounded.
   Take $\delta > 0$ such that each tagged partition of mesh less than $\delta$ has [[Riemann sum|0HBY48G8G1]] within $1$ of $I$.
2. By the [[Archimedean property|0A3GWZ86AY]], fix a partition $P = (x_0, \dots, x_n)$ with all subintervals shorter than $\delta$, and fix tags $t$.
3. Fix $i$ and $x \in [x_{i-1}, x_i]$. Let $t'$ be the tags $t$ with $t_i$ replaced by $x$. Both sums are within $1$ of $I$, so their difference $(f(x) - f(t_i))(x_i - x_{i-1})$ has absolute value less than $2$.
   So $|f(x)| < |f(t_i)| + \frac{2}{x_i - x_{i-1}}$. The largest of these $n$ bounds bounds $f$ on $[a, b]$.
4. Now let $Q$ be any partition and $J$ one of its subintervals. Let $M$ and $m$ be the supremum and infimum of $f$ on $J$, and $M'$ and $m'$ those of $|f|$.
5. For $x, y \in J$, both $f(x)$ and $f(y)$ lie in $[m, M]$. By the [[reverse triangle inequality|0C9S13WKMF]], $|f(x)| - |f(y)| \le |f(x) - f(y)| \le M - m$.
6. Fix $y \in J$. Step 5 says that $|f(y)| + (M - m)$ is an upper bound of $|f|$ on $J$, so $M' \le |f(y)| + (M - m)$.
   So $M' - (M - m)$ is a lower bound of $|f|$ on $J$, and $M' - (M - m) \le m'$. Hence $M' - m' \le M - m$.
7. Multiply by the length of $J$ and add over the subintervals of $Q$. For the [[Darboux sums|0QRQVH0CRW]], $U(|f|, Q) - L(|f|, Q) \le U(f, Q) - L(f, Q)$.
8. Let $\varepsilon > 0$. By [[Riemann's criterion|017DH8WXTE]] for the bounded integrable $f$, there is $Q$ with $U(f, Q) - L(f, Q) < \varepsilon$. By step 7, the same $Q$ works for $|f|$.
   Since $|f|$ is bounded, Riemann's criterion shows that $|f|$ is Riemann integrable.
9. By the [[linearity of the integral|080RWVVSB6]] with coefficients $-1$ and $0$, $-|f|$ is integrable with integral $-\int_a^b |f(x)| \, dx$.
10. By the definition of the [[absolute value|00S7C68D51]], $-|f(x)| \le f(x) \le |f(x)|$ for all $x$. By the [[monotonicity of the integral|0MBWQKM8QR]],
    $$-\int_a^b |f(x)| \, dx \le \int_a^b f(x) \, dx \le \int_a^b |f(x)| \, dx.$$
11. This says $\big| \int_a^b f(x) \, dx \big| \le \int_a^b |f(x)| \, dx$.

## Idea

Taking absolute values can only shrink the spread of values on a subinterval. So the gap between upper and lower sums of $|f|$ is at most that of $f$, and $|f|$ is integrable. The inequality then follows by integrating $-|f| \le f \le |f|$.

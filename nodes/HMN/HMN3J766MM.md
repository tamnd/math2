---
tag: HMN3J766MM
kind: proof
name: Proof of the Banach fixed point theorem by iteration
msc: [47H10]
proves: 0VK6VEH345
uses: [063W5JMY85, 08EWT7J0SC, 0MT2S0ZX4Y, 0MCK8K2D7Z, 06JYPJ4WHH, 01M6CW9VM6, 05APWSX53S, 0Q7K4AXE53]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_fixed-point_theorem
    locator: Proof
---

## Proof

We iterate $f$ from an arbitrary point and show that the iterates form a Cauchy sequence.

1. Let $(X, d)$ be a nonempty [[complete metric space|08EWT7J0SC]], and let $f \colon X \to X$ be a [[contraction|0MT2S0ZX4Y]] with constant $k \in [0, 1)$.
2. Let $x_0 \in X$, which exists since $X$ is nonempty. Put $x_{n+1} = f(x_n)$ for $n \ge 0$, and let $c = d(x_1, x_0)$.
3. We show $d(x_{n+1}, x_n) \le k^n c$ for all $n \ge 0$, by induction on $n$. For $n = 0$ this reads $c \le c$.
4. If it holds for $n$, then $d(x_{n+2}, x_{n+1}) = d(f(x_{n+1}), f(x_n)) \le k \, d(x_{n+1}, x_n) \le k^{n+1} c$.
5. Let $m > n \ge 0$. By the [[triangle inequality|01M6CW9VM6]] applied $m - n - 1$ times, $d(x_m, x_n) \le \sum_{j=n}^{m-1} d(x_{j+1}, x_j)$.
6. By step 3 and the [[sum of a finite geometric series|05APWSX53S]] with ratio $k \ne 1$, this sum is at most $k^n c \sum_{i=0}^{m-n-1} k^i = k^n c \, (1 - k^{m-n}) / (1 - k)$.
7. Since $0 \le k^{m-n}$, we get $d(x_m, x_n) \le k^n c / (1 - k)$ for all $m > n \ge 0$.
8. Since $0 \le k < 1$, [[$k^n \to 0$|0Q7K4AXE53]]. Let $\varepsilon > 0$, and choose $N$ with $k^N c / (1 - k) < \varepsilon$.
9. For $m > n \ge N$, step 7 gives $d(x_m, x_n) \le k^n c / (1 - k) \le k^N c / (1 - k) < \varepsilon$, since $k^n \le k^N$.
10. So $(x_n)$ is a [[Cauchy sequence|0MCK8K2D7Z]]. Since $X$ is complete, it [[converges|06JYPJ4WHH]] to some $x^* \in X$.
11. For each $n$, $d(f(x^*), x^*) \le d(f(x^*), f(x_n)) + d(x_{n+1}, x^*) \le k \, d(x^*, x_n) + d(x_{n+1}, x^*)$.
12. The right side of step 11 tends to $0$ as $n \to \infty$. So $d(f(x^*), x^*) < \varepsilon$ for every $\varepsilon > 0$, hence $d(f(x^*), x^*) = 0$.
13. A metric is positive on distinct points, so $f(x^*) = x^*$. Thus $x^*$ is a fixed point.
14. Let $y$ be a fixed point. Then $d(x^*, y) = d(f(x^*), f(y)) \le k \, d(x^*, y)$, so $(1 - k) \, d(x^*, y) \le 0$.
15. Since $1 - k > 0$ and $d(x^*, y) \ge 0$, we get $d(x^*, y) = 0$, so $y = x^*$. The fixed point is unique.
16. By steps 10 to 15, for each start $x_0$ the iterates converge to a fixed point, which is the unique fixed point $x^*$.
17. Fix $n \ge 0$ and let $m > n$. By the triangle inequality and step 7, $d(x_n, x^*) \le k^n c / (1 - k) + d(x_m, x^*)$.
18. Since $d(x_m, x^*) \to 0$ as $m \to \infty$, step 17 gives $d(x_n, x^*) \le k^n c / (1 - k) + \varepsilon$ for each $\varepsilon > 0$.
19. So $d(x_n, x^*) \le \dfrac{k^n}{1 - k} \, d(x_1, x_0)$ for all $n \ge 0$.

## Idea

Each application of $f$ shrinks the step between consecutive iterates by the factor $k$.
The steps add up to a geometric series, so the iterates form a Cauchy sequence. Completeness gives a limit, and the contraction property makes it a fixed point and the only one.

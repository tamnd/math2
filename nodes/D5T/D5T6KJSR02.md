---
tag: D5T6KJSR02
kind: proof
name: Proof of Chebyshev's inequality
msc: ["60E15"]
proves: 02HZ1BK3MW
uses: [05PWWHYBX5, 007QED3E0Y, 0VTN5RKNC5]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev's_inequality
    locator: Proof
---

## Proof

We apply Markov's inequality to the squared deviation.

1. Let $X$ be a real random variable with finite mean $\mu$ and finite [[variance|007QED3E0Y]] $\sigma^2$. Let $a > 0$.
2. Let $Y = (X - \mu)^2$. Then $Y$ takes values in $[0, \infty)$, and $E[Y] = \sigma^2$ by the definition of the variance.
3. For $u \ge 0$ and $a > 0$, $u \ge a$ holds if and only if $u^2 \ge a^2$, since squaring is increasing on $[0, \infty)$.
4. Apply step 3 to $u = \abs{X - \mu}$. This gives the equality of events $\set{\abs{X - \mu} \ge a} = \set{Y \ge a^2}$.
5. By [[Markov's inequality|05PWWHYBX5]] for $Y$ and the level $a^2 > 0$, $P(Y \ge a^2) \le E[Y]/a^2 = \sigma^2/a^2$.
6. By steps 4 and 5, $P(\abs{X - \mu} \ge a) \le \sigma^2/a^2$.
7. Now let $\sigma > 0$ be the [[standard deviation|0VTN5RKNC5]] and let $k > 0$. Then $a = k\sigma > 0$.
8. Step 6 with this $a$ gives $P(\abs{X - \mu} \ge k\sigma) \le \sigma^2/(k^2\sigma^2) = 1/k^2$.

## Idea

A large deviation $\abs{X - \mu} \ge a$ is the same event as a large squared deviation $(X - \mu)^2 \ge a^2$. Markov's inequality bounds the second event by the mean of the squared deviation, which is the variance.

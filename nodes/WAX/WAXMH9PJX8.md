---
tag: WAXMH9PJX8
kind: proof
name: Proof of the first derivative test
msc: [26A24]
proves: 01A2EGXJEM
uses: [026BJBQNGJ, 07ZMX4ANJS, 0NS8BP96QX, 00999TYPXB, 0Z9JB71BS0]
sources:
  - url: https://en.wikipedia.org/wiki/Derivative_test
---

## Proof

We apply the monotonicity test on each side of $c$.

1. Assume $f'(x) \le 0$ for $c - \delta < x < c$ and $f'(x) \ge 0$ for $c < x < c + \delta$.
2. The function $f$ is [[continuous|07ZMX4ANJS]] at each $x \ne c$, since it is differentiable there. It is continuous at $c$ by hypothesis.
3. Let $x \in (c, c + \delta)$. Then $f$ is continuous on $[c, x]$ and differentiable on $(c, x)$ with $f' \ge 0$ there.
4. By the [[nonnegative derivative test|026BJBQNGJ]] on the interval $[c, x]$, $f$ is increasing there. So $f(c) \le f(x)$.
5. Let $x \in (c - \delta, c)$. The function $-f$ is continuous on $[x, c]$ and differentiable on $(x, c)$.
6. By the [[constant multiple rule|0Z9JB71BS0]], $(-f)' = -f' \ge 0$ on $(x, c)$.
7. By the [[nonnegative derivative test|026BJBQNGJ]], $-f$ is increasing on $[x, c]$. So $-f(x) \le -f(c)$, that is, $f(c) \le f(x)$.
8. Steps 4 and 7 give $f(x) \ge f(c)$ for all $x$ with $|x - c| < \delta$. So $f$ has a [[local minimum|0NS8BP96QX]] at $c$.
9. Now assume the reversed inequalities: $f' \ge 0$ on $(c - \delta, c)$ and $f' \le 0$ on $(c, c + \delta)$.
10. Then $-f$ satisfies the hypotheses of step 1, since $(-f)' = -f'$. By step 8, $-f$ has a local minimum at $c$.
11. So $-f(x) \ge -f(c)$ near $c$, that is, $f(x) \le f(c)$. Thus $f$ has a [[local maximum|00999TYPXB]] at $c$.

## Idea

A function that does not increase up to $c$ and does not decrease after $c$ is lowest at $c$. The mean value theorem, through the monotonicity test, turns the sign conditions on $f'$ into these monotonicity facts. Continuity at $c$ lets the test include the point $c$ itself.

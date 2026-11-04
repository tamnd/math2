---
tag: G97DRHV0X7
kind: proof
name: Proof of the second derivative test
msc: [26A24]
proves: 0FZFHK97P7
uses: [0Y9D2FJRQ4, 0F1WR9C83K, 0TXTSEMHR5, 07J5X2T1ZX, 07ZMX4ANJS, 0NS8BP96QX, 00999TYPXB, 0Z9JB71BS0]
sources:
  - url: https://en.wikipedia.org/wiki/Derivative_test
    locator: Second-derivative test (single variable)
---

## Proof

We read off the sign of $f'$ near $c$ from $f''(c)$, then use strict monotonicity on each side.

1. Let $I$ be the open interval around $c$ on which $f$ is differentiable. Assume first that $f''(c) > 0$.
2. By the definition of the [[second derivative|0Y9D2FJRQ4]] and of the [[derivative|0F1WR9C83K]], $(f'(x) - f'(c))/(x - c) \to f''(c)$ as $x \to c$.
3. Since $f'(c) = 0$, this says $f'(x)/(x - c) \to f''(c)$ as $x \to c$.
4. Apply the definition of the [[limit|0TXTSEMHR5]] with the open interval $V = (0, 2 f''(c))$, which contains $f''(c)$.
5. This gives an open interval $U$ containing $c$ with $f'(x)/(x - c) \in V$ for $x \in U \cap I$, $x \ne c$. Choose $\eta > 0$ with $(c - \eta, c + \eta) \subseteq U \cap I$. Then $f'(x)/(x - c) > 0$ for $0 < |x - c| < \eta$.
6. So $f'(x) < 0$ for $c - \eta < x < c$, and $f'(x) > 0$ for $c < x < c + \eta$.
7. The function $f$ is [[continuous|07ZMX4ANJS]] on $I$, since it is differentiable on $I$.
8. Let $x \in (c, c + \eta)$. On $[c, x]$, $f$ is continuous, and $f' > 0$ on $(c, x)$.
9. By the [[positive derivative test|07J5X2T1ZX]], $f$ is strictly increasing on $[c, x]$. So $f(c) < f(x)$.
10. Let $x \in (c - \eta, c)$. On $[x, c]$, $-f$ is continuous, and $(-f)' = -f' > 0$ on $(x, c)$ by the [[constant multiple rule|0Z9JB71BS0]].
11. By the [[positive derivative test|07J5X2T1ZX]], $-f$ is strictly increasing on $[x, c]$. So $-f(x) < -f(c)$, that is, $f(c) < f(x)$.
12. By steps 9 and 11, $f(x) > f(c)$ for all $x \ne c$ with $|x - c| < \eta$. So $f$ has a strict [[local minimum|0NS8BP96QX]] at $c$.
13. Now assume $f''(c) < 0$. Then $-f$ is differentiable on $I$, $(-f)'(c) = 0$, and $(-f)''(c) = -f''(c) > 0$.
14. By step 12, $-f$ has a strict local minimum at $c$. So $f(x) < f(c)$ for $x \ne c$ near $c$, a strict [[local maximum|00999TYPXB]].

## Idea

Since $f'(c) = 0$, the second derivative is the limit of $f'(x)/(x - c)$. If it is positive, $f'$ has the sign of $x - c$ near $c$. So $f$ strictly falls before $c$ and strictly rises after $c$, which makes $c$ a strict minimum.

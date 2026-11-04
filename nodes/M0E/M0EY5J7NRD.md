---
tag: M0EY5J7NRD
kind: proof
name: Proof of the continuity of the inverse of a strictly monotone continuous function
msc: [26A48]
proves: 07BY47HG5S
uses: [0TR9SR9FTB, 00KAFBR32E, 0TK8Y3J5RW, 0P27W9RW0G, 0W8YHHGCJG]
sources:
  - url: https://www.jirka.org/ra/html/sec_monotonefunc.html
    locator: Proposition 3.6.6
---

## Proof

1. Let $x, x' \in I$ with $x \ne x'$. One is smaller, so $f(x) \ne f(x')$ since $f$ is [[strictly increasing|0TR9SR9FTB]]. So $f$ is injective, and $f^{-1} \colon J \to I$ is defined.
2. Claim: $J$ is an [[interval|0TK8Y3J5RW]]. Let $y_1, y_2 \in J$ and $y_1 \le z \le y_2$. If $z = y_1$ or $z = y_2$, then $z \in J$.
3. Otherwise $y_1 < z < y_2$. Write $y_1 = f(x_1)$ and $y_2 = f(x_2)$ with $x_1, x_2 \in I$. If $x_2 \le x_1$, then $y_2 \le y_1$, which is false. So $x_1 < x_2$.
4. Since $I$ is an interval, $[x_1, x_2] \subseteq I$, and $f$ is [[continuous|0P27W9RW0G]] on it. The [[intermediate value theorem|00KAFBR32E]] gives $c \in [x_1, x_2]$ with $f(c) = z$. So $z \in J$, and $J$ is an interval.
5. Write $g = f^{-1}$. Claim: $g$ is strictly increasing. Let $y < y'$ in $J$. If $g(y) \ge g(y')$, then $y = f(g(y)) \ge f(g(y')) = y'$, which is false. So $g(y) < g(y')$.
6. Now fix $y_0 \in J$ and $\varepsilon > 0$, and put $x_0 = g(y_0)$. We look for $\delta > 0$ as in the [[epsilon-delta form of continuity|0W8YHHGCJG]].
7. If $I$ has a point $p < x_0$, put $x_- = \max(p, x_0 - \frac{\varepsilon}{2})$. Then $p \le x_- < x_0$, so $x_- \in I$. Also $x_- > x_0 - \varepsilon$. Put $\delta_1 = y_0 - f(x_-)$, which is positive. If $I$ has no point below $x_0$, put $\delta_1 = 1$.
8. If $I$ has a point $q > x_0$, put $x_+ = \min(q, x_0 + \frac{\varepsilon}{2})$. Then $x_+ \in I$ and $x_0 < x_+ < x_0 + \varepsilon$. Put $\delta_2 = f(x_+) - y_0 > 0$. Otherwise put $\delta_2 = 1$.
9. Let $\delta = \min(\delta_1, \delta_2) > 0$. Let $y \in J$ with $\abs{y - y_0} < \delta$, and put $x = g(y)$. If $y = y_0$, then $x = x_0$.
10. Suppose $y < y_0$. By step 5, $x < x_0$, so $I$ has a point below $x_0$, and $x_-$ was defined in step 7. Then $y > y_0 - \delta_1 = f(x_-)$.
11. By step 5, $x = g(y) > g(f(x_-)) = x_-$. So $x_0 - \varepsilon < x_- < x < x_0$, and $\abs{x - x_0} < \varepsilon$.
12. Suppose $y > y_0$. In the same way, $x > x_0$, $x_+$ was defined, and $y < f(x_+)$. So $x_0 < x < x_+ < x_0 + \varepsilon$.
13. In all cases $\abs{g(y) - g(y_0)} < \varepsilon$. So $g$ is continuous at $y_0$, for each $y_0 \in J$.
14. Hence $J$ is an interval, and $f^{-1} \colon J \to I$ is continuous and strictly increasing.

## Idea

The image is an interval because the intermediate value theorem fills in every value between two attained values. For continuity of the inverse at $y_0 = f(x_0)$, take points $x_\pm$ of $I$ within $\varepsilon$ of $x_0$ on each side. Their images bracket $y_0$, and since $f^{-1}$ preserves order, every $y$ in that bracket goes back between $x_-$ and $x_+$.

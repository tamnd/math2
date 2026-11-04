---
tag: AWZTK9Y00A
kind: proof
name: Proof of Hoeffding's inequality via Hoeffding's lemma and the Chernoff bound
msc: ["60E15"]
proves: 0WPDNXGSSN
uses: [0XCE070V8B, 0DCT0QZVQ1, 0P7PTC8DDE, 0R46A1XY60, 0D7GRZ2ADX, 0E8HNVBCSP, 0044CPHJBV, 0RKW2X63YR, 07X1QA6BRW, 0RXX2PT1MQ, 0BS0NJPKVE, 0H5ZAZCX2T, 0KN2V7840E, 0P9BNBW2W3, 0NNRNGKMFM, 0WRZ170YEH, 014PEBGDYF]
sources:
  - url: https://en.wikipedia.org/wiki/Hoeffding's_inequality
    locator: Proof
  - url: https://en.wikipedia.org/wiki/Hoeffding's_lemma
---

## Proof

We first prove Hoeffding's lemma, a bound on the moment-generating function of a bounded centred variable. Then we apply the Chernoff bound to the centred sum.

Hoeffding's lemma. Let $X$ be a real random variable with $a \le X \le b$ [[almost surely|0R46A1XY60]], where $a < b$. Let $s \in \R$. We show $E[e^{s(X - E[X])}] \le e^{s^2 (b - a)^2/8}$.

1. $X$ is bounded almost surely, so it is integrable. Let $m = E[X]$ be its [[expected value|0DCT0QZVQ1]]. Since $a \le X \le b$ almost surely, $a \le m \le b$.
2. Let $Y = X - m$, $\alpha = a - m$ and $\beta = b - m$. Then $\alpha \le 0 \le \beta$, $\beta - \alpha = b - a > 0$, $\alpha \le Y \le \beta$ almost surely, and $E[Y] = 0$.
3. Let $y \in [\alpha, \beta]$ and $\lambda = (\beta - y)/(\beta - \alpha) \in [0, 1]$. Then $y = \lambda \alpha + (1 - \lambda) \beta$.
4. The [[exponential function is convex|0D7GRZ2ADX]]. Applied to $s\alpha$ and $s\beta$ with weight $\lambda$, it gives $e^{sy} \le \lambda e^{s\alpha} + (1 - \lambda) e^{s\beta}$. For $\lambda \in \set{0, 1}$ or $s = 0$, this is an equality.
5. Put $y = Y$ on the event $\set{\alpha \le Y \le \beta}$, which has probability $1$. Expectations ignore null sets. By [[linearity of expectation|0P7PTC8DDE]] and $E[Y] = 0$,
$$E[e^{sY}] \le \frac{\beta e^{s\alpha} - \alpha e^{s\beta}}{\beta - \alpha}.$$
6. Let $p = -\alpha/(\beta - \alpha) \in [0, 1]$ and $u = s(\beta - \alpha)$. Then $1 - p = \beta/(\beta - \alpha)$, $s\alpha = -pu$ and $s\beta = (1 - p)u$.
7. By step 6 and the [[exponential of a sum|0E8HNVBCSP]], the right side of step 5 is $(1 - p) e^{-pu} + p e^{(1 - p)u} = e^{-pu} (1 - p + p e^{u})$.
8. For real $v$, let $D(v) = 1 - p + p e^v$. If $p < 1$ then $D(v) \ge 1 - p > 0$. If $p = 1$ then $D(v) = e^v > 0$, as the [[exponential function is positive|0P9BNBW2W3]].
9. Let $L(v) = -pv + \ln D(v)$, with the [[natural logarithm|0044CPHJBV]]. Since [[the logarithm is the inverse of the exponential|0RKW2X63YR]], $e^{L(u)} = e^{-pu} D(u)$. So step 7 says $E[e^{sY}] \le e^{L(u)}$.
10. $D(0) = 1$, so $L(0) = 0$.
11. By the [[derivative of the logarithm|07X1QA6BRW]] and the [[chain rule|0RXX2PT1MQ]], $L'(v) = -p + q(v)$ with $q(v) = p e^v / D(v)$. So $L'(0) = -p + p = 0$.
12. Since $0 \le p e^v \le D(v)$, we have $0 \le q(v) \le 1$. Also $1 - q(v) = (1 - p)/D(v)$.
13. By the [[quotient rule|0BS0NJPKVE]], $q'(v) = p e^v (1 - p)/D(v)^2 = q(v) (1 - q(v))$. So $L''(v) = q(v)(1 - q(v))$.
14. For each real $r$, $r(1 - r) = 1/4 - (r - 1/2)^2 \le 1/4$. So $L''(v) \le 1/4$ for all $v$.
15. If $u = 0$, then $L(u) = 0 = u^2/8$. If $u \ne 0$, [[Taylor's theorem with the Lagrange remainder|0H5ZAZCX2T]] of degree $1$ at $0$ gives $\xi$ with $L(u) = L(0) + L'(0) u + L''(\xi) u^2/2$.
16. By steps 10, 11 and 14, $L(u) \le u^2/8 = s^2 (b - a)^2/8$.
17. The [[exponential function is increasing|0KN2V7840E]]. By steps 9 and 16, $E[e^{sY}] \le e^{s^2 (b - a)^2/8}$. This proves the lemma.

Hoeffding's inequality.

18. Let $X_1, \dots, X_n$ be [[independent|0XCE070V8B]] with $a_i \le X_i \le b_i$ almost surely, where $a_i < b_i$. Let $S_n = X_1 + \dots + X_n$ and fix $t > 0$.
19. Each $X_i$ is integrable by step 1. Let $m_i = E[X_i]$ and $Y_i = X_i - m_i$. By linearity, $E[S_n] = m_1 + \dots + m_n$, so $T := S_n - E[S_n] = Y_1 + \dots + Y_n$.
20. For Borel sets $B_i$, $\set{Y_i \in B_i} = \set{X_i \in B_i + m_i}$, and $B_i + m_i$ is Borel. So the definition of independence passes from the $X_i$ to the $Y_i$.
21. Let $c = \sum_{i=1}^n (b_i - a_i)^2 > 0$, and fix $s > 0$. By the [[product formula for moment-generating functions|0WRZ170YEH]], $M_T(s) = \prod_{i=1}^n E[e^{sY_i}]$.
22. By the lemma for each $X_i$ and the exponential of a sum, $M_T(s) \le \prod_{i=1}^n e^{s^2 (b_i - a_i)^2/8} = e^{s^2 c/8}$.
23. By the [[Chernoff bound|014PEBGDYF]] for $T$ at the level $t$, $P(T \ge t) \le e^{-st} M_T(s) \le e^{-st + s^2 c/8}$. Here $M_T$ is the [[moment-generating function|0NNRNGKMFM]] of $T$.
24. Choose $s = 4t/c > 0$. Then $-st + s^2 c/8 = -4t^2/c + 2t^2/c = -2t^2/c$.
25. So $P(S_n - E[S_n] \ge t) \le \exp\left(-2t^2 / \sum_{i=1}^n (b_i - a_i)^2\right)$.

## Idea

A bounded centred variable has a moment-generating function at most $e^{s^2 (b - a)^2/8}$. Convexity puts $e^{sY}$ below a chord, and a second-order Taylor bound controls the logarithm of the chord value. Independence multiplies these bounds for the sum, and the Chernoff bound with the best $s$ gives the Gaussian tail.

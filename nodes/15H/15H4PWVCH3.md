---
tag: 15H4PWVCH3
kind: proof
name: Proof of uniqueness of solutions for Lipschitz vector fields
msc: [34A12]
proves: 025PKW8AMR
uses: [055VVSN00V, 04SW7WECS8, 0NRQPQX3VA, 0NHGY0N0JB, 0WS1A8E2P9, 080RWVVSB6, 0MBWQKM8QR, 0RFWW56Y22, 0AXWET80YW]
sources:
  - url: https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality
    locator: lead section
---

## Proof

We first prove agreement near a point of agreement, and then spread it along $I$ with a supremum argument.

1. Lemma. Let $c < e$ and let $h : [c, e] \to \R^n$ be continuous. Then $\norm{\int_c^e h} \le \int_c^e \norm{h}$.
2. Proof: let $v = \int_c^e h$, and assume $v \ne 0$. By [[linearity of the integral|080RWVVSB6]], $\norm{v}^2 = \int_c^e v \cdot h$. By [[Cauchy–Schwarz|0RFWW56Y22]] and [[monotonicity|0MBWQKM8QR]], this is at most $\norm{v} \int_c^e \norm{h}$.
3. Let $w = \gamma_1 - \gamma_2$ and $u = \norm{w}$, a continuous function on $I$. We may assume $I$ has more than one point.
4. Local claim: if $t_1 \in I$ and $w(t_1) = 0$, there is $\delta > 0$ with $w = 0$ on $I \cap [t_1 - \delta, t_1 + \delta]$.
5. Proof of the claim. Let $p = (t_1, \gamma_1(t_1)) = (t_1, \gamma_2(t_1)) \in D$. Take a neighbourhood $V \subseteq D$ of $p$ and $K \ge 0$ as in the [[Lipschitz|055VVSN00V]] hypothesis. $V$ contains the open ball of some radius $\rho > 0$ around $p$.
6. The curves $\gamma_1, \gamma_2$ are continuous. So there is $\delta > 0$ with $K \delta < 1$ such that $(t, \gamma_k(t))$ lies within $\rho$ of $p$ for $k = 1, 2$ and $t \in I_\delta = I \cap [t_1 - \delta, t_1 + \delta]$.
7. Shrinking $\delta$, we may assume that $I_\delta$ is a closed bounded interval. Indeed, if $t_1 + \delta' \in I$ with $\delta' > 0$, then $[t_1, t_1 + \delta'] \subseteq I$, and similarly on the left.
8. So $(t, \gamma_k(t)) \in V$ for $t \in I_\delta$. As [[solutions|04SW7WECS8]], the $\gamma_k$ have derivatives $f(t, \gamma_k(t))$, which are [[continuous|0NRQPQX3VA]] in $t$.
9. By the [[fundamental theorem of calculus|0NHGY0N0JB]], componentwise, $w(t) = \int_{t_1}^{t} \left(f(s, \gamma_1(s)) - f(s, \gamma_2(s))\right) ds$ for $t \in I_\delta$, since $w(t_1) = 0$.
10. The integrand has norm at most $K u(s)$, by the choice of $V$. Let $M$ be the maximum of $u$ on $I_\delta$, which exists by the [[extreme value theorem|0WS1A8E2P9]].
11. By the lemma, $u(t) \le K \abs{t - t_1} M \le K \delta M$ for $t \in I_\delta$. So $M \le K \delta M$, that is, $(1 - K \delta) M \le 0$.
12. Since $K \delta < 1$ and $M \ge 0$, we get $M = 0$. This proves the local claim.
13. Right of $t_0$. Suppose $t_2 \in I$, $t_2 > t_0$ and $w(t_2) \ne 0$. Let $A$ be the set of $s \in [t_0, t_2]$ with $w = 0$ on $[t_0, s]$. It contains $t_0$ and is bounded.
14. By the [[completeness axiom|0AXWET80YW]], $s^* = \sup A$ exists, and $t_0 \le s^* \le t_2$. Each $s \in [t_0, s^*)$ lies below some element of $A$, so $w(s) = 0$.
15. By continuity of $w$, also $w(s^*) = 0$. So $s^* \in A$, and $s^* < t_2$ since $w(t_2) \ne 0$.
16. By the local claim at $s^*$, $w = 0$ on $I \cap [s^*, s^* + \delta]$. This interval contains $[s^*, \min(s^* + \delta, t_2)]$, since $t_2 \in I$.
17. So $\min(s^* + \delta, t_2) \in A$, and it is larger than $s^*$. This contradicts $s^* = \sup A$. Hence $w = 0$ on $I \cap [t_0, \infty)$.
18. Left of $t_0$. The same argument, with the infimum of the set of $s \in [t_2, t_0]$ such that $w = 0$ on $[s, t_0]$, gives $w = 0$ on $I \cap (-\infty, t_0]$.
19. So $\gamma_1(t) = \gamma_2(t)$ for all $t \in I$.

## Idea

Near a point where the two solutions meet, their distance $u$ satisfies $u \le K \delta \max u$. On a short interval with $K \delta < 1$, this forces $u = 0$. The set where the solutions agree is therefore open in $I$, and it is closed by continuity. A supremum argument spreads the agreement to all of $I$.

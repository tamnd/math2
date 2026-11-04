---
tag: FQ9DSN9DDB
kind: proof
name: Proof of Lyapunov's stability theorem
msc: [34D20]
proves: 0J6A752DTZ
uses: [04P7B5XC22, 092S6VBECQ, 05Y1JAM3Y5, 02903SSA48, 019VSXSFMQ, 055VVSN00V, 0V4DET59NW, 0PHT6NBYPB, 066HW6D9A7, 0MYFJVMN7M, 02CYB184RC, 0ABP2F2ZP7, 0J7HF2PF1H, 0P6KRD5B7A, 025PKW8AMR, 0A8TJ0VHC7, 026BJBQNGJ, 0BARQY52N5]
sources:
  - url: https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf
    locator: Section 2.6, Corollary 2.15, and Section 6.6, Theorem 6.13
---

## Proof

We first show that a solution which stays in a compact set exists for all $t \ge 0$. Then we use that $V$ does not increase along solutions. Here $\norm{\cdot}$ is the Euclidean norm, and $\gamma_{x_0} : (\alpha, \omega) \to U$ is the [[maximal solution|019VSXSFMQ]] with $\gamma_{x_0}(0) = x_0$, as in the definition of the [[flow|02903SSA48]].

Solutions in a compact set exist for all $t \ge 0$.

1. Let $C \subseteq U$ be compact, and let $x_0 \in U$ with $\gamma_{x_0}(t) \in C$ for all $t \in [0, \omega)$. Write $\gamma = \gamma_{x_0}$. We show $\omega = \infty$. Suppose instead that $\omega < \infty$.
2. A locally Lipschitz map is continuous. By the [[extreme value theorem|0V4DET59NW]], there is $M \ge 0$ with $\norm{f(x)} \le M$ for $x \in C$.
3. For $0 \le s < t < \omega$, the derivative of $\gamma$ on $[s, t]$ is $f(\gamma(r))$, of norm at most $M$. By the [[mean value inequality|02CYB184RC]], $\norm{\gamma(t) - \gamma(s)} \le M (t - s)$.
4. So for every sequence $t_m \to \omega$ in $[0, \omega)$, the sequence $\gamma(t_m)$ is Cauchy. Since [[$\R^n$ is complete|0ABP2F2ZP7]], it converges. Merging two such sequences shows that the limit $p$ does not depend on the sequence.
5. The set $C$ is [[closed|0MYFJVMN7M]], so $p \in C \subseteq U$. Since $f$ is locally Lipschitz, there are $r > 0$ and $K \ge 0$ with $\bar B(p, 2r) \subseteq U$. Moreover $f$ is $K$-[[Lipschitz|055VVSN00V]] on this closed ball.
6. The ball $\bar B(p, 2r)$ is compact by the [[Heine–Borel theorem|0PHT6NBYPB]]. So $\norm{f} \le L$ on it for some $L > 0$. Let $h = r / L$.
7. By step 4, choose $t_1 \in [0, \omega)$ with $\omega - t_1 < h$ and $\norm{\gamma(t_1) - p} \le r$. Let $y_1 = \gamma(t_1)$. The closed ball $B_1 = \bar B(y_1, r)$ lies in $\bar B(p, 2r)$.
8. Let $g(t, x) = f(x)$ for $x \in B_1$ and $g(t, x) = 0$ otherwise, for $t \in [t_1 - h, t_1 + h]$. Then $g$ satisfies the [[Picard–Lindelöf hypotheses|0J7HF2PF1H]] at $(t_1, y_1)$ with constants $r, L, K$, since $L h = r$.
9. By the [[Picard–Lindelöf theorem|0P6KRD5B7A]], there is $\beta : [t_1 - h, t_1 + h] \to B_1$ with $\beta(t_1) = y_1$ and $\beta' = g(t, \beta) = f(\beta)$. So $\beta$ solves $x' = f(x)$, with values in $U$.
10. On the open interval $(\max(\alpha, t_1 - h), \omega)$, the curves $\gamma$ and $\beta$ are solutions that agree at $t_1$. By [[uniqueness of solutions|025PKW8AMR]], they agree on this interval.
11. Let $\tilde\gamma = \gamma$ on $(\alpha, \omega)$ and $\tilde\gamma = \beta$ on $[\omega, t_1 + h)$. By step 10, $\tilde\gamma = \beta$ on $(\max(\alpha, t_1 - h), t_1 + h)$. So $\tilde\gamma$ is a solution on $(\alpha, t_1 + h)$ that extends $\gamma$.
12. Since $t_1 + h > \omega$, this contradicts the maximality of $\gamma$. Hence $\omega = \infty$.

$V$ does not increase along solutions.

13. Let $\gamma$ be a solution on an open interval $I$, and let $[c, d] \subseteq I$ with $\gamma(t) \in W$ for $t \in [c, d]$. Let $v(t) = V(\gamma(t))$.
14. By the [[chain rule|0A8TJ0VHC7]], at each $t \in [c, d]$ we have $v'(t) = \nabla V(\gamma(t)) \cdot f(\gamma(t)) = \dot V(\gamma(t)) \le 0$, as $V$ is a [[Lyapunov function|04P7B5XC22]].
15. So $-v$ has a non-negative derivative on $[c, d]$, and $-v$ is [[increasing|026BJBQNGJ]]. Thus $v$ is non-increasing on $[c, d]$.

Part (1).

16. Let $\varepsilon > 0$. Choose $r \in (0, \varepsilon]$ with $\bar B(x^*, r) \subseteq W$. The sphere $S = \set{x : \norm{x - x^*} = r}$ is compact by Heine–Borel and non-empty.
17. By the extreme value theorem, $V$ has a minimum $m$ on $S$. Since $V > 0$ on $W \setminus \set{x^*}$, we have $m > 0$.
18. Since $V$ is continuous and $V(x^*) = 0$, there is $\delta \in (0, r)$ with $V(x) < m$ whenever $\norm{x - x^*} < \delta$.
19. Let $x_0 \in U$ with $\norm{x_0 - x^*} < \delta$, and let $\gamma = \gamma_{x_0}$. We claim $\norm{\gamma(t) - x^*} < r$ for all $t \in [0, \omega)$.
20. If not, let $T$ be the infimum of the times $t \in [0, \omega)$ with $\norm{\gamma(t) - x^*} \ge r$. By continuity, $T > 0$ and $\norm{\gamma(T) - x^*} = r$. Then $\gamma(t) \in \bar B(x^*, r) \subseteq W$ for $t \in [0, T]$.
21. By step 15, $V(\gamma(T)) \le V(x_0) < m$. But $\gamma(T) \in S$, so $V(\gamma(T)) \ge m$. This contradiction proves the claim.
22. So $\gamma(t)$ lies in the compact set $\bar B(x^*, r) \subseteq U$ for $t \in [0, \omega)$. By steps 1 to 12, $\omega = \infty$.
23. Hence $\varphi_t(x_0)$ exists and $\norm{\varphi_t(x_0) - x^*} < r \le \varepsilon$ for all $t \ge 0$. So $x^*$ is [[Lyapunov stable|092S6VBECQ]].

A convergence lemma for strict $V$.

24. Let $V$ be strict, let $C \subseteq W$ be compact, and let $\gamma$ be a solution on an interval containing $[0, \infty)$ with $\gamma(t) \in C$ for $t \ge 0$. We show $\gamma(t) \to x^*$.
25. Let $v = V \circ \gamma$. By step 15, $v$ is non-increasing on $[0, \infty)$. Also $v \ge 0$. So $v(t)$ tends to a limit $c \ge 0$, and $v(t) \ge c$ for all $t \ge 0$.
26. Suppose $c > 0$. By continuity of $V$ at $x^*$, there is $\rho > 0$ with $V(x) < c$ for $x \in W$ and $\norm{x - x^*} < \rho$.
27. So $\gamma(t) \in A$ for $t \ge 0$, where $A = \set{x \in C : \norm{x - x^*} \ge \rho}$. The set $A$ is a [[closed subset of a compact set|066HW6D9A7]], hence compact, and it is non-empty.
28. The function $\dot V = \nabla V \cdot f$ is continuous on $W$, and it is negative on $A$ because $x^* \notin A$. By the extreme value theorem, $\dot V \le -\mu$ on $A$ for some $\mu > 0$.
29. By step 14, $v' \le -\mu$ on $[0, \infty)$. By the [[mean value theorem|0BARQY52N5]], $v(t) \le v(0) - \mu t$, which is negative for large $t$. This contradicts $v \ge 0$. So $c = 0$.
30. Now let $\rho > 0$ and $A_\rho = \set{x \in C : \norm{x - x^*} \ge \rho}$. If $A_\rho$ is non-empty, it is compact and $V$ has a minimum $m_\rho > 0$ on it.
31. Since $v(t) \to 0$, there is $T$ with $v(t) < m_\rho$ for $t \ge T$. Then $\gamma(t) \notin A_\rho$, so $\norm{\gamma(t) - x^*} < \rho$ for $t \ge T$. Hence $\gamma(t) \to x^*$.

Part (2).

32. Choose $r_0 > 0$ with $\bar B(x^*, r_0) \subseteq W$. Steps 16 to 23 with $\varepsilon = r_0$ give $\eta > 0$ as follows. If $\norm{x_0 - x^*} < \eta$, then $\varphi_t(x_0)$ exists for $t \ge 0$ and lies in $\bar B(x^*, r_0)$.
33. By the lemma with $C = \bar B(x^*, r_0)$, $\varphi_t(x_0) \to x^*$. With part (1), $x^*$ is [[asymptotically stable|05Y1JAM3Y5]].

Part (3).

34. Let $x_0 \in \R^n$ and $\Omega = \set{x : V(x) \le V(x_0)}$. Since $V(x) \to \infty$ as $\norm{x} \to \infty$, there is $R$ with $V(x) > V(x_0)$ for $\norm{x} > R$. So $\Omega$ is bounded.
35. It is closed because $V$ is continuous, so it is compact by Heine–Borel.
36. Let $\gamma = \gamma_{x_0}$. Since $W = \R^n$, step 15 on $[0, t]$ gives $V(\gamma(t)) \le V(x_0)$, so $\gamma(t) \in \Omega$ for $t \in [0, \omega)$. By steps 1 to 12, $\omega = \infty$.
37. By the lemma with $C = \Omega$, $\varphi_t(x_0) \to x^*$. This holds for each $x_0 \in \R^n$, and $x^*$ is Lyapunov stable by part (1). So $x^*$ is globally asymptotically stable.

## Idea

Along a solution, $V$ can only decrease, so a solution that starts where $V$ is small can never reach a sphere on which $V$ is larger. Being trapped in a compact set, the solution cannot blow up and exists for all time. If $V$ strictly decreases away from $x^*$, it must decrease to $0$, and $V$ near $0$ forces the solution near $x^*$.

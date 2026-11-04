---
tag: G4PSWYAWVQ
kind: proof
name: Proof of the estimate for approximate solutions by a first-crossing argument
msc: [34A12, 34A45]
proves: 0JTPMCCZT2
uses: [0FRX8JD7QH, 055VVSN00V, 0FJZMBX0ZZ, 0EX9GFJ0B3, 0RXX2PT1MQ, 0N32V0E3XJ]
sources:
  - url: https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Analysis/ODE/Gronwall.lean#L162
    locator: theorem dist_le_of_approx_trajectories_ODE_of_mem
---

## Proof

We compare $\|\gamma_1 - \gamma_2\|$ with a slightly larger Grönwall bound and look at the first time where the comparison could fail. Here $\|\cdot\|$ is the Euclidean norm on $\mathbb{R}^n$.

1. Let $\varepsilon = \varepsilon_1 + \varepsilon_2$, let $e(t) = \gamma_1(t) - \gamma_2(t)$ and let $\varphi(t) = \|e(t)\|$ for $t \in [a, b]$. Then $\varphi$ is continuous on $[a, b]$.
2. For $t \in (a, b)$, write $e'(t)$ as $\left(\gamma_1'(t) - f(t, \gamma_1(t))\right) + \left(f(t, \gamma_1(t)) - f(t, \gamma_2(t))\right) + \left(f(t, \gamma_2(t)) - \gamma_2'(t)\right)$.
3. By the [[triangle inequality|0FJZMBX0ZZ]], the hypotheses on $\gamma_i$ and the [[Lipschitz condition|055VVSN00V]], $\|e'(t)\| \le \varepsilon_1 + K \varphi(t) + \varepsilon_2 = K \varphi(t) + \varepsilon$.
4. For real $\delta', \varepsilon'$, let $G = G_{\delta', K, \varepsilon'}$ be the [[Grönwall bound|0FRX8JD7QH]]. Then $G(0) = \delta'$ and $G'(x) = K G(x) + \varepsilon'$ for all $x$.
5. Indeed, if $K \ne 0$, the [[chain rule|0RXX2PT1MQ]] and [[the derivative of the exponential|0EX9GFJ0B3]] give $G'(x) = K \delta' e^{Kx} + \varepsilon' e^{Kx}$, and this equals $K G(x) + \varepsilon'$. If $K = 0$, then $G'(x) = \varepsilon' = K G(x) + \varepsilon'$.
6. Fix $\eta > 0$ and let $H = G_{\delta + \eta, K, \varepsilon + \eta}$. By step 4, $H(0) = \delta + \eta$ and $H'(x) = K H(x) + \varepsilon + \eta$.
7. We claim that $\varphi(t) < H(t - a)$ for each $t \in [a, b)$. Suppose not. Then the set $Z = \{ t \in [a, b) : \varphi(t) \ge H(t - a) \}$ is non-empty. Let $t_1 = \inf Z$.
8. We have $\varphi(a) \le \delta < H(0)$. By continuity of $\varphi$ and $H$, there is $\rho > 0$ with $\varphi(t) < H(t - a)$ for $t \in [a, a + \rho)$. So $t_1 \ge a + \rho > a$.
9. By the definition of $t_1$, $\varphi(t) < H(t - a)$ for each $t \in [a, t_1)$. Letting $t \to t_1$ from the left gives $\varphi(t_1) \le H(t_1 - a)$, since [[limits preserve non-strict inequalities|0N32V0E3XJ]].
10. There are points $z_k \in Z$ with $z_k \ge t_1$ and $z_k \to t_1$. By continuity, $\varphi(t_1) \ge H(t_1 - a)$. So $\varphi(t_1) = H(t_1 - a)$. Also $t_1 \le z_1 < b$, so $t_1 \in (a, b)$.
11. Let $s \in (a, t_1)$. By steps 9 and 10, $H(t_1 - a) - H(s - a) < \varphi(t_1) - \varphi(s)$. By the triangle inequality, $\varphi(t_1) - \varphi(s) \le \|e(t_1) - e(s)\|$.
12. Dividing by $t_1 - s > 0$ gives $\dfrac{H(t_1 - a) - H(s - a)}{t_1 - s} \le \left\| \dfrac{e(t_1) - e(s)}{t_1 - s} \right\|$.
13. Let $s \to t_1$ from the left. The left side tends to $H'(t_1 - a)$. The quotient inside the norm tends to $e'(t_1)$, so by the reverse triangle inequality its norm tends to $\|e'(t_1)\|$.
14. So $H'(t_1 - a) \le \|e'(t_1)\|$. By steps 3 and 10, $\|e'(t_1)\| \le K H(t_1 - a) + \varepsilon$.
15. By step 6, $H'(t_1 - a) = K H(t_1 - a) + \varepsilon + \eta$. With step 14 this gives $\eta \le 0$, a contradiction. This proves the claim of step 7.
16. So $\varphi(t) < G_{\delta + \eta, K, \varepsilon + \eta}(t - a)$ for each $t \in [a, b)$ and each $\eta > 0$.
17. For fixed $x$, the value $G_{\delta', K, \varepsilon'}(x)$ is an affine function of $(\delta', \varepsilon')$, so it is continuous in them. Letting $\eta \to 0$ in step 16 gives $\varphi(t) \le G_{\delta, K, \varepsilon}(t - a)$ for $t \in [a, b)$.
18. Both $\varphi$ and $x \mapsto G_{\delta, K, \varepsilon}(x)$ are continuous. Letting $t \to b$ gives the same bound at $t = b$.
19. Hence $\|\gamma_1(t) - \gamma_2(t)\| \le G_{\delta, K, \varepsilon_1 + \varepsilon_2}(t - a)$ for each $t \in [a, b]$.

## Idea

The Grönwall bound $G$ solves $G' = K G + \varepsilon$, while the distance $\varphi$ grows at most at the rate $K \varphi + \varepsilon$. A bound that starts a little higher and grows a little faster can never be reached. At a first touching time, the distance would have to grow faster than the bound. Shrinking the margin to zero gives the estimate.

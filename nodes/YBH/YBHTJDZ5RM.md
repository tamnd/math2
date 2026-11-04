---
tag: YBHTJDZ5RM
kind: proof
name: Proof of the Picard–Lindelöf theorem
msc: [34A12]
proves: 0P6KRD5B7A
uses: [0J7HF2PF1H, 00WAVB68F9, 08XDXP86XE, 0VK6VEH345, 015KK993C5, 09GRCZVR5E, 0ABP2F2ZP7, 06SESV7GQY, 0NRQPQX3VA, 080RWVVSB6, 0MBWQKM8QR, 0RFWW56Y22]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Detailed proof
---

## Proof

We rewrite the problem as a fixed point problem for the Picard operator and use the Banach fixed point theorem.

1. We assume $t_{\min} < t_{\max}$, since a derivative within $J$ needs more than one point. Let $T = \max(t_{\max} - t_0, t_0 - t_{\min})$.
2. $f$ is continuous on $J \times B$. Indeed, $\norm{f(s, x) - f(s', x')} \le K \norm{x - x'} + \norm{f(s, x') - f(s', x')}$, by condition (1) of the [[Picard–Lindelöf hypotheses|0J7HF2PF1H]]. The last term tends to $0$ as $s \to s'$, by condition (2).
3. Let $\pi(x) = x$ if $\norm{x - x_0} \le a$, and $\pi(x) = x_0 + a (x - x_0)/\norm{x - x_0}$ otherwise. Then $\pi : \R^n \to B$ is continuous, since both formulas are continuous and agree where $\norm{x - x_0} = a$. If $a = 0$, then $\pi$ is the constant $x_0$.
4. Let $\tilde f(t, x) = f(t, \pi(x))$. By steps 2 and 3, $\tilde f$ is continuous on $J \times \R^n$. It equals $f$ on $J \times B$, so it satisfies the hypotheses with the same constants $a, L, K$.
5. For each continuous $\gamma : J \to \R^n$, the map $s \mapsto \tilde f(s, \gamma(s))$ is [[continuous|0NRQPQX3VA]], so it is [[integrable|06SESV7GQY]]. So the [[Picard operator|00WAVB68F9]] $P$ of $\tilde f$ at $(t_0, x_0)$ is defined.
6. Let $X$ be the set of continuous $\gamma : J \to B$, with $d(\gamma, \delta) = \sup_{t \in J} \norm{\gamma(t) - \delta(t)}$. It is nonempty, since it contains the constant curve $x_0$.
7. $X$ is complete. The curves in $X$ are bounded, and the space of bounded continuous maps $J \to \R^n$ is [[complete|09GRCZVR5E]], since [[$\R^n$ is complete|0ABP2F2ZP7]]. A Cauchy sequence $(\gamma_k)$ in $X$ converges uniformly to a continuous $\gamma$.
8. For $t \in J$, $\norm{\gamma(t) - x_0} \le \norm{\gamma(t) - \gamma_k(t)} + a$, and the first term tends to $0$. So $\gamma \in X$, and $\gamma_k \to \gamma$ in $X$.
9. Lemma. If $h : [c, e] \to \R^n$ and $\phi : [c, e] \to \R$ are integrable with $\norm{h} \le \phi$, then $\norm{\int_c^e h} \le \int_c^e \phi$.
10. Proof of the lemma: for $v = \int_c^e h \ne 0$, [[linearity|080RWVVSB6]] gives $\norm{v}^2 = \int_c^e v \cdot h$. By [[Cauchy–Schwarz|0RFWW56Y22]] and [[monotonicity|0MBWQKM8QR]], this is at most $\norm{v} \int_c^e \phi$.
11. $P$ maps $X$ into $X$. Let $\gamma \in X$. By condition (3), $\norm{\tilde f(s, \gamma(s))} \le L$. The lemma gives $\norm{(P\gamma)(t) - (P\gamma)(t')} \le L \abs{t - t'}$, so $P\gamma$ is continuous.
12. The lemma also gives $\norm{(P\gamma)(t) - x_0} \le L \abs{t - t_0} \le L T \le a$, by condition (4). So $P\gamma \in X$.
13. By [[the contraction lemma for the Picard operator|08XDXP86XE]], applied to $\tilde f$, there is $m \ge 1$ such that $P^m$ is a contraction of $X$.
14. By the [[Banach fixed point theorem|0VK6VEH345]], $P^m$ has exactly one fixed point $\alpha \in X$.
15. Then $P^m(P\alpha) = P(P^m \alpha) = P\alpha$, and $P\alpha \in X$. So $P\alpha$ is a fixed point of $P^m$, and $P\alpha = \alpha$ by uniqueness.
16. If $\beta \in X$ and $P\beta = \beta$, then $P^m \beta = \beta$, so $\beta = \alpha$. Thus $\alpha$ is the only fixed point of $P$ in $X$.
17. Let $\gamma : J \to B$ be continuous. Apply the [[integral equation form|015KK993C5]] to $\tilde f$, which is continuous on $J \times \R^n$, with $U = \R^n$.
18. It says: $\gamma(t_0) = x_0$ and $\gamma$ has derivative $\tilde f(t, \gamma(t))$ within $J$ at each $t \in J$ if and only if $\gamma = P\gamma$.
19. Since $\gamma$ takes values in $B$, where $\tilde f = f$, we have $\tilde f(t, \gamma(t)) = f(t, \gamma(t))$. So the curves of the statement are exactly the fixed points of $P$ in $X$.
20. By step 16, there is exactly one such curve, namely $\alpha$.

## Idea

A solution is the same as a solution of the integral equation, that is, a fixed point of the Picard operator. A high iterate of this operator is a contraction on the complete space of continuous curves in $B$. The Banach fixed point theorem gives exactly one fixed point, hence exactly one solution.

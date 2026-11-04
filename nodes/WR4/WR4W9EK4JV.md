---
tag: WR4W9EK4JV
kind: proof
name: Proof of the Picard–Lindelöf theorem in integral form
msc: [34A12]
proves: 00BT70ND50
uses: [0J7HF2PF1H, 00WAVB68F9, 08XDXP86XE, 0VK6VEH345, 09GRCZVR5E, 0ABP2F2ZP7, 06SESV7GQY, 0NRQPQX3VA, 080RWVVSB6, 0MBWQKM8QR, 0RFWW56Y22]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Detailed proof
---

## Proof

We find the curve as the unique fixed point of the Picard operator, with the Banach fixed point theorem.

1. If $t_{\min} = t_{\max}$, then $J = \set{t_0}$. The equation at $t_0$ says $\alpha(t_0) = x_0$, so exactly one curve works. From now on let $t_{\min} < t_{\max}$, and let $T = \max(t_{\max} - t_0, t_0 - t_{\min})$.
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
17. For $\gamma \in X$, the values $\gamma(s)$ lie in $B$, where $\tilde f = f$. So $(P\gamma)(t) = x_0 + \int_{t_0}^{t} f(s, \gamma(s))\, ds$.
18. Hence the continuous curves $J \to B$ that satisfy the integral equation are exactly the fixed points of $P$ in $X$. By step 16, there is exactly one, namely $\alpha$.

## Idea

The integral equation says that $\alpha$ is a fixed point of the Picard operator. On continuous curves with values in $B$, the operator itself may not contract, but a high iterate does. The Banach fixed point theorem then gives one fixed point of the iterate, and it is also the only fixed point of $P$.

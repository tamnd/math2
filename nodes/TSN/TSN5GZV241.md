---
tag: TSN5GZV241
kind: statement
role: theorem
name: Lundberg inequality
msc: [91G05, 60G55, 60G44]
uses: [F2NTQY7J54, YSXZZ1HQR5, 0WQVXP7PDB, 0D0GBNDKDH, DC9HZT2HVJ]
about: [YSXZZ1HQR5, F2NTQY7J54]
sources:
  - url: https://en.wikipedia.org/wiki/Ruin_theory
---

## Statement

Consider the [[Cramér–Lundberg model|F2NTQY7J54]] with claim intensity $\lambda > 0$, claims $X_i$ of mean $\mu$, premium rate $c > \lambda \mu$, and [[ruin probability|YSXZZ1HQR5]] $\psi(u)$ for initial capital $u \ge 0$.
Let $M_X(r) = E[e^{r X_1}]$ be the [[moment-generating function|0WQVXP7PDB]] of the claim size.
Assume that there is $R > 0$ with $M_X(R) < \infty$ and
$$\lambda \big( M_X(R) - 1 \big) = c R.$$
Then for all $u \ge 0$
$$\psi(u) \le e^{-R u}.$$

## Remarks

The number $R$ is the adjustment coefficient; when it exists it is unique, since $r \mapsto \lambda(M_X(r) - 1) - cr$ is convex, vanishes at $0$ and has negative slope $\lambda \mu - c$ there.
Proof idea: the choice of $R$ makes $e^{-R U_t}$ a [[martingale|0D0GBNDKDH]].
By [[optional stopping|DC9HZT2HVJ]] at $\tau \wedge t$, $e^{-Ru} = E[e^{-R U_{\tau \wedge t}}] \ge E[e^{-R U_\tau} ; \tau \le t] \ge P(\tau \le t)$, because $U_\tau < 0$ on $\set{\tau \le t}$; let $t \to \infty$.
Example: for exponential claims of mean $\mu$ and $c = (1 + \theta)\lambda\mu$, one finds $R = \theta / ((1 + \theta)\mu)$ and $\psi(u) = e^{-Ru} / (1 + \theta)$, which is below $e^{-Ru}$.
The hypothesis on $R$ needs light tails: for Pareto claims $M_X(r) = \infty$ for all $r > 0$, no $R$ exists, and $\psi(u)$ decays more slowly than any exponential.

## Explanations

### L1 human

The Lundberg inequality says that the chance of ruin of an insurer falls at least exponentially fast in its starting capital.
The rate $R$ depends on the claim sizes, the claim frequency and the premium.
So each extra unit of capital multiplies the worst-case ruin chance by the fixed factor $e^{-R}$.

### L2 human

The bound is the main quantitative result of classical [[ruin theory|YSXZZ1HQR5]] and is used to choose capital and premium levels.
Its martingale proof is the continuous-time analogue of the argument for the gambler's ruin.
Cramér sharpened it to the asymptotic formula $\psi(u) \sim C e^{-Ru}$ as $u \to \infty$, with an explicit constant $C \in (0, 1)$, under a mild moment condition.
For heavy-tailed claims the exponential bound is replaced by subexponential asymptotics, where ruin is typically caused by one very large claim.

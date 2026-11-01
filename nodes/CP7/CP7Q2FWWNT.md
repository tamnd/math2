---
tag: CP7Q2FWWNT
kind: definition
name: Lévy process
msc: [60G51, 60J25]
defines: 8NT5CFG2ZR
uses: [0QH5ENKZM1, 0GQ938GDE0, 0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Lévy_process
---

## Definition

Let $d \ge 1$.
A *Lévy process* in $\R^d$ is a [[stochastic process|0QH5ENKZM1]] $(X_t)_{t \ge 0}$ with values in $\R^d$ such that:

1. $X_0 = 0$ almost surely;
2. for all $0 \le t_0 < t_1 < \cdots < t_n$, the increments $X_{t_1} - X_{t_0}, \ldots, X_{t_n} - X_{t_{n-1}}$ are [[independent|0GQ938GDE0]];
3. for all $0 \le s \le t$, the increment $X_t - X_s$ has the same [[distribution|0DVDCMA2DK]] as $X_{t-s}$;
4. for every $t \ge 0$ and $\varepsilon > 0$, $\lim_{h \to 0} P(\abs{X_{t+h} - X_t} > \varepsilon) = 0$.

## Remarks

Example: the Poisson process $N$ of rate $\lambda$ satisfies the four clauses; $N_t - N_s$ is Poisson with mean $\lambda(t - s)$, and $P(N_{t+h} \ne N_t) = 1 - e^{-\lambda \abs{h}} \to 0$.
Non-example: the deterministic process $X_t = t^2$ satisfies clauses 1, 2 and 4, but $X_{s+1} - X_s = 2s + 1$ depends on $s$, so clause 3 fails.
Every Lévy process has a modification whose paths are right-continuous with left limits, and one usually works with it.
There is a function $\psi$, the characteristic exponent, with $\mathbb{E}[e^{i \langle u, X_t \rangle}] = e^{t \psi(u)}$ for all $u \in \R^d$ and $t \ge 0$.

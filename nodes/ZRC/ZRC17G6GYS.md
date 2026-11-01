---
tag: ZRC17G6GYS
kind: definition
name: Feller process
msc: [60J25, 60J35, 47D07]
defines: 4HS3C12472
uses: [0QH5ENKZM1, 0B77KZCQ51, 0XMEM406JM, 06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Feller_process
---

## Definition

Let $E$ be a locally compact Hausdorff space with a countable base.
Let $C_0(E)$ be the [[Banach space|06GZ956657]] of continuous functions $f \colon E \to \R$ that vanish at infinity, with the sup norm.
A *Feller semigroup* on $C_0(E)$ is a family $(T_t)_{t \ge 0}$ of linear maps $T_t \colon C_0(E) \to C_0(E)$ such that:

1. if $f \in C_0(E)$ and $0 \le f \le 1$, then $0 \le T_t f \le 1$;
2. $T_0 = \id$ and $T_{s+t} = T_s T_t$ for all $s, t \ge 0$;
3. $\norm{T_t f - f} \to 0$ as $t \downarrow 0$, for every $f \in C_0(E)$.

Let $(X_t)_{t \ge 0}$ be a time-homogeneous [[Markov process|0B77KZCQ51]] in $E$, and let $\mathbb{E}_x$ be the expectation for the process started at $x$.
The process is a *Feller process* if the formula
$$T_t f(x) = \mathbb{E}_x[f(X_t)]$$
defines a Feller semigroup.

## Remarks

Example: Brownian motion on $\R$ is a Feller process.
Here $T_t f(x) = \int f(y) \frac{1}{\sqrt{2\pi t}} e^{-(y - x)^2/(2t)}\, dy$; this is in $C_0(\R)$ when $f$ is, it preserves $0 \le f \le 1$, and it tends to $f$ uniformly because $f$ is uniformly continuous.
Non-example: on $E = \R$, let the process started at $x$ jump at once to $0$ if $x > 0$ and to $1$ if $x \le 0$, then stay there.
Then $T_t f = f(0)$ on $(0, \infty)$ and $T_t f = f(1)$ on $(-\infty, 0]$, which is not continuous in $x$, so $T_t$ does not map $C_0(E)$ into itself.
Clause 1 allows $T_t 1 < 1$, so the process may be killed; one then adds a cemetery point to $E$.
Every Feller process has a modification with right-continuous paths with left limits, and that modification is strong Markov.

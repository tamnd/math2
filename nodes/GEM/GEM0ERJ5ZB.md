---
tag: GEM0ERJ5ZB
kind: statement
role: theorem
name: Tanaka's formula
msc: [60J55, 60J65, 60H05]
uses: [22735FGJV6, E7ZC459PSA, JA95NH206E, 2J1RVQB0CM, 8CKDVESXT6]
about: [E7ZC459PSA]
sources:
  - url: https://en.wikipedia.org/wiki/Tanaka%27s_formula
same_as:
  wikidata: Q3068230
  wikipedia: Tanaka's formula
---

## Statement

Let $(B_t)_{t \ge 0}$ be a standard one-dimensional [[Brownian motion|22735FGJV6]] with $B_0 = 0$, and let $L(t, x)$ be its [[local time|E7ZC459PSA]].
Let $\sgn(y) = 1$ for $y > 0$, $\sgn(y) = -1$ for $y < 0$ and $\sgn(0) = 0$.
Then for every $x \in \R$, almost surely, for all $t \ge 0$,
$$\abs{B_t - x} = \abs{x} + \int_0^t \sgn(B_s - x) \, dB_s + L(t, x),$$
where the integral is an [[Itô integral|JA95NH206E]].

## Remarks

The function $y \mapsto \abs{y - x}$ is not twice differentiable at $x$, so [[Itô's lemma|2J1RVQB0CM]] does not apply to it directly.
Apply Itô's lemma to the convex functions $f_\varepsilon$ that agree with $\abs{y - x}$ outside $(x - \varepsilon, x + \varepsilon)$ and are quadratic with $f_\varepsilon'' = 1/\varepsilon$ inside.
These functions are only $C^1$, but Itô's lemma still holds for them, by smoothing $f_\varepsilon$ further, because $f_\varepsilon''$ is bounded with two jumps.
The second-order term is $\frac{1}{2\varepsilon} \int_0^t \mathbf{1}_{\set{\abs{B_s - x} < \varepsilon}} \, ds$, which tends to $L(t, x)$ as $\varepsilon \to 0$.
The value chosen for $\sgn(0)$ does not matter, because Brownian motion spends a set of times of Lebesgue measure zero at $x$.
Example: taking expectations with $x = 0$ gives $E[L(t, 0)] = E\abs{B_t} = \sqrt{2t/\pi}$.

## Explanations

### L1 human

Tanaka's formula is Itô's chain rule for the absolute value of a Brownian motion.
The kink of $\abs{y}$ at $0$ produces an extra term, the local time at $0$.
This term grows only when the path is at $0$ and pushes $\abs{B}$ up so that it stays nonnegative.

### L2 human

The formula shows that $\abs{B}$ is a semimartingale: a martingale part plus an increasing part $L(\cdot, 0)$.
By [[Lévy's characterization|8CKDVESXT6]], the integral $W_t = \int_0^t \sgn(B_s) \, dB_s$ is a Brownian motion.
Then $\abs{B} = W + L(\cdot, 0)$ and the Skorokhod reflection lemma give $L(t, 0) = \max_{s \le t} (-W_s)$.
This leads to Lévy's identity in law between $\abs{B}$ and $M - B$, where $M$ is the running maximum.
The same idea gives the Itô–Tanaka formula for differences of convex functions.

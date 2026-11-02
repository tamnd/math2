---
tag: 6KQCNP7P01
kind: definition
name: Vanishing mean oscillation
msc: [42B35, 30H35]
defines: QGA9ABJEXQ
uses: [QJYTXFT8Y4, 2Z2QVWZ262, JS2CCR3RNS]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_mean_oscillation
---

## Definition

Let $n \ge 1$ and let $f$ be a function of [[bounded mean oscillation|QJYTXFT8Y4]] on $\R^n$.
For a cube $Q$ with sides parallel to the axes, let $\abs{Q}$ be its [[Lebesgue measure|2Z2QVWZ262]] and $f_Q = \frac{1}{\abs{Q}} \int_Q f$.
For $\delta > 0$ let
$$\omega_f(\delta) = \sup_{\abs{Q} \le \delta} \frac{1}{\abs{Q}} \int_Q \abs{f(x) - f_Q} \, dx.$$
The function $f$ has *vanishing mean oscillation* if $\omega_f(\delta) \to 0$ as $\delta \to 0$.
The space of such functions is denoted $\mathrm{VMO}(\R^n)$.

## Remarks

VMO is a closed subspace of BMO, and Sarason showed that it is the closure in BMO of the uniformly continuous functions in BMO.
Some authors use a smaller space on $\R^n$, also called VMO: the closure in BMO of the continuous functions with compact support.
The dual space of this smaller space is the real Hardy space $H^1$.

Example: every uniformly continuous $f$ in BMO is in VMO.
If $\abs{f(x) - f(y)} \le \varepsilon$ whenever $\abs{x - y} \le \eta$, then on a cube $Q$ of diameter at most $\eta$ one has $\abs{f(x) - f_Q} \le \varepsilon$ for $x \in Q$, so $\omega_f(\delta) \le \varepsilon$ for $\delta$ small.

Example with a singularity: if $n \ge 2$ and $\nabla f \in L^n(\R^n)$, then the [[Poincaré inequality|JS2CCR3RNS]] on cubes gives $\frac{1}{\abs{Q}} \int_Q \abs{f - f_Q} \le C \left( \int_Q \abs{\nabla f}^n \right)^{1/n}$, which tends to $0$ uniformly as $\abs{Q} \to 0$.
So such $f$ are in VMO, although they can be unbounded.

Non-example: $f(x) = \log \abs{x}$ on $\R$ is in BMO but not in VMO.
For $r > 0$, $f(r x) = f(x) + \log r$, so the mean oscillation of $f$ on $[-r, r]$ equals its mean oscillation on $[-1, 1]$, which is a fixed positive number.
Hence $\omega_f(\delta)$ does not tend to $0$.

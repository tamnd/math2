---
tag: 6YGSZXF0HZ
kind: definition
name: Adaptive control
msc: [93C40, 93D21, "93E35"]
defines: F2RD2ZTZ8V
uses: [7NYES2D0Z4, 01REYCJ371]
sources:
  - url: https://en.wikipedia.org/wiki/Adaptive_control
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a family of control systems with state $x$, input $u$ and output $y$, where the true parameter $\theta \in \Theta$ is unknown.
An *adaptive controller* for this family consists of two parts:

1. a control law $u = K(\hat{\vartheta}, y, r)$, a [[feedback|7NYES2D0Z4]] law that depends on an adjustable parameter vector $\hat{\vartheta}$ and on a reference signal $r$;
2. an adaptation law that updates $\hat{\vartheta}$ from the measured signals, for example $\hat{\vartheta}' = F(\hat{\vartheta}, y, r)$ in continuous time.

The controller solves the *adaptive control problem* if the following holds for every $\theta \in \Theta$ and every initial condition.
All signals of the closed loop stay bounded and the control objective holds asymptotically.
Typical objectives are $y(t) \to 0$ or $y(t) - y_m(t) \to 0$ for a reference trajectory $y_m$.

## Remarks

In indirect adaptive control, the adaptation law estimates $\theta$ and the control law uses the estimate as if it were exact.
In direct adaptive control, the adaptation law updates the controller parameters without estimating $\theta$.
Example: the family $x' = \theta x + u$, $y = x$, with $\theta \in \R$ unknown, the law $u = -\hat{k} x$ and the adaptation $\hat{k}' = \gamma x^2$ with $\gamma > 0$.
Pick $k^* > \theta$ and set $V = \frac{1}{2} x^2 + \frac{1}{2\gamma}(\hat{k} - k^*)^2$.
Then $V' = (\theta - \hat{k}) x^2 + (\hat{k} - k^*) x^2 = (\theta - k^*) x^2 \le 0$, so $V$ is a [[Lyapunov function|01REYCJ371]].
Hence $x$ and $\hat{k}$ stay bounded, $x$ is square integrable, $x'$ is bounded, and [[Barbalat's lemma|4KPNX1SZYR]] gives $x(t) \to 0$.
Non-example: a fixed robust controller $u = -k x$ with constant $k$ has no adaptation law; it stabilizes the family only for $\theta < k$, so it fails for large $\theta$.

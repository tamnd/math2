---
tag: D3FHYZ4P1R
kind: definition
name: Feedback linearization
msc: [93B18, 93C10]
defines: 1J2KTGXB34
uses: [ZPDTVZQN5K, 0299VCW1TH, 0KZZ70ZHXP, A9WFM77Z4P, 68FGQEBD6J]
sources:
  - url: https://en.wikipedia.org/wiki/Feedback_linearization
---

## Definition

Let $\Omega \subseteq \R^n$ be open, and let $f, g \colon \Omega \to \R^n$ be smooth [[vector fields|0299VCW1TH]].
Consider the single-input control-affine [[control system|ZPDTVZQN5K]] $x' = f(x) + g(x) u$ with $u \in \R$, and let $x_0 \in \Omega$.
The system is *locally feedback linearizable* at $x_0$ if there are the following data.
An open neighbourhood $W \subseteq \Omega$ of $x_0$, and a smooth [[diffeomorphism|0KZZ70ZHXP]] $\Phi$ from $W$ onto an open subset of $\R^n$.
Smooth functions $\alpha, \beta \colon W \to \R$ with $\beta(x) \ne 0$ for all $x \in W$.
These data must satisfy two conditions:

1. under the feedback $u = \alpha(x) + \beta(x) v$, the new state $z = \Phi(x)$ satisfies $z' = A z + B v$ for a real $n \times n$ matrix $A$ and a vector $B \in \R^n$;
2. the linear system $z' = A z + B v$ is [[controllable|A9WFM77Z4P]].

*Feedback linearization* is the construction of such $\Phi$, $\alpha$ and $\beta$.

## Remarks

Example: the pendulum $x_1' = x_2$, $x_2' = -\sin x_1 + u$ has $f(x) = (x_2, -\sin x_1)$ and $g(x) = (0, 1)$; with $\Phi = \id$, $\alpha(x) = \sin x_1$ and $\beta = 1$ one gets $z_1' = z_2$, $z_2' = v$, which is controllable.
Non-example: with $g \equiv 0$ the input has no effect, so clause 2 fails for every choice of $\Phi$, $\alpha$ and $\beta$.
Write $\mathrm{ad}_f g = [f, g]$ for the [[Lie bracket|68FGQEBD6J]].
The system is locally feedback linearizable at $x_0$ if and only if two conditions hold.
The vectors $g, \mathrm{ad}_f g, \ldots, \mathrm{ad}_f^{n-1} g$ are linearly independent at $x_0$.
The distribution spanned by $g, \mathrm{ad}_f g, \ldots, \mathrm{ad}_f^{n-2} g$ is involutive near $x_0$.
The related input–output linearization only makes the map from $v$ to a chosen output linear, and may leave internal dynamics.

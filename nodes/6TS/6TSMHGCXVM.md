---
tag: 6TSMHGCXVM
kind: statement
role: theorem
name: Modica–Mortola theorem
msc: [49J45, 49Q20]
uses: [NW9MM370A5, M4CEZ5K9HP, SASP14MA1Z, Y68BHXZJBV]
about: [NW9MM370A5]
sources:
  - url: https://en.wikipedia.org/wiki/Γ-convergence
---

## Statement

Let $\Omega \subseteq \R^n$ be a bounded open set with Lipschitz boundary, and let $W(t) = t^2 (1 - t)^2$ for $t \in \R$.
For $\varepsilon > 0$ define $F_\varepsilon \colon L^1(\Omega) \to [0, +\infty]$ by
$$F_\varepsilon(u) = \int_\Omega \Big( \varepsilon \abs{\nabla u}^2 + \frac{1}{\varepsilon} W(u) \Big) \, dx$$
if $u$ lies in the [[Sobolev space|M4CEZ5K9HP]] $W^{1,2}(\Omega)$, and $F_\varepsilon(u) = +\infty$ otherwise.
Define $F \colon L^1(\Omega) \to [0, +\infty]$ by
$$F(u) = c_W \operatorname{Per}(E; \Omega), \qquad c_W = 2 \int_0^1 \sqrt{W(s)} \, ds = \frac13,$$
if $u = \mathbf{1}_E$ is the characteristic function of a set $E \subseteq \Omega$ of finite [[perimeter|Y68BHXZJBV]] $\operatorname{Per}(E; \Omega)$ in $\Omega$, and $F(u) = +\infty$ otherwise.
Then $F_\varepsilon$ [[Γ-converges|NW9MM370A5]] to $F$ in the [[Lp space|SASP14MA1Z]] $L^1(\Omega)$ as $\varepsilon \to 0$.

## Remarks

The lower bound comes from the inequality $a^2 + b^2 \ge 2ab$, which gives $\varepsilon \abs{\nabla u}^2 + W(u)/\varepsilon \ge 2 \sqrt{W(u)} \abs{\nabla u} = \abs{\nabla (\phi \circ u)}$ with $\phi(t) = 2 \int_0^t \sqrt{W(s)} \, ds$.
The lower semicontinuity of the total variation then bounds the limit from below by the perimeter of $E$ times $\phi(1) - \phi(0) = c_W$.
For the recovery sequence, one puts the optimal one-dimensional profile across $\partial E$.
Here $q(s) = 1/(1 + e^{-s})$ solves $q' = \sqrt{W(q)}$.
When $\partial E$ is smooth, $u_\varepsilon(x) = q(d(x)/\varepsilon)$ works, with $d$ the signed distance to $\partial E$.
The same result holds for other continuous double-well potentials $W \ge 0$ that vanish exactly at two points and grow suitably at infinity.
Then $c_W$ is the integral of $2\sqrt{W}$ between the two wells.

The theorem is often combined with a volume constraint $\int_\Omega u \, dx = m$.
Then the [[fundamental theorem of Γ-convergence|23RK8EZ20P]] shows that minimizers of $F_\varepsilon$ converge, along subsequences, to characteristic functions of sets of least perimeter with the given volume.

## Explanations

### L1 human

A mixture of two fluids, such as oil and water, can be described by a function $u$ that is near $0$ in one phase and near $1$ in the other.
The energy $F_\varepsilon$ punishes values between the phases through $W$ and punishes fast changes through the gradient term.
When the parameter $\varepsilon$ becomes small, the transition layer gets thin and its energy concentrates on the interface.
The theorem says that in the limit the energy is a constant times the area of the interface, so minimizing the energy means minimizing the area of the interface.

### L2 human

This is the model example of [[Γ-convergence|NW9MM370A5]] and the reason it became popular.
It connects the diffuse-interface energy behind the [[Allen–Cahn equation|7S813PEV69]] with the sharp-interface perimeter functional of geometric measure theory.
The constant $c_W$ is the energy per unit area of the optimal one-dimensional transition profile.
The result is due to Luciano Modica and Stefano Mortola, and Modica used it to study phase transitions with a volume constraint.

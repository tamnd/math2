---
tag: KDZN92Z8JR
kind: definition
name: Automatic differentiation
msc: [65D25, 68W30]
defines: BW7FEZ8WM1
uses: [0V1EJCT8G6, 09EGC6F8PT, 047NDTEPCV]
sources:
  - url: https://en.wikipedia.org/wiki/Automatic_differentiation
---

## Definition

Let $U \subseteq \R^n$ be open and let $f \colon U \to \R^m$ be given by an *evaluation trace*.
Its first variables $v_{1-n}, \ldots, v_0$ are the inputs $x_1, \ldots, x_n$.
The others are given for $k = 1, \ldots, \ell$ by
$$v_k = \varphi_k\big( (v_j)_{j \in P_k} \big),$$
where $P_k \subseteq \set{1 - n, \ldots, k - 1}$ and each $\varphi_k$ is a differentiable elementary function, such as $+$, $\times$, $\sin$ or $\exp$.
The outputs $y_1, \ldots, y_m$ are some of the $v_k$.

1. *Forward mode* takes a direction $\dot x \in \R^n$, sets $\dot v_{i - n} = \dot x_i$, and computes along with each $v_k$ the value $\dot v_k = \sum_{j \in P_k} \frac{\partial \varphi_k}{\partial v_j} \dot v_j$.
2. *Reverse mode* first evaluates the trace and takes $\bar y \in \R^m$.
It sets the adjoint $\bar v$ of each output to its entry of $\bar y$ and all other adjoints to $0$.
Then for $k = \ell, \ell - 1, \ldots, 1$ it adds $\bar v_k \frac{\partial \varphi_k}{\partial v_j}$ to $\bar v_j$ for each $j \in P_k$.

*Automatic differentiation* is the computation of derivatives of $f$ by these propagation rules.
Forward mode returns $\dot y = J_f(x) \dot x$, where $J_f(x)$ is the [[Jacobian matrix|047NDTEPCV]].
Reverse mode returns $\bar x = J_f(x)^{T} \bar y$, where $\bar x_i = \bar v_{i-n}$.

## Remarks

Example: $f(x_1, x_2) = x_1 x_2 + \sin x_1$ has the trace $v_1 = v_{-1} v_0$, $v_2 = \sin v_{-1}$, $v_3 = v_1 + v_2$.
Forward mode at $(x_1, x_2) = (1, 2)$ with $\dot x = (1, 0)$ gives $\dot v_1 = 2$, $\dot v_2 = \cos 1$, $\dot v_3 = 2 + \cos 1$, which is the [[partial derivative|09EGC6F8PT]] $\partial f / \partial x_1 = x_2 + \cos x_1$ at $(1, 2)$.
Reverse mode with $\bar y = 1$ gives $\bar v_1 = \bar v_2 = 1$, then $\bar v_0 = v_{-1} = 1$ and $\bar v_{-1} = v_0 + \cos v_{-1} = 2 + \cos 1$, the full gradient in one backward sweep.
Non-example: the difference quotient $\frac{f(x + h e_1) - f(x)}{h}$ is not automatic differentiation; it does not use the trace and has a truncation error of order $h$.
Forward mode can be described with dual numbers $a + b\varepsilon$, $\varepsilon^2 = 0$: evaluating the program on $x + \dot x \varepsilon$ gives $f(x) + (J_f(x) \dot x) \varepsilon$.

## Explanations

### L1 human

Automatic differentiation follows the program step by step and differentiates each step by the rules of calculus.
Forward mode answers how all outputs change when one input direction changes; reverse mode answers how one output depends on all inputs at once.

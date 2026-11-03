---
tag: YTP9XCQVAE
kind: definition
name: Mirror descent
msc: [90C25, 65K05]
defines: ZREVY65RM4
uses: [07GR3TNW4H, 0AEAHMFSCA, 9C5WXYYQEK, 02AS45T3H9, YX1DJK2QAG, PQBW43X5RE, 12317R8RTJ]
sources:
  - url: https://en.wikipedia.org/wiki/Mirror_descent
---

## Definition

Let $C \subseteq \R^n$ be a nonempty closed [[convex set|02AS45T3H9]], and let $f \colon C \to \R$ be a [[convex function|07GR3TNW4H]] with [[subgradients|9C5WXYYQEK]] $g(x)$ at each $x \in C$.
Let $D \subseteq \R^n$ be an open convex set whose closure contains $C$, and let $\psi \colon D \to \R$ be a differentiable [[strictly convex function|0AEAHMFSCA]], the *mirror map*.
Its *Bregman divergence* is $D_\psi(x, y) = \psi(x) - \psi(y) - \nabla \psi(y)^T (x - y)$ for $x, y \in D$.
Let $x_0 \in C \cap D$ and let $(\eta_k)$ be positive step sizes.
*Mirror descent* produces the sequence
$$x_{k+1} = \operatorname*{arg\,min}_{x \in C \cap D} \Big( \eta_k \, g(x_k)^T x + D_\psi(x, x_k) \Big) \qquad (k \ge 0),$$
under the standing assumption that this minimiser exists in $C \cap D$.

## Remarks

Equivalently, one steps in the mirror space, $\nabla \psi(y_{k+1}) = \nabla \psi(x_k) - \eta_k g(x_k)$, and then projects back by $x_{k+1} = \operatorname*{arg\,min}_{x \in C \cap D} D_\psi(x, y_{k+1})$.
These two forms agree when $\nabla \psi$ maps $D$ onto $\R^n$.

Example: $\psi(x) = \tfrac12 \norm{x}^2$ on $D = \R^n$.
Then $D_\psi(x, y) = \tfrac12 \norm{x - y}^2$, and the update is the Euclidean projection of $x_k - \eta_k g(x_k)$ onto $C$, the projected subgradient method; with $C = \R^n$ and differentiable $f$ it is [[gradient descent|12317R8RTJ]].

Example: $C$ the probability [[simplex|YX1DJK2QAG]] and $\psi(x) = \sum_i x_i \ln x_i$ on $D = \R^n_{>0}$.
Then $D_\psi(x, y) = \sum_i x_i \ln(x_i / y_i)$ on $C$, the [[Kullback–Leibler divergence|PQBW43X5RE]], and the update is $x_{k+1, i} = x_{k, i} e^{-\eta_k g_i} / \sum_j x_{k, j} e^{-\eta_k g_j}$, where $g = g(x_k)$.

Non-example: $\psi(x) = c^T x$ is not a valid mirror map, since it is not strictly convex.
Then $D_\psi = 0$, and the update minimises a linear function over $C$.
This need not have a unique solution, or any solution in $C \cap D$.

---
tag: 5PWD6ZBFQV
kind: definition
name: Hebbian learning
msc: [92B20, 68T05, 92C20]
defines: VQZVSFF179
uses: [000AYPA9AJ, 0V7G6WMFK0]
sources:
  - url: https://en.wikipedia.org/wiki/Hebbian_theory
---

## Definition

Consider a linear model neuron with input $x \in \R^n$, weight vector $w \in \R^n$ and output $y = w^T x$.
Let $\eta > 0$ be a learning rate.
The *Hebbian learning rule* is the update
$$w \leftarrow w + \eta\, y\, x,$$
that is, $\Delta w_i = \eta\, x_i\, y$ for each $i$, applied for each input presented.
In continuous time it is written $\tau\, \frac{dw}{dt} = y\, x$ with a time constant $\tau > 0$.

## Remarks

Example: for $n = 2$, $w = (1, 0)$, $x = (1, 1)$ and $\eta = 0.1$, the output is $y = 1$ and the new weight is $(1.1, 0.1)$; both weights grow, since both inputs were active together with the output.
Non-example: the update $w \leftarrow w + \eta\, (t - y)\, x$ with a target $t$ is not Hebbian, because it depends on an external teaching signal and not only on the input and output activities.
If the inputs have zero mean and [[covariance matrix|0V7G6WMFK0]] $C$, averaging gives $\tau\, dw/dt = C w$, so $w$ grows exponentially along the eigenvectors of $C$ with positive eigenvalue and its norm is unbounded.
Normalised variants fix this; the covariance rule $\Delta w_i = \eta (x_i - \bar x_i)(y - \bar y)$ subtracts mean activities.

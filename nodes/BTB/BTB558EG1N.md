---
tag: BTB558EG1N
kind: definition
name: Perceptron
msc: [68T07, 92B20, 68T05]
defines: Q2SV2SPH06
uses: [09C4JP7Y0M, 0X05GS525E]
sources:
  - url: https://en.wikipedia.org/wiki/Perceptron
---

## Definition

Let $n \ge 1$, let $w \in \R^n$ be a weight vector and let $b \in \R$ be a bias.
The *perceptron* with weights $w$ and bias $b$ is a function $f \colon \R^n \to \set{0, 1}$.
It is given by
$$f(x) = \begin{cases} 1 & \text{if } w^T x + b > 0, \\ 0 & \text{otherwise.} \end{cases}$$
Let $(x, t)$ be a labelled example with $t \in \set{0, 1}$, and let $\eta > 0$ be a learning rate.
The *perceptron learning rule* updates
$$w \leftarrow w + \eta\, (t - f(x))\, x, \qquad b \leftarrow b + \eta\, (t - f(x)).$$

## Remarks

So $f(x) = H(w^T x + b)$, where $H$ is the [[Heaviside step function|09C4JP7Y0M]] with the value $0$ at $0$.
Example: $w = (1, 1)$, $b = -1.5$ on $\set{0, 1}^2$ gives $f(1,1) = 1$ since $0.5 > 0$, and $f(x) = 0$ for the other three points since their sums are $-0.5$ or $-1.5$; this is the [[Boolean function|0X05GS525E]] AND.
Non-example: exclusive or on $\set{0,1}^2$ is not of this form; from $f(1,0) = f(0,1) = 1$ one gets $w_1 + b > 0$ and $w_2 + b > 0$, and from $f(0,0) = 0$ one gets $b \le 0$, so $w_1 + w_2 + b > -b \ge 0$, which forces $f(1,1) = 1$.
The rule changes the weights only on misclassified examples.
If the training set is finite and linearly separable, the rule stops changing after finitely many updates (the perceptron convergence theorem of Novikoff).

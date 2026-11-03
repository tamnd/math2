---
tag: PHG485NGHA
kind: definition
name: Solow–Swan model
msc: [91B62]
defines: 223GCENAVJ
uses: [0NT64JV96A, 0GCM7B6PBK, XWMZSDDKTZ]
sources:
  - url: https://en.wikipedia.org/wiki/Solow%E2%80%93Swan_model
---

## Definition

Let $F \colon [0, \infty)^2 \to [0, \infty)$ be a production function with constant returns to scale: $F(\lambda K, \lambda N) = \lambda F(K, N)$ for all $\lambda > 0$.
Let $f(k) = F(k, 1)$ be its intensive form.
Assume that $f(0) = 0$ and that $f$ is twice differentiable, strictly increasing and strictly [[concave|0GCM7B6PBK]] on $(0, \infty)$.
Assume also the Inada conditions: $f'(k) \to \infty$ as $k \to 0$ and $f'(k) \to 0$ as $k \to \infty$.
Let $s \in (0, 1)$ be the saving rate, $\delta \ge 0$ the depreciation rate, $n \ge 0$ the growth rate of labour and $g \ge 0$ the growth rate of technology, with $n + g + \delta > 0$.

The *Solow–Swan model* is the system in which, at each time $t \ge 0$:

1. labour $L$ and technology $A$ grow as $L(t) = L(0) e^{nt}$ and $A(t) = A(0) e^{gt}$;
2. output is $Y(t) = F(K(t), A(t) L(t))$, where $K(t)$ is the capital stock;
3. capital evolves by $\dot K(t) = s Y(t) - \delta K(t)$.

In terms of capital per effective worker $k = K/(AL)$, the model is the [[ordinary differential equation|0NT64JV96A]]
$$\dot k(t) = s f(k(t)) - (n + g + \delta) k(t).$$
A *steady state* is a value $k^* > 0$ with $s f(k^*) = (n + g + \delta) k^*$.

## Remarks

Example: for the [[Cobb–Douglas|XWMZSDDKTZ]] function $F(K, N) = K^\alpha N^{1 - \alpha}$ with $0 < \alpha < 1$, the intensive form is $f(k) = k^\alpha$.
It satisfies all the hypotheses.
The steady state is $k^* = \left( s/(n + g + \delta) \right)^{1/(1 - \alpha)}$.
Indeed $s (k^*)^\alpha = (n + g + \delta) k^*$ is equivalent to $(k^*)^{1 - \alpha} = s/(n + g + \delta)$.

Non-example: the function $F(K, N) = aK$ with $a > 0$ has constant returns to scale but violates the Inada conditions, since $f'(k) = a$.
Then $\dot k = (sa - n - g - \delta) k$, so there is no steady state when $sa \ne n + g + \delta$, and $k$ grows or shrinks exponentially.

Under the hypotheses, the steady state exists, is unique, and every solution with $k(0) > 0$ converges to it.
In the steady state, output per worker $Y/L = A f(k^*)$ grows at the rate $g$.

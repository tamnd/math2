---
tag: 0CC4VC7KR3
kind: example
name: Logistic equation
aliases: [verhulst-equation]
msc: [92D25]
instance_of: [074E9A8ZJK, 0T92VGGVWP]
uses: [075VBY4K4X, 00SVP6W3CB]
sources:
  - url: https://en.wikipedia.org/wiki/Logistic_function
    locator: Logistic differential equation
  - url: https://en.wikipedia.org/wiki/Logistic_function
    locator: 'In ecology: modeling population growth'
inventory: [1J9TVXNMVP]
---

## Example

Let $r > 0$ and $K > 0$ be constants. The logistic equation is
$$P'(t) = r\, P(t) \left(1 - \frac{P(t)}{K}\right).$$
For an initial value $P(0) = P_0 > 0$, its solution is
$$P(t) = \frac{K}{1 + \left(\frac{K - P_0}{P_0}\right) e^{-r t}}, \qquad t \ge 0.$$
With $r = K = 1$, the function $f(t) = 1 / \left(1 + e^{-t}\right)$ is the standard logistic function. It satisfies $f' = f(1 - f)$ and $f(0) = 1/2$.

## Remarks

The constant functions $P = 0$ and $P = K$ are the [[equilibrium points|0N8NGKDZDZ]]. For each $P_0 > 0$, $P(t) \to K$ as $t \to \infty$.
For small $P$, the equation is close to $P' = r P$, which is [[exponential growth|00SVP6W3CB]].
If $0 < P_0 < K/2$, the graph of $P$ is an S-shaped curve with its inflection point at the value $P = K/2$.
The equation is separable, and it is a [[Bernoulli equation|0T92VGGVWP]] with exponent $2$.

## Explanations

### L1 human

The logistic equation is a model of a population with limited resources.
When the population is small, it grows almost exponentially. When it is close to the capacity $K$, the growth slows down and stops.
The constant $K$ is the carrying capacity: the largest population that the environment can support.

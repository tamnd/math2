---
tag: 0WGDPYR30Q
kind: definition
name: Continuous uniform distribution
msc: ["60E05"]
defines: 0AREFQ9Z65
uses: [04YG690N5V, 0TK8Y3J5RW]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
    locator: Probability density function
inventory: [C7763YCGJW]
---

## Definition

Let $a < b$ be real numbers.
The continuous uniform distribution on the [[interval|0TK8Y3J5RW]] $[a, b]$ is the distribution on $\mathbb{R}$ with the [[probability density function|04YG690N5V]]
$$f(x) = \begin{cases} \dfrac{1}{b - a} & \text{if } a \le x \le b, \\ 0 & \text{otherwise.} \end{cases}$$
One writes $X \sim \operatorname{U}(a, b)$.

## Remarks

For $a \le c \le d \le b$, $P(c \le X \le d) = (d - c)/(b - a)$.
The cumulative distribution function is $F(x) = (x - a)/(b - a)$ for $a \le x \le b$, with $F(x) = 0$ for $x < a$ and $F(x) = 1$ for $x > b$.
The mean is $(a + b)/2$ and the variance is $(b - a)^2 / 12$.
If $U \sim \operatorname{U}(0, 1)$ and $F$ is a cumulative distribution function with [[quantile function|0B3Q3XDM5X]] $Q$, then $Q(U)$ has the cumulative distribution function $F$.

## Explanations

### L1 human

The uniform distribution is "a point chosen at random in an interval, with no preference".
For $\operatorname{U}(0, 10)$, the chance to land between $2$ and $5$ is $3/10$, the length of the piece over the length of the interval.

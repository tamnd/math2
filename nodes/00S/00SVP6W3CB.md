---
tag: 00SVP6W3CB
kind: example
name: Exponential growth and decay
msc: [34A05]
instance_of: [074E9A8ZJK, 07JH131FVP]
uses: [075VBY4K4X]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_growth
    locator: Differential equation
same_as:
  wikidata: Q582659
  wikipedia: Exponential growth
---

## Example

Let $k$ and $y_0$ be real numbers.
The [[initial value problem|075VBY4K4X]] $y'(t) = k\, y(t)$, $y(0) = y_0$ has the unique solution
$$y(t) = y_0\, e^{k t}, \qquad t \in \mathbb{R}.$$
If $k > 0$ and $y_0 > 0$, the solution grows: this is exponential growth. If $k < 0$ and $y_0 > 0$, the solution decreases to $0$: this is exponential decay.

## Remarks

For $k > 0$, the doubling time is $\ln 2 / k$: we have $y(t + \ln 2 / k) = 2\, y(t)$ for each $t$.
For $k < 0$, the half-life is $\ln 2 / |k|$. Radioactive decay follows this law.
Uniqueness: if $y$ is a solution, then the derivative of $y(t) e^{-k t}$ is $0$, so $y(t) e^{-kt}$ is the constant $y_0$.

## Explanations

### L1 human

The equation says that the rate of change is proportional to the present amount.
A population with no limits, or money with continuous interest, grows like this.
The larger the amount, the faster it grows, so the growth gets faster and faster.

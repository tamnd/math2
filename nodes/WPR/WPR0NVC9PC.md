---
tag: WPR0NVC9PC
kind: concept
name: Stieltjes function
msc: [26A48, 28A12, 26A42]
specializes: [0A7KV2WB7A]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue%E2%80%93Stieltjes_integration
---

## Summary

A Stieltjes function is a non-decreasing, right-continuous function from the real line to itself.
Each Stieltjes function $F$ gives a [[Lebesgue–Stieltjes measure|QV75XJBFCS]] that assigns the mass $F(b) - F(a)$ to each interval $(a, b]$.
Conversely, every Borel measure on $\R$ that is finite on bounded sets comes from a Stieltjes function, unique up to an additive constant.
Cumulative distribution functions of random variables are the main examples.

## Explanations

### L1 human

Picture $F(x)$ as the total amount of sand piled up to the left of the point $x$.
As $x$ moves right, the amount can only grow, so $F$ is non-decreasing.
Where a single grain of positive mass sits at a point, $F$ jumps there, and right-continuity fixes the value at the jump to the upper one.
For example, $F(x) = x$ is a Stieltjes function and gives Lebesgue measure.
The step function equal to $0$ for $x < 0$ and $1$ for $x \ge 0$ is another, and it gives a unit mass at $0$.

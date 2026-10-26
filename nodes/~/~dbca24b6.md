---
tag: ~dbca24b6
kind: statement
role: theorem
name: Binet's formula
msc: [11B39]
uses: [~bc16f766, ~2297c8d3]
sources:
  - url: https://en.wikipedia.org/wiki/Fibonacci_sequence
    locator: Closed-form expression
---

## Statement

Let $n$ be a natural number, and let $F_n$ be the $n$-th [[Fibonacci number|~bc16f766]].
Let $\varphi = \frac{1 + \sqrt{5}}{2}$ be the [[golden ratio|~2297c8d3]] and let $\psi = \frac{1 - \sqrt{5}}{2}$.
Then
$$F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}.$$

## Remarks

The proof uses the [[characteristic polynomial|~9efe1ccd]] $x^2 - x - 1$ of the recurrence. Its roots are $\varphi$ and $\psi$, so $\varphi^n$ and $\psi^n$ are [[solutions|~4eb1a320]], and the initial values fix the coefficients.
Because $|\psi^n / \sqrt{5}| < \frac{1}{2}$, $F_n$ is the integer nearest to $\varphi^n / \sqrt{5}$.

## Explanations

### L1 human

Fibonacci numbers are integers, but this formula uses $\sqrt{5}$, and the irrational parts cancel.
The term with $\psi^n$ is very small, so $F_n$ is close to $\varphi^n / \sqrt{5}$.

---
tag: 0VGPKZ8MRK
kind: statement
role: theorem
name: Continuity is equivalent to sequential continuity in metric spaces
msc: ["54E35"]
uses: [0SY9ECQ19Q, 06JYPJ4WHH, 0EKGKY5TGH]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Sequences and nets
---

## Statement

Let $X$ and $Y$ be [[metric spaces|063W5JMY85]] and let $f \colon X \to Y$ be a function.
Then $f$ is [[continuous|0SY9ECQ19Q]] if and only if $f(x_n) \to f(x)$ for each sequence $(x_n)$ in $X$ that [[converges|06JYPJ4WHH]] to a point $x$.

## Remarks

The condition on sequences is sequential continuity.
Proof of the converse: if $f$ is not continuous at $x$, then by [[epsilon-delta continuity|0EKGKY5TGH]] there are $\varepsilon > 0$ and points $x_n$ with $d(x_n, x) < 1/n$ and $d(f(x_n), f(x)) \ge \varepsilon$. Then $x_n \to x$, but $f(x_n) \not\to f(x)$.
The same equivalence holds at each single point.
In general topological spaces, continuity implies sequential continuity, but the converse can fail.

## Explanations

### L1 human

A continuous map sends convergent sequences to convergent sequences, with the right limit.
To show that a map is not continuous, it is often enough to find one sequence $x_n \to x$ with $f(x_n) \not\to f(x)$.

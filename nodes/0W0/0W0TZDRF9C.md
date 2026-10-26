---
tag: 0W0TZDRF9C
kind: statement
role: theorem
name: Continuous functions on a closed bounded interval are uniformly continuous
msc: [26A15]
uses: [0P27W9RW0G, 0A3CK6DVVB, 0KDJD249DT]
sources:
  - url: https://en.wikipedia.org/wiki/Heine–Cantor_theorem
    locator: lead section
---

## Statement

Let $a \le b$ and let $f \colon [a, b] \to \mathbb{R}$ be [[continuous|0P27W9RW0G]].
Then $f$ is [[uniformly continuous|0A3CK6DVVB]] on $[a, b]$.

## Remarks

Suppose not. Then there is $\varepsilon > 0$ and points $x_n, y_n$ with $|x_n - y_n| < 1/n$ and $|f(x_n) - f(y_n)| \ge \varepsilon$. A [[convergent subsequence|0KDJD249DT]] of $(x_n)$ leads to a contradiction with continuity.
The interval must be closed and bounded. The function $1/x$ is continuous on $(0, 1]$ but not uniformly continuous there.
The name honors Eduard Heine and Georg Cantor. Mathlib states it for compact sets, as `IsCompact.uniformContinuousOn_of_continuous`.

## Explanations

### L1 human

On a closed bounded interval, continuity at each point upgrades to uniform continuity.
There is no room for the function to become steeper and steeper.

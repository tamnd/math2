---
tag: ~fdc305aa
kind: statement
role: corollary
name: Reverse triangle inequality
msc: [26A03]
uses: [~5a13ada6]
sources:
  - url: https://en.wikipedia.org/wiki/Triangle_inequality
    locator: Reverse triangle inequality
---

## Statement

For all real numbers $a$ and $b$,
$$\bigl| |a| - |b| \bigr| \le |a - b|.$$

## Remarks

Proof: the [[triangle inequality|~5a13ada6]] gives $|a| = |(a - b) + b| \le |a - b| + |b|$, thus $|a| - |b| \le |a - b|$. Exchange $a$ and $b$ for the other sign.
It shows that the function $x \mapsto |x|$ is continuous on $\mathbb{R}$.

## Explanations

### L1 human

Two numbers that are close to each other have absolute values that are also close.
The difference of the distances to $0$ is at most the distance between the two numbers.

---
tag: 08NM8KQPDQ
kind: definition
name: Infinite limit
msc: [26A03]
defines: 0BH9JH7HBY
uses: [0TXTSEMHR5]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_function
    locator: Infinite limits
---

## Definition

Let $D \subseteq \mathbb{R}$, let $f \colon D \to \mathbb{R}$, and let $a$ be a limit point of $D$.
We say $f(x) \to +\infty$ as $x \to a$ if for each real $M$ there is $\delta > 0$ with $f(x) > M$ for all $x \in D$ with $0 < |x - a| < \delta$.
We define $f(x) \to -\infty$ in the same way, with $f(x) < M$.

## Remarks

An infinite limit is not a limit in the sense of [[limit of a function|0TXTSEMHR5]], which requires a real value $L$.
For example, $1/x^2 \to +\infty$ as $x \to 0$.
The same idea gives $f(x) \to +\infty$ as $x \to +\infty$. An example is $f(x) = x^2$.

## Explanations

### L1 human

An infinite limit means that $f(x)$ becomes as large as we like when $x$ is close to $a$.
The graph then has a vertical asymptote at $x = a$.

---
tag: ~ffcb9cda
kind: statement
role: proposition
name: C^1 functions are strictly differentiable
aliases: [continuously-differentiable-implies-strictly-differentiable]
msc: [26B05]
uses: [~a72eb5d5, ~1adf7722, ~fb845291]
sources:
  - url: https://en.wikipedia.org/wiki/Strict_differentiability
    locator: Basic definition
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, and let $f \colon U \to \mathbb{R}^m$ be of [[class C^1|~1adf7722]] on $U$.
Then $f$ is [[strictly differentiable|~a72eb5d5]] at each point $a \in U$, with linear map $Df(a)$.

## Remarks

Proof: let $\varepsilon > 0$ and choose $r > 0$ with $\|Df(z) - Df(a)\| \le \varepsilon$ for $\|z - a\| < r$. Apply the [[mean value inequality|~fb845291]] to $g(z) = f(z) - Df(a) z$ on the ball of radius $r$. This gives $\|f(x) - f(y) - Df(a)(x - y)\| \le \varepsilon \|x - y\|$ for $x, y$ in that ball.
For a function of one variable on an open interval, strict differentiability at each point is equivalent to being of class $C^1$.

## Explanations

### L1 human

If the derivative changes continuously, then near $a$ it stays close to $Df(a)$.
So every chord of the graph near $a$ has a slope close to $Df(a)$, which is what strict differentiability asks.

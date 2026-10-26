---
tag: 0VZVV8VME5
kind: statement
role: theorem
name: Compact closed unit ball implies finite dimension
msc: [46B50]
uses: [097C7KCAT5, 0K8SGQSV7G, 0ABP2F2ZP7, 0PHT6NBYPB]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz%27s_lemma
    locator: Characterization of finite dimension
---

## Statement

Let $X$ be a normed space over $\mathbb{R}$ or $\mathbb{C}$.
If the closed unit ball $\{ x \in X : \|x\| \le 1 \}$ is [[compact|00R0X1WGPX]], then $X$ is finite-dimensional.

## Remarks

Proof: if $X$ is infinite-dimensional, build unit vectors $x_1, x_2, \ldots$ by [[Riesz's lemma|097C7KCAT5]], with $x_{n+1}$ at distance at least $\tfrac{1}{2}$ from the span of $x_1, \ldots, x_n$. That span is finite-dimensional, so it is [[complete|0ABP2F2ZP7]] and closed. Then $\|x_m - x_n\| \ge \tfrac{1}{2}$ for $m \neq n$, so no subsequence converges, and the ball is not [[sequentially compact|0K8SGQSV7G]].
With the [[Heine–Borel theorem in finite dimension|0PHT6NBYPB]], we get: a normed space is finite-dimensional if and only if its closed unit ball is compact.
Equivalently, a normed space is locally compact if and only if it is finite-dimensional.

## Explanations

### L1 human

In infinite dimensions, the closed unit ball is never compact: there is always room for infinitely many unit vectors that stay far apart.
This is one of the main differences between finite and infinite dimensions.

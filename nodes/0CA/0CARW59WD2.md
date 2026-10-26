---
tag: 0CARW59WD2
kind: definition
name: Sequential compactness
aliases: [sequentially-compact-space, sequentially-compact-set]
msc: [54D30]
defines: 0FRMJH3CY7
uses: [0CNQXVBHCX]
sources:
  - url: https://en.wikipedia.org/wiki/Sequentially_compact_space
    locator: lead section
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $K \subseteq X$.
The set $K$ is sequentially compact when each sequence $(x_n)$ of points of $K$ has a subsequence $(x_{n_k})$ that converges to a point of $K$.
The space $X$ is sequentially compact when $X$ itself is a sequentially compact set.

## Remarks

Here a sequence $(y_k)$ converges to $y$ when each open set that contains $y$ contains $y_k$ for all large $k$. In a metric space, this is the [[usual convergence|06JYPJ4WHH]].
The interval $[0, 1]$ is sequentially compact by the Bolzano–Weierstrass theorem. The real line is not: the sequence $x_n = n$ has no convergent subsequence.
For metric spaces, [[compactness and sequential compactness agree|0K8SGQSV7G]]. In general topological spaces, neither notion implies the other.

## Explanations

### L1 human

In a sequentially compact set, a sequence cannot escape: some part of it always settles down to a point of the set.
In $(0, 1]$, the sequence $1/n$ tries to escape to $0$, which is outside the set. So $(0, 1]$ is not sequentially compact.

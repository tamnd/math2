---
tag: 0NRT0E2QT2
kind: statement
role: proposition
name: Connected components are closed
msc: [54D05]
uses: [0R37DFJKFW, 0DRKT1QJR7, 05GK32H72H]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: Connected components
---

## Statement

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $x \in X$.
The connected component of $x$ is the [[union|05GK32H72H]] $C(x)$ of all [[connected subsets|0R37DFJKFW]] of $X$ that contain $x$.
Then $C(x)$ is connected and [[closed|0G5AV9Q4RR]] in $X$.

## Remarks

Proof: a union of connected sets with a common point is connected, so $C(x)$ is the largest connected set that contains $x$. The [[closure|0DRKT1QJR7]] of $C(x)$ is also connected, so it equals $C(x)$.
The components of $X$ form a partition of $X$.
Components need not be open. In $\mathbb{Q}$, the components are the single points, which are not open.
If $X$ has only finitely many components, then each of them is also open.

## Explanations

### L1 human

The component of a point is the largest piece of the space that contains the point and is in one piece.
Taking the closure cannot make the piece larger, so each component is closed.

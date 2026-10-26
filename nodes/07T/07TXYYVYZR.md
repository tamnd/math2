---
tag: 07TXYYVYZR
kind: definition
name: Distance from a point to a set
msc: ["54E35"]
defines: 0WQ19TJV24
uses: [063W5JMY85, 04KFTA34C5]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_distance
    locator: Definition
---

## Definition

Let $(X, d)$ be a [[metric space|063W5JMY85]], let $A$ be a nonempty subset of $X$ and let $x \in X$.
The distance from $x$ to $A$ is the real number
$$d(x, A) = \inf \{ d(x, a) : a \in A \}.$$

## Remarks

The [[infimum|04KFTA34C5]] exists, because the set is nonempty and bounded below by $0$.
If $x \in A$, then $d(x, A) = 0$. The converse is false: in $\mathbb{R}$, $d(0, (0, 1)) = 0$ but $0 \notin (0, 1)$.
In general $d(x, A) = 0$ if and only if $x$ is in the [[closure|0DRKT1QJR7]] of $A$.
For all $x, y \in X$, $|d(x, A) - d(y, A)| \le d(x, y)$. Thus $x \mapsto d(x, A)$ is [[Lipschitz|0TMZ21WKCN]] with constant $1$.

## Explanations

### L1 human

The distance from a point to a set is the shortest distance from the point to the set, when a shortest distance exists.
For example, the distance from $3$ to the interval $[0, 1]$ is $2$.

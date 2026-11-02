---
tag: ESPDZT91QP
kind: example
name: Young's lattice
msc: [06D05, 05A17, "05E10"]
instance_of: [0HM0HQCK6N, 1C7TKGTB2F]
uses: [0JV30XN73Z, 096AHMB3P4, Q6TH9PH2R7]
sources:
  - url: https://en.wikipedia.org/wiki/Young's_lattice
---

## Example

Young's lattice $\mathbb{Y}$ is the set of all [[integer partitions|0JV30XN73Z]] $\lambda = (\lambda_1 \ge \lambda_2 \ge \cdots)$, including the empty partition.
It is ordered by $\lambda \le \mu$ when $\lambda_i \le \mu_i$ for all $i$, that is, when the [[Young diagram|096AHMB3P4]] of $\lambda$ fits inside that of $\mu$.

It is a [[distributive lattice|0HM0HQCK6N]].
The meet and join are $(\lambda \wedge \mu)_i = \min(\lambda_i, \mu_i)$ and $(\lambda \vee \mu)_i = \max(\lambda_i, \mu_i)$, the intersection and union of the diagrams.
Both are again weakly decreasing sequences, and $\min$ and $\max$ distribute over each other.

It is a [[graded poset|1C7TKGTB2F]] with rank function $\rho(\lambda) = \abs{\lambda} = \lambda_1 + \lambda_2 + \cdots$.
Indeed, $\mu$ covers $\lambda$ exactly when the diagram of $\mu$ is that of $\lambda$ with one more box.

## Remarks

The saturated chains from $\varnothing$ to $\lambda$ add one box at a time, so they correspond to the standard [[Young tableaux|Q6TH9PH2R7]] of shape $\lambda$.
For $\lambda = (2, 1)$ there are two of them: $\varnothing, (1), (2), (2, 1)$ and $\varnothing, (1), (1, 1), (2, 1)$.
The partitions of $n$ form the rank $n$ level, and their number is the partition number $p(n)$.

## Explanations

### L1 human

Draw each partition as a staircase of boxes in the top-left corner of a grid.
One staircase is below another if it fits inside it.
Going up one step in the lattice means adding one box, so climbing from nothing to a shape is a way of building that shape box by box.

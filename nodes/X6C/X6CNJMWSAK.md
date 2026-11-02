---
tag: X6CNJMWSAK
kind: definition
name: Exponential functions on semigroups
msc: [39B52, 20M15, 43A40]
defines: QWQ45PQTZT
uses: [0XMEM406JM, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Character_(mathematics)
---

## Definition

Let $S$ be a [[semigroup|0XMEM406JM]], with its operation written as $(x, y) \mapsto xy$.
An *exponential function* on $S$, or *exponential*, is a [[function|0EPAT51DXQ]] $m \colon S \to \C$ such that
$$m(xy) = m(x)\, m(y) \quad \text{for all } x, y \in S.$$

## Remarks

Example: on $S = (\R, +)$, $m(x) = e^{(1 + 2i) x}$ is an exponential, since $e^{(1 + 2i)(x + y)} = e^{(1 + 2i) x} e^{(1 + 2i) y}$.
Non-example: on $S = (\R, +)$, $m(x) = 2 e^x$ is not an exponential, since $m(0 + 0) = 2$ while $m(0) m(0) = 4$.
The zero function is an exponential; some authors exclude it.
If $S$ is a group and $m$ is not identically zero, then $m(e) = 1$, $m$ never vanishes, and $m$ is a homomorphism into the multiplicative group $\C^{\times}$.
An exponential on an abelian group whose values all have absolute value $1$ is a [[character|H1WNVN5V7F]] of the group.

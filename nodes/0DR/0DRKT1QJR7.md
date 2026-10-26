---
tag: 0DRKT1QJR7
kind: definition
name: Closure
msc: [54A05]
defines: 0QEAJB91GZ
uses: [0CNQXVBHCX, 0G5AV9Q4RR, 0839XNQXDK]
sources:
  - url: https://en.wikipedia.org/wiki/Closure_(topology)
    locator: Definitions
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $S \subseteq X$.
The closure of $S$ is the [[intersection|0839XNQXDK]] of all [[closed sets|0G5AV9Q4RR]] $F$ of $X$ with $S \subseteq F$.
It is written $\overline{S}$ or $\operatorname{cl} S$.

## Remarks

The family of these closed sets is not empty, because it contains $X$.
A point $x$ is in $\overline{S}$ if and only if each open set that contains $x$ meets $S$.
In $\mathbb{R}$, the closure of $(0, 1)$ is $[0, 1]$, and the closure of $\mathbb{Q}$ is $\mathbb{R}$.
The closure and the [[interior|0C38S0KMJK]] are related by $X \setminus \overline{S} = \operatorname{int}(X \setminus S)$.

## Explanations

### L1 human

The closure of a set adds to the set all the points that you can approach from inside it.
For the open interval $(0, 1)$, you add the two end points $0$ and $1$.

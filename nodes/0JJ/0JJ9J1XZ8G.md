---
tag: 0JJ9J1XZ8G
kind: definition
name: Boundary
aliases: [frontier, boundary-of-a-set]
msc: [54A05]
defines: 05D5EGMFYV
uses: [0DRKT1QJR7, 0C38S0KMJK, 0DT0TCV75N]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_(topology)
    locator: Definitions
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $S \subseteq X$.
The boundary of $S$ is the [[set difference|0DT0TCV75N]]
$$\partial S = \overline{S} \setminus \operatorname{int} S,$$
where $\overline{S}$ is the [[closure|0DRKT1QJR7]] and $\operatorname{int} S$ is the [[interior|0C38S0KMJK]] of $S$.

## Remarks

A point $x$ is in $\partial S$ if and only if each open set that contains $x$ meets both $S$ and $X \setminus S$.
The boundary is closed, and $\partial S = \partial (X \setminus S)$.
In $\mathbb{R}$, the boundary of $(0, 1)$ is $\{0, 1\}$, and the boundary of $\mathbb{Q}$ is $\mathbb{R}$.
Another name for the boundary is the frontier.

## Explanations

### L1 human

The boundary is the edge of a set. It has the points where you can step into the set and also out of it with a very small step.
For a disc in the plane, the boundary is its circle.

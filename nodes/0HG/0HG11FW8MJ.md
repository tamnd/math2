---
tag: 0HG11FW8MJ
kind: definition
name: First-countable space
msc: [54D70]
defines: 0CP5NDD21C
uses: [0CNQXVBHCX, 09CJ00H3NW, 0ZG61TFBES]
sources:
  - url: https://en.wikipedia.org/wiki/First-countable_space
    locator: lead section
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]].
The space $X$ is first-countable when each point $x \in X$ has a sequence $(N_n)_{n \ge 1}$ of [[neighbourhoods|09CJ00H3NW]] with this property: each neighbourhood of $x$ contains some $N_n$.

## Remarks

Such a sequence is a [[countable|0ZG61TFBES]] neighbourhood basis at $x$. One can choose the sets $N_n$ open, and also decreasing.
Each metric space is first-countable: take $N_n = B(x, 1/n)$, as in [[open balls form a basis|02EEX96DFS]].
Each [[second-countable space|00RE1R4W7N]] is first-countable.
In a first-countable space, a point is in the closure of a set $A$ exactly when it is a limit of a sequence in $A$.

## Explanations

### L1 human

At each point, you can shrink to the point along a countable list of neighbourhoods.
In a metric space, the balls of radius $1/n$ do this.

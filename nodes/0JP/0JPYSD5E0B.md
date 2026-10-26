---
tag: 0JPYSD5E0B
kind: definition
name: Order of an element
msc: [20A05]
defines: 0WE2NHZJ7B
uses: [G5S1M9, 00DRK90Z6K]
sources:
  - url: https://en.wikipedia.org/wiki/Order_(group_theory)
    locator: lead section
---

## Definition

Let $G$ be a [[group|G5S1M9]] with identity element $e$, and let $g \in G$.
When there is a positive integer $n$ with $g^n = e$, the order of $g$ is the smallest such $n$.
When there is no such $n$, the element $g$ has infinite order.
We write $\operatorname{ord}(g)$ or $|g|$ for the order of $g$.

## Remarks

The identity element is the only element of order $1$.
In $(\mathbb{Z}, +)$, each nonzero element has infinite order.
In the multiplicative group $\{1, i, -1, -i\}$, the element $-1$ has order $2$ and the element $i$ has order $4$.
In a finite group, each element has finite order, and the order of $g$ equals the [[order|0B85S2V2DR]] of the subgroup that $g$ generates.

## Explanations

### L1 human

Take an element and multiply it by itself again and again.
The order is the number of steps that you need to come back to the identity for the first time.
For a rotation by $90$ degrees, you need $4$ steps, so its order is $4$.

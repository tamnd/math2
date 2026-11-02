---
tag: QDJMVNVY8T
kind: definition
name: Ring of sets
msc: [28A05]
defines: KWE1DBMN9B
uses: [0SJ3RX9TXA, 07KVB4JSC7, 0HBRW4E6G1, PYH82FMXQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Ring_of_sets
---

## Definition

Let $X$ be a [[set|0SJ3RX9TXA]].
A *ring of sets* on $X$ is a nonempty family $\mathcal{R}$ of subsets of $X$ such that, for all $A, B \in \mathcal{R}$:

1. the [[union|07KVB4JSC7]] $A \cup B$ is in $\mathcal{R}$;
2. the difference $A \setminus B$ is in $\mathcal{R}$.

## Remarks

The finite subsets of $\N$ form a ring of sets: the union and the difference of two finite sets are finite.
This ring does not contain $\N$, so it is not an algebra of sets.
The bounded intervals of $\R$ do not form a ring of sets, since clause 2 fails: $[0, 3] \setminus [1, 2] = [0, 1) \cup (2, 3]$ is not an interval.
A ring contains $\varnothing = A \setminus A$ and the [[intersection|0HBRW4E6G1]] $A \cap B = A \setminus (A \setminus B)$.
It also contains the symmetric difference $A \mathbin{\triangle} B = (A \setminus B) \cup (B \setminus A)$.
With $\triangle$ as addition and $\cap$ as multiplication, a ring of sets is a commutative ring in the sense of algebra, possibly without identity.
Every ring of sets is a [[semiring of sets|PYH82FMXQ2]].

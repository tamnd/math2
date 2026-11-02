---
tag: MCPFA4DC9Z
kind: definition
name: Unknotting number
msc: [57K10]
defines: PW9D9QKAD4
uses: [QYEAZTYGPT, 1TQ06R4Q66]
sources:
  - url: https://en.wikipedia.org/wiki/Unknotting_number
---

## Definition

Let $K$ be a tame [[knot|QYEAZTYGPT]] in $\R^3$, and let $D$ be a diagram of $K$.
A *crossing change* at a crossing of $D$ exchanges the over-strand and the under-strand at that crossing.
Let $u(D)$ be the least number of crossings of $D$ whose simultaneous change gives a diagram of the [[unknot|1TQ06R4Q66]].
The *unknotting number* of $K$ is
$$u(K) = \min \set{u(D) : D \text{ is a diagram of } K}.$$

## Remarks

The number $u(D)$ is finite: changing suitable crossings of any diagram gives a diagram of the unknot.
Example: the standard three-crossing diagram of the [[trefoil knot|VYTYSVHN4A]] becomes a diagram of the unknot after one crossing change.
The trefoil is not the unknot, so its unknotting number is $1$.
Non-example of the minimum: a single diagram may need more changes than $u(K)$, so $u(D)$ for one fixed diagram $D$ is only an upper bound for $u(K)$.
A knot has $u(K) = 0$ if and only if it is the unknot.
The unknotting number of the [[torus knot|NS60VV786W]] $T(p, q)$ with coprime $p, q \ge 2$ is $(p-1)(q-1)/2$; this is the [[Milnor conjecture|5SDA7ZXT95]].

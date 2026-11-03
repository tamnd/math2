---
tag: DM88DY78CM
kind: definition
name: Statically indeterminate structure
msc: [70C20, 74K10]
defines: SKVPKD5VZN
uses: [0ZC9YTXZRY]
sources:
  - url: https://en.wikipedia.org/wiki/Statically_indeterminate
---

## Definition

Consider a structure in the linear (small displacement) setting.
Let its $n$ unknown static quantities, the support reactions and the internal member forces, form a vector $t \in \R^n$.
Let $m$ independent equilibrium equations relate them to the applied loads $f \in \R^m$ in the form $B t = f$, with an $m \times n$ equilibrium matrix $B$.
Assume that the structure is not a mechanism, that is, $B$ has [[rank|0ZC9YTXZRY]] $m$, so every load can be balanced.
The structure is *statically determinate* if $n = m$, so that $t = B^{-1} f$ is fixed by equilibrium alone.
It is *statically indeterminate* if $n > m$, and its *degree of static indeterminacy* is $n - m$, the dimension of the kernel of $B$.

## Remarks

Example: a straight beam in the plane with a pin at its left end and rollers at its middle and at its right end.
The unknowns are the two pin reactions and the two roller reactions, so $n = 4$, while plane equilibrium gives $m = 3$ equations.
The beam is statically indeterminate of degree $1$.

Non-example: the same beam with the middle roller removed is simply supported.
Then $n = 3 = m$, and the three reactions follow from equilibrium alone.

The vectors $t$ in the kernel of $B$ are the states of self-stress: internal forces in equilibrium with zero load.

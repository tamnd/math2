---
tag: XK7YECSHR9
kind: example
name: The subgroup 2Z of Z has no complement
msc: ["15A03", "13C05"]
topics: [QHKTJ89V6S]
audience: ug2
not_instance_of:
  - target: 0M83V17KHX
    note: Z is a module over the ring Z, which is not a field, and no submodule W of Z satisfies 2Z + W = Z and 2Z ∩ W = 0
illustrates: [0P9T8WHNMH]
uses: [04C3BAHV03, 0V33SPH7RR]
sources:
  - url: https://en.wikipedia.org/wiki/Complemented_subspace
    locator: Algebraic direct sum
---

## Example

Consider $\Z$ as a module over the ring $\Z$, and its submodule $2\Z$ of even integers.
We check that no submodule $W$ of $\Z$ satisfies $\Z = 2\Z \oplus W$.

1. The submodules of $\Z$ are the subgroups, and every subgroup of $\Z$ is $n\Z$ for some integer $n \ge 0$. So $W = n\Z$.
2. If $n = 0$, then $W = \{0\}$ and $2\Z + W = 2\Z \ne \Z$, since $1 \notin 2\Z$.
3. If $n \ge 1$, then $2n$ lies in $2\Z$ and in $n\Z$, and $2n \ne 0$. So the [[intersection|0V33SPH7RR]] $2\Z \cap W$ is not $\{0\}$.
4. In both cases, $W$ is not a [[complement|04C3BAHV03]] of $2\Z$.

So the [[existence of complements|0P9T8WHNMH]] fails when the field is replaced by the ring $\Z$.

## Remarks

The proof of existence over a field breaks at the step that divides by a nonzero scalar.
Here, $1 \notin 2\Z$, but $\Z \cdot 1 = \Z$ meets $2\Z$ in $2\Z \ne \{0\}$, because $2 \cdot 1 \in 2\Z$ and $2$ cannot be inverted in $\Z$.
The quotient $\Z / 2\Z$ has two elements and is not isomorphic to any submodule of $\Z$, since every nonzero submodule of $\Z$ is infinite.

## Explanations

### L1 human

Over the integers, we cannot divide by $2$.
Every nonzero set of the form $n\Z$ contains an even nonzero number, so it overlaps with the even numbers.

### L2 human

Over a field, the theorem on complements gives a subspace isomorphic to the quotient.
Here the quotient $\Z / 2\Z$ is a finite group, and $\Z$ has no finite nonzero subgroup.
This is a second reason why no complement exists.

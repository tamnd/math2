---
tag: 0B1FSS1VZW
kind: definition
name: Complement
msc: ["03E20"]
defines: 0RKF1ZT5JJ
uses: [0BPYRMHJ48, 0FE8Q5S42Y, 0EZ758XE73]
sources:
  - url: https://en.wikipedia.org/wiki/Complement_(set_theory)
    locator: lead section
---

## Definition

Let $U$ be a [[universal set|0BPYRMHJ48]] and let $A$ be a [[subset|0FE8Q5S42Y]] of $U$.
The complement of $A$ in $U$ is the set
$$A^{c} = \{x \in U \mid x \notin A\}.$$

## Remarks

Other notations are $\overline{A}$, $A'$ and $U \setminus A$.
Example: in $U = \mathbb{Z}$, the complement of the set of even integers is the set of odd integers.
The complement of $A^c$ is $A$, and $A \cup A^c = U$, $A \cap A^c = \varnothing$.
The complement of $A$ in $U$ is the [[set difference|0DT0TCV75N]] $U \setminus A$.

## Explanations

### L1 human

The complement is "everything else".
It depends on the universe: the complement of the even numbers is the odd numbers in $\mathbb{Z}$, but not in $\mathbb{R}$.

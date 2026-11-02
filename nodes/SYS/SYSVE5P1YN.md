---
tag: SYSVE5P1YN
kind: statement
role: theorem
name: Bogomolov–Miyaoka–Yau inequality
msc: [14J29, 32J15]
uses: [SV4CK2XP8M, KFTECAATKG, PAD37GKDPD, W05VYY4HBR]
about: [SV4CK2XP8M]
sources:
  - url: https://en.wikipedia.org/wiki/Bogomolov%E2%80%93Miyaoka%E2%80%93Yau_inequality
same_as:
  wikidata: Q4937705
  wikipedia: Bogomolov–Miyaoka–Yau inequality
---

## Statement

Let $X$ be a smooth projective [[surface of general type|SV4CK2XP8M]] over $\C$.
Let $c_1^2 = K_X^2$ be the self-intersection of its [[canonical divisor|W05VYY4HBR]], and let $c_2$ be its second [[Chern number|PAD37GKDPD]], equal to the topological Euler characteristic of $X$.
Then
$$c_1^2 \le 3 c_2.$$

## Remarks

Miyaoka and Yau proved the inequality independently, Miyaoka by algebraic methods and Yau by constructing Kähler–Einstein metrics; Bogomolov had earlier proved the weaker bound $c_1^2 \le 4 c_2$.
Yau's proof shows that equality holds exactly when $X$ is a quotient of the unit ball in $\C^2$ by a discrete group acting freely.
Examples are the fake projective planes, with $c_1^2 = 9$ and $c_2 = 3$.
Example: a smooth quintic surface in $\mathbb{P}^3$ has $c_1^2 = 5$ and $c_2 = 55$, and $5 \le 165$.
The hypothesis on the Kodaira dimension is needed: for $X = C \times \mathbb{P}^1$ with $C$ of genus $2$, one has $c_1^2 = 8(1 - 2) = -8$ and $c_2 = 4(1 - 2) = -4$, so $c_1^2 > 3 c_2 = -12$.
The inequality fails in positive characteristic in general.

## Explanations

### L1 human

Two numbers measure a complex surface: the self-intersection of its canonical class and its Euler characteristic.
For surfaces of general type, the first is never more than three times the second.
So surfaces of general type cannot be too curved compared with their topology.

### L2 human

Together with Noether's inequality $c_1^2 \ge 2 \chi(\mathcal{O}_X) - 6$ for minimal surfaces, the inequality confines the Chern numbers of surfaces of general type to a wedge, the domain of the geography of surfaces.
It is the surface case of the Chern number inequalities for varieties with Kähler–Einstein metrics.
Yau used the equality case to prove that every compact complex surface homotopy equivalent to $\mathbb{P}^2$ is isomorphic to $\mathbb{P}^2$.

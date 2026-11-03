---
tag: 4Q9PB2WPAY
kind: statement
role: theorem
name: Buckingham π theorem
msc: [76M55, 00A71]
uses: [T3R5FWV91P, 0ZC9YTXZRY, 0PHDYNR24D, 03GSZ8RTZJ, 0KCQ9Y3QKA]
about: [T3R5FWV91P]
sources:
  - url: https://en.wikipedia.org/wiki/Buckingham_π_theorem
same_as:
  wikidata: Q999783
  wikipedia: Buckingham π theorem
---

## Statement

Let $q_1, \dots, q_n$ be positive physical quantities whose dimensions are expressed in $k$ base dimensions.
Let $D$ be the $k \times n$ dimension matrix: its column $j$ lists the exponents of the base dimensions in $[q_j]$.
Let $r$ be the [[rank|0ZC9YTXZRY]] of $D$.

1. The exponent vectors $a \in \Q^n$ for which $q_1^{a_1} \cdots q_n^{a_n}$ is dimensionless are the elements of the [[null space|0PHDYNR24D]] of $D$, which has [[dimension|03GSZ8RTZJ]] $n - r$. A [[basis|0KCQ9Y3QKA]] $a^{(1)}, \dots, a^{(n-r)}$ of it gives dimensionless products $\pi_i = q_1^{a^{(i)}_1} \cdots q_n^{a^{(i)}_n}$, and every dimensionless power product of the $q_j$ is a product of real powers of $\pi_1, \dots, \pi_{n-r}$.
2. Let $f(q_1, \dots, q_n) = 0$ be a dimensionally homogeneous physical law. This means that it stays true when the units of the base dimensions are changed by any positive factors. Then for some function $F$ of $n - r$ variables, $f(q_1, \dots, q_n) = 0$ holds if and only if $F(\pi_1, \dots, \pi_{n-r}) = 0$.

## Remarks

Part 1 is linear algebra: the dimension of a power product is $D a$, and rank–nullity gives the dimension $n - r$ of the null space.
For part 2, choose $r$ of the quantities with independent dimensions.
A change of units sets these all equal to $1$, and then the other quantities become dimensionless products, which are the $\pi_i$.
Example: the period $T$ of a pendulum of length $\ell$ and mass $m$ under gravity $g$ involves $n = 4$ quantities and the $k = 3$ dimensions mass, length and time, with $r = 3$.
So there is one product $\pi_1 = T \sqrt{g / \ell}$, and the law reads $F(\pi_1) = 0$, that is $T = C \sqrt{\ell / g}$ for a constant $C$; the mass drops out.
The theorem does not give $F$ or the constant $C$, and it gives nothing if a relevant quantity is left out of the list.

## Explanations

### L1 human

Physical laws cannot depend on whether you measure in metres or in feet.
The theorem turns this simple fact into a counting rule: a law involving $n$ quantities built from $r$ independent units can always be rewritten with only $n - r$ unit-free combinations.
So an experiment that seemed to depend on many variables really depends on fewer.
For a pendulum, it shows without solving any equation that the period is proportional to the square root of the length.

### L2 human

The theorem is the formal basis of dimensional analysis and of the [[dimensionless numbers of fluid mechanics|T3R5FWV91P]].
Take the drag force on a sphere in a viscous fluid.
The quantities force, density, speed, diameter and viscosity give $5 - 3 = 2$ dimensionless groups, the drag coefficient and the Reynolds number.
So the drag coefficient is a function of the Reynolds number alone.
This is what makes model tests possible: matching the dimensionless groups of a model and of a full-scale object makes their dimensionless behaviour equal.
The choice of the basis of the null space is not unique, so different authors may use different but equivalent sets of $\pi$ groups.

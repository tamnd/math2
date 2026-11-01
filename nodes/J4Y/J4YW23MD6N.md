---
tag: J4YW23MD6N
kind: statement
role: proposition
name: Quasi-compactness of the spectrum
msc: [14A05, 13A15, 54D30]
uses: [FB45BHHA2J, 8SQK7RTB63, N6JX9BCKQP, 0TVJZYB6SH, 096Z9MP2ME]
about: [FB45BHHA2J]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_of_a_ring
---

## Statement

Let $R$ be a [[commutative ring|0310REJJY8]].
Then the [[spectrum|FB45BHHA2J]] $\operatorname{Spec} R$ with the [[Zariski topology|8SQK7RTB63]] is quasi-compact: every cover of $\operatorname{Spec} R$ by open sets has a finite subcover.

## Remarks

It is enough to treat covers by [[basic open sets|N6JX9BCKQP]] $D(f_i) = \set{\mathfrak p : f_i \notin \mathfrak p}$, $i \in I$.
These cover $\operatorname{Spec} R$ exactly when no prime ideal contains all $f_i$.
Since every proper [[ideal|096Z9MP2ME]] lies in a [[maximal ideal|0PV74TR5FP]], this means that the $f_i$ generate the unit ideal.
Then $1 = a_1 f_{i_1} + \cdots + a_n f_{i_n}$ for finitely many indices, and $D(f_{i_1}), \ldots, D(f_{i_n})$ already cover.

Example: $D(2)$ and $D(3)$ cover $\operatorname{Spec} \Z$, because $1 = 3 - 2$.

The word "quasi-compact" is used because the space is usually not [[Hausdorff|0S1FJ8VEX9]], and some authors reserve "[[compact|0TVJZYB6SH]]" for Hausdorff spaces.
The same argument shows that each basic open set $D(f)$ is quasi-compact, since $D(f) \cong \operatorname{Spec} R_f$.

## Explanations

### L1 human

However you cover the spectrum of a ring with open sets, a finite number of them already do the job.
The reason is algebraic: covering the space means producing $1$ from the given elements, and any such expression uses only finitely many of them.

### L2 human

Quasi-compactness of $\operatorname{Spec} R$ is the algebraic shadow of the fact that $1$ is a finite sum.
It is used to pass from local to global data in finitely many steps.
For example, it lets one glue finitely many local constructions, or bound a quantity over a finite cover.
In scheme theory, it says that affine schemes are quasi-compact.
It is one of the conditions in [[Hochster's theorem on spectral spaces|C82AXZK2BS]].

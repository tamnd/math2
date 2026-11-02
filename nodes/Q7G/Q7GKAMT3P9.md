---
tag: Q7GKAMT3P9
kind: statement
role: theorem
name: Denjoy theorem on rotation number
msc: ["37E10", "37E45"]
uses: [DP4WWQBJJF, 0KZZ70ZHXP, HNXXAPQKG3, 2Q1J7RZ4TK, A8251BHCMP, 0BXNDZFQME, NZZE9KCAD8]
about: [DP4WWQBJJF]
sources:
  - url: https://en.wikipedia.org/wiki/Denjoy%27s_theorem_on_rotation_number
same_as:
  wikidata: Q4454940
  wikipedia: Denjoy's theorem on rotation number
---

## Statement

Let $f$ be an orientation-preserving $C^1$ [[diffeomorphism|0KZZ70ZHXP]] of the circle $S^1 = \R / \Z$ such that $\log f'$ has [[bounded variation|A8251BHCMP]]; for example, let $f$ be of class $C^2$.
Assume that the [[rotation number|DP4WWQBJJF]] $\rho$ of $f$ is irrational.
Then $f$ is [[topologically conjugate|HNXXAPQKG3]] to the rotation $R_\rho(x) = x + \rho$: there is a homeomorphism $h$ of $S^1$ with $h \circ f = R_\rho \circ h$.

## Remarks

By Poincaré's classification, $f$ is semiconjugate to $R_\rho$, and it is conjugate unless $f$ has a wandering interval, an open interval $J$ whose images $f^n(J)$, $n \in \Z$, are pairwise disjoint.
The proof rules out wandering intervals.
Let $q_n$ be the denominators of the continued fraction of $\rho$.
A combinatorial argument finds intervals whose images under $f^{q_n}$ overlap little, and the Denjoy inequality bounds $\abs{\log (f^{q_n})'}$ by the total variation of $\log f'$.
For a wandering interval $J$ this gives a constant $c > 0$ with $\abs{f^{q_n}(J)} + \abs{f^{-q_n}(J)} \ge c \abs{J}$ for all $n$.
But the images of $J$ are pairwise disjoint, so their lengths tend to $0$, which is a contradiction.

The smoothness hypothesis cannot be dropped.
Denjoy also built $C^1$ diffeomorphisms with irrational rotation number that have a wandering interval.
For them the omega-limit set of every point is a [[Cantor set|0BXNDZFQME]] and $f$ is not conjugate to a rotation.
Such examples exist even of class $C^{1 + \alpha}$ for every $\alpha < 1$.

The conjugacy $h$ is only a homeomorphism in general; whether it is smooth depends on arithmetic properties of $\rho$, a question studied by Arnold, Herman and Yoccoz.

## Explanations

### L1 human

A smooth map of the circle that never brings a point back to itself turns out to be a rigid irrational rotation in disguise.
One can change coordinates on the circle, continuously, so that the map becomes a plain rotation.
For maps that are only once differentiable this can fail: some intervals may wander around the circle forever without overlapping.

### L2 human

The theorem completes Poincaré's classification for smooth circle diffeomorphisms: up to topological conjugacy, a $C^2$ diffeomorphism with irrational rotation number is determined by that number.
It implies that every orbit of such a map is dense and that the map is minimal and [[uniquely ergodic|NZZE9KCAD8]], since the [[irrational rotation|2Q1J7RZ4TK]] has these properties.
The key tool, control of the distortion of $(f^n)'$ through bounded variation of $\log f'$, reappears in many places in one-dimensional dynamics.
Denjoy published the theorem in 1932.

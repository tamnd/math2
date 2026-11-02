---
tag: PDVJTYCK8F
kind: statement
role: theorem
name: Bishop–Phelps theorem
msc: [46B20, 47A30]
uses: [06GZ956657, 4A82S5FVRT, 02AS45T3H9, 0BSJSX7ME2]
about: [4A82S5FVRT]
sources:
  - url: https://en.wikipedia.org/wiki/Bishop%E2%80%93Phelps_theorem
same_as:
  wikidata: Q16842437
  wikipedia: Bishop–Phelps theorem
---

## Statement

Let $X$ be a real [[Banach space|06GZ956657]] with [[continuous dual space|4A82S5FVRT]] $X^*$, and let $C \subseteq X$ be a nonempty, closed, bounded [[convex set|02AS45T3H9]].
Say that $f \in X^*$ attains its supremum on $C$ when $f(c) = \sup_{x \in C} f(x)$ for some $c \in C$.
Then the set of such functionals is [[dense|0BSJSX7ME2]] in $X^*$ for the norm topology.
In particular, taking $C$ to be the closed unit ball, the functionals $f \in X^*$ with $f(x) = \norm{f}$ for some $x$ with $\norm{x} \le 1$ are dense in $X^*$.

## Remarks

Proof idea: given $f \in X^*$ and $\varepsilon > 0$, one considers a cone determined by $f$ and $\varepsilon$.
A maximality argument, in the spirit of Zorn's lemma or of Ekeland's principle, gives $c \in C$ such that the cone translated to $c$ meets $C$ only at $c$.
The Hahn–Banach separation theorem then gives a functional $g$ that attains its supremum on $C$ at $c$ and satisfies $\norm{f - g} \le \varepsilon$.

Example: let $X = c_0$ be the space of real sequences tending to $0$, with the supremum norm.
The functional $f(x) = \sum_{n \ge 1} 2^{-n} x_n$ does not attain its norm $1$ on the unit ball, since that would need $x_n = 1$ for all $n$.
The truncations $g_N(x) = \sum_{n \le N} 2^{-n} x_n$ attain their norm at $x = (1, \ldots, 1, 0, 0, \ldots)$ and converge to $f$ in norm, as the theorem predicts.

The density cannot be improved to equality in general: by James' theorem, every functional attains its norm on the unit ball only when $X$ is reflexive.
The analogue for bounded operators between Banach spaces, in place of functionals, fails in general.

## Explanations

### L1 human

A functional attains its norm if some vector of length at most $1$ realizes its largest value.
In infinite dimensions this can fail, because the unit ball is not compact.
The theorem says that such failures are rare: every functional can be approximated as closely as one likes by functionals that do attain their norm.

### L2 human

Norm-attaining functionals correspond to supporting hyperplanes of the unit ball, so the theorem says that support points of closed bounded convex sets are plentiful.
It is used in the geometry of Banach spaces, for instance in the study of smoothness and of subdifferentials of convex functions.
The complex case follows from the real one, by viewing a complex Banach space as a real one.

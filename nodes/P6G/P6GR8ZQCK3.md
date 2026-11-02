---
tag: P6GR8ZQCK3
kind: statement
role: theorem
name: Wirtinger presentation
msc: [57K10, 57M05]
uses: [QYEAZTYGPT, AQVHM3FP0D, 0JGEQXQ4AC]
about: [AQVHM3FP0D]
sources:
  - url: https://en.wikipedia.org/wiki/Wirtinger_presentation
same_as:
  wikidata: Q8027029
  wikipedia: Wirtinger presentation
---

## Statement

Let $K$ be an oriented tame [[knot|QYEAZTYGPT]] in $\R^3$, with a diagram that has $n \ge 1$ crossings.
The diagram breaks into $n$ arcs $a_1, \ldots, a_n$, each running from one undercrossing to the next.
Take a base point above the plane of the diagram.
For each arc $a_i$, let $x_i$ be the class of a loop from the base point that passes once under $a_i$, by the right-hand rule.
At a crossing, let $a_k$ be the over-arc, let $a_i$ be the incoming under-arc and let $a_j$ be the outgoing under-arc.
Let $\varepsilon = \pm 1$ be the sign of the crossing.
Write $r$ for the relation $x_j = x_k^{\varepsilon} x_i x_k^{-\varepsilon}$ at this crossing.
Then the [[knot group|AQVHM3FP0D]] of $K$ has the [[presentation|0JGEQXQ4AC]]
$$\pi_1(\R^3 \setminus K) \cong \langle x_1, \ldots, x_n \mid r_1, \ldots, r_n \rangle,$$
with one relation $r_c$ for each crossing $c$.
Any one of the relations may be omitted.

## Remarks

The proof applies the Seifert–van Kampen theorem to the complement, cut into the half-space above the diagram plane and small pieces near the crossings.
The half-space above, with tunnels under the arcs, gives a free group on the $x_i$, and each crossing adds one relation.
The sign convention for $\varepsilon$ depends on the orientation chosen for the loops $x_i$; with the opposite choice, $\varepsilon$ becomes $-\varepsilon$.
For the trefoil with arcs $a_1, a_2, a_3$, the relations read $x_3 = x_1 x_2 x_1^{-1}$, $x_1 = x_2 x_3 x_2^{-1}$ and $x_2 = x_3 x_1 x_3^{-1}$ for one orientation.
Eliminating $x_3$ and dropping the last relation gives $\langle x_1, x_2 \mid x_1 x_2 x_1 = x_2 x_1 x_2 \rangle$.
All generators are conjugate, because each relation conjugates one generator to another and the arcs are connected by the knot.
The hypothesis $n \ge 1$ is needed: a diagram of the unknot with no crossings has one arc and no crossing, and its group is $\Z$.

## Explanations

### L1 human

The knot group describes loops that wind around a knot.
The Wirtinger presentation reads this group off a picture of the knot: one generator for each strand of the picture, and one rule for each crossing.
The rule says that passing under one side of the crossing equals passing under the other side, conjugated by the strand on top.

### L2 human

It is the standard way to compute knot groups and their invariants.
Representations of the knot group into a finite group can be found from it by assigning elements to arcs.
[[Tricolorability|KNAGK0W65G]] is the case of the symmetric group on three letters.
The Alexander polynomial can be computed from it by Fox calculus.
The presentation has deficiency one, with one more generator than essential relations.

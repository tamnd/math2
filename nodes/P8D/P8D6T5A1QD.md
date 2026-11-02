---
tag: P8D6T5A1QD
kind: conjecture
name: Littlewood conjecture
msc: ["11J13", "37A17", "22E40"]
uses: [0DZXAXEJQ9, 04P2RJ4WPS]
about: [0DZXAXEJQ9]
sources:
  - url: https://en.wikipedia.org/wiki/Littlewood_conjecture
same_as:
  wikidata: Q6653177
  wikipedia: Littlewood conjecture
history:
  posed_by: "John Edensor Littlewood"
  first_stated: "1930"
---

## Statement

For a real number $x$, let $\norm{x}$ denote the distance from $x$ to the nearest integer.
For every pair of real numbers $\alpha$ and $\beta$,
$$\liminf_{n \to \infty} \, n \, \norm{n\alpha} \, \norm{n\beta} = 0,$$
where $n$ runs over the positive integers.

## Remarks

The problem is open; Littlewood posed it around 1930.
It holds if $\alpha$ is not badly approximable, that is, if $\liminf_n n \norm{n\alpha} = 0$.
Indeed $\norm{n\beta} \le 1/2$ gives $n \norm{n\alpha} \norm{n\beta} \le n \norm{n\alpha} / 2$.
Rational numbers are not badly approximable, and the same holds with the roles of $\alpha$ and $\beta$ exchanged.
By the theory of [[continued fractions|04P2RJ4WPS]], a number is badly approximable exactly when its partial quotients are bounded, so the open case is a pair of such [[irrational numbers|0DZXAXEJQ9]].
Cassels and Swinnerton-Dyer proved it in 1955 when $1, \alpha, \beta$ span a totally real cubic number field.
Einsiedler, Katok and Lindenstrauss proved in 2006 that the set of pairs $(\alpha, \beta)$ for which it fails has Hausdorff dimension $0$.
Their proof uses the action of the diagonal group on $\mathrm{SL}_3(\R)/\mathrm{SL}_3(\Z)$ and the rigidity of measures invariant under it.

## Explanations

### L1 human

Every real number can be approximated by fractions, and some numbers, like the golden ratio, resist this as much as possible.
The conjecture says that two such numbers cannot resist at the same time: some multiple $n\alpha$ and $n\beta$ are both unusually close to integers.
Here unusually close means that the product of the two errors beats $1/n$ by any factor you like.
It is a simple-looking statement about pairs of numbers that has been open for nearly a century.

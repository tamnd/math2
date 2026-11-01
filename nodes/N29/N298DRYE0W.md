---
tag: N298DRYE0W
kind: conjecture
name: Andrews–Curtis conjecture
msc: ["20F05", "57M20"]
uses: [0JGEQXQ4AC, 0KTW26C80J, 0DXD4QSZ8A]
about: [0JGEQXQ4AC]
sources:
  - url: https://en.wikipedia.org/wiki/Andrews%E2%80%93Curtis_conjecture
same_as:
  wikidata: Q2409999
  wikipedia: Andrews–Curtis conjecture
history:
  posed_by: "James J. Andrews and Morton L. Curtis"
  first_stated: "1965"
---

## Statement

A [[presentation|0JGEQXQ4AC]] $\langle x_1, \ldots, x_n \mid r_1, \ldots, r_n \rangle$ is *balanced* if it has as many relators as generators.
The *Andrews–Curtis moves* on such a presentation, with $r_i$ elements of the [[free group|0KTW26C80J]] $F$ on $x_1, \ldots, x_n$, are:

1. replace some $r_i$ by $r_i^{-1}$;
2. replace some $r_i$ by $r_i r_j$ for some $j \ne i$;
3. replace some $r_i$ by $g r_i g^{-1}$ for some $g \in F$.

The conjecture: every balanced presentation of the trivial group can be turned into the trivial presentation $\langle x_1, \ldots, x_n \mid x_1, \ldots, x_n \rangle$ by a finite sequence of Andrews–Curtis moves.

## Remarks

Each move keeps the normal closure of the relators, so it keeps the group.
A presentation of the trivial group with $n$ generators has at least $n$ relators, since the abelianization $\Z^n$ must become trivial; so the balanced ones are the extreme case.
A weaker stable form of the conjecture also allows adding a generator $x_{n+1}$ with relator $x_{n+1}$, and removing such a pair.
Andrews and Curtis stated the conjecture in 1965, in connection with the topology of $2$-dimensional complexes and $4$-dimensional manifolds.
It is open; many experts expect it to be false, and several families of balanced presentations of the trivial group are studied as potential counterexamples.

## Explanations

### L1 human

Write the trivial group with $n$ generators and $n$ rules in a complicated way.
The conjecture says that one can always simplify the rules to the obvious ones, $x_1 = 1, \ldots, x_n = 1$.
Only three simple moves are allowed: invert a rule, multiply a rule by another, or conjugate a rule.
For example, $\langle x, y \mid x y^{-1}, y \rangle$ becomes trivial: multiply the first rule by the second to get $x$.
The difficulty is that the needed sequence of moves may be extremely long or may not exist at all.

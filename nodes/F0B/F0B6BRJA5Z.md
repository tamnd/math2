---
tag: F0B6BRJA5Z
kind: problem
name: Whitehead problem
msc: [20K20, 20K35, "03E35"]
uses: [082GHNPJ53, 0JYTG5K9Y4, 0WJX8MGG37, 4P7GBWJ4RR, 0HE5WDQ9FJ]
about: [0WJX8MGG37, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Whitehead_problem
same_as:
  wikidata: Q2905020
  wikipedia: Whitehead problem
history:
  posed_by: "J. H. C. Whitehead"
---

## Problem

Let $A$ be an [[abelian group|082GHNPJ53]].
Then $A$ is a *Whitehead group* if the following holds for every abelian group $B$.
For every surjective [[homomorphism|0JYTG5K9Y4]] $f \colon B \to A$ with kernel isomorphic to $\Z$, there is a homomorphism $g \colon A \to B$ with $f \circ g = \id_A$.
Equivalently, $\mathrm{Ext}^1(A, \Z) = 0$, in terms of the [[Ext functor|4P7GBWJ4RR]].
The Whitehead problem asks: is every Whitehead group a [[free abelian group|0WJX8MGG37]]?

## Remarks

Every free abelian group is a Whitehead group, because a surjection onto a free abelian group always splits: send each basis element to any preimage.
Every countable Whitehead group is free, so the question concerns uncountable groups.
Shelah showed in 1974 that the problem is independent of [[ZFC|0HE5WDQ9FJ]].
If the axiom of constructibility $V = L$ holds, then every Whitehead group is free.
If Martin's axiom holds together with the negation of the continuum hypothesis, then there is a Whitehead group that is not free.

## Explanations

### L1 human

An abelian group is free if it has a basis, like $\Z^n$.
Free groups have a lifting property: any map onto them from a bigger group, with kernel $\Z$, can be reversed.
J. H. C. Whitehead asked whether this lifting property characterises the free groups.
The surprising answer is that the usual axioms of set theory cannot decide it: in some models of set theory the answer is yes, in others it is no.

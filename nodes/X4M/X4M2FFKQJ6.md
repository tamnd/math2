---
tag: X4M2FFKQJ6
kind: statement
role: lemma
name: Schur's lemma
msc: [16D60, 20C05]
uses: [09VDS2W1E8, G00C22AEDH]
about: [G00C22AEDH]
sources:
  - url: https://en.wikipedia.org/wiki/Schur%27s_lemma
same_as:
  wikidata: Q1816952
  wikipedia: Schur's lemma
---

## Statement

Let $R$ be a ring and let $M$ and $N$ be [[simple|G00C22AEDH]] left [[$R$-modules|09VDS2W1E8]].
Let $f \colon M \to N$ be a homomorphism of $R$-modules.
Then either $f = 0$ or $f$ is an isomorphism.

## Remarks

The kernel of $f$ is a submodule of $M$, so it is $0$ or $M$.
The image of $f$ is a submodule of $N$, so it is $0$ or $N$.
If $f \ne 0$, the kernel is not $M$ and the image is not $0$, so $f$ is injective and surjective.
Example: a nonzero group homomorphism $\Z/p\Z \to \Z/p\Z$, for $p$ prime, is a bijection.
Simplicity is needed: the map $\Z/4\Z \to \Z/4\Z$, $x \mapsto 2x$, is nonzero and not an isomorphism.
A common form concerns an algebraically closed field $k$, a $k$-algebra $A$, and a simple $A$-module $M$ of finite dimension over $k$.
Then every endomorphism of $M$ is multiplication by a scalar.

## Explanations

### L1 human

A simple module has no proper nonzero pieces.
A map between two simple modules therefore has no room to be "partly" zero: it either kills everything or matches the two modules exactly.

### L2 human

Schur's lemma is the first tool of representation theory.
It shows that the endomorphism ring of a simple module is a division ring.
For representations of a group over $\C$ it gives that the endomorphisms of an irreducible representation are scalars.
This is the key step in the orthogonality relations for characters and in the decomposition of semisimple modules into isotypic parts.

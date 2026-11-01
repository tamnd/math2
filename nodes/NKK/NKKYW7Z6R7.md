---
tag: NKKYW7Z6R7
kind: statement
role: theorem
name: Alexander subbase theorem
msc: [54D30]
uses: [0CQHFPGJ45, 09S8DV34Y0, 049PXYHW1T, 0TVJZYB6SH, 04RXTQA5ZA]
about: [0TVJZYB6SH, 09S8DV34Y0]
sources:
  - url: https://en.wikipedia.org/wiki/Alexander's_subbase_lemma
---

## Statement

Let $X$ be a [[topological space|0CQHFPGJ45]], and let $\mathcal S$ be a [[subbasis|09S8DV34Y0]] of its topology.
Suppose that every [[cover|049PXYHW1T]] of $X$ by members of $\mathcal S$ has a finite subcover.
Then $X$ is [[compact|0TVJZYB6SH]].

## Remarks

Suppose $X$ is not compact.
By [[Zorn's lemma|04RXTQA5ZA]], there is an open cover $\mathcal C$ without finite subcover that is maximal for inclusion among such covers.
For $x \in U \in \mathcal C$, choose $S_1, \ldots, S_n \in \mathcal S$ with $x \in S_1 \cap \cdots \cap S_n \subseteq U$.
If no $S_i$ were in $\mathcal C$, maximality would give finite sets $\mathcal C_i \subseteq \mathcal C$ with $S_i \cup \bigcup \mathcal C_i = X$, and then $U$ with all $\mathcal C_i$ would be a finite subcover.
So $\mathcal C \cap \mathcal S$ covers $X$, and by hypothesis it has a finite subcover, a contradiction.

Example: the sets $[0, c)$ and $(c, 1]$ for $0 < c < 1$ form a subbasis of $[0, 1]$.
A cover by such sets contains some $[0, c)$ and some $(c', 1]$ with $c' < c$, by a supremum argument, so $[0, 1]$ is compact.
The theorem also gives a direct proof of [[Tychonoff's theorem|0JTRSJKCFB]].

The subbasis hypothesis is needed.
On $\R$, the family $\set{\R}$ has the finite subcover property, but it is not a subbasis of the usual topology, and $\R$ is not compact.

## Explanations

### L1 human

To show that a space is compact, one must handle every open cover.
The theorem says that it is enough to handle covers made of the simplest open sets, those of a chosen subbasis.
This cuts down the work a lot when the subbasis is easy to describe.

### L2 human

The product topology has a natural subbasis: the preimages of open sets under single projections.
With the theorem, compactness of a product of compact spaces reduces to covers by such sets, which is a short argument; this is one standard proof of Tychonoff's theorem.
The proof uses Zorn's lemma, and the theorem is equivalent to the ultrafilter lemma over the axioms of set theory without choice.

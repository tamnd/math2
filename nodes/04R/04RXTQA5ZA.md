---
tag: 04RXTQA5ZA
kind: statement
role: theorem
name: Zorn's lemma
aliases: [zorn-lemma, kuratowski-zorn-lemma]
msc: ["03E25"]
uses: [0GP9ASVQ1X, 0H5J02P8S9, 0TZEEFTNCC, 0HTGB13FE2]
sources:
  - url: https://en.wikipedia.org/wiki/Zorn's_lemma
    locator: Statement of the lemma
same_as:
  wikidata: Q290810
  wikipedia: Zorn's lemma
---

## Statement

Assume the [[axiom of choice|0HTGB13FE2]].
Let $(P, \le)$ be a nonempty [[partially ordered set|011C29Q1S1]] in which each [[chain|0GP9ASVQ1X]] has an [[upper bound|0H5J02P8S9]] in $P$.
Then $P$ has a [[maximal element|0TZEEFTNCC]].

## Remarks

Over ZF, Zorn's lemma is equivalent to the axiom of choice.
If one requires an upper bound also for the empty chain, the hypothesis "$P$ is nonempty" is not needed.
Applications: each vector space has a basis, and each nonzero ring with unity has a maximal ideal.

## History

Kazimierz Kuratowski proved the lemma in 1922, and Max Zorn proved it independently in 1935.
The [[Hausdorff maximal principle|0KM4KVR9MV]] of 1914 is an earlier statement of the same kind.

## Explanations

### L1 human

Zorn's lemma is a tool to show that a maximal object exists.
You check that each increasing chain of objects has an object above it.
Then the lemma gives an object that you cannot enlarge any more.

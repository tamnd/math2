---
tag: 0QTZDKJEDV
kind: statement
role: lemma
name: Frattini argument
aliases: [frattinis-argument]
msc: [20D20]
uses: [09GCQ5STVJ, 0AT1ZSNM25, 0NS1YTGM19]
sources:
  - url: https://en.wikipedia.org/wiki/Frattini's_argument
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Frattini's_argument
    locator: lead section
same_as:
  wikidata: Q1053997
  wikipedia: Frattini's argument
---

## Statement

Let $G$ be a finite [[group|G5S1M9]], let $H$ be a [[normal subgroup|0CB0DX5BVV]] of $G$, and let $P$ be a [[Sylow p-subgroup|0053CQE9Y2]] of $H$.
Then $G = N_G(P) H$, where $N_G(P)$ is the [[normaliser|0YGN3VAA0D]] of $P$ in $G$.

## Remarks

For $g \in G$, the subgroup $gPg^{-1}$ lies in $H$, because $H$ is normal, and it is a Sylow $p$-subgroup of $H$.
By the [[second Sylow theorem|09GCQ5STVJ]] in $H$, there is $h \in H$ with $gPg^{-1} = hPh^{-1}$, so $h^{-1}g \in N_G(P)$.
The argument is used in the proof that a finite [[nilpotent group|0Q7MMQHC1P]] is the [[direct product of its Sylow subgroups|00Y9N80VSS]].

## History

Giovanni Frattini used the argument in a paper from 1885.
He took it, as he said himself, from a paper of Alfredo Capelli from 1884.

## Explanations

### L1 human

Conjugation by an element of $G$ moves $P$ to another Sylow subgroup of $H$.
An element of $H$ can move it back.
So each element of $G$ is an element of $H$ times an element that normalises $P$.

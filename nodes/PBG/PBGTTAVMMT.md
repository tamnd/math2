---
tag: PBGTTAVMMT
kind: problem
name: Word problem for groups
msc: [20F10, 03D40]
uses: [0JGEQXQ4AC, 0KTW26C80J, PPGD5KW8JC]
about: [0JGEQXQ4AC]
sources:
  - url: https://en.wikipedia.org/wiki/Word_problem_for_groups
same_as:
  wikidata: Q8034369
  wikipedia: Word problem for groups
history:
  posed_by: "Max Dehn"
  first_stated: "1911"
---

## Problem

Let $G = \langle S \mid R \rangle$ be a group given by a finite [[presentation|0JGEQXQ4AC]], with a finite set $S$ of generators and a finite set $R$ of relators.
A *word* is a finite sequence of elements of $S \cup S^{-1}$, that is, an element of the [[free group|0KTW26C80J]] $F(S)$.
The word problem for $G$ asks for an algorithm that decides, for every word $w$, whether $w$ represents the identity element of $G$.
Equivalently: is the set of words that represent the identity a [[computable set|PPGD5KW8JC]]?

## Remarks

The answer depends on the group.
The word problem is solvable for free groups, by free reduction, and for finite groups.
Magnus showed that it is solvable for every group with one defining relator.
Dehn gave an algorithm for the fundamental groups of closed orientable surfaces of genus at least $2$.
Novikov (1955) and Boone (1958) independently constructed finitely presented groups whose word problem is unsolvable.
The set of words that represent the identity is always computably enumerable, so the word problem asks only whether its complement is too.
Whether the word problem is solvable does not depend on the chosen finite presentation of $G$.

## Explanations

### L1 human

A group can be described by a few generators and a few rules saying which products equal the identity.
The question is whether there is a mechanical way to tell, for any product of generators, whether it equals the identity.
For many familiar groups there is, but there are groups, described by finitely many rules, where no computer program can answer the question.

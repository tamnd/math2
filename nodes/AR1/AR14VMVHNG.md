---
tag: AR14VMVHNG
kind: problem
name: Word problem for free algebras of a variety
msc: [08A50, 08B20, 03B25]
uses: [GTS4DRRMZR, AJNZJD8442, 9Q008GMZSW, F1M51B4MDG, PKD440G2XW, KZSB5E471K]
about: [GTS4DRRMZR, F1M51B4MDG]
sources:
  - url: https://en.wikipedia.org/wiki/Word_problem_(mathematics)
    locator: History
history:
  posed_by: "Axel Thue"
  first_stated: "1914"
  notes: "Thue posed the word problem for finitely presented semigroups in 1914, after Max Dehn posed it for groups in 1911."
---

## Problem

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of finite signature with a finite [[equational basis|9Q008GMZSW]] $\Sigma$.
Let $X$ be a countably infinite set of variables, and let $F_{\mathcal{V}}(X)$ be the [[free algebra|GTS4DRRMZR]] of $\mathcal{V}$ on $X$.
The problem asks for an algorithm, that is, a [[computable function|KZSB5E471K]], with the following task.
For any two terms $s$ and $t$ over $X$, it decides whether $s$ and $t$ denote the same element of $F_{\mathcal{V}}(X)$.
Equivalently, it asks whether the [[equational theory|F1M51B4MDG]] of $\mathcal{V}$ is decidable.
That is, can one decide whether the [[identity|PKD440G2XW]] $s \approx t$ holds in every algebra of $\mathcal{V}$?

## Remarks

Since $\Sigma$ is finite, the identities of $\mathcal{V}$ are computably enumerable by listing all derivations in equational logic; the difficulty is to certify that an identity fails.
The problem is solvable for many classical varieties.
In groups, every element of a free group has a unique reduced word.
In semigroups and monoids, the free algebras are the algebras of words, so equality is literal equality of words.
In Boolean algebras, an identity holds exactly when it holds in the two-element Boolean algebra, which can be checked by truth tables.
It is unsolvable in general: Tarski showed that the equational theory of relation algebras, which form a finitely based variety, is undecidable.

## Explanations

### L1 human

Fix a list of laws, such as the group laws.
The question is whether there is a mechanical test that decides if an equation between two expressions follows from those laws.
For groups the test is to cancel $x x^{-1}$ until nothing cancels and compare the results.
For some finite lists of laws, no such test exists.

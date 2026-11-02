---
tag: 7F3QQQ63WR
kind: statement
role: theorem
name: Markov theorem
msc: [57K10, 20F36]
uses: [1A5WRCNTM3, BNR4H5GCTP, 0DEBXAJ5SA, PRWP1JF486, T3HAGWYKK7]
about: [1A5WRCNTM3, BNR4H5GCTP]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_theorem
same_as:
  wikidata: Q48971805
  wikipedia: Markov theorem
---

## Statement

For $n \ge 1$, let $B_n$ be the [[braid group|BNR4H5GCTP]] with generators $\sigma_1, \ldots, \sigma_{n-1}$.
View $B_n$ as a subgroup of $B_{n+1}$ by adding a straight strand on the right.
For a braid $\beta$, let $\hat\beta$ be its closure, an oriented [[link|1A5WRCNTM3]] in $\R^3$.
The two Markov moves on braids are:

1. Conjugation: replace $\beta \in B_n$ by $\gamma \beta \gamma^{-1}$ for some $\gamma \in B_n$, or the converse.
2. Stabilization: replace $\beta \in B_n$ by $\beta \sigma_n$ or by $\beta \sigma_n^{-1}$ in $B_{n+1}$, or the converse.

Let $\beta \in B_n$ and $\beta' \in B_m$.
Then $\hat\beta$ and $\hat\beta'$ are ambient isotopic as oriented links if and only if a finite sequence of Markov moves turns $\beta$ into $\beta'$.

## Remarks

One direction is a direct check.
Closing up $\gamma \beta \gamma^{-1}$ lets $\gamma$ slide around the closure and cancel $\gamma^{-1}$, so the closure does not change.
Closing up $\beta \sigma_n^{\pm 1}$ adds one strand with a single kink, which a first [[Reidemeister move|T3HAGWYKK7]] removes.
The hard direction follows an isotopy of closed braids step by step and shows that each step is a combination of Markov moves.
For example, $\sigma_1 \in B_2$ and the identity braid in $B_1$ both close up to the unknot, and they differ by one stabilization.
Conjugation alone does not suffice, since conjugation never changes the number of strands, while braids with different numbers of strands can close to the same link.

## Explanations

### L1 human

Many different braids close up to the same knot.
The theorem lists two simple changes, and says these are the only ones you ever need.
You may slide a piece of the braid around the closure to the other end, and you may add or remove an extra strand with one twist.

### L2 human

By [[Alexander's theorem|PRWP1JF486]], every oriented link is a closed braid.
The Markov theorem then says that oriented links up to isotopy are the same as braids in all $B_n$ up to the two Markov moves.
So a family of functions $f_n$ on $B_n$ gives a link invariant when $f_n$ is constant on [[conjugacy classes|0DEBXAJ5SA]] and $f_{n+1}(\beta \sigma_n^{\pm 1})$ equals $f_n(\beta)$.
Traces on the Temperley–Lieb and Hecke algebras with this property give the [[Jones polynomial|4SPC17FPXE]] and the [[HOMFLY polynomial|QBQ0BH589C]].

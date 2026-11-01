---
tag: WQQTFRZFBD
kind: statement
role: theorem
name: McKay conjecture
msc: [20C15, 20D20]
uses: [G5S1M9, 0053CQE9Y2, 0YGN3VAA0D, RMWMYBY8TC, FX3NEFYFFN]
about: [RMWMYBY8TC, 0053CQE9Y2]
sources:
  - url: https://en.wikipedia.org/wiki/McKay_conjecture
same_as:
  wikidata: Q28401746
  wikipedia: McKay conjecture
---

## Statement

Let $G$ be a finite [[group|G5S1M9]], let $p$ be a prime, and let $P$ be a [[Sylow $p$-subgroup|0053CQE9Y2]] of $G$ with [[normaliser|0YGN3VAA0D]] $N_G(P)$.
For a finite group $H$, let $\operatorname{Irr}_{p'}(H)$ be the set of irreducible complex [[characters|RMWMYBY8TC]] of $H$ whose degree is not divisible by $p$.
Then
$$\abs{\operatorname{Irr}_{p'}(G)} = \abs{\operatorname{Irr}_{p'}(N_G(P))}.$$

## Remarks

John McKay stated the conjecture in the early 1970s.
Isaacs, Malle and Navarro reduced it in 2007 to a stronger condition on finite simple groups, the inductive McKay condition.
Malle and Späth completed the case $p = 2$ in 2016.
Cabanes and Späth completed the proof for all primes in 2024, so the statement is now a theorem, though it keeps its name.
Example: let $G = S_3$ and $p = 3$, with $P = A_3$ normal.
Then $N_G(P) = G$, so both sides count the same set.
For $p = 2$ and $G = S_3$, take $P = \set{1, (1\,2)}$; then $N_G(P) = P$ has $2$ characters of odd degree, and $S_3$ has the characters of degrees $1, 1, 2$, so $2$ of odd degree.

## Explanations

### L1 human

The conjecture compares a finite group with a much smaller subgroup, the normaliser of a Sylow subgroup.
It says that both have the same number of irreducible characters whose degree is not a multiple of $p$.
So a global count is determined by local data near the prime $p$.

### L2 human

It is the prototype of the local-global conjectures of modular representation theory, with Alperin's weight conjecture and Dade's conjecture.
For $p$-solvable groups it was proved earlier, by Okuyama and Wajima.
The proof for all groups goes through the [[classification of finite simple groups|06J6P03MG7]] and the character theory of groups of Lie type, using [[Deligne–Lusztig theory|ZH21D5B62C]].

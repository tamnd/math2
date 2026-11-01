---
tag: 5M0HYY3RYV
kind: conjecture
name: Brauer's height zero conjecture
msc: [20C20, 20C15]
uses: [G5S1M9, 0053CQE9Y2, RMWMYBY8TC, FX3NEFYFFN, MNP2HBWB5Q]
about: [RMWMYBY8TC]
sources:
  - url: https://en.wikipedia.org/wiki/Brauer%27s_height_zero_conjecture
same_as:
  wikidata: Q131191617
  wikipedia: Brauer's height zero conjecture
history:
  posed_by: "Richard Brauer"
  first_stated: "1955"
---

## Statement

Let $G$ be a finite [[group|G5S1M9]] and let $p$ be a prime.
Let $B$ be a $p$-block of $G$, that is, a block of the [[group algebra|MNP2HBWB5Q]] of $G$ over an algebraically closed field of characteristic $p$.
Let $D$ be a defect group of $B$.
Write $\abs{G}_p = p^a$ and $\abs{D} = p^d$.
Each complex irreducible [[character|RMWMYBY8TC]] $\chi$ in $B$ has degree $\chi(1)$ with $p$-part $\chi(1)_p = p^{a - d + h}$ for an integer $h \ge 0$, the height of $\chi$.
Then every irreducible character in $B$ has height $0$ if and only if $D$ is abelian.

## Remarks

Richard Brauer posed the conjecture in 1955.
For the principal block, a defect group is a [[Sylow $p$-subgroup|0053CQE9Y2]] of $G$.
The direction "if $D$ is abelian, then all heights are zero" was proved by Kessar and Malle in 2013, using the [[classification of finite simple groups|06J6P03MG7]].
The converse direction was proved by Malle, Navarro, Schaeffer Fry and Tiep, so the conjecture is now a theorem.
For $p$-solvable groups the conjecture was proved earlier by Gluck and Wolf.

## Explanations

### L1 human

A block is a piece of the representation theory of a finite group that belongs together when one works modulo a prime $p$.
Each block has a defect group, a $p$-subgroup that measures how complicated the block is.
The conjecture says that a simple numerical pattern in the character degrees of the block, all heights being zero, happens exactly when the defect group is commutative.
So local information, a small subgroup, is read off from global information, the character degrees.

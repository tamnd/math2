---
tag: QYXGVES1XM
kind: statement
role: theorem
name: Tits alternative
msc: ["20E05", 20G15, 20H20]
uses: [04C5ZBG1WT, 0FCHE902D7, 082DWWXMRJ, 0X1JXT47GA, 0KTW26C80J, 0FXJ7YFMMX, 0DTXBQPA2S]
about: [0FCHE902D7, 0KTW26C80J, 0FXJ7YFMMX]
sources:
  - url: https://en.wikipedia.org/wiki/Tits_alternative
same_as:
  wikidata: Q3613173
  wikipedia: Tits alternative
---

## Statement

Let $F$ be a [[field|04C5ZBG1WT]], let $n \ge 1$, and let $G$ be a [[finitely generated|082DWWXMRJ]] [[subgroup|0X1JXT47GA]] of the [[general linear group|0FCHE902D7]] $\mathrm{GL}_n(F)$.
Then exactly one of the following holds:

1. $G$ contains a non-abelian [[free group|0KTW26C80J]].
2. $G$ is virtually [[solvable|0FXJ7YFMMX]]: it has a solvable subgroup of finite [[index|0DTXBQPA2S]].

If $F$ has characteristic $0$, the same conclusion holds for every subgroup $G$ of $\mathrm{GL}_n(F)$, finitely generated or not.

## Remarks

The two cases exclude each other, because subgroups of virtually solvable groups are virtually solvable and a non-abelian free group is not.
Suppose $G$ is not virtually solvable.
Tits embeds the relevant field into a suitable local field and finds two elements of $G$ that act on projective space with attracting and repelling points in general position.
High powers of these elements then satisfy the ping-pong lemma, and so generate a free group of rank $2$.

Example: $\mathrm{SL}_2(\Z)$ is not virtually solvable, and indeed the matrices $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}$ generate a free group of rank $2$.
Example: the group of upper triangular invertible matrices is solvable, so it has no non-abelian free subgroup.

In positive characteristic, finite generation is needed.
Let $\bar{\F}_p$ be an algebraic closure of $\F_p$.
Every finitely generated subgroup of $\mathrm{GL}_2(\bar{\F}_p)$ is finite, so $\mathrm{GL}_2(\bar{\F}_p)$ has no free subgroup of rank $2$.
But it is not virtually solvable, since it has the infinite simple group $\mathrm{PSL}_2(\bar{\F}_p)$ as a quotient of a subgroup.

## Explanations

### L1 human

A group of invertible matrices is either tame or wild.
Tame means that, after passing to a finite-index piece, it is built from commutative layers.
Wild means it contains two matrices that satisfy no relation at all, like the generators of a free group.
The theorem says there is nothing in between for finitely generated matrix groups.

### L2 human

The theorem gives strong consequences for linear groups.
A finitely generated linear group is [[amenable|CEAT9BESKK]] if and only if it is virtually solvable, since groups with free subgroups are not amenable.
Combined with the Milnor–Wolf theorem on finitely generated solvable groups, it shows that the [[growth|4CMRM3975W]] of a finitely generated linear group is either polynomial or exponential.
Groups outside linear groups are said to satisfy the Tits alternative when the same dichotomy holds for their subgroups; examples include [[hyperbolic groups|JWJ8YPR7EB]] and [[Out(F_n)|7Z5ZS7KNXS]].

---
tag: FSXA3CF365
kind: statement
role: theorem
name: Krull–Akizuki theorem
msc: ["13E05", "13B22", "13F05"]
uses: [0MVH4Y1CRZ, 09S3PFBEPM, 0VF11ZTTMD, MVGBS3J1P7, CZSCNZH8VY]
about: [0670T59HGE, MVGBS3J1P7]
sources:
  - url: https://en.wikipedia.org/wiki/Krull–Akizuki_theorem
same_as:
  wikidata: Q6439289
  wikipedia: Krull–Akizuki theorem
---

## Statement

Let $A$ be a [[Noetherian|0MVH4Y1CRZ]] [[integral domain|09S3PFBEPM]] of [[Krull dimension|MVGBS3J1P7]] $1$.
Let $K$ be the [[field of fractions|0VF11ZTTMD]] of $A$ and let $L$ be a finite field extension of $K$.
Let $B$ be a ring with $A \subseteq B \subseteq L$.
Then $B$ is Noetherian and has Krull dimension at most $1$.
Moreover, for every nonzero ideal $J$ of $B$, the quotient $B/J$ has finite [[length|CZSCNZH8VY]] as an $A$-module.

## Remarks

The general case reduces to the case $L = K$.
There the key step is the bound $\ell_A(B/aB) \le \ell_A(A/aA)$ for each nonzero $a \in A$, where $\ell_A$ is the length; the right side is finite because $A$ has dimension $1$.
Each nonzero ideal $J$ of $B$ contains a nonzero element $a$ of $A$, so $J/aB$ has finite length, and $J$ is finitely generated.
A main application: the [[integral closure|G0V86SJBQW]] of $A$ in $L$ is a Noetherian integrally closed domain of dimension at most $1$, that is, a Dedekind domain or a field.
For example, with $A = \Z$ and $L$ a number field, this shows that the ring of integers of $L$ is Noetherian.
The ring $B$ need not be a finitely generated $A$-module, so the result is not a consequence of [[Hilbert's basis theorem|0YKA9J3XEE]].

## Explanations

### L1 human

Start with a nice ring of dimension one, such as the integers.
Take any ring that sits between it and a finite extension of its fraction field.
The theorem says that this new ring is still Noetherian and still has dimension at most one.
So rings of integers in number fields keep the finiteness of $\Z$.

### L2 human

The theorem is the standard route to the following fact.
The integral closure of a one-dimensional Noetherian domain in a finite extension of its fraction field is a Dedekind domain, even when it is not a finite module.
It is special to dimension $1$: for any Noetherian domain, the [[Mori–Nagata theorem|J8YYYP5CDN]] only gives a Krull domain, and the integral closure can fail to be Noetherian.
The proof uses [[lengths of modules|CZSCNZH8VY]] and the fact that $A/aA$ is Artinian for $a \ne 0$.

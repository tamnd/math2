---
tag: 21BZEVVT7G
kind: definition
name: Elementary substructure
msc: [03C07]
defines: 8WZF9SBP39
uses: [676H7EGTKJ, 983GZBQYT4, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
---

## Definition

Let $L$ be a signature and let $\mathcal{M}$ and $\mathcal{N}$ be $L$-[[structures|983GZBQYT4]] with domains $M$ and $N$.
The structure $\mathcal{M}$ is an elementary substructure of $\mathcal{N}$, written $\mathcal{M} \preceq \mathcal{N}$, when the following hold.

1. $\mathcal{M}$ is a [[substructure|676H7EGTKJ]] of $\mathcal{N}$.
2. For every $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$ and all $a_1, \dots, a_n \in M$, $\mathcal{M} \models \varphi(a_1, \dots, a_n)$ if and only if $\mathcal{N} \models \varphi(a_1, \dots, a_n)$.

Then $\mathcal{N}$ is an elementary extension of $\mathcal{M}$.

## Remarks

Example: $(\Q, <) \preceq (\R, <)$.
It follows from quantifier elimination for dense linear orders without endpoints: each formula is equivalent in these orders to a quantifier-free one.
A quantifier-free formula has the same truth value in a structure and in its substructures.

Non-example: let $P = \set{1, 2, 3, \dots}$.
Then $(P, <)$ is a substructure of $(\N, <)$, but not an elementary one.
For $\varphi(x) = \exists y \, (y < x)$, $(P, <) \models \neg \varphi(1)$ and $(\N, <) \models \varphi(1)$.

Taking $n = 0$ in clause 2 shows that $\mathcal{M} \preceq \mathcal{N}$ implies $\mathcal{M} \equiv \mathcal{N}$.
The non-example shows that the converse fails, since $(P, <)$ and $(\N, <)$ are isomorphic.
The [[Tarski–Vaught test|60SA99BER7]] gives a practical criterion.

## Explanations

### L1 human

In an elementary substructure, every statement about some of its elements is true there exactly when it is true in the bigger structure.
This is stronger than having the same sentences, because the statements may mention elements.

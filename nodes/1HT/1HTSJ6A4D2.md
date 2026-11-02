---
tag: 1HTSJ6A4D2
kind: statement
role: theorem
name: Evans's theorem on word problems
msc: [08A50, 08A55, 03D40]
uses: [7ZKBV18BFG, 43M1WFPYGQ, AJNZJD8442, H7RX5729ZB]
about: [7ZKBV18BFG]
sources:
  - url: https://en.wikipedia.org/wiki/Word_problem_(mathematics)
    locator: The word problem in universal algebra
---

## Statement

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of finite signature.
A finite [[partial algebra|H7RX5729ZB]] $P$ of the same signature *embeds in* $\mathcal{V}$ if there are $B \in \mathcal{V}$ and an injective map $e \colon P \to B$ with the following property.
Whenever $f(p_1, \ldots, p_n)$ is defined in $P$, one has $e(f(p_1, \ldots, p_n)) = f(e(p_1), \ldots, e(p_n))$ in $B$.
Then the following are equivalent:

1. The uniform [[word problem|7ZKBV18BFG]] for finitely presented algebras of $\mathcal{V}$ is solvable.
2. There is an algorithm that decides, for any finite partial algebra $P$ of the signature, whether $P$ embeds in $\mathcal{V}$.

## Remarks

From 1 to 2: take the [[presentation|43M1WFPYGQ]] whose generators are the elements of $P$ and whose relations are the entries of the partial operation tables.
Then $P$ embeds in $\mathcal{V}$ exactly when distinct elements of $P$ stay distinct in the presented algebra.
From 2 to 1: given relations $R$ and terms $s, t$, let $S$ be the finite set of subterms of $s$, $t$ and the terms in $R$.
Then $s \ne t$ in $\langle X \mid R \rangle_{\mathcal{V}}$ exactly when some quotient of $S$, as a partial algebra, satisfies $R$, separates $s$ and $t$, and embeds in $\mathcal{V}$.
There are finitely many quotients to test.
A useful sufficient condition: if $\mathcal{V}$ is finitely based and every finite partial algebra that embeds in $\mathcal{V}$ embeds in a finite algebra of $\mathcal{V}$, then condition 2 holds.
Indeed, one can search at the same time for two things.
One is a finite algebra of $\mathcal{V}$ in which $P$ embeds.
The other is an equational derivation that identifies two distinct elements of $P$ in the presented algebra.
Example: Boolean algebras are finitely based.
A finite partial Boolean algebra that embeds in some Boolean algebra embeds in the finite subalgebra it generates.
So finitely presented Boolean algebras have solvable word problem.

## Explanations

### L1 human

The word problem asks whether two expressions are equal in an algebra given by generators and relations.
The theorem says that this is the same question as deciding whether a small finite table of partial operations can be completed inside some algebra of the variety.
So word problems can be attacked by thinking about finite pieces of algebras.

### L2 human

The theorem, due to Trevor Evans, connects the word problem with embeddings of partial algebras.
Combined with the finite embeddability property, it explains why finitely based varieties such as Boolean algebras have solvable word problems.
It also explains why unsolvability results for semigroups and groups are hard: one must build finite partial algebras whose embeddability encodes a halting problem.

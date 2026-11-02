---
tag: SKTMN14X5P
kind: statement
role: theorem
name: Lefschetz principle
msc: [03C60, 12L12]
uses: [MT8TDVPBXB, 0PF6TM8TWT, 1ZB13N78XW, DKFGQTRYZE, 1NR3HAWG9D, 09FTAET5Z4]
about: [MT8TDVPBXB]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraically_closed_field
---

## Statement

Let $\varphi$ be a first-order [[sentence|DKFGQTRYZE]] in the signature of rings $\set{+, -, \cdot, 0, 1}$.
The following are equivalent:

1. $\varphi$ holds in the field $\C$ of [[complex numbers|09FTAET5Z4]].
2. $\varphi$ holds in every [[algebraically closed field|0PF6TM8TWT]] of [[characteristic|1ZB13N78XW]] $0$.
3. $\varphi$ holds in some algebraically closed field of characteristic $0$.
4. There is an integer $m$ such that $\varphi$ holds in every algebraically closed field of characteristic $p$, for every prime $p > m$.
5. $\varphi$ holds in algebraically closed fields of characteristic $p$ for infinitely many primes $p$.

## Remarks

Clauses 1, 2 and 3 are equivalent because the theory $\mathrm{ACF}_0$ of [[algebraically closed fields|MT8TDVPBXB]] of characteristic $0$ is complete.
Suppose $\varphi$ holds in $\mathrm{ACF}_0$.
By the [[compactness theorem|1NR3HAWG9D]], $\varphi$ follows from $\mathrm{ACF}$ and finitely many of the axioms $1 + \cdots + 1 \ne 0$.
So it holds in characteristic $p$ for all large $p$, which is clause 4.
Clause 4 gives 5, since there are infinitely many primes.
If $\varphi$ fails in $\mathrm{ACF}_0$, then $\neg \varphi$ holds there, so $\neg \varphi$ holds in all large characteristics and 5 fails.

Example: fix $n$ and $d$.
The statement "every injective polynomial map $K^n \to K^n$ whose components have degree at most $d$ is surjective" is a first-order sentence about the field $K$.
It holds in the algebraic closure of each finite field $\F_p$, so by clause 5 it holds in $\C$.
This is the model-theoretic proof of the Ax–Grothendieck theorem.

The principle holds only for first-order sentences.
The statement "every element is algebraic over the prime field" holds in the algebraic closure of each $\F_p$ but fails in $\C$.
It is not expressible by a single first-order sentence.

## Explanations

### L1 human

Algebraically closed fields of the same characteristic cannot be told apart by first-order statements in the language of rings.
So a statement of this kind about the complex numbers is true exactly when it is true in every algebraically closed field of characteristic $0$.
It is also true exactly when it holds in algebraically closed fields of all large prime characteristics.

### L2 human

The principle lets one prove algebraic facts about $\C$ by working over finite fields, where counting arguments are available, or the other way around.
It comes from the completeness of $\mathrm{ACF}_p$ for each $p$, which itself follows from quantifier elimination or from uncountable categoricity and the Łoś–Vaught test.
Take the algebraic closures of the fields $\F_p$ and a non-principal ultrafilter on the primes.
Their ultraproduct is an algebraically closed field of characteristic $0$, which gives another view of clause 4.

---
tag: 13JZKN6WKC
kind: definition
name: Proof complexity
msc: ["03F20", "68Q17"]
defines: 1Q046J0AW2
uses: [N4EDJNMTEF, 09K9MWD2QQ, 0D1AHYPM8N, 0XHDTE5YMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
---

## Definition

Let $\Sigma$ be a finite alphabet, and let $\mathrm{TAUT} \subseteq \Sigma^*$ be the set of [[tautologies|0D1AHYPM8N]] of [[propositional logic|09K9MWD2QQ]], coded as strings.
A *propositional proof system*, in the sense of Cook and Reckhow, is a [[function|0XHDTE5YMZ]] $P \colon \Sigma^* \to \Sigma^*$ such that:

1. $P$ is computable in time polynomial in the length of its input;
2. the image of $P$ is exactly $\mathrm{TAUT}$.

A string $w$ with $P(w) = \varphi$ is a *$P$-proof* of $\varphi$.
The system $P$ is *polynomially bounded* if there is a polynomial $p$ such that every $\varphi \in \mathrm{TAUT}$ has a $P$-proof of length at most $p(\abs{\varphi})$.
*Proof complexity* is the study of the lengths of proofs in such systems, and of the relations between systems.

## Remarks

Example: the truth table system is a proof system.
Let $P$ send a string made of a formula $\varphi$ and its full truth table, with all rows true, to $\varphi$.
Let $P$ send every other string to the fixed tautology $p \vee \neg p$.
The check takes time polynomial in the length of the input, and the image of $P$ is $\mathrm{TAUT}$.
This system is not polynomially bounded, because the table of a formula with $n$ variables has $2^n$ rows.
Non-example: the map that sends each string to itself is not a proof system, because its image is all of $\Sigma^*$, not $\mathrm{TAUT}$.
Cook and Reckhow proved that a polynomially bounded proof system exists if and only if $\mathrm{NP} = \mathrm{coNP}$.
Haken proved in 1985 that resolution is not polynomially bounded, using the pigeonhole principle.
For stronger systems such as Frege systems, no superpolynomial lower bound is known.

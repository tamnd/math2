---
tag: GYMRH1GC71
kind: definition
name: L-system
msc: [68Q42, 92C80, 92C15]
defines: QV27JTGWQ0
uses: [RABRP2KG81, 1P6EP01HZF, CV013KHVJG, 0GA9K57A39]
sources:
  - url: https://en.wikipedia.org/wiki/L-system
---

## Definition

Let $V$ be a finite [[alphabet|RABRP2KG81]], and let $V^*$ be the set of [[strings|1P6EP01HZF]] over $V$.
A *context-free L-system* (or 0L-system) is a triple $G = (V, \omega, P)$ such that:

1. $\omega \in V^*$ is a nonempty string, the *axiom*;
2. $P \subseteq V \times V^*$ is a finite set of *productions*, written $a \to u$;
3. each letter $a \in V$ has at least one production $a \to u$ in $P$.

A string $y$ is *derived in one step* from $x = a_1 a_2 \cdots a_m$ if $y = u_1 u_2 \cdots u_m$ with $a_k \to u_k$ in $P$ for every $k$.
The system is *deterministic* (a D0L-system) if each letter has exactly one production; then the derivation is a sequence $\omega = w_0, w_1, w_2, \dots$ with $w_{k+1}$ derived from $w_k$.

## Remarks

A D0L-system is the same as a monoid endomorphism $h$ of the [[free monoid|CV013KHVJG]] $V^*$ together with a starting word, and $w_k = h^k(\omega)$.
Example: $V = \set{A, B}$, $\omega = A$, $P = \set{A \to AB,\ B \to A}$ is a D0L-system; its words are $A, AB, ABA, ABAAB, \dots$, and their lengths $\ell_k$ satisfy $\ell_{k+2} = \ell_{k+1} + \ell_k$, because $w_{k+2} = w_{k+1} w_k$; so they are [[Fibonacci numbers|0GA9K57A39]].
Non-example: if $P = \set{A \to AB}$ over $V = \set{A, B}$, clause 3 fails, since $B$ has no production.
The difference with a Chomsky grammar is that all letters are rewritten in each step, and there is no separate set of terminal symbols.
Context-sensitive and stochastic L-systems are common extensions used in plant modelling.

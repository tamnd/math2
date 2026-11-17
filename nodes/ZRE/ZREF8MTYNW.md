---
tag: ZREF8MTYNW
kind: definition
name: Dialectica interpretation
msc: ["03F10", "03F25", "03F50"]
defines: HZ17ES9PDY
topics: [8XY7JYZKFW]
audience: grad
uses: [RXHJPVMPJH, CK8ZQRN183, 5NVA2JRHPV, HGJVM49PA4, S9DK13K5PS, ~62fef358]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Formula translation
---

## Definition

Let $\mathrm{T}$ be [[Gödel's system T|~62fef358]] of [[primitive recursive|5NVA2JRHPV]] functionals of finite type.
To each formula $A$ of [[Heyting arithmetic|RXHJPVMPJH]], the *Dialectica interpretation* assigns a formula $A^D = \exists x\, \forall y\, A_D(x, y)$.
Here $x$ and $y$ are finite tuples of variables of finite type, and $A_D$ is quantifier-free.
Write $A^D = \exists x\, \forall y\, A_D(x, y)$ and $B^D = \exists u\, \forall v\, B_D(u, v)$.
The clauses are these.

1. If $A$ is atomic, then $A^D = A_D = A$, with empty tuples $x$ and $y$.
2. $(A \wedge B)^D = \exists x, u\, \forall y, v\, \bigl( A_D(x, y) \wedge B_D(u, v) \bigr)$.
3. $(A \vee B)^D = \exists z, x, u\, \forall y, v\, \bigl( (z = 0 \to A_D(x, y)) \wedge (z \ne 0 \to B_D(u, v)) \bigr)$, where $z$ is a number variable.
4. $(A \to B)^D = \exists f, g\, \forall x, v\, \bigl( A_D(x, f x v) \to B_D(g x, v) \bigr)$.
5. $(\exists z\, A(z))^D = \exists z, x\, \forall y\, A_D(x, y, z)$.
6. $(\forall z\, A(z))^D = \exists f\, \forall z, y\, A_D(f z, y, z)$.

Negation $\neg A$ is read as $A \to (0 = 1)$.

## Notation

The tuple $x$ is the witness and the tuple $y$ the counterexample, or challenge.
In clause 4, $f$ maps a witness of $A$ and a challenge of $B$ to a challenge of $A$, and $g$ maps a witness of $A$ to a witness of $B$.
We write $f x v$ for the application $(f\, x)\, v$, as in [[system T|~62fef358]].
In examples we treat $n < m$ as an atomic formula, as in HA with symbols for all primitive recursive functions and relations.

## Remarks

The [[soundness theorem|~9cb2c479]] (Gödel): if Heyting arithmetic proves a closed formula $A$, then there is a tuple $t$ of closed terms of $\mathrm{T}$ such that $\mathrm{T}$ proves $A_D(t, y)$.
Example: for $A = \forall n\, \exists m\, (n < m)$, clauses 5 and 6 give $A^D = \exists f\, \forall n\, (n < f n)$, and the term $f = \lambda n.\, n + 1$ is a witness.
Non-example: let $P(n, k)$ be the primitive recursive relation, given by [[Kleene's T predicate|S9DK13K5PS]], which says that the program $n$ on input $n$ halts within $k$ steps.
The formula $\forall n\, (\exists k\, P(n, k) \vee \neg \exists k\, P(n, k))$ has no witness in $\mathrm{T}$.
A witness would give a computable function $n \mapsto z$ that decides the halting problem.
Combined with a [[double-negation translation|HGJVM49PA4]], it interprets Peano arithmetic in system $\mathrm{T}$.

## Explanations

### L1 human

The interpretation turns each statement into a game with one move for each player.
The first player picks a witness $x$, the second picks a challenge $y$, and a simple check $A_D(x, y)$ decides the winner.
For "every number $n$ has a larger number $m$", the first player picks a rule $f$, the second picks $n$, and the check is $n < f(n)$.
The rule $f(n) = n + 1$ always wins, and it is the computational content of the statement.

### L2 human

We compute the interpretation of $A = \exists m\, (m \cdot m = 9) \wedge \forall n\, (\neg (S\, n = 0))$.

1. By clause 5, $(\exists m\, (m \cdot m = 9))^D = \exists m\, (m \cdot m = 9)$, with witness $m$ and no challenge.
2. By clauses 1, 4 and 6, $(\forall n\, (\neg (S\, n = 0)))^D = \forall n\, (\neg (S\, n = 0))$, with no witness and challenge $n$.
3. By clause 2, $A^D = \exists m\, \forall n\, (m \cdot m = 9 \wedge \neg (S\, n = 0))$.
4. The witness $m = 3$ works, since $3 \cdot 3 = 9$, and $S\, n = 0$ is false for every $n$.

The typical use is to compute the type of the witness before a proof is interpreted.
A trap is clause 4: the challenge $f x v$ for the premise depends on the challenge $v$ of the conclusion.

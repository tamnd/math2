---
tag: ZREF8MTYNW
kind: definition
name: Dialectica interpretation
msc: ["03F10", "03F25", "03F50"]
defines: HZ17ES9PDY
uses: [RXHJPVMPJH, CK8ZQRN183, 5NVA2JRHPV, HGJVM49PA4, S9DK13K5PS]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
---

## Definition

Let $\mathrm{T}$ be Gödel's system of [[primitive recursive|5NVA2JRHPV]] functionals of finite type.
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

## Remarks

Soundness theorem (Gödel): if Heyting arithmetic proves a closed formula $A$, then there is a tuple $t$ of closed terms of $\mathrm{T}$ such that $\mathrm{T}$ proves $A_D(t, y)$.
Example: for $A = \forall n\, \exists m\, (n < m)$, clauses 5 and 6 give $A^D = \exists f\, \forall n\, (n < f n)$, and the term $f = \lambda n.\, n + 1$ is a witness.
Non-example: let $P(n, k)$ be the primitive recursive relation, given by [[Kleene's T predicate|S9DK13K5PS]], which says that the program $n$ on input $n$ halts within $k$ steps.
The formula $\forall n\, (\exists k\, P(n, k) \vee \neg \exists k\, P(n, k))$ has no witness in $\mathrm{T}$.
A witness would give a computable function $n \mapsto z$ that decides the halting problem.
Combined with a [[double-negation translation|HGJVM49PA4]], it interprets Peano arithmetic in system $\mathrm{T}$.

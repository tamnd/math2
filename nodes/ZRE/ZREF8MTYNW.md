---
tag: ZREF8MTYNW
kind: definition
name: Dialectica interpretation
msc: ["03F10", "03F25", "03F50"]
defines: HZ17ES9PDY
topics: [8XY7JYZKFW]
audience: grad
uses: [RXHJPVMPJH, CK8ZQRN183, 5NVA2JRHPV, HGJVM49PA4, S9DK13K5PS, A4WR995XZP]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Formula translation
---

## Definition

The Dialectica interpretation rewrites each formula of arithmetic as one block of existential quantifiers, then one block of universal quantifiers, then a quantifier-free formula.

Let $\mathrm{T}$ be [[Gödel's system T|A4WR995XZP]] of [[primitive recursive|5NVA2JRHPV]] functionals of finite type.
To each formula $A$ of [[Heyting arithmetic|RXHJPVMPJH]] the *Dialectica interpretation* assigns a formula $A^D = \exists x\, \forall y\, A_D(x, y)$.
Here $x$ and $y$ are finite tuples of variables of finite type, and $A_D$ is a quantifier-free formula of $\mathrm{T}$.
The assignment is defined by induction on $A$.
Assume $A^D = \exists x\, \forall y\, A_D(x, y)$ and $B^D = \exists u\, \forall v\, B_D(u, v)$.

1. If $A$ is atomic, then $A^D = A_D = A$, with empty tuples $x$ and $y$.
2. $(A \wedge B)^D = \exists x, u\, \forall y, v\, \bigl( A_D(x, y) \wedge B_D(u, v) \bigr)$.
3. $(A \vee B)^D = \exists z, x, u\, \forall y, v\, \bigl( (z = 0 \to A_D(x, y)) \wedge (z \ne 0 \to B_D(u, v)) \bigr)$, where $z$ has type $\mathbb{N}$.
4. $(A \to B)^D = \exists U, Y\, \forall x, v\, \bigl( A_D(x, Y x v) \to B_D(U x, v) \bigr)$.
5. $(\exists z\, A(z))^D = \exists z, x\, \forall y\, A_D(x, y, z)$.
6. $(\forall z\, A(z))^D = \exists f\, \forall z, y\, A_D(f z, y, z)$.

Negation $\neg A$ is read as $A \to 0 = 1$.

## Notation

The tuple $x$ is the *witness* and the tuple $y$ is the *challenge*, or counterexample.
In clause 4, $U$ maps a witness of $A$ to a witness of $B$, and $Y$ maps a witness of $A$ and a challenge of $B$ to a challenge of $A$.
We write $Y x v$ for the application $(Y\, x)\, v$, as in [[system T|A4WR995XZP]], and $\mathbb{N}$ for the type of numbers, which many books call type $0$.
In examples we treat relations such as $n < m$ as atomic, as in a version of HA with symbols for all primitive recursive functions and relations.

## Remarks

Each clause has a reason.
Clause 1 says that a decidable fact needs no witness and allows no challenge.
Clause 2 puts the two games side by side.
Clause 3 adds a number $z$ that says which side of the disjunction holds, so a witness of $A \vee B$ must decide between $A$ and $B$.
Clause 5 adds the number $z$ to the witness, and clause 6 makes the witness a function of $z$, which is the Skolem step.
Clause 4 is the heart: witnesses of the premise go forward to the conclusion, and challenges of the conclusion go back to the premise.

A small example: for $A = \forall n\, \exists m\, (n < m)$, clauses 5 and 6 give $A^D = \exists f\, \forall n\, (n < f n)$, and $f = \lambda n.\, n + 1$ is a witness.
Notice what the shape allows: $f n$ may depend on $n$, which comes before it, but not on a challenge that would come after it.

A case that fails is excluded middle for halting.
Let $P(n, k)$ be the primitive recursive relation, given by [[Kleene's T predicate|S9DK13K5PS]], that says that program $n$ on input $n$ halts within $k$ steps.
By clauses 3 and 6, a witness of $\forall n\, (\exists k\, P(n, k) \vee \neg \exists k\, P(n, k))$ contains a function $n \mapsto z$ that says which side holds, and such a function would decide the halting problem.
So the interpretation is sound for HA but not for PA, and classical proofs first go through a [[double-negation translation|HGJVM49PA4]].
The [[soundness theorem|6QFRG42QQR]] and the uses of the [[Dialectica interpretation|HZ17ES9PDY]] build on these clauses.

## Explanations

### L1 human

The interpretation turns each statement into a game with one move for each player.
The first player picks a witness $x$, the second picks a challenge $y$, and a simple check $A_D(x, y)$ decides the winner.
For "every number $n$ has a larger number $m$", the first player picks a rule $f$, the second picks $n$, and the check is $n < f(n)$.
The rule $f(n) = n + 1$ always wins, and it is the computational content of the statement.

### L2 human

We compute the interpretation of $A = \exists m\, (m \cdot m = 9) \wedge \forall n\, \neg (S\, n = 0)$.
By clause 5, the left part is its own interpretation, with witness $m$ and no challenge.
The formula $\neg (S\, n = 0)$ is $S\, n = 0 \to 0 = 1$, which is quantifier-free, so clause 6 gives $\forall n\, \neg (S\, n = 0)$, with an empty witness and challenge $n$.
Clause 2 then puts them together:
$$A^D = \exists m\, \forall n\, \bigl( m \cdot m = 9 \wedge \neg (S\, n = 0) \bigr).$$
The witness $m = 3$ works, since $3 \cdot 3 = 9$ and $S\, n = 0$ is false for every $n$.

The typical use is to compute the types of the witness and the challenge before a proof is interpreted.
Watch out for clause 4: the challenge $Y x v$ sent to the premise depends on the challenge $v$ of the conclusion, but the witness $U x$ does not.

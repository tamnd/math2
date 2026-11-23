---
tag: 0P3A06QNDP
kind: statement
role: theorem
name: Negation of a universal statement
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
about: [0GHS47PDAQ, 0MSRQHCNN9, 029JBBF693]
uses: [0B88PQTJ66, 0JW2FHW7G3, 0XR7A7RSXB, 0T3DPBG981, 0JMR2HM2N2]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/De_Morgan%27s_laws
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.2
history:
  notes: "Aristotle treated 'every A is B' and 'some A is not B' as contradictory statements. Frege's Begriffsschrift (1879) had only the universal quantifier and expressed 'some' as 'not all not'."
---

## Statement

"Not every number from $1$ to $5$ is odd" says the same as "some number from $1$ to $5$ is not odd", and both are true because of $2$.
In general, let $D$ be a domain of discourse and let $P(x)$ be a [[predicate|0T3DPBG981]] on $D$.
In classical logic,
$$\neg \forall x \, P(x) \;\equiv\; \exists x \, \neg P(x).$$
Here $\forall$ is the [[universal quantifier|0B88PQTJ66]], $\exists$ is the [[existential quantifier|0JW2FHW7G3]], $\neg$ is [[negation|0XR7A7RSXB]], and $\equiv$ is [[logical equivalence|0JMR2HM2N2]].
The two directions have a different status.

1. The direction $\exists x \, \neg P(x) \to \neg \forall x \, P(x)$ holds in classical and in [[intuitionistic logic|Q11N8X99FK]].
2. The direction $\neg \forall x \, P(x) \to \exists x \, \neg P(x)$ holds in classical logic, and its proof uses the [[law of excluded middle|0RYYK8PG4S]].
   It is not valid in intuitionistic logic.

The same holds for the restricted form: $\neg \forall x \in A \; P(x) \equiv \exists x \in A \; \neg P(x)$.
In Mathlib, the classical equivalence is `Classical.not_forall`, which states `(¬ ∀ x, P x) ↔ ∃ x, ¬ P x`.
The proof is in [[proof of the negation of a universal statement|DTM9GQV88K]].

## Remarks

### A check on a small domain

Let $D = \{1, 2, 3\}$ and let $P(x)$ be "$x$ is odd".
Then $\forall x \, P(x)$ is $P(1) \land P(2) \land P(3)$, which is false because $P(2)$ is false.
So $\neg \forall x \, P(x)$ is true.
The formula $\exists x \, \neg P(x)$ is $\neg P(1) \lor \neg P(2) \lor \neg P(3)$, which is true because $\neg P(2)$ is true.
On a finite domain the statement is the [[De Morgan law|09PKJKA6J0]] $\neg (P(a_1) \land \cdots \land P(a_n)) \equiv \neg P(a_1) \lor \cdots \lor \neg P(a_n)$.

### Why classical logic is needed

Classical logic is the only hypothesis beyond the definitions, and only direction 2 needs it.
Take a Kripke model of intuitionistic logic with worlds $w_0 \leq w_1 \leq w_2 \leq \cdots$, domain $\mathbb{N}$ at every world, and $P(k)$ forced at $w_n$ exactly when $k < n$.
At $w_n$ the instance $P(n)$ is not forced, so no world forces $\forall x \, P(x)$, and $\neg \forall x \, P(x)$ is forced at $w_0$.
Each $P(k)$ is forced at $w_{k + 1}$, so no $\neg P(k)$ is forced at $w_0$, and $\exists x \, \neg P(x)$ is not forced at $w_0$.
The statement needs no nonempty domain.
For $D = \varnothing$, the formula $\forall x \, P(x)$ is true by [[vacuous truth|0V4QXPGJQK]], so both sides are false.

### Consequences

One [[counterexample|0ED72CTBNP]] refutes a universal statement, and this uses only direction 1.
Combined with the [[negation of an existential statement|05SZQKH75K]], the statement negates any string of quantifiers: each $\forall$ becomes $\exists$, each $\exists$ becomes $\forall$, and $\neg$ moves to the predicate.
For example, $\neg \forall x \, \exists y \, P(x, y) \equiv \exists x \, \forall y \, \neg P(x, y)$.
In classical logic, $\forall x \, P(x) \equiv \neg \exists x \, \neg P(x)$, so either quantifier can be defined from the other.
The negation of a restricted statement keeps the restriction: $\neg \forall \varepsilon > 0 \; Q(\varepsilon) \equiv \exists \varepsilon > 0 \; \neg Q(\varepsilon)$.
The practice in mathematical English is in [[negating mathematical statements|K930V33BSC]].

### Converse and generalizations

The statement is an equivalence, so the question of a converse becomes the question of which direction holds without excluded middle, and the answer is direction 1.
In set language, the [[complement|0RKF1ZT5JJ]] of the truth set of $P$ is nonempty exactly when the truth set is not all of $D$.
In a complete [[Boolean algebra|0XADJKM699]], the complement of the meet of a family equals the join of the complements.

## History

Aristotle treated "every $A$ is $B$" and "some $A$ is not $B$" as contradictory statements, so that exactly one of them is true.
Gottlob Frege's Begriffsschrift of 1879 had only the universal quantifier, and it expressed "some $x$ has $P$" as "not every $x$ has not $P$".
The Dutch mathematician Luitzen Brouwer rejected the general law of excluded middle, and with it direction 2 of this statement.

## Explanations

### L1 human

"Not every student passed the test" means "some student did not pass".
To deny that all members of a group have a property, it is enough to find one member without it.
For example, "every number from $1$ to $5$ is odd" is false, because $2$ is even.
So "not every number from $1$ to $5$ is odd" is true, and so is "some number from $1$ to $5$ is not odd".

### L2 human

Negate "every function $f \colon \mathbb{R} \to \mathbb{R}$ with $f(0) = 0$ satisfies $f(1) = 0$", and decide which version is true.
In symbols the statement is $\forall f \; (f(0) = 0 \to f(1) = 0)$, with $f$ ranging over functions $\mathbb{R} \to \mathbb{R}$.
By the theorem, the negation is $\exists f \; \neg (f(0) = 0 \to f(1) = 0)$.
The negation of $p \to q$ is $p \land \neg q$, so the negation becomes $\exists f \; (f(0) = 0 \land f(1) \neq 0)$.
The function $f(x) = x$ has $f(0) = 0$ and $f(1) = 1 \neq 0$, so the negation is true and the original statement is false.
Pushing $\neg$ through the quantifier in this way tells you what a counterexample must satisfy.
Watch out: the negation of "every $x$ has $P$" is not "every $x$ lacks $P$", and for the numbers $1$ to $5$ with $P$ meaning "odd" the second is false while the correct negation is true.

### L3 human

Classical logic treats $\forall$ and $\exists$ as duals, the infinite forms of $\land$ and $\lor$, and the theorem is the infinite De Morgan law.
Intuitionistic logic keeps only one direction, because a proof of $\neg \forall x \, P(x)$ shows that the universal claim is absurd but does not produce a specific $a$ with $\neg P(a)$.
In a [[Heyting algebra|NG943XNQWH]], $\neg \bigwedge_i a_i \geq \bigvee_i \neg a_i$ always holds, and equality can fail.
In proof assistants, a proof that uses `Classical.not_forall` is non-constructive, and the witness that it produces cannot in general be computed.

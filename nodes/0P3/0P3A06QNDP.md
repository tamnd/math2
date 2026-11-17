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

Let $D$ be a domain of discourse and let $P(x)$ be a [[predicate|0T3DPBG981]] on $D$.
In classical logic,
$$\neg \forall x \, P(x) \;\equiv\; \exists x \, \neg P(x).$$
Here $\forall$ is the [[universal quantifier|0B88PQTJ66]], $\exists$ is the [[existential quantifier|0JW2FHW7G3]], $\neg$ is [[negation|0XR7A7RSXB]], and $\equiv$ is [[logical equivalence|0JMR2HM2N2]].
In words: "not every $x$ has property $P$" holds exactly when "some $x$ does not have property $P$" holds.
The two directions have a different status.

1. The direction $\exists x \, \neg P(x) \to \neg \forall x \, P(x)$ holds in classical and in [[intuitionistic logic|Q11N8X99FK]].
2. The direction $\neg \forall x \, P(x) \to \exists x \, \neg P(x)$ holds in classical logic, and its proof uses the [[law of excluded middle|0RYYK8PG4S]]. It is not valid in intuitionistic logic.

The same holds for the restricted form: $\neg \forall x \in A \; P(x) \equiv \exists x \in A \; \neg P(x)$.
In Mathlib, the classical equivalence is `Classical.not_forall`, which states `(¬ ∀ x, P x) ↔ ∃ x, ¬ P x`.
The proof is on the page [[proof of the negation of a universal statement|DTM9GQV88K]].

## Remarks

### Why each hypothesis is needed

The only hypothesis beyond the definitions is the use of classical logic, and it is needed only for direction 2.
Without excluded middle, direction 2 fails.
In a Kripke model of intuitionistic logic with worlds $w_0 \leq w_1 \leq w_2 \leq \cdots$, domain $\mathbb{N}$ at every world, and $P(k)$ forced at $w_n$ exactly when $k < n$, the formula $\neg \forall x \, P(x)$ is forced at $w_0$, but $\exists x \, \neg P(x)$ is not.
The reason is that each $P(k)$ becomes true at a later world, so no $k$ is a witness for $\neg P(k)$.
The statement does not need a non-empty domain.
For $D = \varnothing$, the formula $\forall x \, P(x)$ is true by [[vacuous truth|0V4QXPGJQK]], so both sides are false.

### Consequences

1. One [[counterexample|0ED72CTBNP]] refutes a universal statement: to prove $\neg \forall x \, P(x)$, it is enough to give one $a$ with $\neg P(a)$. This uses only direction 1.
2. Combined with the [[negation of an existential statement|05SZQKH75K]], it negates any string of quantifiers: each $\forall$ becomes $\exists$, each $\exists$ becomes $\forall$, and $\neg$ moves to the predicate. For example, $\neg \forall x \, \exists y \, P(x, y) \equiv \exists x \, \forall y \, \neg P(x, y)$.
3. $\forall x \, P(x) \equiv \neg \exists x \, \neg P(x)$ in classical logic. So either quantifier can be defined from the other with negation.
4. The negation of a restricted universal statement keeps the restriction: $\neg \forall \varepsilon > 0 \; Q(\varepsilon) \equiv \exists \varepsilon > 0 \; \neg Q(\varepsilon)$. The page [[negating mathematical statements|K930V33BSC]] gives the practice in mathematical English.

### Converse

The statement is an equivalence, so its converse is the statement itself.
The two directions are separate implications, and the converse question is which of them holds without excluded middle.
Direction 1, from $\exists x \, \neg P(x)$ to $\neg \forall x \, P(x)$, holds in every logic with the usual rules of quantifiers and negation.
Direction 2 is the classical one.

### Generalizations

1. For a finite domain $D = \{a_1, \ldots, a_n\}$, the statement is the [[De Morgan law|09PKJKA6J0]] $\neg (P(a_1) \land \cdots \land P(a_n)) \equiv \neg P(a_1) \lor \cdots \lor \neg P(a_n)$.
2. In set language, it says that the [[complement|0RKF1ZT5JJ]] of the truth set of $P$ is not empty exactly when the truth set is not all of $D$.
3. In a [[Boolean algebra|0XADJKM699]] with infinite meets and joins, the complement of the meet of a family equals the join of the complements.

## History

Aristotle treated "every $A$ is $B$" and "some $A$ is not $B$" as contradictory statements: exactly one of them is true.
Gottlob Frege's Begriffsschrift of 1879 had only the universal quantifier, and it expressed "some $x$ has $P$" as "not every $x$ has not $P$".
The Dutch mathematician Luitzen Brouwer rejected the general law of excluded middle, and with it direction 2 of this statement.

## Explanations

### L1 human

"Not every student passed the test" means "some student did not pass".
To deny that all members of a group have a property, it is enough to find one member without it.
For example, "every number from $1$ to $5$ is odd" is false, because $2$ is even.
So "not every number from $1$ to $5$ is odd" is true, and "some number from $1$ to $5$ is not odd" is true.

### L2 human

We negate the statement "every function $f \colon \mathbb{R} \to \mathbb{R}$ with $f(0) = 0$ satisfies $f(1) = 0$" and decide which one is true.

1. Write it in symbols: $\forall f \; (f(0) = 0 \to f(1) = 0)$, with $f$ ranging over functions $\mathbb{R} \to \mathbb{R}$.
2. Apply the theorem: the negation is $\exists f \; \neg (f(0) = 0 \to f(1) = 0)$.
3. The negation of an implication $p \to q$ is $p \land \neg q$, so the negation is $\exists f \; (f(0) = 0 \land f(1) \neq 0)$.
4. The function $f(x) = x$ has $f(0) = 0$ and $f(1) = 1 \neq 0$, so the negation is true.
5. So the original statement is false, and $f(x) = x$ is a counterexample.

The typical use is to find what a counterexample must satisfy, by pushing $\neg$ through the quantifier.
A trap is to write the negation of "every $x$ has $P$" as "every $x$ has not $P$".
For the numbers $1$ to $5$ and $P$ meaning "odd", the second statement is false, while the correct negation is true.

### L3 human

Classical logic treats $\forall$ and $\exists$ as duals, as the infinite forms of $\land$ and $\lor$, and the theorem is the infinite De Morgan law.
Intuitionistic logic keeps only one direction, because a proof of $\neg \forall x \, P(x)$ shows that the universal claim is absurd but does not produce a specific $a$ with $\neg P(a)$.
In a [[Heyting algebra|NG943XNQWH]], $\neg \bigwedge_i a_i \geq \bigvee_i \neg a_i$ always holds, and equality can fail.
In proof assistants, a proof that uses `Classical.not_forall` is non-constructive, and the witness that it produces cannot in general be computed.

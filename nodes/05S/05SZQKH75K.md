---
tag: 05SZQKH75K
kind: statement
role: theorem
name: Negation of an existential statement
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
about: [0MSRQHCNN9, 0GHS47PDAQ, 029JBBF693]
uses: [0B88PQTJ66, 0JW2FHW7G3, 0XR7A7RSXB, 0T3DPBG981, 0JMR2HM2N2]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/De_Morgan%27s_laws
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.2
history:
  notes: "Aristotle treated 'no A is B' and 'some A is B' as contradictory statements. Frege's Begriffsschrift (1879) introduced the quantifier with a bound variable."
---

## Statement

"No number from $1$ to $5$ is larger than $7$" says the same as "every number from $1$ to $5$ is not larger than $7$", and both are true.
In general, let $D$ be a domain of discourse and let $P(x)$ be a [[predicate|0T3DPBG981]] on $D$.
Then
$$\neg \exists x \, P(x) \;\equiv\; \forall x \, \neg P(x).$$
Here $\exists$ is the [[existential quantifier|0JW2FHW7G3]], $\forall$ is the [[universal quantifier|0B88PQTJ66]], $\neg$ is [[negation|0XR7A7RSXB]], and $\equiv$ is [[logical equivalence|0JMR2HM2N2]].
Both directions hold in classical logic and in [[intuitionistic logic|Q11N8X99FK]], because the proof does not use the [[law of excluded middle|0RYYK8PG4S]].
The same holds for the restricted form: $\neg \exists x \in A \; P(x) \equiv \forall x \in A \; \neg P(x)$.
In Mathlib, the equivalence is `not_exists`, which states `(¬ ∃ x, P x) ↔ ∀ x, ¬ P x`, and its proof there uses no classical axiom.
The proof is in [[proof of the negation of an existential statement|GANHAKFNTA]].

## Remarks

### A check on a small domain

Let $D = \{1, 2, 3\}$ and let $P(x)$ be "$x > 7$".
Then $\exists x \, P(x)$ is $P(1) \lor P(2) \lor P(3)$, which is false, so $\neg \exists x \, P(x)$ is true.
The formula $\forall x \, \neg P(x)$ is $\neg P(1) \land \neg P(2) \land \neg P(3)$, which is true.
On a finite domain the statement is the [[De Morgan law|09PKJKA6J0]] $\neg (P(a_1) \lor \cdots \lor P(a_n)) \equiv \neg P(a_1) \land \cdots \land \neg P(a_n)$, which is also valid intuitionistically.

### Why no hypothesis is needed

The statement holds for every domain and every predicate, with no hypothesis beyond the definitions of the symbols.
It needs no nonempty domain: for $D = \varnothing$, $\exists x \, P(x)$ is false, so $\neg \exists x \, P(x)$ is true, and $\forall x \, \neg P(x)$ is true by [[vacuous truth|0V4QXPGJQK]].
It needs no classical logic, unlike the [[negation of a universal statement|0P3A06QNDP]], where only the direction from $\exists x \, \neg P(x)$ to $\neg \forall x \, P(x)$ is intuitionistic.
The position of $\neg$ matters: $\neg \exists x \, P(x)$ is not equivalent to $\exists x \, \neg P(x)$.
Over $\mathbb{Z}$ with $P(x)$ meaning $x > 0$, the first is false because $1 > 0$, and the second is true because $0$ is not positive.

### Consequences

To prove that no object has a property, take an arbitrary $x$ and show $\neg P(x)$, as in [[proving universal statements|CX38X989TB]].
Applied to $\neg P$ in place of $P$, the statement gives $\neg \exists x \, \neg P(x) \equiv \forall x \, \neg \neg P(x)$.
With the classical [[double negation law|0NFAGWH84K]], this becomes $\forall x \, P(x) \equiv \neg \exists x \, \neg P(x)$.
Negating both sides gives $\exists x \, P(x) \to \neg \forall x \, \neg P(x)$ in every logic, and the equivalence $\exists x \, P(x) \equiv \neg \forall x \, \neg P(x)$ in classical logic.
Together with the negation of a universal statement, it negates any prefix of quantifiers.
For example, $\neg \exists y \, \forall x \, P(x, y) \equiv \forall y \, \neg \forall x \, P(x, y)$ in every logic, and this is equivalent to $\forall y \, \exists x \, \neg P(x, y)$ in classical logic.

### Converse and generalizations

The statement is an equivalence, and each direction holds without excluded middle, so the equivalence is valid intuitionistically.
In set language, the truth set of $P$ is empty exactly when every element lies in its [[complement|0RKF1ZT5JJ]].
In a complete [[Heyting algebra|NG943XNQWH]], $\neg \bigvee_i a_i = \bigwedge_i \neg a_i$ for every family $(a_i)$, because $a \mapsto (a \to 0)$ turns joins into meets.

## History

Aristotle treated "no $A$ is $B$" and "some $A$ is $B$" as contradictory statements, so that exactly one of them is true.
Gottlob Frege introduced the quantifier with a bound variable in his Begriffsschrift of 1879, and the law takes its modern form in that language.

## Explanations

### L1 human

"No student in the class has a dog" means "every student in the class has no dog".
To show that nobody has a property, we check that each one fails to have it.
For example, "no number from $1$ to $5$ is larger than $7$" is true, because $1, 2, 3, 4, 5$ are all at most $7$.
One number larger than $7$ in the list would make the sentence false.

### L2 human

Prove that no real number $x$ satisfies $x^2 + 1 = 0$.
In symbols, the claim is $\neg \exists x \in \mathbb{R} \; (x^2 + 1 = 0)$.
By the theorem, it is equivalent to $\forall x \in \mathbb{R} \; (x^2 + 1 \neq 0)$.
Let $x$ be an arbitrary real number; then $x^2 \geq 0$, so $x^2 + 1 \geq 1 > 0$.
So $x^2 + 1 \neq 0$ for every real $x$, and the claim is proved.
The theorem turns a claim of non-existence into a universal claim, which has a standard method of proof.
Watch out: "there is an $x$ with $x^2 + 1 \neq 0$" is a much weaker claim, and $x = 0$ already proves it.

### L3 human

In categorical logic, $\exists x$ is the left adjoint of the operation that adds a dummy variable, and $\neg \varphi$ is $\varphi \to \bot$, where $\bot$ does not depend on $x$.
The adjunction gives $(\exists x \, \varphi) \to \bot \;\equiv\; \forall x \, (\varphi \to \bot)$, which is the law.
The dual law would need $(\forall x \, \varphi) \to \bot$ to equal $\exists x \, (\varphi \to \bot)$, and no adjunction gives this, because $\forall x$ is a right adjoint.
This explains why one law of quantifier negation is intuitionistic and the other is classical.
In Lean, where `Not a` is `a → False`, the law is the currying of a function out of a dependent pair.

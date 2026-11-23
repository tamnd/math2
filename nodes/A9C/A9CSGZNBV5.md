---
tag: A9CSGZNBV5
kind: statement
role: theorem
name: Laws of propositional logic
aliases: [algebraic-laws-of-propositional-logic]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
about: [0JMR2HM2N2, 025YZN3VJW, 0F72FK8EKB]
uses: [0JMR2HM2N2, 025YZN3VJW, 0F72FK8EKB, 029JBBF693, 05RSK4Q657]
history:
  first_stated: "George Boole, The Mathematical Analysis of Logic (1847) and The Laws of Thought (1854), in the language of his algebra of logic"
  notes: "Augustus De Morgan stated the laws that carry his name in Formal Logic (1847)."
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_algebra
    locator: Laws
  - url: https://en.wikipedia.org/wiki/Algebra_of_sets
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Statement

The laws of propositional logic are the rules of algebra for "and" and "or": they let you rewrite a formula without changing its truth value.
"It is cold and it rains" says the same as "it rains and it is cold", and "it rains or it rains" says no more than "it rains".

Let $p$, $q$ and $r$ be propositional variables.
Let $\top$ be a formula that is true under every valuation, and let $\bot$ be a formula that is false under every valuation.
With $\land$ for [[conjunction|025YZN3VJW]] and $\lor$ for [[disjunction|0F72FK8EKB]], the following [[logical equivalences|0JMR2HM2N2]] hold.

1. Commutative laws: $p \land q \equiv q \land p$ and $p \lor q \equiv q \lor p$.
2. Associative laws: $(p \land q) \land r \equiv p \land (q \land r)$ and $(p \lor q) \lor r \equiv p \lor (q \lor r)$.
3. Distributive laws: $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ and $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$.
4. Absorption laws: $p \land (p \lor q) \equiv p$ and $p \lor (p \land q) \equiv p$.
5. Idempotent laws: $p \land p \equiv p$ and $p \lor p \equiv p$.
6. Identity laws: $p \land \top \equiv p$ and $p \lor \bot \equiv p$.
7. Domination laws: $p \lor \top \equiv \top$ and $p \land \bot \equiv \bot$.
8. Duality principle: let $\varphi$ and $\psi$ be formulas built from propositional variables, $\top$ and $\bot$ with the connectives $\neg$, $\land$ and $\lor$ only.
   Let the dual $\varphi^d$ be the formula obtained from $\varphi$ by exchanging $\land$ with $\lor$ and $\top$ with $\bot$ at every place.
   If $\varphi \equiv \psi$, then $\varphi^d \equiv \psi^d$.

By the substitution property of logical equivalence, laws 1 to 7 stay true when $p$, $q$ and $r$ are replaced by any formulas.
The [[proof by truth tables|BZDZ15FMZT]] checks every law.

## Remarks

### A simplification worked out

The laws earn their keep when a formula is too long to read.
Take $(p \lor q) \land (p \lor \neg q)$.
Read the second distributive law from right to left, then use the [[law of noncontradiction|MP4R7T546Z]] and the identity law:
$$(p \lor q) \land (p \lor \neg q) \equiv p \lor (q \land \neg q) \equiv p \lor \bot \equiv p.$$
Check: if $p$ is T, both brackets are T; if $p$ is F, the brackets are $q$ and $\neg q$, and one of them is F.
So the formula has the column of $p$, as the laws said.

### Why the exact form of each law matters

Laws 1 to 7 have no hypotheses, so the useful question is which close variants fail.
Mixed brackets do not regroup: $(p \land q) \lor r \not\equiv p \land (q \lor r)$, since in the row $p$ F, $q$ F, $r$ T the left side is T and the right side is F.
[[Negation|029JBBF693]] does not distribute over "and": in the row $p$ T, $q$ F, the formula $\neg(p \land q)$ is T but $\neg p \land \neg q$ is F, and the correct rule is [[De Morgan's law|09PKJKA6J0]].
Absorption needs two different connectives: in the row $p$ T, $q$ F, the formula $p \land (p \land q)$ is F while $p$ is T.

[[Material implication|0NMG7W7Q11]] is neither commutative nor associative.
In the row $p$ T, $q$ F, the formula $p \to q$ is F and $q \to p$ is T.
In the row where all three variables are F, $(p \to q) \to r$ is F and $p \to (q \to r)$ is T.

The duality principle needs its restriction to $\neg$, $\land$ and $\lor$.
The equivalence $p \to p \equiv \top$ is correct, but exchanging $\top$ with $\bot$ alone gives $p \to p \equiv \bot$, which fails when $p$ is T.
Rewrite $p \to p$ as $\neg p \lor p$ first, and the dual $\neg p \land p \equiv \bot$ is correct.

### What the laws give you

By the associative and commutative laws, brackets and order do not matter in a long conjunction or disjunction, so we write $p_1 \land p_2 \land \cdots \land p_n$ without brackets.
Each law in the list comes with its dual, and the duality principle turns one member of each pair into the other.
With the complement laws $p \lor \neg p \equiv \top$ and $p \land \neg p \equiv \bot$, laws 1, 3 and 6 are the axioms of a [[Boolean algebra|0XADJKM699]].
Every correct equivalence between formulas in $\neg$, $\land$, $\lor$, $\top$ and $\bot$ then follows from these laws by replacement of equivalents.
The laws, De Morgan's laws and the [[double negation law|0NFAGWH84K]] also turn each formula into an equivalent one in [[disjunctive normal form|0GVDFAY4KW]] or in [[conjunctive normal form|0B3D4C8YF2]].

### The same laws for sets

For subsets $A$ and $B$ of a universal set $U$, an element $x$ is in $A \cap B$ exactly when $x \in A$ and $x \in B$, and in $A \cup B$ exactly when $x \in A$ or $x \in B$.
So each law of logic gives a law of the [[algebra of sets|PFMGZ7988V]], by the dictionary below.

| Logic | Sets |
|---|---|
| $\land$, $\lor$, $\neg$ | [[intersection|0ZNMMA9TF5]] $\cap$, [[union|0X1GSWNBN1]] $\cup$, [[complement|0RKF1ZT5JJ]] $A^c$ |
| $\top$, $\bot$ | the [[universal set|0JNXSS9TJ9]] $U$, the [[empty set|0ECVK59Y03]] $\varnothing$ |
| $\equiv$ | $=$ |
| $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |
| $p \lor (p \land q) \equiv p$ | $A \cup (A \cap B) = A$ |
| $p \land \bot \equiv \bot$ | $A \cap \varnothing = \varnothing$ |

The [[distributive laws for sets|08N6EVA7DV]], [[De Morgan's laws for sets|0VK0W4D5Y5]] and [[Venn diagrams|0KCT6DPXJK]] show the same facts as pictures.

### The converse

Each of laws 1 to 7 is an equivalence, so it already contains both directions: each side is a logical consequence of the other.
The converse of the duality principle holds too: if $\varphi^d \equiv \psi^d$, then $\varphi \equiv \psi$.
The reason is that the dual of $\varphi^d$ is $\varphi$ again, so the principle applied to $\varphi^d$ and $\psi^d$ gives the converse.

### Generalizations

The distributive laws extend to $n$ terms, $p \land (q_1 \lor \cdots \lor q_n) \equiv (p \land q_1) \lor \cdots \lor (p \land q_n)$, by induction on $n$.
Laws 1 to 5 hold in every [[distributive lattice|0HM0HQCK6N]], and laws 1 to 7 in every bounded distributive lattice.
Every [[Heyting algebra|NG943XNQWH]] is a bounded distributive lattice, so laws 1 to 7 are valid in [[intuitionistic logic|Q11N8X99FK]] as well.
The duality principle fails there: $p \land \neg p \equiv \bot$ holds intuitionistically, but its dual $p \lor \neg p \equiv \top$, the [[law of excluded middle|0RYYK8PG4S]], does not.
In a [[Boolean ring|0RCV1ZFP8G]], conjunction becomes multiplication and [[exclusive or|PTMR3P9J6C]] becomes addition, so the idempotent law becomes $x^2 = x$.

## History

George Boole introduced an algebra of logic in The Mathematical Analysis of Logic of 1847 and in The Laws of Thought of 1854.
In his algebra the law $xx = x$ holds, and this idempotent law separates his algebra from the algebra of numbers.
Augustus De Morgan stated his laws for the negation of a conjunction and of a disjunction in Formal Logic of 1847.
Truth tables, which give a mechanical proof of each law, were used by Ludwig Wittgenstein and by Emil Post in 1921.

## Explanations

### L1 human

The laws of logic are rules for rewriting a sentence without changing what it says.
"It is cold and it rains" says the same as "it rains and it is cold": that is the commutative law.
"It is cold, or it is cold and it rains" says the same as "it is cold": that is absorption.
"It rains or it rains" says no more than "it rains": that is the idempotent law.
Each law has a twin with "and" and "or" exchanged, and the same rules hold for collections of things, with "and" as the common part and "or" as the union.

### L2 human

Here is a typical simplification: reduce $\varphi = (p \lor q) \land (p \lor \neg q) \land (p \lor r)$.
The first two brackets combine as in "A simplification worked out":
$$(p \lor q) \land (p \lor \neg q) \equiv p.$$
By replacement of equivalents, $\varphi \equiv p \land (p \lor r)$, and the absorption law finishes the job:
$$p \land (p \lor r) \equiv p.$$
Check with the table of 8 rows: when $p$ is T every bracket is T, and when $p$ is F the first two brackets are $q$ and $\neg q$, so $\varphi$ is F.
The same steps simplify conditions in programs, logic circuits and set expressions.
Watch out for an invented distributive law such as $p \land (q \lor r) \equiv (p \land q) \lor r$: it fails in the row $p$ F, $q$ F, $r$ T.

### L3 human

Laws 1 to 7, with the complement laws, say that the classes of formulas modulo logical equivalence form a Boolean algebra, the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]].
Every Boolean algebra satisfies the same equations as the two-element algebra $\{\mathrm{F}, \mathrm{T}\}$, so a law of logic is the same thing as an identity of Boolean algebras.
That is why a law checked by a truth table also holds for sets, for events in probability and for switching circuits.

The duality principle is the order reversal of [[duality in order theory|MRYFDAG5G8]]: the dual of a lattice is the same set with the order turned around.
In classical logic, negation is an isomorphism from the Lindenbaum-Tarski algebra to its dual, and this is why De Morgan's laws prove the principle.
In intuitionistic logic, negation is not such an isomorphism, laws 1 to 7 survive, and the duality principle fails.
[[The propositional calculus|JDK63589SA]] treats the laws as theorems of a formal system.

---
tag: 09PKJKA6J0
kind: statement
role: theorem
name: De Morgan's laws (logic)
aliases: [de-morgan-laws]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
about: [029JBBF693, 025YZN3VJW, 0F72FK8EKB]
uses: [029JBBF693, 025YZN3VJW, 0F72FK8EKB, 0JMR2HM2N2, 05RSK4Q657]
history:
  first_stated: "Augustus De Morgan, Formal Logic (1847)"
sources:
  - url: https://en.wikipedia.org/wiki/De_Morgan's_laws
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
  - book: isbn:9780122384523
    locator: Section 1.2
same_as:
  wikidata: Q173300
  wikipedia: De Morgan's laws
---

## Statement

Let $p$ and $q$ be propositional variables.
In classical propositional logic, these two [[logical equivalences|0JMR2HM2N2]] hold.
$$\neg(p \lor q) \equiv \neg p \land \neg q \qquad (1)$$
$$\neg(p \land q) \equiv \neg p \lor \neg q \qquad (2)$$
Here $\neg$ is [[negation|029JBBF693]], $\land$ is [[conjunction|025YZN3VJW]] and $\lor$ is [[disjunction|0F72FK8EKB]].
By substitution, the laws hold for all formulas $\varphi$ and $\psi$ in place of $p$ and $q$.

In [[intuitionistic logic|Q11N8X99FK]], law (1) holds in both directions.
Law (2) holds only in the direction $\neg p \lor \neg q \to \neg(p \land q)$.

For a [[predicate|0QHEWQD30B]] $P(x)$ on a domain $D$, the quantifier versions are
$$\neg \forall x \, P(x) \equiv \exists x \, \neg P(x) \qquad \text{and} \qquad \neg \exists x \, P(x) \equiv \forall x \, \neg P(x).$$
They are the pages [[negation of a universal statement|0P3A06QNDP]] and [[negation of an existential statement|05SZQKH75K]].

In Mathlib, law (1) is `not_or`, with the statement `¬(a ∨ b) ↔ ¬a ∧ ¬b`, and its proof uses no classical axiom.
Law (2) is `not_and_or`, with the statement `¬(a ∧ b) ↔ ¬a ∨ ¬b`, and its proof uses classical logic.
The quantifier versions are `Classical.not_forall` and `not_exists`.

The [[proof by truth tables|68VBVMFJSW]] gives the classical laws.
The [[proof by natural deduction|~af25eb09]] proves each direction separately and marks the one step that needs the [[law of excluded middle|0RYYK8PG4S]].

## Remarks

### Why each hypothesis is needed

The laws have no hypotheses on $p$ and $q$.
We show instead that the tempting wrong forms fail, each by one row of a [[truth table|05RSK4Q657]].

1. Negation does not distribute over conjunction: $\neg(p \land q) \not\equiv \neg p \land \neg q$. In the row $p = \mathrm{T}$, $q = \mathrm{F}$, the left side is $\neg \mathrm{F}$, which is T, and the right side is $\mathrm{F} \land \mathrm{T}$, which is F.
2. Negation does not distribute over disjunction: $\neg(p \lor q) \not\equiv \neg p \lor \neg q$. In the row $p = \mathrm{T}$, $q = \mathrm{F}$, the left side is $\neg \mathrm{T}$, which is F, and the right side is $\mathrm{F} \lor \mathrm{T}$, which is T.
3. Classical logic is needed for one direction of law (2). In intuitionistic logic, $\neg(p \land q) \to \neg p \lor \neg q$ is not provable. The L3 explanation gives a model where it fails.

### Consequences

1. Negation of compound statements. The negation of "$0 \le x$ and $x \le 1$" is "$x < 0$ or $x > 1$". See [[negating mathematical statements|K930V33BSC]].
2. Each of $\land$ and $\lor$ can be expressed by the other and $\neg$: $p \lor q \equiv \neg(\neg p \land \neg q)$ and $p \land q \equiv \neg(\neg p \lor \neg q)$. So $\{\neg, \land\}$ and $\{\neg, \lor\}$ are [[functionally complete|TDZVCWYJ9F]] sets of connectives.
3. With the [[double negation law|0NFAGWH84K]], the laws push each negation inward until it stands before a variable. This is the first step of the conversion to [[disjunctive normal form|0GVDFAY4KW]] and [[conjunctive normal form|0B3D4C8YF2]].
4. The laws prove the duality principle on the page [[laws of propositional logic|~5fa904ea]].
5. The [[Sheffer stroke|1NNYWRN6B8]] $p \uparrow q$, defined as $\neg(p \land q)$, is equivalent to $\neg p \lor \neg q$ by law (2).
6. For sets, the laws become $(A \cup B)^c = A^c \cap B^c$ and $(A \cap B)^c = A^c \cup B^c$. See [[De Morgan's laws for sets|0VK0W4D5Y5]].

### Converse

Each law is an equivalence, so it contains its own converse, and the question is the status of each of the four directions.

1. $\neg(p \lor q) \to \neg p \land \neg q$ holds intuitionistically.
2. $\neg p \land \neg q \to \neg(p \lor q)$ holds intuitionistically.
3. $\neg p \lor \neg q \to \neg(p \land q)$ holds intuitionistically.
4. $\neg(p \land q) \to \neg p \lor \neg q$ holds classically but not intuitionistically. Over intuitionistic logic, this direction for all formulas is equivalent to the [[law of the weak excluded middle|CX032ACTMZ]] $\neg p \lor \neg\neg p$ for all formulas.

The quantifier versions behave in the same way.
The equivalence $\neg \exists x \, P(x) \leftrightarrow \forall x \, \neg P(x)$ holds intuitionistically, and so does $\exists x \, \neg P(x) \to \neg \forall x \, P(x)$.
The direction $\neg \forall x \, P(x) \to \exists x \, \neg P(x)$ needs classical logic.

### Generalizations

1. For $n$ formulas, $\neg(p_1 \land \cdots \land p_n) \equiv \neg p_1 \lor \cdots \lor \neg p_n$ and $\neg(p_1 \lor \cdots \lor p_n) \equiv \neg p_1 \land \cdots \land \neg p_n$. The proof is by induction on $n$, with law (2) or (1) and the associative law in the induction step.
2. Over a finite domain $D = \{a_1, \ldots, a_n\}$, the formula $\forall x \, P(x)$ is equivalent to $P(a_1) \land \cdots \land P(a_n)$ and $\exists x \, P(x)$ to $P(a_1) \lor \cdots \lor P(a_n)$. Then the quantifier versions are the $n$-term laws of item 1.
3. In every [[Boolean algebra|0XADJKM699]], $\neg(a \lor b) = \neg a \land \neg b$ and $\neg(a \land b) = \neg a \lor \neg b$. See [[De Morgan's laws in a Boolean algebra|0XYVDWGQX2]].
4. In a [[Heyting algebra|NG943XNQWH]], law (1) holds and law (2) can fail. See [[the De Morgan laws in a Heyting algebra|V43C5CQ7AK]].
5. A [[De Morgan algebra|5Q53XWV0QN]] is a bounded distributive lattice with a negation that satisfies both laws and $\neg\neg a = a$, but not necessarily $a \land \neg a = 0$.

## History

Augustus De Morgan stated the laws in his book Formal Logic of 1847, and they carry his name.
In the same years George Boole developed his algebra of logic, in which the laws become identities.

## Explanations

### L1 human

To negate a statement with "and", change "and" to "or" and negate each part.
"It is not true that the shop is open and has bread" means "the shop is closed, or it has no bread".
To negate a statement with "or", change "or" to "and" and negate each part.
"It is not true that I will have tea or coffee" means "I will not have tea, and I will not have coffee".
A check with four situations for the two parts confirms each rule.

### L2 human

We negate the statement "$x \in [0, 1]$ or $x > 5$" about a real number $x$.

1. Write the statement as $p \lor q$, with $p$ the statement "$0 \le x \land x \le 1$" and $q$ the statement "$x > 5$".
2. By law (1), $\neg(p \lor q) \equiv \neg p \land \neg q$.
3. By law (2), $\neg p = \neg(0 \le x \land x \le 1) \equiv x < 0 \lor x > 1$.
4. Also $\neg q$ is $x \le 5$.
5. So the negation is "$(x < 0$ or $x > 1)$ and $x \le 5$", that is, $x < 0$ or $1 < x \le 5$.
6. Check with $x = 3$: the statement is false, since $3 \notin [0, 1]$ and $3 \le 5$, and the negation is true, since $1 < 3 \le 5$.

The typical use is the negation of a definition before a proof by contradiction or a search for a counterexample.
A trap is to negate the parts and keep the connective, as in the wrong forms above.

### L3 human

Law (1) says that negation turns a join into a meet, and it holds in any lattice where $\neg a$ is the largest element disjoint from $a$, such as a [[Heyting algebra|NG943XNQWH]].
Law (2) needs more: it fails in the Heyting algebra of open subsets of $\mathbb{R}$, where the negation of an open set is the interior of its complement.
For $U = (-\infty, 0)$ and $V = (0, \infty)$, we have $U \cap V = \varnothing$, so $\neg(U \cap V) = \mathbb{R}$, but $\neg U \cup \neg V = V \cup U = \mathbb{R} \setminus \{0\}$.
A [[Kripke model|NGHWZ9Y7ZV]] with a root and two incomparable later worlds, $p$ true at one of them and $q$ at the other, refutes the same direction at the root.

In a Boolean algebra, negation is an isomorphism from the algebra to its order dual, and De Morgan's laws say exactly this.
The quantifier versions are the same laws for infinite conjunctions and disjunctions, and the intuitionistic status is the same: the law for $\exists$ survives, the law for $\forall$ does not.
In a Heyting algebra, $b \le \neg a$ holds exactly when $a \le \neg b$.
So negation is a Galois connection between the algebra and its order dual, and such a map sends every join to the meet of the images.
This gives law (1), even for infinite joins, and the law for $\exists$ is its quantifier form.

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

De Morgan's laws tell you how to negate an "and" or an "or": negate each part and swap the connective.
"It is not true that I will have tea or coffee" means "I will not have tea, and I will not have coffee".

Let $p$ and $q$ be propositional variables.
In classical propositional logic these two [[logical equivalences|0JMR2HM2N2]] hold:
$$\neg(p \lor q) \equiv \neg p \land \neg q \qquad (1)$$
$$\neg(p \land q) \equiv \neg p \lor \neg q \qquad (2)$$
Here $\neg$ is [[negation|029JBBF693]], $\land$ is [[conjunction|025YZN3VJW]] and $\lor$ is [[disjunction|0F72FK8EKB]].
By substitution, the laws hold for all formulas $\varphi$ and $\psi$ in place of $p$ and $q$.

In [[intuitionistic logic|Q11N8X99FK]], law (1) holds in both directions, and law (2) holds only in the direction $\neg p \lor \neg q \to \neg(p \land q)$.

For a [[predicate|0QHEWQD30B]] $P(x)$ on a domain $D$, the quantifier versions are
$$\neg \forall x \, P(x) \equiv \exists x \, \neg P(x) \qquad \text{and} \qquad \neg \exists x \, P(x) \equiv \forall x \, \neg P(x),$$
treated in [[negation of a universal statement|0P3A06QNDP]] and [[negation of an existential statement|05SZQKH75K]].

In Mathlib, law (1) is `not_or`, with the statement `¬(a ∨ b) ↔ ¬a ∧ ¬b`, and its proof uses no classical axiom.
Law (2) is `not_and_or`, with the statement `¬(a ∧ b) ↔ ¬a ∨ ¬b`, and its proof uses classical logic.
The quantifier versions are `Classical.not_forall` and `not_exists`.
The [[proof by truth tables|68VBVMFJSW]] gives the classical laws, and the [[proof by natural deduction|PQ22Q2DYP0]] proves each direction separately and marks the one step that needs the [[law of excluded middle|0RYYK8PG4S]].

## Remarks

### Checking law (1) on the tea example

Let $p$ be "I will have tea" and $q$ be "I will have coffee".
There are four cases, and in each one compare $\neg(p \lor q)$ with $\neg p \land \neg q$:

| $p$ | $q$ | $p \lor q$ | $\neg(p \lor q)$ | $\neg p$ | $\neg q$ | $\neg p \land \neg q$ |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | F | T | F | F | T | F |
| F | T | T | F | T | F | F |
| F | F | F | T | T | T | T |

Both columns are true only in the last row, where I have neither drink.
Law (2) works the same way with the row "both true": $\neg(p \land q)$ and $\neg p \lor \neg q$ are false only when $p$ and $q$ are both true.

### The wrong forms and the intuitionistic gap

The tempting mistake is to negate the parts and keep the connective, and one row of a [[truth table|05RSK4Q657]] refutes it.
In the row $p$ T, $q$ F, the formula $\neg(p \land q)$ is T, but $\neg p \land \neg q$ is F.
In the same row, $\neg(p \lor q)$ is F, but $\neg p \lor \neg q$ is T.

Classical logic is needed for one direction of law (2).
Intuitionistically, a refutation of $p \land q$ need not tell you which part to refute, so $\neg(p \land q) \to \neg p \lor \neg q$ is not provable there.
The other three directions hold in both logics, and the L3 explanation gives a model where the fourth fails.

### What the laws give you

The laws negate compound statements: the negation of "$0 \le x$ and $x \le 1$" is "$x < 0$ or $x > 1$", as in [[negating mathematical statements|K930V33BSC]].
They express each of $\land$ and $\lor$ through the other and $\neg$: $p \lor q \equiv \neg(\neg p \land \neg q)$ and $p \land q \equiv \neg(\neg p \lor \neg q)$.
So $\{\neg, \land\}$ and $\{\neg, \lor\}$ are [[functionally complete|TDZVCWYJ9F]] sets of connectives.

With the [[double negation law|0NFAGWH84K]], the laws push each negation inward until it stands before a variable.
This is the first step of the conversion to [[disjunctive normal form|0GVDFAY4KW]] and [[conjunctive normal form|0B3D4C8YF2]].
The laws also prove the duality principle among the [[laws of propositional logic|A9CSGZNBV5]].
The [[Sheffer stroke|1NNYWRN6B8]] $p \uparrow q$, defined as $\neg(p \land q)$, is equivalent to $\neg p \lor \neg q$ by law (2).
For sets, the laws become $(A \cup B)^c = A^c \cap B^c$ and $(A \cap B)^c = A^c \cup B^c$, the [[De Morgan's laws for sets|0VK0W4D5Y5]].

### The four directions

Each law is an equivalence, so it contains its own converse, and the interesting question is the status of each of the four directions.
Both directions of law (1) hold intuitionistically, and so does $\neg p \lor \neg q \to \neg(p \land q)$.
The fourth direction, $\neg(p \land q) \to \neg p \lor \neg q$, holds classically but not intuitionistically.
Over intuitionistic logic, this direction for all formulas is equivalent to the [[law of the weak excluded middle|CX032ACTMZ]] $\neg p \lor \neg\neg p$ for all formulas.

The quantifier versions behave in the same way.
Both directions of $\neg \exists x \, P(x) \leftrightarrow \forall x \, \neg P(x)$ hold intuitionistically, and so does $\exists x \, \neg P(x) \to \neg \forall x \, P(x)$.
The direction $\neg \forall x \, P(x) \to \exists x \, \neg P(x)$ needs classical logic.

### Generalizations

For $n$ formulas, $\neg(p_1 \land \cdots \land p_n) \equiv \neg p_1 \lor \cdots \lor \neg p_n$ and $\neg(p_1 \lor \cdots \lor p_n) \equiv \neg p_1 \land \cdots \land \neg p_n$, by induction on $n$ with the associative law.
Over a finite domain $D = \{a_1, \ldots, a_n\}$, $\forall x \, P(x)$ is equivalent to $P(a_1) \land \cdots \land P(a_n)$ and $\exists x \, P(x)$ to $P(a_1) \lor \cdots \lor P(a_n)$, so the quantifier versions are the $n$-term laws.

In every [[Boolean algebra|0XADJKM699]], $\neg(a \lor b) = \neg a \land \neg b$ and $\neg(a \land b) = \neg a \lor \neg b$, as in [[De Morgan's laws in a Boolean algebra|0XYVDWGQX2]].
In a [[Heyting algebra|NG943XNQWH]], law (1) holds and law (2) can fail, as in [[the De Morgan laws in a Heyting algebra|V43C5CQ7AK]].
A [[De Morgan algebra|5Q53XWV0QN]] is a bounded distributive lattice with a negation that satisfies both laws and $\neg\neg a = a$, but not necessarily $a \land \neg a = 0$.

### Try it

Negate "$n$ is even and $n > 10$" for an integer $n$.
By law (2) the negation is "$n$ is odd or $n \le 10$".

Negate "$x < -1$ or $x > 1$" for a real number $x$.
By law (1) it is "$x \ge -1$ and $x \le 1$", that is, $-1 \le x \le 1$.

## History

Augustus De Morgan stated the laws in his book Formal Logic of 1847, and they carry his name.
In the same years George Boole developed his algebra of logic, in which the laws become identities.

## Explanations

### L1 human

To negate a statement with "and", change "and" to "or" and negate each part.
"It is not true that the shop is open and has bread" means "the shop is closed, or it has no bread".
To negate a statement with "or", change "or" to "and" and negate each part.
"It is not true that I will have tea or coffee" means "I will not have tea, and I will not have coffee".
A check of the four possible situations confirms each rule.

### L2 human

Here is a typical negation: the statement "$x \in [0, 1]$ or $x > 5$" about a real number $x$.
Write it as $p \lor q$, with $p$ the statement "$0 \le x \land x \le 1$" and $q$ the statement "$x > 5$".
Law (1) turns the outer negation into a conjunction, and law (2) handles the inner "and":
$$\neg(p \lor q) \equiv \neg p \land \neg q \equiv (x < 0 \lor x > 1) \land x \le 5.$$
So the negation is "$x < 0$, or $1 < x \le 5$".
Check with $x = 3$: the statement is false, since $3 \notin [0, 1]$ and $3 \le 5$, and the negation is true, since $1 < 3 \le 5$.
Negations like this come before every proof by contradiction and every search for a counterexample.
Watch out for the step $\neg q$: the negation of $x > 5$ is $x \le 5$, not $x < 5$.

### L3 human

Law (1) says that negation turns a join into a meet, and it holds in any lattice where $\neg a$ is the largest element disjoint from $a$, such as a Heyting algebra.
Law (2) needs more: it fails in the Heyting algebra of open subsets of $\mathbb{R}$, where the negation of an open set is the interior of its complement.
For $U = (-\infty, 0)$ and $V = (0, \infty)$ we have $U \cap V = \varnothing$, so $\neg(U \cap V) = \mathbb{R}$, but $\neg U \cup \neg V = V \cup U = \mathbb{R} \setminus \{0\}$.
A [[Kripke model|NGHWZ9Y7ZV]] with a root and two incomparable later worlds, $p$ true at one of them and $q$ at the other, refutes the same direction at the root.

In a Heyting algebra, $b \le \neg a$ holds exactly when $a \le \neg b$.
So negation is a Galois connection between the algebra and its order dual, and such a map sends every join to the meet of the images.
This gives law (1) even for infinite joins, and the law for $\exists$ is its quantifier form, while the law for $\forall$ fails as law (2) does.
In a Boolean algebra, negation is an isomorphism onto the order dual, and De Morgan's laws say exactly this.

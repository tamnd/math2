---
tag: DZVEFDYYZX
kind: concept
name: Plural quantification
aliases: [plural-logic, plural-quantifier]
msc: ["03A05", "03B16", "03B65"]
topics: [MDHDYV8QZW]
audience: research
uses: [086QKPF0A6, G6X7SZSNC5]
sources:
  - url: https://en.wikipedia.org/wiki/Plural_quantification
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Plural_quantification
    locator: History
  - url: https://en.wikipedia.org/wiki/Plural_quantification
    locator: Nominalism
  - url: https://en.wikipedia.org/wiki/Plural_quantification
    locator: Formal definition
---

## Summary

Plural quantification speaks about several objects at once without collecting them into a new object.
Its two forms are "there are some things $xx$ such that $\varphi(xx)$" and "for any things $xx$, $\varphi(xx)$".
George Boolos proposed to read the set variables of monadic [[second-order logic|G6X7SZSNC5]] in this way, so that $Xy$ means "$y$ is one of them".
On this reading, monadic second-order logic speaks only about the objects of the domain and assumes no sets.

Plural logic is [[first-order logic|086QKPF0A6]] with plural variables $xx, yy, \ldots$, the quantifiers $\exists xx$ and $\forall xx$, and a binary predicate $y \prec xx$, read "$y$ is one of $xx$".
Its axioms are the first-order axioms for both kinds of variables and the axiom $\forall xx \, \exists y \, (y \prec xx)$: some things are at least one thing.
It also has the comprehension schema, with $xx$ not free in $\varphi$:
$$\exists y \, \varphi(y) \to \exists xx \, \forall y \, \big( y \prec xx \leftrightarrow \varphi(y) \big).$$

## Motivation

Ordinary language has plural quantifiers, as in "some critics admire only one another".
The usual first-orderization adds a set: "there is a nonempty set $S$ of critics such that ...".
This changes the subject, since the sentence was about critics and the paraphrase is about a set.
For some sentences, first-order logic cannot avoid the change.
[[The Geach-Kaplan sentence|655T2GTWNV]] has no first-order paraphrase that uses only its own predicates.

The set paraphrase even fails in set theory.
"There are some sets that are exactly the sets that are not members of themselves" is true.
"There is a set of all sets that are not members of themselves" is false, by [[Russell's paradox|0HESMMSYEG]].
Plural quantification keeps the plural form and needs no collection as a new object.
This matters for the old question whether second-order logic is logic or set theory.

## Notation

The philosophical literature often writes $xx, yy$ for plural variables and $y \prec xx$ for "$y$ is one of $xx$".
"Is among" is another reading of $\prec$.
Other authors write $\bar{x}$, or use second-order letters $X, Y$ with $Xy$ for "$y$ is one of $X$", as Boolos did.
Boolos's translation from monadic second-order logic sends an atom $Xy$ to $y \prec xx$, and a quantifier $\exists X \, \varphi(X)$ to this formula:
$$\varphi[\emptyset] \lor \exists xx \, \varphi[xx].$$
Here $\varphi[\emptyset]$ replaces each atom $Xy$ by $y \neq y$, and $\varphi[xx]$ replaces it by $y \prec xx$.
The first disjunct handles the empty set, which has no plural counterpart.

## Remarks

### Sentences that are plural

The Geach-Kaplan sentence has a plural quantifier at its core:
$$\exists xx \, \big( \forall x \, (x \prec xx \to Cx) \land \forall x \, \forall y \, ((x \prec xx \land Axy) \to (x \neq y \land y \prec xx)) \big).$$
It has no first-order equivalent in $C$ and $A$, and [[the example|655T2GTWNV]] gives the proof.

Induction has a plural form.
Take any things $xx$ such that $0$ is among them and the successor of each of them is among them.
Then every natural number is among them.
With the full semantics, this axiom makes the [[Peano axioms|0QFT7Z76N5]] categorical.

There are some sets that are exactly the sets that are not members of themselves, and no set has exactly them as members, as [[this example|T97GY9ZT21]] shows.

Some plural sentences are first-order in disguise.
"Some numbers are prime" is $\exists xx \, \forall y \, (y \prec xx \to Py)$, and it is equivalent to $\exists y \, Py$, because one prime is already some numbers that are all prime.

### What is not plural

The second-order sentence $\exists X \, \forall x \, \neg Xx$ says "there is an empty set", and it has no direct plural reading.
No things are no things, as [[this non-example|R496E8BXRB]] shows.

A quantifier over binary relations, $\exists R \, \varphi(R)$, is not plural quantification over the domain.
A relation is a plurality of ordered pairs, so a plural reading needs the pairs as objects of the domain.

The paraphrase "there is a set $S$ of critics such that ..." is a singular quantifier over a set.
It is true only if the set exists, so it fails for pluralities that do not form a set.

### Plural logic and monadic second-order logic

Boolos's translation and the reverse translation, which sends $xx$ to $X$ and adds $\exists x \, Xx$, interpret each logic in the other.
In the usual set-theoretic model theory, a plural variable ranges over the nonempty subsets of the domain.
So plural logic has the properties of monadic second-order logic with the full semantics.

Let $\mathrm{PA}^2_{+}$ be plural Peano arithmetic with the recursion equations for $+$ and $\cdot$.
Its models are all isomorphic to $(\mathbb{N}, 0, S, +, \cdot)$.
So $\mathrm{PA}^2_{+} \to \varphi$ is valid exactly when $\varphi$ is true in $\mathbb{N}$, and the valid plural sentences are not recursively enumerable.

Compactness fails.
Plural Peano arithmetic with a new constant $c$ and the sentences $c \neq 0, c \neq S0, c \neq SS0, \ldots$ is finitely satisfiable, but it has no model.
The downward Löwenheim-Skolem property fails too, because the ordered field axioms with plural completeness have only models isomorphic to $\mathbb{R}$.

### Why comprehension is safe

Plural comprehension does not lead to Russell's paradox.
The predicate $\prec$ takes a singular term on its left, so "$xx \prec xx$" is not a formula.
No axiom turns a plurality into an object, so Russell's argument cannot start.

Plural logic alone does not give Frege's arithmetic from [[Hume's principle|J36EHBHF6J]], which quantifies over binary relations.
Frege's definition of the ancestral of a relation needs only monadic quantifiers, so it has a plural reading.

### History

Peter Geach proposed the sentence "some critics admire only one another", and David Kaplan proved that it has no first-order paraphrase in its own predicates.
George Boolos argued in 1984 that plural quantification interprets monadic second-order logic.
The paper is "To be is to be a value of a variable (or to be some values of some variables)".
He developed the formal system in "Nominalist Platonism" in 1985.
David Lewis used plural quantification as a basis for set theory in "Parts of Classes" of 1991.

### Watch out

Do not read a plural variable as a variable for sets.
On Boolos's reading, $\exists xx$ ranges over the same objects as $\exists x$, taken several at a time.

Do not translate $\exists X$ directly as $\exists xx$.
That drops the empty set, and then the translation of the valid sentence $\exists X \, \forall x \, \neg Xx$ is false.

Do not use plural comprehension like set comprehension.
It gives some things, not an object that has them as members.

### Try it

Translate $\exists X \, \exists x \, Xx$ with Boolos's rule.
The first disjunct is $\exists x \, (x \neq x)$, which is false, so the translation is equivalent to $\exists xx \, \exists x \, (x \prec xx)$, which is true.

## Explanations

### L1 human

We often speak about several things at once without collecting them into a new thing.
"Some students lifted the table" is about students, not about a set of students.
Plural quantification is the logic of such phrases: "there are some things such that ..." and "for any things ...".
For example, among the numbers $1$ to $10$ there are some numbers that are all odd and all prime: $3$, $5$ and $7$.
The claim is about these three numbers, and it does not ask whether a set $\set{3, 5, 7}$ exists.
Boolos showed that a large part of second-order logic can be read in this way.

### L2 human

We translate the monadic second-order sentence "every nonempty set of natural numbers has a least element" into plural logic.

1. The second-order form is $\forall X \, \big( \exists x \, Xx \to \exists x \, (Xx \land \forall y \, (Xy \to x \leq y)) \big)$.
2. Write $\forall X$ as $\neg \exists X \, \neg$.
   Boolos's translation of $\exists X \, \psi$ is $\psi[\emptyset] \lor \exists xx \, \psi[xx]$.
3. Here $\psi(X)$ is $\exists x \, Xx \land \neg \exists x \, (Xx \land \forall y \, (Xy \to x \leq y))$.
4. When $Xx$ is replaced by $x \neq x$, the first conjunct of $\psi$ becomes $\exists x \, (x \neq x)$, which is false.
   So $\psi[\emptyset]$ is false.
5. So the translation is $\neg \exists xx \, \psi[xx]$.
   It says that for any numbers $xx$, some number $x$ is one of them and is at most each of them.
6. This is the well-ordering principle in the form "any natural numbers have a least one among them".

The typical use of the translation is to restate a second-order axiom with no reference to sets.
Watch out: do not skip step 4.
In other sentences the empty case is true, and then the whole translation is true because of it.

### L3 human

Plural logic sits between first-order logic and full second-order logic.
It has the expressive power of monadic second-order logic with the full semantics, so it characterizes $\mathbb{N}$ and $\mathbb{R}$, and it has no complete proof system.
The philosophical debate is about its status.
Quine called second-order logic "set theory in sheep's clothing".
Boolos replied that, on the plural reading, the monadic part commits us only to the objects of the domain.
The model theory of plural logic can be given in set theory, where pluralities become nonempty subsets, or in a metalanguage that itself has plural quantifiers.
The plural reading matches the full semantics and not the [[Henkin semantics|KWEJFK5943]]: "any things" means any things whatever, not any things from a chosen family.

In set theory, plural quantifiers give a reading of proper classes without class objects.
Separation and replacement become single axioms with a plural variable, as in second-order [[Zermelo–Fraenkel set theory|0HE5WDQ9FJ]].
These axioms need no class objects, unlike [[von Neumann–Bernays–Gödel set theory|JTPZ1HZ9KK]].
For replacement, a class function becomes a plurality of ordered pairs.
Plural separation, for example, says: for any set $a$ and any things $xx$, some set has as members exactly the members of $a$ among $xx$.
Extensions of the idea include higher-level plurals, called superplurals, and the use of plural logic in [[logicism|5PGSQYB5Y1]].
Another extension adds plural predicates such as "they surround the building", which do not apply to each thing separately.

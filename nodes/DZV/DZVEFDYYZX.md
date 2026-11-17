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

Plural quantification is quantification of the form "there are some things $xx$ such that $\varphi(xx)$" and "for any things $xx$, $\varphi(xx)$".
Plural logic is [[first-order logic|086QKPF0A6]] with plural variables $xx, yy, \ldots$, the quantifiers $\exists xx$ and $\forall xx$, and the binary predicate $y \prec xx$, read "$y$ is one of $xx$".
Its axioms are the first-order axioms for both kinds of variables and the axiom $\forall xx \, \exists y \, (y \prec xx)$ (some things are at least one thing).
It also has the comprehension schema
$$\exists y \, \varphi(y) \to \exists xx \, \forall y \, \big( y \prec xx \leftrightarrow \varphi(y) \big),$$
with $xx$ not free in $\varphi$.
George Boolos proposed to read the set variables of monadic [[second-order logic|G6X7SZSNC5]] (full semantics) as plural variables.
Then $Xy$ means "$y$ is one of them".
On this reading, monadic second-order logic speaks only about the objects of the domain and assumes no sets.
This matters for the question whether second-order logic is logic.

## Motivation

Ordinary language has plural quantifiers, as in "some critics admire only one another".
Another example is "for any numbers, if $0$ is among them and so is the successor of each, then every number is among them".
The usual way to formalize such a sentence in first-order logic introduces a set: "there is a nonempty set $S$ of critics such that ...".
This changes the subject: the sentence was about critics, and the paraphrase is about a set.
For some sentences the change cannot be avoided in first-order logic: the Geach-Kaplan sentence has no first-order paraphrase that uses only its own predicates.
The change also fails in set theory itself.
"There are some sets that are exactly the sets not members of themselves" is true.
But "there is a set of all sets not members of themselves" is false, by [[Russell's paradox|0HESMMSYEG]].
Plural quantification keeps the plural form and needs no collection as a new object.

## Notation

The notation $xx$, $yy$ for plural variables and $y \prec xx$ for "$y$ is one of $xx$" is common in the philosophical literature.
Other authors write $\bar{x}$, or use second-order letters $X, Y$ with $Xy$ for "$y$ is one of $X$", as Boolos did.
"Is among" is another reading of $\prec$.
In Boolos's translation from monadic second-order logic, an atom $X y$ becomes $y \prec xx$, and a quantifier $\exists X \, \varphi(X)$ becomes
$$\varphi[\emptyset] \lor \exists xx \, \varphi[xx],$$
where $\varphi[\emptyset]$ replaces each atom $Xy$ by $y \neq y$, and $\varphi[xx]$ replaces it by $y \prec xx$.
The first disjunct handles the empty set, which has no plural counterpart.

## Remarks

### Examples

- The Geach-Kaplan sentence "some critics admire only one another": $\exists xx \, \big( \forall x \, (x \prec xx \to Cx) \land \forall x \, \forall y \, ((x \prec xx \land Axy) \to (x \neq y \land y \prec xx)) \big)$. It has no first-order equivalent in $C$ and $A$; [[this example|655T2GTWNV]] gives the proof.
- Induction for the natural numbers: take any things $xx$ such that $0$ and the successor of each of them are among them. Then every natural number is among them. With full semantics this axiom makes the [[Peano axioms|0QFT7Z76N5]] categorical.
- Completeness of the real numbers: any real numbers that have an upper bound have a least upper bound. The plural form fits, since "any real numbers" are at least one number, as the usual axiom requires.
- Russell's class: there are some sets that are exactly the sets not members of themselves. No set has exactly them as members; see [[this example|T97GY9ZT21]].
- "Some numbers are prime": $\exists xx \, \forall y \, (y \prec xx \to Py)$. This plural sentence is equivalent to the first-order $\exists y \, Py$, since one prime is already some numbers that are all prime.

### Non-examples

- The second-order sentence $\exists X \, \forall x \, \neg Xx$ ("there is an empty set") has no plural reading: no things are no things. See [[this non-example|R496E8BXRB]].
- Quantification over binary relations, $\exists R \, \varphi(R)$, is not plural quantification over the domain. A relation is a plurality of ordered pairs, so a plural reading needs pairs as objects of the domain.
- The set paraphrase "there is a set $S$ of critics such that ..." is singular quantification over a set. It is true only if the set exists, and it fails for plurals that do not form a set, as in Russell's class.

### Basic properties

- Boolos's translation and the reverse translation ($xx \mapsto X$ with $\exists x \, Xx$ added) show that plural logic and monadic second-order logic are interpretable in each other.
- In the standard set-theoretic model theory, a plural variable ranges over the nonempty subsets of the domain. Then plural logic inherits the properties of monadic second-order logic with full semantics.
- Plural induction makes second-order Peano arithmetic categorical, as in the example above. So the valid plural sentences are not recursively enumerable: $\mathrm{PA}^2 \to \varphi$ is valid exactly when $\varphi$ is true in $\mathbb{N}$.
- Plural logic is not compact: plural Peano arithmetic, a new constant $c$, and the sentences $c \neq 0, c \neq S0, c \neq SS0, \ldots$ are finitely satisfiable but have no model.
- Plural logic does not have the downward Löwenheim-Skolem property: the ordered field axioms with plural completeness have only models isomorphic to $\mathbb{R}$.
- Comprehension does not lead to Russell's paradox. The predicate $\prec$ takes a singular term on its left, so "$xx \prec xx$" is not a formula, and no axiom turns a plurality into an object.
- Plural logic alone is not enough for Frege's arithmetic from [[Hume's principle|J36EHBHF6J]], which quantifies over binary relations. Frege's definition of the ancestral of a relation needs only monadic quantification, so it has a plural reading.

### History

Peter Geach proposed the sentence "some critics admire only one another", and David Kaplan proved that it has no first-order paraphrase in its own predicates.
George Boolos argued in 1984 that plural quantification interprets monadic second-order logic.
The paper is "To be is to be a value of a variable (or to be some values of some variables)".
He developed the formal system in "Nominalist Platonism" in 1985.
David Lewis used plural quantification as a basis for set theory in "Parts of Classes" (1991).

### Common errors

- To read a plural variable as a variable for sets. On Boolos's reading, $\exists xx$ ranges over the same objects as $\exists x$, taken several at a time.
- To translate $\exists X$ directly as $\exists xx$. This drops the case of the empty set, and the translation of $\exists X \, \forall x \, \neg Xx$ becomes false.
- To use plural comprehension like set comprehension. Comprehension gives some things, not an object that has them as members, so Russell's argument does not start.

## Explanations

### L1 human

We often speak about several things at once without collecting them into a new thing.
"Some students lifted the table" talks about students, not about a set of students.
Plural quantification is the logic of such phrases: "there are some things such that ..." and "for any things ...".
For example, among the numbers $1$ to $10$ there are some numbers that are all odd and all prime: $3$, $5$ and $7$.
The claim is about these three numbers, and it does not ask whether a set $\{3, 5, 7\}$ exists.
Boolos showed that a large part of second-order logic can be read in this way.

### L2 human

We translate the monadic second-order sentence "every nonempty set of natural numbers has a least element" into plural logic.

1. In second-order form: $\forall X \, \big( \exists x \, Xx \to \exists x \, (Xx \land \forall y \, (Xy \to x \leq y)) \big)$.
2. Write $\forall X$ as $\neg \exists X \, \neg$. Boolos's translation of $\exists X \, \psi$ is $\psi[\emptyset] \lor \exists xx \, \psi[xx]$.
3. Here $\psi(X)$ is $\exists x \, Xx \land \neg \exists x \, (Xx \land \forall y \, (Xy \to x \leq y))$.
4. With $Xx$ replaced by $x \neq x$, the first conjunct of $\psi$ becomes $\exists x \, x \neq x$, which is false. So $\psi[\emptyset]$ is false.
5. So the translation is $\neg \exists xx \, \psi[xx]$, that is: for any numbers $xx$, some number $x$ is one of them and is at most each of them.
6. The plural sentence is the well-ordering principle in the form "any natural numbers have a least one among them".

The typical use of the translation is to restate a second-order axiom with no reference to sets.
A trap is to skip step 4: in other sentences the empty case is true, and then the whole translation is true because of it.

### L3 human

Plural logic sits between first-order logic and full second-order logic.
Its expressive power is that of monadic second-order logic with full semantics, so it can characterize $\mathbb{N}$ and $\mathbb{R}$ and has no complete proof system.
The philosophical debate is about its status.
Quine called second-order logic "set theory in sheep's clothing".
Boolos replied that, on the plural reading, the monadic part commits us only to the objects of the domain.
The model theory of plural logic can be given in set theory, where pluralities become nonempty subsets.
It can also be given in a metalanguage that itself has plural quantifiers.
The plural reading matches full semantics and not [[Henkin semantics|KWEJFK5943]]: "any things" means any things whatever, not any things from a chosen family.

In set theory, plural quantification offers a reading of proper classes without class objects.
Separation and replacement can be stated as single axioms with a plural variable, as in second-order [[Zermelo–Fraenkel set theory|0HE5WDQ9FJ]].
These axioms need no class objects, unlike [[von Neumann–Bernays–Gödel set theory|JTPZ1HZ9KK]].
For replacement, a class function becomes a plurality of ordered pairs.
For example, plural separation says: for any set $a$ and any things $xx$, some set has as members exactly the members of $a$ among $xx$.
Extensions of the idea include higher-level plurals ("superplurals") and the use of plural logic in [[logicism|5PGSQYB5Y1]].
Another extension is plural predicates such as "they surround the building", which do not apply to each thing separately.

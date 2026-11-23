---
tag: G0DTR159RN
kind: statement
role: theorem
name: Model existence theorem
aliases: [model-existence-theorem, model-existence-lemma]
msc: ["03C07", "03B10"]
topics: [FBWW4J1XWG]
audience: ug2
about: [VM8TQ70CVJ, QN7M1JCGT9, 086QKPF0A6]
uses: [AVD7T7J063, SC0BSJ3GT6, RY8KRKR097, VM8TQ70CVJ, DKFGQTRYZE, MVCH6N9SNW, QN7M1JCGT9, 01TQB88H4C, 0G0ASKNA6Z]
history:
  first_stated: "Leon Henkin, 1949, for first-order languages of any cardinality"
  notes: "Henkin proved it with witness constants and term models."
sources:
  - wikipedia: en:12450@r1371782634
    locator: Gödel's completeness theorem, section Statement > Model existence theorem
    note: adopted
    mention: wikipedia://en/12450#2V6I
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem
    locator: Model existence theorem
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem
    locator: As a theorem of arithmetic
  - book: isbn:9780122384523
    locator: Section 2.5
  - url: https://builds.openlogicproject.org/
    locator: The Completeness Theorem
inventory: [WCMCVZR0SC]
---

## Statement

The model existence theorem says that a set of axioms from which no contradiction can be derived always has a structure that makes all the axioms true.

Let $L$ be a first-order language with equality, and let $\vdash$ be derivability in the Hilbert system $H$ of the [[soundness theorem|AVD7T7J063]].
A set of [[sentences|DKFGQTRYZE]] is [[consistent|VM8TQ70CVJ]] when it derives no pair $\psi$, $\neg \psi$.
We write $|L|$ for the [[cardinality|0G0ASKNA6Z]] of the set of symbols of $L$.

**Theorem (model existence).**

1. Every consistent set $\Gamma$ of sentences of $L$ has a [[model|MVCH6N9SNW]].
2. The model can be chosen with at most $|L| + \aleph_0$ elements, that is, at most $\max(|L|, \aleph_0)$ elements.
   In particular, when $L$ is [[countable|01TQB88H4C]], $\Gamma$ has a model that is finite or countably infinite.
3. Part 1 is equivalent to strong completeness: for every set $\Gamma$ of sentences and every sentence $\varphi$, if $\Gamma \models \varphi$, then $\Gamma \vdash \varphi$.

The [[proof by the Henkin construction|FMZMD0GGYK]] gives every detail for countable $L$, and its Variants section treats uncountable $L$, where the axiom of choice is used.

## Remarks

### A first use: a model as a certificate

Do the axioms of a partial order prove that any two elements are comparable?
Take the structure with universe $\{ a, b \}$ in which $a \le a$ and $b \le b$ hold and nothing else does.
It is reflexive, antisymmetric and transitive, so it is a partial order, and $a$, $b$ are not comparable.
So "any two elements are comparable" fails in a model of the axioms, and by soundness it is not derivable.

The model existence theorem says that this method always works.
If $\Gamma \nvdash \varphi$, then $\Gamma \cup \{ \neg \varphi \}$ is consistent, so it has a model, and that model is a certificate of non-derivability.
For sets of sentences, "consistent" and "[[satisfiable|QN7M1JCGT9]]" are the same property: soundness gives one direction, and the theorem gives the other.

### How the model is built

The proof has no model to start from, so it builds one out of the language itself.
It adds a witness constant for each existential sentence, extends the set to a maximal consistent one by [[Lindenbaum's lemma|SC0BSJ3GT6]], and takes the closed terms modulo provable equality as the elements.
This is the [[Henkin construction|RY8KRKR097]], and part 2 comes for free: the elements are classes of closed terms, and there are at most $|L| + \aleph_0$ closed terms.

### Why each hypothesis is needed

Consistency is needed because, by part 3 of the soundness theorem, a set with a model is consistent.

The proof system must handle equality.
Remove axiom group 6 from $H$, and the set $\{ a = b, P(a), \neg P(b) \}$ derives no contradiction, since $=$ may then be read as any reflexive relation.
But it has no model, because in a structure $=$ means identity.

The bound $|L| + \aleph_0$ cannot be lowered to $|L|$.
The empty language has $|L|$ finite, and the sentences "there are at least $n$ elements", for all $n \ge 1$, have only infinite models.

For languages of every size, part 1 is equivalent in ZF to the [[Boolean prime ideal theorem|STPBXBKSZP]].
For countable $L$, no choice is needed, because the sentences can be listed.

### Why it is the same as completeness

Suppose part 1 holds and $\Gamma \models \varphi$.
Then $\Gamma \cup \{ \neg \varphi \}$ has no model, so it is inconsistent, and fact (P5) of the [[proof of Lindenbaum's lemma|DCR0S91GYY]] gives $\Gamma \vdash \varphi$.
This is [[Gödel's completeness theorem|WQ1ZE255SF]].

Conversely, assume strong completeness, and let $\Gamma$ have no model.
Then $\Gamma \models \forall x \, (x = x)$ and $\Gamma \models \neg \forall x \, (x = x)$ hold, since there is no model to check.
So $\Gamma$ derives both sentences and is inconsistent.

### What else it gives you

The [[compactness theorem|1NR3HAWG9D]] follows at once: a finitely satisfiable set is consistent, because a derivation uses finitely many sentences, and so it has a model.
Part 2 is a first form of the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]]: a consistent theory in a countable language has a countable model.
For example, ZFC, if it is consistent, has a countable model, which is [[Skolem's paradox|68QZWDXAQ4]].

### Watch out

The model that the theorem gives is built from syntax, and it is often not the model you had in mind.
The axioms of fields with characteristic $0$ have the model $\mathbb{Q}$, but they decide neither $\exists x \, (x \cdot x = 1 + 1)$ nor its negation.
Lindenbaum's lemma may put that sentence into $\Delta$, and then the Henkin model is a field with a square root of $2$, so it is not $\mathbb{Q}$.
The theorem promises some model, not a particular one.

### Generalizations

For formulas with free variables, replace the free variables by new constants; a consistent set of formulas then has a structure and an assignment that satisfy it.
In a language without equality, the term model needs no quotient, and the bound on the size is the same.
Many-sorted logic and the theory of types with general models have the same theorem, with the same Henkin proof.

For a consistent, computably axiomatized theory $T$, the Henkin construction can be carried out inside Peano arithmetic.
It gives a model of $T$ whose relations are defined by arithmetical formulas, of complexity $\Delta_2$, though in general not computable.
The theorem fails for [[second-order logic|G6X7SZSNC5]] with full semantics: no sound and effective proof system makes every consistent set satisfiable.

### Try it

First, show that the group axioms do not derive $\forall x \, (x \cdot x = e)$.
The group $\mathbb{Z}/3\mathbb{Z}$ is a model in which $1 + 1 = 2 \ne 0$, so the sentence fails there.

Second, a consistent theory $T$ in a language with $\aleph_1$ symbols has a model of what size at most?
Part 2 gives at most $\aleph_1 + \aleph_0 = \aleph_1$ elements.

## History

Kurt Gödel proved the completeness theorem for countable languages in his dissertation of 1929, published in 1930.
Leon Henkin published the model existence form and its proof by witness constants in 1949.
His proof works for languages of any cardinality and gives the bound on the size of the model.
Anatoly Malcev had already proved the compactness theorem for uncountable languages in 1936.

## Explanations

### L1 human

A list of axioms is consistent when no proof from it reaches a contradiction.
The theorem says that every such list describes some world in which all the axioms are true.
So "no contradiction can be proved" and "there is an example" mean the same thing.
For example, the axioms of a group with an element of order $3$ are consistent, and the group $\mathbb{Z}/3\mathbb{Z}$ satisfies them.

### L2 human

Here is a typical use, in a question about orders.
Let $\Gamma$ be the axioms of a linear order, and ask whether $\Gamma$ derives "between any two different elements there is a third".
The integers with their usual order satisfy $\Gamma$, and nothing lies strictly between $0$ and $1$, so the sentence fails in a model.
So $\Gamma$ does not derive it.
Now ask whether $\Gamma$ derives "if $x < y$ and $y < z$, then not $z < x$".
Every linear order satisfies this sentence, because $x < y < z$ gives $x < z$ by transitivity, and $z < x$ would contradict asymmetry.
So the sentence is a consequence of $\Gamma$, and part 3 says that a derivation exists, even though we did not write one.
The lesson is that models refute derivability, and the theorem turns "true in every model" into derivability.

### L3 human

Part 1 says that the syntactic notion of consistency and the semantic notion of satisfiability coincide for first-order logic.
In algebraic terms, the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of a consistent theory has an ultrafilter that respects the quantifiers, and that ultrafilter gives a model.
By [[Lindström's theorem|FYZ3CJGZYV]], first-order logic is the largest regular logic with compactness and the downward Löwenheim-Skolem property, and both properties follow from parts 1 and 2.
The arithmetized form is a tool in the study of models of arithmetic, next to the [[incompleteness theorems|X9WYNYE29C]].

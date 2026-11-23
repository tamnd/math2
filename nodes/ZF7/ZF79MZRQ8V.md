---
tag: ZF79MZRQ8V
kind: statement
role: theorem
name: Decidable prefix classes
aliases: [classical-decision-problem, bernays-schonfinkel-ramsey-class, ackermann-class, godel-kalmar-schutte-class, prefix-classes-of-first-order-logic]
msc: ["03B25", "03B10"]
topics: [E4AVTNWE9E]
audience: research
uses: [CS82V969DE, QN7M1JCGT9, VA6BNNY2YC, AS0NHQMAKA, 983GZBQYT4]
about: [086QKPF0A6, QN7M1JCGT9]
history:
  first_stated: "1928"
  notes: Bernays and Schönfinkel (1928) and Ackermann (1928) solved the first prefix classes; Ramsey (1930) added equality to the class with prefix ∃*∀*; the classification was completed with the undecidability results of Kahr, Moore and Wang (1962) and Goldfarb (1984), and is presented in the book The Classical Decision Problem of Börger, Grädel and Gurevich (1997).
sources:
  - url: https://en.wikipedia.org/wiki/Bernays%E2%80%93Sch%C3%B6nfinkel_class
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Entscheidungsproblem
    locator: Negative answer
---

## Statement

The order of the quantifiers at the front of a sentence decides whether a computer can test the sentence for a model.
For example, $\exists x \, \forall y \, (R(x, y) \wedge \neg R(y, y))$ has its "there is" before its "for all", and we can decide it by looking at one-element structures only.

A prefix is a word over the alphabet $\{ \exists, \forall \}$.
For a set $\Pi$ of prefixes, the prefix class $[\Pi]$ is the set of first-order sentences in [[prenex normal form|CS82V969DE]] $Q_1 x_1 \cdots Q_l x_l \, \varphi$ such that $\varphi$ is quantifier-free, $Q_1 \cdots Q_l \in \Pi$, and the signature has relation symbols only.
We write $\exists^*$ for any number of $\exists$, and $\forall^2$ for $\forall \forall$.

1. Bernays-Schönfinkel-Ramsey class.
   Let $\sigma = \exists x_1 \cdots \exists x_m \, \forall y_1 \cdots \forall y_n \, \varphi$ be in $[\exists^* \forall^*]$, with or without equality.
   If $\sigma$ has a model, then $\sigma$ has a model with at most $\max(m, 1)$ elements.
   So [[satisfiability|QN7M1JCGT9]] in $[\exists^* \forall^*]$ is decidable.
2. Ackermann class.
   Satisfiability in $[\exists^* \forall \exists^*]$ without equality is decidable, and each satisfiable sentence of the class has a finite model.
3. Gödel-Kalmár-Schütte class.
   Satisfiability in $[\exists^* \forall^2 \exists^*]$ without equality is decidable, and each satisfiable sentence of the class has a finite model.
4. Classification without equality.
   Let $p$ be a prefix.
   If $p$ matches $\exists^* \forall^*$, $\exists^* \forall \exists^*$ or $\exists^* \forall^2 \exists^*$, then $[p]$ is decidable.
   Otherwise $p$ contains $\forall \exists \forall$ or $\forall^3 \exists$ as a subsequence, and $[p]$ is undecidable.

The [[proof|3BB4TKGPCY]] proves part 1, and it derives part 4 from parts 1 to 3 and the undecidability of $[\forall \exists \forall]$ and $[\forall^3 \exists]$.
Parts 2 and 3 and these two results are cited.

## Remarks

### A first decision by hand

Take $\sigma = \exists x \, \exists y \, \forall z \, (P(x) \wedge \neg P(y) \wedge (R(z, x) \to P(z)))$.
The prefix is $\exists^2 \forall$, so $m = 2$, and part 1 says that we only need to try domains with 1 or 2 elements.
One element cannot work, because $x$ and $y$ would be the same element, and $P(x) \wedge \neg P(y)$ would fail.
So try the domain $\{a, b\}$ with $P = \{a\}$, $R = \emptyset$, $x = a$ and $y = b$.
Then $P(a)$ and $\neg P(b)$ hold, and $R(z, a) \to P(z)$ holds for every $z$ because $R$ is empty.
Check: both values $z = a$ and $z = b$ make the matrix true, so $\sigma$ is satisfiable.

The search is finite because the existential witnesses alone already form a model.
That is the whole idea of part 1, and the [[proof|3BB4TKGPCY]] makes it exact.

### Why each hypothesis is needed

The signature must have no function symbols.
The sentence $\forall x \, \forall y \, (f(x) = f(y) \to x = y) \wedge \forall x \, (f(x) \neq c)$ has the prefix $\forall^2$ after prenexing.
It has only infinite models, because $f$ is injective and misses the value of $c$.
With relation symbols only, a sentence with prefix $\forall^2$ lies in $[\exists^* \forall^*]$ and has a one-element model if it has any model.

The order of the quantifiers matters.
The [[sentence with only infinite models|KH3ZG4RXAW]] says that $<$ is irreflexive, transitive and has no greatest element.
In prenex form its prefix is $\forall^3 \exists$, so a class of the form $[\forall^* \exists^*]$ does not have the finite model property.

For part 3, equality matters.
Goldfarb proved in 1984 that the class $[\forall^2 \exists]$ with equality is undecidable.
For part 1 it does not, since the bound $\max(m, 1)$ holds with or without equality.

### What it gives you

Validity of sentences in $[\forall^* \exists^*]$ is decidable.
A sentence $\sigma$ is valid exactly when $\neg \sigma$ has no model, and moving the negation inward turns $\neg \sigma$ into a sentence of $[\exists^* \forall^*]$.

In automated reasoning, the Bernays-Schönfinkel-Ramsey class is called effectively propositional logic.
A sentence of the class becomes a propositional formula when we put the witness constants in for the universal variables in every possible way.
With $m \ge 1$ witnesses and $n$ universal variables, there are $m^n$ such instances, a finite list.

Together with [[Church's theorem|VA6BNNY2YC]], part 4 marks the exact border between decidable and undecidable prefixes for sentences without equality and function symbols.

### The converse: decidability and finite models

Decidability and the finite model property are different things in general, but in part 4 they agree: each decidable class there has the finite model property.
The direction from finite models to decidability always works for a decidable class of sentences.
Finite satisfiability is computably enumerable, since we can search through finite structures.
Unsatisfiability is computably enumerable too, by the [[completeness theorem|WQ1ZE255SF]].
Running both searches side by side decides satisfiability.

So the undecidable classes of part 4 cannot have the finite model property.
This fits [[Trakhtenbrot's theorem|XP6FW2WDWT]], which says that finite satisfiability and satisfiability come apart for full first-order logic.

### Watch out

Prenex forms are not unique, and the choice changes the class.
The sentence $\forall x \, P(x) \wedge \exists y \, Q(y)$ can be written as $\exists y \, \forall x \, (P(x) \wedge Q(y))$, which is in $[\exists \forall]$, or as $\forall x \, \exists y \, (P(x) \wedge Q(y))$, which is in $[\forall \exists]$.
Pull the existential quantifiers out first when you want to use part 1.

A second slip is to read $\forall y \, \exists x \, R(x, y)$ as a member of the Bernays-Schönfinkel-Ramsey class.
Its prefix is $\forall \exists$, which matches the Ackermann pattern, not $\exists^* \forall^*$.

### Generalizations

The book of Börger, Grädel and Gurevich classifies prefix classes also by the number and arity of the relation symbols, with equality, and with function symbols.
Other decidable fragments are cut out by the number of variables, as in [[two-variable logic|S7C3C7DJRF]], or by guards, as in the [[guarded fragment|Y7YS1C3GAE]].
The [[monadic predicate calculus|SERN6CRVWW]] is decidable for every prefix, because a sentence with unary relation symbols only has the finite model property.

### Try it

Is $\exists x \, \forall y \, (R(x, y) \to R(y, x))$ satisfiable?
Yes: here $m = 1$, and the one-element structure with $R$ empty is a model, since the implication has a false premise.

Which pattern of part 4 does the prefix $\exists \forall \forall \exists \exists$ match?
It is $\exists^1 \forall^2 \exists^2$, so it lies in the Gödel-Kalmár-Schütte class, and its class is decidable without equality.

## History

Bernays and Schönfinkel proved the decidability of the class $[\exists^* \forall^*]$ without equality in 1928, and Ackermann proved the decidability of his class in the same year.
Ramsey extended the first result to sentences with equality in 1930, and [[Ramsey's theorem|00TQV3F5S4]] in combinatorics first appeared in that paper.
Gödel, Kalmár and Schütte proved the decidability of the class $[\exists^* \forall^2 \exists^*]$ without equality in the early 1930s.
Gödel had stated that the result extends to equality, and Goldfarb showed in 1984 that it does not.
Kahr, Moore and Wang proved in 1962 that $[\forall \exists \forall]$ is undecidable, with a coding of tiling problems.

## Explanations

### L1 human

A logical sentence often starts with a row of quantifiers, such as "there is, for all, there is".
The order of these words decides whether a computer can always tell if the sentence can be true.
If every "there is" comes before every "for all", the test is short.
With two "there is" words, we only need to try worlds with one or two objects.
For other orders, such as "for all, there is, for all", no computer program can decide every sentence.

### L2 human

We decide the satisfiability of $\sigma = \exists x \, \forall y \, (R(x, y) \wedge \neg R(y, y))$.
The prefix is $\exists \forall$, so $\sigma$ is in the Bernays-Schönfinkel-Ramsey class with $m = 1$.
By part 1, if $\sigma$ has a model, it has a model with one element, so we check the one-element structures.
In the domain $\{a\}$ both variables take the value $a$, and the matrix becomes the following formula:
$$R(a, a) \wedge \neg R(a, a).$$
It is false whatever $R$ is.
So no one-element structure is a model, and $\sigma$ is unsatisfiable.
Check: in any model with witness $a$ for $x$, the choice $y = a$ gives both $R(a, a)$ and $\neg R(a, a)$.

The typical use is a sentence whose universal part speaks about a fixed finite set of named objects, as in a database or a planning problem.
Watch out: the sentence $\forall y \, \exists x \, R(x, y)$ has prefix $\forall \exists$, and part 1 does not apply to it.

### L3 human

The classical decision problem asks, for each natural class of first-order sentences, whether satisfiability is decidable.
For prefix classes without equality and function symbols, part 4 gives a clean answer, with three largest decidable classes and two smallest undecidable ones.
Decidability proofs go through the finite model property, often with a combinatorial argument such as Ramsey's theorem.
Undecidability proofs code Turing machines or tiling problems, as in [[Wang tile undecidability|AJH5HPD2B7]].
The same pattern appears for [[two-variable logic|S7C3C7DJRF]], the [[guarded fragment|Y7YS1C3GAE]] and modal logics, where decidability comes with a small model property or a tree model property.

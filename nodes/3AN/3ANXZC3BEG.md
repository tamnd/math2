---
tag: 3ANXZC3BEG
kind: concept
name: Recursively axiomatizable theory
msc: ["03B25", "03D35"]
topics: [FBWW4J1XWG]
audience: grad
uses: [92SWXST1ZM, DKFGQTRYZE, PPGD5KW8JC, TN9G24VABN, MFJXPAF0R0, WQ1ZE255SF, 655K8Y7VS8]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section R
    note: adopted
    mention: wikipedia://en/76765067#SYU8
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: Decidability of a theory
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: Semidecidability
  - book: isbn:9780122384523
    locator: Section 2.6
inventory: [AC1W7794JJ]
---

## Summary

The theory of groups has three axioms, so a computer can tell at once whether a given sentence is one of them.
A theory is recursively axiomatizable when it has a set of axioms with this property, and then a computer can check every proof in the theory and list all its theorems.

Fix a countable signature $L$ whose symbols are coded by natural numbers, so that each string of symbols has a [[Gödel number|MFJXPAF0R0]].
A set of strings is decidable when the set of their Gödel numbers is a [[computable set|PPGD5KW8JC]].
A [[theory|92SWXST1ZM]] $T$, that is, a set of $L$-[[sentences|DKFGQTRYZE]], is recursively axiomatizable when some decidable set $\Sigma$ of $L$-sentences has the same theorems as $T$:
$$\Sigma \vdash \sigma \iff T \vdash \sigma \quad \text{for every } L\text{-sentence } \sigma.$$
Such a set $\Sigma$ is a recursive axiomatization of $T$.
By [[Craig's theorem|6AN62NQ8AN]], $T$ is recursively axiomatizable if and only if its set of theorems is [[computably enumerable|TN9G24VABN]].

## Motivation

A proof is only useful when a reader can check it.
In a Hilbert system, a derivation from $\Sigma$ is a finite list of formulas, and each entry is a logical axiom, a member of $\Sigma$, or the result of modus ponens on two earlier entries.
To check the list, the reader must be able to tell whether a formula belongs to $\Sigma$.
For the group axioms this is a comparison with three strings, and for Peano arithmetic it is a test of the shape of a formula.
For the set of all sentences true in $\mathbb{N}$, no such test exists.

The notion therefore separates the theories whose proofs a machine can check from all the others.
It is the hypothesis of [[Gödel's incompleteness theorems|X9WYNYE29C]], and it is the first thing to check in any proof that a theory is decidable or undecidable.
Later it returns in the study of [[decidable theories|HWC687ES0Q]].

## Notation

We write $\Sigma \vdash \sigma$ for derivability in the Hilbert system and $\Sigma \models \sigma$ for [[logical consequence|1HK0VYWTV7]].
By the [[soundness theorem|AVD7T7J063]] and [[Gödel's completeness theorem|WQ1ZE255SF]], the two relations agree.
We write $\operatorname{Thm}(\Sigma)$ for the set of sentences derivable from $\Sigma$; Enderton writes $\operatorname{Cn} \Sigma$.
Enderton calls a theory only a set closed under consequence, and calls $T$ axiomatizable when $T = \operatorname{Cn} \Sigma$ for a decidable $\Sigma$.
Other names are effectively axiomatizable, computably axiomatizable and recursively axiomatized.
"Recursive" is the older word for "computable".

## Remarks

### First examples

The [[theory of groups|WHW13HJB3F]] has three axioms, and every finite set of strings is decidable by comparison.
[[Peano arithmetic|4HDC97G2E9]] has infinitely many induction axioms, but a program can test whether a sentence has the shape of an induction axiom.
[[Zermelo-Fraenkel set theory|0HE5WDQ9FJ]] with choice works the same way: its schemas of separation and replacement are infinite, and membership is a test of shape.
The empty theory has the decidable axiom set $\emptyset$, and its theorems are the valid sentences of $L$.
The theory of [[dense linear orders without endpoints|2W4S2H4VYA]] has six axioms and is complete.
[[Presburger arithmetic|4W0E9G7PPV]], the theory of $(\mathbb{N}, 0, 1, +)$, has a decidable set of axioms and is complete and decidable.

### Two non-examples

[[True arithmetic is not recursively axiomatizable|YSC90EM2M7]].
The set of sentences true in $(\mathbb{N}, 0, S, +, \cdot)$ is complete, and the first incompleteness theorem shows that no decidable set of axioms has exactly these theorems.

A second non-example needs no incompleteness.
Let $L = \{ 0, S, P \}$ with $P$ unary, let $A \subseteq \mathbb{N}$ be a set that is not computably enumerable, and let $T_A = \{ P \underline{n} : n \in A \}$.
The structure $(\mathbb{N}, 0, S, A)$ is a model of $T_A$ in which $P \underline{n}$ fails for $n \notin A$, so $T_A \vdash P \underline{n}$ exactly when $n \in A$.
If $T_A$ had a recursive axiomatization, its theorems would be computably enumerable, as shown below, and so $A$ would be too.

### Proofs can be checked by a machine

A finite axiom set is decidable: compare the input with each axiom, symbol by symbol.
The logical axioms of the Hilbert system also form a decidable set.
A parser decides whether a string is a formula or a sentence.
A tautology is recognized by its truth table, and each quantifier axiom is recognized by comparing its parts.
So, for a decidable $\Sigma$, a program can decide whether a finite list of formulas is a derivation from $\Sigma$: it checks each entry against $\Sigma$, the logical axioms and modus ponens, and there are finitely many entries.

### Theorems can be listed

If $\Sigma$ is a recursive axiomatization of $T$, then $\operatorname{Thm}(T)$ is computably enumerable.
A program runs through all finite lists of strings in order of their Gödel numbers.
For each list it tests, as above, whether the list is a derivation from $\Sigma$, and if so it prints the last line.
Every printed sentence is a theorem, and every theorem has a derivation that the program reaches after finitely many steps.

With $\Sigma = \emptyset$ this lists the valid sentences of $L$, by the completeness theorem.
For some finite signatures that set is not decidable, by [[Church's theorem|VA6BNNY2YC]], so "listable" cannot be improved to "decidable".

### Complete theories are decidable

Suppose $T$ is recursively axiomatizable and [[complete|655K8Y7VS8]]: for every sentence $\sigma$, $T \vdash \sigma$ or $T \vdash \neg \sigma$.
Then $\operatorname{Thm}(T)$ is decidable.
If $T$ is inconsistent, every sentence is a theorem, and the parser decides the set.
If $T$ is consistent, run the listing program until $\sigma$ or $\neg \sigma$ appears; one of them does, by completeness.
Answer "yes" if $\sigma$ appears and "no" if $\neg \sigma$ appears, and the answer is right because $T$ does not prove both.
We need not know which case holds to know that a deciding program exists.

The converse of the listing result is [[Craig's theorem on axiomatizability|6AN62NQ8AN]]: if $\operatorname{Thm}(T)$ is computably enumerable, then $T$ is recursively axiomatizable.
A recursively axiomatizable theory need not be decidable: the theory of groups and Peano arithmetic are undecidable, so by the result above neither is complete.

### History

In 1936 Church and Turing gave precise definitions of an algorithm, and these made the notion of a decidable set of axioms exact.
Gödel's first incompleteness theorem of 1931 is the main theorem about recursively axiomatizable theories that contain enough arithmetic.
William Craig proved in 1953 that every theory with a computably enumerable set of theorems has a decidable set of axioms.

### Watch out

Decidable axioms do not give decidable theorems.
The axioms of Peano arithmetic form a decidable set, but its set of theorems is not decidable.

The result on complete theories needs both hypotheses.
True arithmetic is complete but undecidable, because it is not recursively axiomatizable.
The theory of groups is recursively axiomatizable but undecidable, because it is not complete.

A complete theory, which decides each sentence, is a different idea from the completeness theorem, which says that $\models$ and $\vdash$ agree; see [[completeness versus incompleteness|28AX3A4N86]].

### Try it

First, is the theory with the infinitely many axioms $\lambda_n$, "there are at least $n$ elements", recursively axiomatizable?
Yes: a program builds $\lambda_n$ for the $n$ read off the input and compares the two strings.

Second, a theory is complete and its theorems are computably enumerable; is it decidable?
Yes: by Craig's theorem it is recursively axiomatizable, and complete recursively axiomatizable theories are decidable.

## Explanations

### L1 human

A theory is a collection of starting facts, called axioms, together with everything that follows from them by logic.
A recursively axiomatizable theory is one where a computer can tell whether a given sentence is an axiom.
The rules of a group are only three sentences, so a computer compares a sentence with these three.
Then a computer can also check any written proof, line by line, and it can list all the theorems, one after the other, without end.
It may still be impossible to decide whether a given sentence is a theorem, because the sentence may never appear in the list.

### L2 human

We show that the theory $\mathrm{DLO}$ of dense linear orders without endpoints is decidable.
Its six axioms in the signature $\{ < \}$ say that $<$ is irreflexive, transitive and total, that it is dense, and that there is no least and no greatest element.
The axiom set is finite, so it is decidable, and $\mathrm{DLO}$ is recursively axiomatizable.
$\mathrm{DLO}$ is consistent, since $(\mathbb{Q}, <)$ is a model, and it is complete by the Łoś-Vaught test, as the example [[dense linear order|2W4S2H4VYA]] shows.
So a program decides each sentence $\sigma$ by listing theorems until $\sigma$ or $\neg \sigma$ appears.
For example, $\forall x \exists y \, (x < y)$ appears, because it is an axiom, and $\exists x \forall y \, \neg (y < x)$ never appears, because its negation is a theorem.

The typical use is a proof of decidability: find a decidable set of axioms, then prove completeness by a model-theoretic method.
Watch out: for the theory of groups, the same program waits forever on $\forall x \forall y \, (x \cdot y = y \cdot x)$, because neither it nor its negation is a theorem.

### L3 human

In the [[arithmetical hierarchy|7CVJCQKY41]], the theorems of a recursively axiomatizable theory form a $\Sigma^0_1$ set, and by Craig's theorem every $\Sigma^0_1$ theory has this form.
A complete one is $\Delta^0_1$, that is, computable.
The set of sentences true in $\mathbb{N}$ is not even arithmetical, by [[Tarski's undefinability theorem|YRV6SYK2BY]].
The proof of [[Lindenbaum's lemma|SC0BSJ3GT6]] can be run with an oracle for $\operatorname{Thm}(T)$, so every consistent recursively axiomatizable theory has a complete consistent extension computable from the halting set.
Gödel and Rosser showed that for theories that contain Robinson arithmetic, such an extension is never itself recursively axiomatizable.
The same notion makes sense for every logic with a decidable set of formulas and a decidable proof relation.

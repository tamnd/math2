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

Fix a countable signature $L$ whose symbols are coded by natural numbers, so that each string of symbols has a [[Gödel number|MFJXPAF0R0]].
A set of strings is decidable when the set of their Gödel numbers is a [[computable set|PPGD5KW8JC]].
A [[theory|92SWXST1ZM]] $T$, a set of $L$-[[sentences|DKFGQTRYZE]], is recursively axiomatizable when there is a decidable set $\Sigma$ of $L$-sentences with the same theorems as $T$.
This means that $\Sigma \vdash \sigma$ if and only if $T \vdash \sigma$, for every $L$-sentence $\sigma$.
Such a set $\Sigma$ is a recursive axiomatization of $T$.
The idea matters because a proof from $\Sigma$ can be checked by a machine, so the theorems of $T$ can be listed by a machine, and Gödel's incompleteness theorems are about such theories.

## Motivation

A proof is useful only when a reader can check it.
In the Hilbert system $H$ of Enderton, a derivation from $\Sigma$ is a finite list of formulas.
Each entry is a logical axiom, a member of $\Sigma$, or follows from two earlier entries by modus ponens.
To check a derivation, the reader must be able to tell whether a given formula belongs to $\Sigma$.
For the group axioms this is a comparison with three strings.
For the axioms of Peano arithmetic it is a test of the shape of a formula.
For the set of all sentences true in $\N$ no such test exists.
The notion of a recursively axiomatizable theory separates the theories whose proofs can be checked by a machine from the other theories.

## Notation

We write $\Sigma \vdash \sigma$ for derivability in the Hilbert system $H$ and $\Sigma \models \sigma$ for [[logical consequence|1HK0VYWTV7]].
By the [[soundness theorem|AVD7T7J063]] and [[Gödel's completeness theorem|WQ1ZE255SF]], the two relations agree.
We write $\operatorname{Thm}(\Sigma)$ for the set of sentences $\sigma$ with $\Sigma \vdash \sigma$; Enderton writes $\operatorname{Cn} \Sigma$.
Here a theory is any set of sentences, and its theorems are its consequences.
Enderton calls a theory only a set of sentences closed under consequence, and he calls $T$ axiomatizable when $T = \operatorname{Cn} \Sigma$ for a decidable $\Sigma$.
Other names in the literature are effectively axiomatizable, computably axiomatizable and recursively axiomatized.
Some books ask only for a [[computably enumerable|TN9G24VABN]] set of axioms; by [[Craig's theorem|6AN62NQ8AN]] this gives the same class of theories.
The word "recursive" means computable here, as in the older name "recursive set".

## Remarks

### Examples

1. The [[theory of groups|WHW13HJB3F]]: its three axioms form a finite set, and every finite set of strings is decidable.
2. [[Peano arithmetic|4HDC97G2E9]]: the induction schema has infinitely many instances, but a program tests whether a sentence has the shape of an instance.
3. The empty theory: its theorems are the valid sentences of $L$, and $\emptyset$ is a decidable set of axioms.
4. [[Zermelo-Fraenkel set theory|0HE5WDQ9FJ]] with choice: the schemas of separation and of replacement are infinite, but membership in each schema is a test of shape.
5. The theory of dense linear orders without endpoints: it has finitely many axioms, and it is [[complete|655K8Y7VS8]] by the example [[dense linear order|2W4S2H4VYA]].
6. [[Presburger arithmetic|B66JYY3K58]], the theory of $(\N, 0, 1, +)$: it has a decidable set of axioms, and it is complete and decidable.

### Non-examples

1. [[True arithmetic is not recursively axiomatizable|YSC90EM2M7]]. The set $\operatorname{Th}(\N, 0, S, +, \cdot)$ of sentences true in $\N$ is complete, and by the first incompleteness theorem no decidable set of axioms has exactly these theorems.
2. Let $L = \set{0, S, P}$ with $P$ a unary relation symbol, let $A \subseteq \N$ be a set that is not computably enumerable, and let $T_A = \set{P \underline{n} : n \in A}$, where $\underline{n}$ is the numeral $S \cdots S 0$. The structure $(\N, 0, S, A)$ shows that $T_A \vdash P \underline{n}$ only for $n \in A$. So $n \in A$ if and only if $P \underline{n} \in \operatorname{Thm}(T_A)$. If $T_A$ were recursively axiomatizable, property 3 below would make $\operatorname{Thm}(T_A)$, and so $A$, computably enumerable.

### Basic properties

Property 1: A finitely axiomatizable theory is recursively axiomatizable.

1. Let $\Sigma = \set{\sigma_1, \dots, \sigma_k}$ be a finite set of axioms for $T$.
2. To decide whether a string $\tau$ lies in $\Sigma$, compare $\tau$ with $\sigma_1, \dots, \sigma_k$ symbol by symbol. This takes finitely many steps and always stops.

Property 2: The set $\Lambda$ of logical axioms of $H$ and the set of derivations from a decidable $\Sigma$ are decidable.

1. The sets of terms, formulas and sentences are decidable: a parsing program reads a string and checks the formation rules, and it checks which variables occur free.
2. Each logical axiom of $H$ is a generalization $\forall x_1 \cdots \forall x_m \, \alpha$ where $\alpha$ is an instance of one of six schemas. A string has only finitely many such prefixes, so we try each one.
3. A tautology is recognized by a truth table over its finitely many prime formulas. Each of the other five schemas is recognized by comparing the parts of $\alpha$; for the schema $\forall x \, \alpha \to \alpha^x_t$, either $x$ is not free in $\alpha$ and the consequent must equal $\alpha$, or $t$ is a subterm of the consequent. So only finitely many terms $t$ need to be tested.
4. A finite list $(\varphi_1, \dots, \varphi_n)$ is a derivation from $\Sigma$ when each $\varphi_i$ lies in $\Lambda \cup \Sigma$ or comes from $\varphi_j$ and $\varphi_k = (\varphi_j \to \varphi_i)$ with $j, k < i$. Each test is decidable by step 3 and by the hypothesis on $\Sigma$, and there are finitely many tests.

Property 3: If $T$ is recursively axiomatizable, then $\operatorname{Thm}(T)$ is a computably enumerable set.

1. Let $\Sigma$ be a recursive axiomatization of $T$. Then $\operatorname{Thm}(T) = \operatorname{Thm}(\Sigma)$ by the definition.
2. A program lists all finite lists of strings, in order of their Gödel numbers. This is possible because $L$ is coded by natural numbers.
3. For each list, the program tests whether it is a derivation from $\Sigma$, by property 2. When it is one and its last entry is a sentence, the program outputs that last entry.
4. Each output is a theorem of $\Sigma$. Each theorem $\sigma$ of $\Sigma$ has a derivation, and this derivation appears in the list after finitely many steps, so $\sigma$ is output.

Property 4: The set of valid $L$-sentences is computably enumerable.

1. Apply property 3 to the empty theory, with the decidable axiom set $\emptyset$. So $\operatorname{Thm}(\emptyset)$ is computably enumerable.
2. By the soundness theorem and Gödel's completeness theorem, $\vdash \sigma$ if and only if $\models \sigma$. So $\operatorname{Thm}(\emptyset)$ is the set of valid sentences.
3. For some finite signatures this set is not decidable, by [[Church's theorem|VA6BNNY2YC]]. So property 3 cannot be improved to "decidable".

Property 5: A complete recursively axiomatizable theory $T$ is decidable: $\operatorname{Thm}(T)$ is a computable set.

1. Here complete means that for every sentence $\sigma$, $T \vdash \sigma$ or $T \vdash \neg \sigma$.
2. Case 1: $T$ is inconsistent. Then every sentence is a theorem of $T$, and the set of sentences is decidable by property 2, step 1.
3. Case 2: $T$ is consistent. Given a string $\tau$, first test whether it is a sentence; if not, answer "no".
4. If $\tau$ is a sentence, run the program of property 3 until it outputs $\tau$ or $\neg \tau$. One of them is output after finitely many steps, by completeness.
5. Answer "yes" when $\tau$ appears and "no" when $\neg \tau$ appears. The answer "no" is correct, because a consistent theory does not prove both $\tau$ and $\neg \tau$.
6. In each case there is a program that decides $\operatorname{Thm}(T)$. We need not know which case holds to know that such a program exists.

Property 6: The converse of property 3 holds: if $\operatorname{Thm}(T)$ is computably enumerable, then $T$ is recursively axiomatizable.
This is [[Craig's theorem on axiomatizability|6AN62NQ8AN]].
So $T$ is recursively axiomatizable if and only if its theorems form a computably enumerable set.

Property 7: A recursively axiomatizable theory need not be decidable.
The theory of groups and Peano arithmetic are recursively axiomatizable and undecidable: see the [[elementary theory of groups|RX9MB386C5]] and [[Gödel's incompleteness theorems|X9WYNYE29C]].
By property 5, such a theory is not complete.

### History

In 1936 Church and Turing gave precise definitions of an algorithm, and these made the notion of a decidable set of axioms exact.
Gödel's first incompleteness theorem of 1931 is the main theorem about recursively axiomatizable theories that contain enough arithmetic.
William Craig proved in 1953 that every theory with a computably enumerable set of theorems has a decidable set of axioms.

### Common errors

1. Decidable axioms do not give a decidable theory. The axioms of Peano arithmetic form a decidable set, but the set of its theorems is not decidable.
2. Property 5 needs both hypotheses. True arithmetic is complete but not decidable, because it is not recursively axiomatizable.
3. A complete theory, which decides each sentence, is a different idea from the completeness theorem, which says that $\models$ and $\vdash$ agree; see [[completeness versus incompleteness|28AX3A4N86]].

## Explanations

### L1 human

A theory is a collection of starting facts, called axioms, and everything that follows from them by logic.
A recursively axiomatizable theory is one where a computer can tell whether a given sentence is an axiom.
For example, the rules of a group are only three sentences, so a computer compares a sentence with these three.
Then a computer can also check any written proof, line by line.
So a computer can list all theorems of the theory, one after the other, without end.
It may still be impossible for a computer to decide, for a given sentence, whether it is a theorem: the sentence may never appear in the list.

### L2 human

We show that the theory $\mathrm{DLO}$ of dense linear orders without endpoints is decidable.

1. $\mathrm{DLO}$ has six axioms in the signature $\set{<}$: irreflexivity, transitivity, totality, density, no least element and no greatest element.
2. The axiom set is finite, so it is decidable, by property 1.
3. $\mathrm{DLO}$ is complete, as shown in the example [[dense linear order|2W4S2H4VYA]] with the Łoś-Vaught test.
4. $\mathrm{DLO}$ is consistent, because $(\mathbb{Q}, <)$ is a model.
5. By property 5, a program decides each sentence $\sigma$: list the theorems until $\sigma$ or $\neg \sigma$ appears.
6. For example, $\forall x \exists y \, (x < y)$ appears, because it is an axiom, and $\exists x \forall y \, \neg (y < x)$ never appears, because its negation is a theorem.

The typical use of property 5 is to prove that a theory is decidable: first find a decidable set of axioms, then prove completeness by a model-theoretic method.
The trap is to forget the hypothesis of completeness.
For the theory of groups, the program of property 5 waits forever on the sentence $\forall x \forall y \, (x \cdot y = y \cdot x)$, because neither it nor its negation is a theorem.

### L3 human

In the language of the [[arithmetical hierarchy|7CVJCQKY41]], the set of theorems of a recursively axiomatizable theory is $\Sigma^0_1$, and by Craig's theorem every $\Sigma^0_1$ theory has this form.
A complete one is $\Delta^0_1$, that is, computable.
The set of sentences true in $\N$ is not even arithmetical, by [[Tarski's undefinability theorem|YRV6SYK2BY]].
The proof of [[Lindenbaum's lemma|SC0BSJ3GT6]] can be run with an oracle for $\operatorname{Thm}(T)$, so every consistent recursively axiomatizable theory has a complete consistent extension computable from the halting set.
Gödel's and Rosser's theorems say that for theories that contain Robinson arithmetic, such an extension is never itself recursively axiomatizable.
The same notion makes sense for every logic with a decidable set of formulas and a decidable proof relation, for example for propositional logic and for second-order logic with a fixed deductive system.

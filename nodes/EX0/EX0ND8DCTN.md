---
tag: EX0ND8DCTN
kind: concept
name: Inquisitive logic
aliases: [inquisitive-semantics, inqb, logic-of-questions]
msc: ["03B65", "03B20", "03B60"]
topics: [CQM9SRN8PM]
audience: research
uses: [09K9MWD2QQ, Q11N8X99FK]
sources:
  - url: https://en.wikipedia.org/wiki/Inquisitive_semantics
    locator: Basic notions
  - book: isbn:9780198814795
    locator: Ciardelli, Groenendijk and Roelofsen, Inquisitive Semantics
---

## Summary

The question "does it rain?" is settled by the information that it rains and by the information that it does not, but not by the information that it is cold.
Inquisitive logic is built on this idea: a formula is judged by the bodies of information that settle it, so questions and statements get meanings of the same kind.
Let $W$ be the set of valuations of a set of atoms of [[propositional logic|09K9MWD2QQ]], and call a set $s \subseteq W$ of worlds that are still possible an information state.
Support $s \models \varphi$ is defined by these clauses.

1. $s \models p$ when $w(p) = 1$ for every $w \in s$, and $s \models \bot$ when $s = \emptyset$.
2. $s \models \varphi \wedge \psi$ when $s \models \varphi$ and $s \models \psi$.
3. $s \models \varphi \vee \psi$ when $s \models \varphi$ or $s \models \psi$.
4. $s \models \varphi \to \psi$ when every $t \subseteq s$ with $t \models \varphi$ also has $t \models \psi$.

Negation is $\neg\varphi := \varphi \to \bot$, and the polar question "whether $p$" is $?p := p \vee \neg p$.
A formula is valid when every state supports it, and the valid formulas form the basic inquisitive logic $\mathsf{InqB}$.

## Motivation

In classical logic every formula denotes a set of worlds, the information it conveys.
A question such as "is it raining?" conveys no information, yet it is not trivial: it asks which of two sets of worlds holds.
Support semantics captures this by assigning to a formula the set of states that settle it.
A state settles $?p$ when it decides $p$ one way.
So the full state $W$ does not settle $?p$, although $?p$ is true at every world.
Entailment between questions then expresses dependency: knowing the answer to one question determines the answer to another.
This lets one logic treat questions and their dependencies with the same tools as statements and their consequences.

## Notation

We write $[\varphi] = \{s \subseteq W : s \models \varphi\}$ for the proposition expressed by $\varphi$, and $\mathrm{info}(\varphi) = \bigcup [\varphi]$ for its informative content.
The alternatives of $\varphi$ are the maximal elements of $[\varphi]$.
A formula is a statement when it has exactly one alternative, and it is inquisitive otherwise.
Truth at a world, written $w \models \varphi$, means $\{w\} \models \varphi$.
The formula $!\varphi := \neg\neg\varphi$ is the non-inquisitive projection of $\varphi$.

## Remarks

### A first model

Take two atoms $p$ and $q$, and write a world as $ab$, with $a$ the value of $p$ and $b$ the value of $q$.
Let $s = \{11, 00\}$, the state of someone who knows only that $p$ and $q$ have the same value.
The state does not support $?p$, since $11$ and $00$ disagree on $p$.
It does support $?p \to ?q$.
The substates that support $?p$ are $\emptyset$, $\{11\}$ and $\{00\}$, and each of them supports $?q$.
So $s$ answers neither question, but it knows that the answer to the first settles the second.
In general $s \models ?p \to ?q$ holds exactly when, among the worlds of $s$, the value of $q$ is a function of the value of $p$.

### Statements and questions

Every atom and every negation is a statement.
The polar question $?p$ has the two alternatives $|p|$ and $|\neg p|$, and its informative content is $W$, as [[the polar question|Y9CNKCV26N]] shows.
The disjunction $p \vee q$ has the two alternatives $|p|$ and $|q|$.
The state $|p| \cup |q|$ makes $p \vee q$ true at each of its worlds but does not support it, as [[inquisitive disjunction|XDZ6MRQD78]] shows.
Every formula is equivalent to a finite disjunction of negations $\neg\alpha_1 \vee \dots \vee \neg\alpha_n$, so every question is a disjunction of statements.

### The laws you can use

Support is persistent: if $s \models \varphi$ and $t \subseteq s$, then $t \models \varphi$.
The empty state supports every formula.
Truth at a world is classical, so $w \models \varphi$ holds exactly when $\varphi$ is true at $w$ in classical logic.
A state supports $\neg\varphi$ when no world of it makes $\varphi$ true, so it supports $\neg\neg\varphi$ when every world of it makes $\varphi$ true.
Ciardelli and Roelofsen axiomatized $\mathsf{InqB}$ as [[intuitionistic propositional logic|Q11N8X99FK]] plus the Kreisel-Putnam schema $(\neg\varphi \to \psi \vee \chi) \to (\neg\varphi \to \psi) \vee (\neg\varphi \to \chi)$ plus $\neg\neg p \to p$ for atoms $p$.
The logic is not closed under uniform substitution, as [[double negation and substitution|Z82FS0BX8G]] shows.
The formulas all of whose substitution instances are valid form Medvedev's logic of finite problems.

### What it is not

The meaning of $p \vee q$ is not its classical truth set $\{w : w \models p \vee q\}$.
It is the set of states included in $|p|$ or in $|q|$.
Inquisitive logic is not classical logic either, since $?p = p \vee \neg p$ is not valid.
It is not intuitionistic logic, since $\neg\neg p \to p$ is valid for every atom $p$.

### Watch out

The first trap is to read $\vee$ as classical disjunction.
Truth at a world is classical, but support is not, and $W \not\models p \vee \neg p$.
The second trap is to expect substitution instances of valid formulas to be valid.
The atomic law $\neg\neg p \to p$ is valid, but $\neg\neg ?p \to ?p$ is not.
The third trap is to identify support in a state with truth at all its worlds.
The two agree exactly for statements.

### History

Inquisitive semantics was developed by Ciardelli, Groenendijk, Mascarenhas and Roelofsen.
Ciardelli and Roelofsen published the axiomatization and the link with Medvedev's logic in "Inquisitive logic" (Journal of Philosophical Logic, 2011).
Ciardelli, Groenendijk and Roelofsen gave a book-length account in Inquisitive Semantics (Oxford University Press, 2019).
Earlier erotetic logics treated questions as sets of answers, while inquisitive logic makes questions formulas of the same language as statements.

### Try it

First, does the state $\{10, 01\}$ support $?p \to ?q$?
Among its worlds, $p = 1$ gives $q = 0$ and $p = 0$ gives $q = 1$, so the value of $q$ is a function of the value of $p$, and the answer is yes.

Second, does the state $\{11, 10\}$ support $?p \to ?q$?
The state itself supports $?p$, since $p$ is true at both worlds, but it does not support $?q$, so the answer is no.

## Explanations

### L1 human

A statement gives information, and a question asks for it.
Inquisitive logic gives both a meaning of the same kind.
The meaning of a sentence is the set of bodies of information that settle it.
"It rains" is settled by knowing that it rains.
"Does it rain?" is settled by knowing that it rains or by knowing that it does not.

### L2 human

Take one atom $p$ and the two worlds $w_1$, where $p$ is true, and $w_0$, where $p$ is false.
The states are $\emptyset$, $\{w_1\}$, $\{w_0\}$ and $W = \{w_0, w_1\}$.
The atom $p$ is supported by $\emptyset$ and $\{w_1\}$, and $\neg p$ is supported by $\emptyset$ and $\{w_0\}$.
So $?p = p \vee \neg p$ is supported by $\emptyset$, $\{w_1\}$ and $\{w_0\}$, but not by $W$.
Thus $?p$ is true at both worlds but is not valid, which makes it a question.
The typical use is to model what a question asks and which questions determine which.
Watch out: the implication clause quantifies over all substates, as in the Kripke semantics of intuitionistic logic, so it is not the material conditional.

### L3 human

The implication clause is the intuitionistic Kripke clause on states ordered by reverse inclusion.
The posets of nonempty subsets of a finite set are the Medvedev frames, and this explains why $\mathsf{InqB}$ lies between intuitionistic and classical logic.
The statements form a classical fragment, and questions are disjunctions of statements.
Entailment between questions is a form of dependency, related to dependence logic.
Inquisitive modal and first-order logics extend the approach to knowledge of answers and to "which" questions.

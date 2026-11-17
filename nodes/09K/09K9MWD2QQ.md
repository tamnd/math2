---
tag: 09K9MWD2QQ
kind: concept
name: Propositional calculus
aliases: [sentential-logic, propositional-logic, sentential-calculus, statement-calculus]
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
uses: [0ZGC7ZESYN, QS0XVAN9BG, 05RSK4Q657, 05006AJ7DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Propositional_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Propositional_logic
    locator: History
  - url: https://en.wikipedia.org/wiki/Propositional_logic
    locator: Proof systems
  - url: https://en.wikipedia.org/wiki/Paul_Bernays
    locator: Mathematical work
  - url: https://en.wikipedia.org/wiki/Emil_Leon_Post
    locator: Early work
  - book: isbn:9781482237726
    locator: Chapter 1
  - book: isbn:9780122384523
    locator: Chapter 1
same_as:
  wikidata: Q200694
  wikipedia: Propositional logic
---

## Summary

The classical propositional calculus is the formal system with three parts.
Its language is the set of [[propositional formulas|~7139c138]], built from propositional variables $p_0, p_1, \ldots$ with the connectives $\neg$, $\land$, $\lor$, $\to$ and $\leftrightarrow$.
Its semantics gives each formula a truth value $0$ or $1$ under each [[truth valuation|~41f42e3d]], computed from the values of the variables by the [[truth tables|05RSK4Q657]] of the connectives.
Its deductive part is a proof system, for example the [[Hilbert system|1MGMQX43B8]] $L$, that derives formulas from axioms by rules.
The semantic relation $\Gamma \models \varphi$ ([[logical consequence|1HK0VYWTV7]]) and the deductive relation $\Gamma \vdash \varphi$ (derivability) coincide, by the [[soundness theorem|~7a1817da]] and the [[completeness theorem|~e697b103]].
The propositional calculus is the simplest logic with a full metatheory, and it is the model on which first-order logic and the non-classical logics are built.

## Motivation

Some arguments are correct because of their form alone, whatever their sentences say.
"If it rains, the street is wet; it rains; so the street is wet" has the same form as "if $n$ is even, then $n^2$ is even; $n$ is even; so $n^2$ is even".
Both are correct for one reason: from a statement $p$ and the statement "if $p$ then $q$", the statement $q$ follows.
To study such forms precisely, we replace each simple statement by a letter and keep only the words "not", "and", "or", "if ... then" and "if and only if".
The result is a formal language with exact rules.
Two questions then arise: which formulas are true in every case, and which formulas can be proved from axioms.
The propositional calculus answers both questions, and it shows that the two answers agree.

## Notation

The variables are also called propositional letters, atoms or sentence letters; [[this page|AC4HD34AXX]] treats them.
Books write negation as $\neg p$, $\sim p$ or $\bar{p}$, conjunction as $p \land q$, $p \mathbin{\&} q$ or $p \cdot q$, implication as $p \to q$ or $p \supset q$, and the biconditional as $p \leftrightarrow q$ or $p \equiv q$.
In the Polish notation of Łukasiewicz the connectives are the prefix letters $N$, $K$, $A$, $C$ and $E$, for negation, conjunction, disjunction, implication and equivalence.
The symbol $\models$ (double turnstile) marks the semantic relation, and the symbol $\vdash$ ([[turnstile|2QQMJMS8M5]]) marks derivability.
The arrow $\Rightarrow$ belongs to the [[metalanguage|D9G8M42GKC]] in many books, and the arrow $\to$ belongs to the formulas.
Other names for the subject are propositional logic, sentential logic, sentential calculus, statement calculus and zeroth-order logic.

## Remarks

### The language

A [[propositional formula|~7139c138]] is built from variables by the formation rules: if $\varphi$ and $\psi$ are formulas, then so are $(\neg \varphi)$, $(\varphi \land \psi)$, $(\varphi \lor \psi)$, $(\varphi \to \psi)$ and $(\varphi \leftrightarrow \psi)$.
The [[unique readability theorem|~26f00b05]] says that each formula is built in exactly one way.
Because of it, we can prove facts about all formulas by [[structural induction|12MQ2NJ29A]] and define functions on all formulas by recursion.
Some books use fewer primitive connectives, for example only $\neg$ and $\to$, and treat the others as abbreviations.

### The semantic side

A truth assignment gives each variable a value $0$ or $1$.
It extends in exactly one way to a [[truth valuation|~41f42e3d]] $\bar{v}$ on all formulas, by the truth tables of the connectives.
A formula is a [[tautology|05006AJ7DZ]] when every valuation gives it the value $1$, and it is [[satisfiable|QN7M1JCGT9]] when some valuation gives it the value $1$.
A formula $\varphi$ is a [[logical consequence|1HK0VYWTV7]] of a set $\Gamma$, written $\Gamma \models \varphi$, when every valuation that makes all members of $\Gamma$ true makes $\varphi$ true.
Normal forms ([[conjunctive|0B3D4C8YF2]] and [[disjunctive|0GVDFAY4KW]]) and [[functional completeness|TDZVCWYJ9F]] describe which truth functions formulas can express: all of them.

### The deductive side

A proof system fixes axioms and rules, and a derivation is a finite list of formulas built by these rules.
This sub-area uses the [[Hilbert system|1MGMQX43B8]] $L$ of Mendelson, with three axiom schemas and [[modus ponens|0Y0MQYST0M]].
We write $\Gamma \vdash \varphi$ when $\varphi$ has a derivation from the hypotheses $\Gamma$.
Other proof systems for the same logic are [[natural deduction|6KT3BJZ7D1]], the [[sequent calculus|W72CA3R9MP]], tableaux and [[resolution|~99ab3fe3]].
All of them derive the same formulas, because each is sound and complete for the same semantics.

### The metatheorems

- [[Soundness|~7a1817da]]: if $\Gamma \vdash \varphi$, then $\Gamma \models \varphi$.
- [[Completeness|~e697b103]]: if $\Gamma \models \varphi$, then $\Gamma \vdash \varphi$.
- [[Compactness|~205aa33d]]: a set of formulas is satisfiable if each of its finite subsets is satisfiable.
- The [[deduction theorem|9X08XK5RV2]]: $\Gamma \cup \set{\varphi} \vdash \psi$ if and only if $\Gamma \vdash \varphi \to \psi$.

### Decidability

The value of a formula depends only on the values of the variables that occur in it.
A formula with $n$ variables therefore has a truth table with $2^n$ rows, and the table decides whether the formula is a tautology.
So the set of tautologies is decidable, and by completeness the set of theorems of $L$ is decidable too.
The truth-table method takes time about $2^n$.
No method is known that decides tautologies in time polynomial in the length of the formula.
Deciding satisfiability is NP-complete by the [[Cook-Levin theorem|CTK8AH98Z1]], and deciding whether a formula is a tautology is coNP-complete; see the [[Boolean satisfiability problem|3QKF32ZAKN]].

### Place among logics

The propositional calculus is the part of [[first-order logic|086QKPF0A6]] without terms, predicates of positive arity and quantifiers.
It cannot express "all" or "some", so it cannot analyse an argument whose correctness depends on these words.
[[Intuitionistic logic|Q11N8X99FK]] has the same language and proves fewer formulas; it does not prove $p \lor \neg p$.
[[Many-valued logics|66NMTCQNQV]] keep the language and change the set of truth values.
Modal logics add new connectives, such as "necessarily", whose meaning is not a truth function.
Classical propositional logic is [[Post complete|WK2P0E82B4]]: adding any formula that is not a tautology as a new axiom schema makes the system inconsistent.

### Examples

- The formula $p \lor \neg p$ is a tautology: its truth table has the value $1$ in both rows.
- The argument from $p \to q$, $q \to r$ and $\neg r$ to $\neg p$ is valid; [[this example|~db2cac4f]] checks all eight rows of its truth table.
- A circuit of switches computes a formula, with switches in series for $\land$ and in parallel for $\lor$; [[this example|~43d769e4]] reads a staircase light as $(p \land q) \lor (\neg p \land \neg q)$.
- In the system $L$ the formula $p \to p$ has a derivation of five lines. It uses two instances of (A1), one instance of (A2) and modus ponens twice.

### Non-examples

- The syllogism "all humans are mortal; Socrates is a human; so Socrates is mortal" is valid, but not by its propositional form. Its three sentences are three unrelated variables, and the form $p, q \models r$ fails; see [[this non-example|~5ae88e68]].
- The sentence "necessarily $p$" is not a propositional formula in $p$. Its truth value is not a function of the truth value of $p$, so no truth table defines it.
- The question "is $7$ prime?" is not a [[proposition|0ZGC7ZESYN]], so no variable stands for it.

### Basic properties

- Each formula has a unique parse ([[unique readability|~26f00b05]]).
- Each truth assignment has a unique extension to all formulas ([[truth valuation|~41f42e3d]]).
- Each Boolean function of $n \geq 1$ arguments is defined by some formula in disjunctive normal form ([[disjunctive normal form|0GVDFAY4KW]]).
- $\Gamma \vdash \varphi$ if and only if $\Gamma \models \varphi$ (soundness and completeness).
- The set of tautologies is decidable by truth tables.

### History

The Stoic logician Chrysippus, in the 3rd century BC, is often credited with a deductive system for reasoning with connectives.
George Boole treated logic as algebra in 1847 and 1854, and Gottlob Frege gave the first axiomatic system with modus ponens in his Begriffsschrift of 1879.
Paul Bernays gave the first known proof of the completeness of the propositional part of Principia Mathematica in his habilitation thesis of 1918.
Emil Post proved the same result independently in 1921, with truth tables as his method.

### Common errors

- To confuse $\vdash$ with $\models$. The first is about derivations in a proof system, and the second is about truth under all valuations; completeness is the theorem that they agree.
- To read $p \to q$ as a claim that $p$ causes $q$. The material implication is false only when $p$ is true and $q$ is false.
- To think that a formula is true or false by itself. A formula with variables has a value only under a valuation; only tautologies and unsatisfiable formulas have one value under all valuations.

## Explanations

### L1 human

The propositional calculus is a small exact language for "not", "and", "or" and "if ... then".
Each simple statement becomes a letter, such as $p$ for "it rains" and $q$ for "the street is wet".
Each letter can be true or false, and a table tells whether a combined statement is true in each case.
With two letters there are four cases, and with three letters there are eight.
A statement that is true in every case, such as "it rains or it does not rain", is a law of logic.
There is also a way to prove such laws from a few starting laws, step by step.
The main result of the subject says that the provable statements are exactly the laws of logic.

### L2 human

We decide whether $\varphi = (p \to q) \to (\neg q \to \neg p)$ is a tautology.

1. The formula has two variables, $p$ and $q$, so its truth table has $2^2 = 4$ rows.
2. Row $p = 1$, $q = 1$: $p \to q = 1$, $\neg q = 0$, so $\neg q \to \neg p = 1$, and $\varphi = 1$.
3. Row $p = 1$, $q = 0$: $p \to q = 0$, so $\varphi = 1$, because an implication with a false antecedent is true.
4. Row $p = 0$, $q = 1$: $\neg q = 0$, so $\neg q \to \neg p = 1$, and $\varphi = 1$.
5. Row $p = 0$, $q = 0$: $p \to q = 1$, $\neg q = 1$, $\neg p = 1$, so $\neg q \to \neg p = 1$, and $\varphi = 1$.
6. All four rows give $1$, so $\varphi$ is a tautology.

By the completeness theorem, $\varphi$ is then also derivable in the system $L$, with no hypotheses.
The typical use of the calculus is this pair of views: we check a law by a table, and we know that a formal proof exists.
A trap is to think that the table is itself a derivation in $L$.
The table and the derivation are different objects, and a derivation that comes from a table is much longer than the table.

### L3 human

The propositional calculus is the base case of most of mathematical logic.
Its semantics is the two-element [[Boolean algebra|0XADJKM699]], and the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of its formulas modulo provable equivalence is the free Boolean algebra on the variables.
Completeness then says that a formula is provable exactly when it holds in every homomorphism to the two-element algebra, and compactness for uncountably many variables is equivalent to the [[Boolean prime ideal theorem|STPBXBKSZP]] over the axioms of set theory without choice.
First-order logic adds quantifiers, and its completeness and compactness theorems ([[Gödel's completeness theorem|WQ1ZE255SF]], [[the compactness theorem|1NR3HAWG9D]]) extend the propositional ones.
Herbrand's theorem reduces the validity of a first-order sentence to the search for a propositional tautology among finitely many of its instances.
On the computational side, the question whether tautologies have short proofs in some proof system is equivalent to the question whether NP equals coNP, and it is the subject of [[propositional proof complexity|CBAF7J051K]].

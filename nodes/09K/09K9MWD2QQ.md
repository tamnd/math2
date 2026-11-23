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

The propositional calculus is the logic of "not", "and", "or" and "if ... then", made into an exact formal system.
It has a language of formulas, a way to compute the truth value of each formula, and a way to prove formulas from axioms.
Its main theorem says that the provable formulas are exactly the formulas that are always true.

Here is the heart of the semantic side, the truth table of implication:
$$\begin{array}{cc|c} p & q & p \to q \\ \hline 1 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array}$$
The last two rows are the ones that surprise students: when $p$ is false, $p \to q$ is true, whatever $q$ is.

In full, the classical propositional calculus has three parts.
Its language is the set of [[propositional formulas|TT7WT5HPN9]], built from variables $p_0, p_1, \ldots$ with the connectives $\neg$, $\land$, $\lor$, $\to$ and $\leftrightarrow$.
Its semantics gives each formula a value $0$ or $1$ under each [[truth valuation|H31CS3HK5P]], computed by the [[truth tables|05RSK4Q657]] of the connectives.
Its deductive part is a proof system, such as the [[Hilbert system|1MGMQX43B8]] $L$, which derives formulas from axioms by rules.
The semantic relation $\Gamma \models \varphi$ of [[logical consequence|1HK0VYWTV7]] and the relation $\Gamma \vdash \varphi$ of derivability are equal, by the [[soundness theorem|XD629S54CS]] and the [[completeness theorem|81ZNY1XKYJ]].

## Motivation

Some arguments are correct because of their form alone.
"If it rains, the street is wet; it rains; so the street is wet" has the same form as "if $n$ is even, then $n^2$ is even; $n$ is even; so $n^2$ is even".
Both are correct for one reason: from $p$ and "if $p$ then $q$", the statement $q$ follows.
To study such forms exactly, we replace each simple statement by a letter and keep only the connecting words.

Two questions then arise.
Which formulas are true in every case, and which formulas can we prove from axioms by fixed rules?
The propositional calculus answers both, and the answers agree.
It is the smallest logic where this whole story can be told with full proofs, so it is the model for [[first-order logic|086QKPF0A6]] and for the non-classical logics.
It is also the language of digital circuits and of the SAT solvers that check hardware and software.

## Notation

Books write negation as $\neg p$, $\sim p$ or $\bar{p}$, conjunction as $p \land q$, $p \mathbin{\&} q$ or $p \cdot q$, implication as $p \to q$ or $p \supset q$, and the biconditional as $p \leftrightarrow q$ or $p \equiv q$.
In the Polish notation of Łukasiewicz the connectives are the prefix letters $N$, $K$, $A$, $C$ and $E$.
The double turnstile $\models$ marks the semantic relation, and the [[turnstile|2QQMJMS8M5]] $\vdash$ marks derivability.
The variables are also called propositional letters or atoms, and [[propositional variables|AC4HD34AXX]] treats them.
Watch out for the arrow $\Rightarrow$: many books use it in the [[metalanguage|D9G8M42GKC]], to talk about formulas, while $\to$ is a symbol inside formulas.
Other names for the subject are propositional logic, sentential logic and zeroth-order logic.

## Remarks

### Reading the table of implication

Why is $p \to q$ true when $p$ is false?
Think of $p \to q$ as a promise: "if you pass the exam, you get a prize".
The promise is broken only when you pass and get no prize, which is the row $p = 1$, $q = 0$.
If you fail the exam, the promise says nothing, so it is not broken, and logic counts an unbroken promise as true.

A mathematical case shows that this choice is the useful one.
We want "for every integer $n$, if $n > 2$ then $n^2 > 4$" to be true.
For $n = 1$ the instance is "if $1 > 2$ then $1 > 4$", with both parts false, and for $n = -3$ it is "if $-3 > 2$ then $9 > 4$", with a false first part and a true second part.
The general statement is true only if both instances count as true, and the table makes them true.

### The language and its meaning

A [[propositional formula|TT7WT5HPN9]] is built from variables by the rules: if $\varphi$ and $\psi$ are formulas, so are $(\neg \varphi)$, $(\varphi \land \psi)$, $(\varphi \lor \psi)$, $(\varphi \to \psi)$ and $(\varphi \leftrightarrow \psi)$.
The [[unique readability theorem|6KBJX91N7G]] says that each formula is built in exactly one way, so we can define functions on formulas by recursion and prove facts by [[structural induction|12MQ2NJ29A]].

A truth assignment gives each variable a value $0$ or $1$, and it extends in exactly one way to a [[truth valuation|H31CS3HK5P]] on all formulas.
A formula is a [[tautology|05006AJ7DZ]] when every valuation gives it $1$, and [[satisfiable|QN7M1JCGT9]] when some valuation gives it $1$.
For example, $p \lor \neg p$ is a tautology, $p \land \neg p$ is not satisfiable, and $p \to q$ is satisfiable but not a tautology, by its second row.
The [[normal forms|0GVDFAY4KW]] and [[functional completeness|TDZVCWYJ9F]] show that formulas can express every truth function.

### The deductive side

A proof system fixes axioms and rules, and a derivation is a finite list of formulas, each an axiom, a hypothesis or the result of a rule.
We use the [[Hilbert system|1MGMQX43B8]] $L$ of Mendelson, with three axiom schemas and [[modus ponens|0Y0MQYST0M]] as the only rule.
In $L$ the formula $p \to p$ has a derivation of five lines: two instances of the first axiom, one of the second, and two steps of modus ponens.
Other proof systems for the same logic are [[natural deduction|6KT3BJZ7D1]], the [[sequent calculus|W72CA3R9MP]], tableaux and [[resolution|ZDW6N1PGJ7]].
All of them prove the same formulas, because each is sound and complete for the same semantics.

### The four metatheorems

The theory of the calculus rests on four results about the whole system.

1. [[Soundness|XD629S54CS]]: if $\Gamma \vdash \varphi$, then $\Gamma \models \varphi$.
2. [[Completeness|81ZNY1XKYJ]]: if $\Gamma \models \varphi$, then $\Gamma \vdash \varphi$.
3. [[Compactness|4X9126SEMM]]: a set of formulas is satisfiable when each of its finite subsets is satisfiable.
4. The [[deduction theorem|9X08XK5RV2]]: $\Gamma \cup \{ \varphi \} \vdash \psi$ if and only if $\Gamma \vdash \varphi \to \psi$.

Soundness says that the rules never lead from truth to falsehood.
Completeness says that the rules are strong enough to reach every consequence.
Together they let you switch freely between a truth table and a proof.

### Deciding by truth tables

The value of a formula depends only on the variables that occur in it.
So a formula with $n$ variables has a truth table of $2^n$ rows, and checking all rows decides whether it is a tautology.
By completeness, the same table decides whether the formula is a theorem of $L$.
The table grows fast, though: $30$ variables already give more than a billion rows.
No method is known that decides tautologies in time polynomial in the length of the formula.
Satisfiability is NP-complete by the [[Cook-Levin theorem|CTK8AH98Z1]], and the tautology problem is coNP-complete; see the [[Boolean satisfiability problem|3QKF32ZAKN]].

### What it cannot express

The syllogism "all humans are mortal; Socrates is a human; so Socrates is mortal" is valid, but not because of its propositional form.
Its three sentences become three unrelated variables $p, q, r$, and $p, q \models r$ fails at $p = q = 1$, $r = 0$; see [[the Socrates non-example|EMK23RRKPR]].
The words "all" and "some" need [[first-order logic|086QKPF0A6]], of which the propositional calculus is the part without terms and quantifiers.
The sentence "necessarily $p$" is not a propositional formula either, because its truth value is not a function of the value of $p$.
A question such as "is $7$ prime?" is not a [[proposition|0ZGC7ZESYN]] at all, so no variable stands for it.

### Other logics with the same language

[[Intuitionistic logic|Q11N8X99FK]] has the same formulas and proves fewer of them; it does not prove $p \lor \neg p$.
[[Many-valued logics|66NMTCQNQV]] keep the language and change the set of truth values.
Modal logics add connectives such as "necessarily", which are not truth functions.
Classical propositional logic is [[Post complete|WK2P0E82B4]]: if we add as a new axiom schema any formula that is not a tautology, the system becomes inconsistent.

### Watch out

The most common slip is to confuse $\vdash$ with $\models$.
$\Gamma \vdash \varphi$ says that a derivation exists, and $\Gamma \models \varphi$ says that every valuation that makes $\Gamma$ true makes $\varphi$ true; completeness is the theorem that they agree, not a definition.
A second slip is to read $p \to q$ as "$p$ causes $q$".
"If $2 + 2 = 5$, then the moon is cheese" is true by the last row of the table, with no causal link at all.
A third slip is to call a formula true or false by itself: $p \to q$ has a value only under a valuation.

### History

The Stoic logician Chrysippus, in the third century BC, is often credited with a deductive system for reasoning with connectives.
George Boole treated logic as algebra in 1847 and 1854, and Gottlob Frege gave an axiomatic system with modus ponens in his Begriffsschrift of 1879.
Paul Bernays proved the completeness of the propositional part of Principia Mathematica in his habilitation thesis of 1918.
Emil Post proved the same result independently in 1921, by truth tables.

### Try it

Is $(p \to q) \lor (q \to p)$ a tautology?
Yes: if $q = 1$ the first disjunct is $1$, and if $q = 0$ the second disjunct is $1$, because its antecedent is false.

Find a valuation that makes $(p \to q) \to p$ false.
The formula is false only when $p = 0$ and $p \to q = 1$, and $p = 0$ already makes $p \to q$ true, so $p = 0$ with any $q$ works.

## Explanations

### L1 human

The propositional calculus is a small exact language for "not", "and", "or" and "if ... then".
Each simple statement becomes a letter, such as $p$ for "it rains" and $q$ for "the street is wet".
Each letter can be true or false, and a table tells whether a combined statement is true in each case.
With two letters there are four cases, and with three letters there are eight.
A statement that is true in every case, such as "it rains or it does not rain", is a law of logic.
There is also a way to prove such laws from a few starting laws, step by step, and the main result says that the provable statements are exactly the laws of logic.

### L2 human

We decide whether $\varphi = (p \to q) \to (\neg q \to \neg p)$ is a tautology.
It has two variables, so its table has four rows:
$$\begin{array}{cc|cccc|c} p & q & p \to q & \neg q & \neg p & \neg q \to \neg p & \varphi \\ \hline 1 & 1 & 1 & 0 & 0 & 1 & 1 \\ 1 & 0 & 0 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 1 & 1 & 1 \end{array}$$
Check: in the second row the antecedent $p \to q$ is $0$, so $\varphi$ is $1$ by the table of implication.
Every row gives $1$, so $\varphi$ is a tautology, and by the completeness theorem it also has a derivation in $L$ from no hypotheses.

The typical use of the calculus is this pair of views: we check a law by a table, and we know that a formal proof exists.
The trap is to think that the table is itself a derivation in $L$.
The table and the derivation are different objects, and a derivation built from a table by the completeness proof is much longer than the table.

### L3 human

The propositional calculus is the base case of most of mathematical logic.
Its semantics is the two-element [[Boolean algebra|0XADJKM699]], and the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of formulas modulo provable equivalence is the free Boolean algebra on the variables.
Completeness then says that a formula is provable exactly when every homomorphism to the two-element algebra sends it to $1$.
Compactness for uncountably many variables is equivalent, over set theory without choice, to the [[Boolean prime ideal theorem|STPBXBKSZP]].

First-order logic adds quantifiers, and [[Gödel's completeness theorem|WQ1ZE255SF]] and [[the compactness theorem|1NR3HAWG9D]] extend the propositional results.
Herbrand's theorem reduces the validity of a first-order sentence to a propositional tautology among finitely many of its instances.
On the computational side, some proof system gives every tautology a proof of polynomial length exactly when NP equals coNP, and this question drives [[propositional proof complexity|CBAF7J051K]].

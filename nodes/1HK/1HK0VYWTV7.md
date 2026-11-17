---
tag: 1HK0VYWTV7
kind: concept
name: Logical consequence
aliases: [semantic-consequence, entailment]
msc: ["03B05", "03B10"]
topics: [JDK63589SA]
audience: ug1
uses: [TT7WT5HPN9, H31CS3HK5P, 0NMG7W7Q11, FWHBT4HABW]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_consequence
    locator: Semantic consequence
  - url: https://en.wikipedia.org/wiki/Bernard_Bolzano
    locator: Logic
  - book: isbn:9780122384523
    locator: Chapter 1
same_as:
  wikidata: Q374182
  wikipedia: Logical consequence
---

## Summary

Let $\Gamma$ be a set of [[propositional formulas|TT7WT5HPN9]] and let $\varphi$ be a formula.
The formula $\varphi$ is a logical consequence of $\Gamma$, written $\Gamma \models \varphi$, when every truth assignment $v$ with $\bar v(\gamma) = 1$ for all $\gamma \in \Gamma$ also has $\bar v(\varphi) = 1$, where $\bar v$ is the [[truth valuation|H31CS3HK5P]] of $v$.
In first-order logic the definition is the same, with a [[structure|983GZBQYT4]] and an assignment of its elements to the variables in place of a truth assignment.
Logical consequence is the exact meaning of "the conclusion follows from the premises", and the proof systems of logic are judged by whether they capture it.

## Motivation

A mathematical argument starts from premises and ends with a conclusion.
We call the argument valid when the conclusion cannot be false while all the premises are true.
This depends only on the form of the sentences, and not on what they are about.
For example, "if $n$ is divisible by $4$, then $n$ is even; $n$ is divisible by $4$; so $n$ is even" is valid for every integer $n$.
It stays valid for every pair of statements put in the place of the two parts.
The propositional calculus makes "form" precise: we replace the parts by variables $p$ and $q$, and we check all ways to give truth values to $p$ and $q$.
Logical consequence is the relation that this check defines.
It is the semantic side of logic, and derivability $\Gamma \vdash \varphi$ in a proof system is the syntactic side.

## Notation

The symbol $\models$ is the double turnstile; the page [[turnstile|2QQMJMS8M5]] compares it with the single turnstile $\vdash$.
We write $\Gamma, \varphi \models \psi$ for $\Gamma \cup \set{\varphi} \models \psi$, and $\varphi_1, \ldots, \varphi_n \models \psi$ for $\set{\varphi_1, \ldots, \varphi_n} \models \psi$.
We write $\models \varphi$ for $\emptyset \models \varphi$; this says that $\varphi$ is true under every truth assignment, that is, $\varphi$ is a [[tautology|05006AJ7DZ]].
We write $\Gamma \not\models \varphi$ when $\varphi$ is not a logical consequence of $\Gamma$.
Other names are "semantic consequence", "entailment", and, in Enderton's book, "$\Gamma$ tautologically implies $\varphi$"; see [[tautological consequence|4N2HHE7PC1]].
The same symbol $\models$ also expresses satisfaction, as in $v \models \varphi$ or $\mathcal{M} \models \varphi$, so the reader must look at what stands on its left.
The symbols $\models$ and $\vdash$ are easy to confuse in print: $\models$ has two horizontal bars and speaks about truth, while $\vdash$ has one bar and speaks about derivations.

## Remarks

### Examples

- $p, \; p \to q \models q$. Of the four truth assignments to $p$ and $q$, only $p = q = 1$ makes both premises true, and it makes $q$ true. See [[this example|H8H9ZYZZEJ]].
- $p \lor q, \; \neg p \models q$. Only $p = 0$, $q = 1$ makes both premises true. See [[this example|V5H6FW6F9M]].
- $\models p \lor \neg p$. Every truth assignment makes $p \lor \neg p$ true, so the empty set of premises suffices.
- $p \land \neg p \models q$. No truth assignment makes $p \land \neg p$ true, so the condition of the definition holds for no assignment and fails for none.
- $\set{p_0} \cup \set{p_n \to p_{n+1} : n \ge 0} \models p_{17}$. A truth assignment that makes all premises true has $v(p_0) = 1$, and then $v(p_n) = 1$ for each $n$ by [[induction|0ASJVEFA9J]] on $n$.

### Non-examples

- $p \to q, \; q \not\models p$. The assignment $p = 0$, $q = 1$ makes both premises true and the conclusion false, so the condition of the definition fails for it. This is the form of [[affirming the consequent|J7KFCFQRBT]]. See [[this example|ZW5A420AA9]].
- $p \lor q, \; p \not\models \neg q$. The assignment $p = q = 1$ makes both premises true and $\neg q$ false.
- $p \not\models p \land q$. The assignment $p = 1$, $q = 0$ makes the premise true and the conclusion false.

### Basic properties

An assignment that makes all formulas of $\Gamma$ true and $\varphi$ false is a [[countermodel|FWHBT4HABW]]; so $\Gamma \not\models \varphi$ holds exactly when a countermodel exists.

1. Reflexivity: if $\varphi \in \Gamma$, then $\Gamma \models \varphi$. An assignment that makes all of $\Gamma$ true makes $\varphi$ true, since $\varphi$ is one of them.
2. Monotonicity: if $\Gamma \subseteq \Gamma'$ and $\Gamma \models \varphi$, then $\Gamma' \models \varphi$. An assignment that makes all of $\Gamma'$ true makes all of $\Gamma$ true, so it makes $\varphi$ true.
3. Cut: if $\Gamma \models \psi$ for each $\psi \in \Delta$, and $\Gamma \cup \Delta \models \varphi$, then $\Gamma \models \varphi$. An assignment that makes $\Gamma$ true makes each $\psi \in \Delta$ true, so it makes $\Gamma \cup \Delta$ true, and so it makes $\varphi$ true.
4. Explosion: if no truth assignment makes all of $\Gamma$ true, then $\Gamma \models \varphi$ for every $\varphi$. The condition of the definition is then about an empty set of assignments.
5. Validity and consequence: $\Gamma \models \varphi$ holds exactly when $\Gamma \cup \set{\neg \varphi}$ is not [[satisfiable|QN7M1JCGT9]]; the page on satisfiability proves this.
6. Compactness: $\Gamma \models \varphi$ holds exactly when $\Gamma_0 \models \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$. This is a form of the [[compactness theorem|4X9126SEMM]].
7. Decidability for finite $\Gamma$: if $\Gamma$ is finite and $\Gamma \cup \set{\varphi}$ has $k$ variables, a [[truth table|05RSK4Q657]] with $2^k$ rows decides whether $\Gamma \models \varphi$, because the value of a formula depends only on the values of its own variables.

The semantic deduction theorem connects $\models$ with the connective $\to$.

> For every set $\Gamma$ and all formulas $\varphi$, $\psi$: $\Gamma \cup \set{\varphi} \models \psi$ if and only if $\Gamma \models \varphi \to \psi$.

We prove it in steps.

1. Assume $\Gamma \cup \set{\varphi} \models \psi$, and let $v$ make every formula of $\Gamma$ true. We show $\bar v(\varphi \to \psi) = 1$.
2. If $\bar v(\varphi) = 0$, then $\bar v(\varphi \to \psi) = 1$ by the truth table of [[implication|0NMG7W7Q11]].
3. If $\bar v(\varphi) = 1$, then $v$ makes all of $\Gamma \cup \set{\varphi}$ true, so $\bar v(\psi) = 1$ by the assumption of step 1. Then $\bar v(\varphi \to \psi) = 1$ by the truth table of implication.
4. Steps 2 and 3 cover all cases, so $\Gamma \models \varphi \to \psi$.
5. Conversely, assume $\Gamma \models \varphi \to \psi$, and let $v$ make every formula of $\Gamma \cup \set{\varphi}$ true.
6. Then $\bar v(\varphi \to \psi) = 1$ by the assumption, and $\bar v(\varphi) = 1$. The only row of the truth table of $\to$ with these two values has $\bar v(\psi) = 1$.
7. So $\Gamma \cup \set{\varphi} \models \psi$.

Applied $n$ times, the theorem gives: an argument with premises $\varphi_1, \ldots, \varphi_n$ and conclusion $\psi$ is valid exactly when $\varphi_1 \to (\varphi_2 \to \cdots (\varphi_n \to \psi) \cdots)$ is a tautology.
The [[deduction theorem|9X08XK5RV2]] is the same statement for $\vdash$.
The [[soundness theorem|XD629S54CS]] and the [[completeness theorem|81ZNY1XKYJ]] say that $\Gamma \vdash \varphi$ and $\Gamma \models \varphi$ hold for the same $\Gamma$ and $\varphi$.

### History

Bernard Bolzano, in his Wissenschaftslehre of 1837, called a proposition deducible from another when every replacement of certain parts that makes the first true also makes the second true.
Alfred Tarski gave the modern definition, in terms of all interpretations of the non-logical parts, in his paper "On the concept of logical consequence" of 1936.
For the propositional calculus, the interpretations are the truth assignments.

### Common errors

- To read $\Gamma \models \varphi$ as "the premises are true and so is the conclusion". The relation says nothing about the actual truth of the premises; an argument with false premises can be valid.
- To confuse $\models$ with $\to$. The formula $\varphi \to \psi$ is an object of the language, while $\varphi \models \psi$ is a statement about formulas. The semantic deduction theorem links them, but they are not the same thing.
- To forget explosion. A set of premises that no assignment satisfies has every formula as a consequence, which surprises readers who expect a link of content between premises and conclusion.

## Explanations

### L1 human

A conclusion follows logically from some premises when there is no way to make all the premises true and the conclusion false.
Take the premises "it rains or it snows" and "it does not rain".
The conclusion "it snows" follows: the only way to make both premises true is no rain and snow.
We can check this by listing all four cases of "rains" true or false and "snows" true or false.
Only the form of the sentences matters, so the same check works for any two statements in place of "it rains" and "it snows".
When some case makes the premises true and the conclusion false, that case is a counterexample, and the conclusion does not follow.

### L2 human

We decide whether $p \to q, \; q \to r \models p \to r$.

1. The formulas have the three variables $p$, $q$, $r$, so there are $2^3 = 8$ truth assignments.
2. We look for a countermodel: an assignment with $p \to r$ false and both premises true.
3. The conclusion $p \to r$ is false only when $p = 1$ and $r = 0$.
4. With $p = 1$, the premise $p \to q$ is true only when $q = 1$.
5. With $q = 1$ and $r = 0$, the premise $q \to r$ is false.
6. So no assignment makes both premises true and the conclusion false, and $p \to q, \; q \to r \models p \to r$.

This is the typical use of the definition: instead of a full truth table, we search for a countermodel and show that each attempt fails.
By the semantic deduction theorem, the same work shows that $(p \to q) \to ((q \to r) \to (p \to r))$ is a tautology.

A trap: the check must range over all assignments to all variables that occur, in premises and conclusion together.
For $p \models p \lor q$ we must look at the four assignments to $p$ and $q$, not only at the two values of $p$.
Here the check succeeds, but for $p \models q$ a countermodel needs a value for $q$ that the premise does not mention.

### L3 human

Logical consequence is a relation between sets of formulas and formulas, and properties 1 to 3 above make it a consequence relation in the sense of Tarski: it is reflexive, monotone and closed under cut.
Property 6, compactness, adds that it is finitary.
Each logic in this area defines its own consequence relation by its own class of interpretations: structures for [[predicate logic|086QKPF0A6]], Kripke models for modal and intuitionistic logic, truth-value algebras for [[many-valued logic|66NMTCQNQV]].
A propositional consequence remains a consequence in first-order logic after substitution of first-order formulas for the variables.
The converse fails: "every man is mortal, Socrates is a man, so Socrates is mortal" is a first-order consequence, while its propositional form gives $p, q \not\models r$.
The central metatheorems of logic compare $\models$ with a derivability relation $\vdash$: soundness says $\vdash \subseteq \models$, and completeness says $\models \subseteq \vdash$.
In algebraic terms, $\Gamma \models \varphi$ says that $\varphi$ lies in the filter generated by $\Gamma$ in the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]], a [[Boolean algebra|0XADJKM699]].
Non-monotonic logics, studied in artificial intelligence, drop property 2 on purpose, so that a new premise can withdraw a conclusion.

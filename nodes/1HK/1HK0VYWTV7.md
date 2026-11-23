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

A conclusion is a logical consequence of some premises when no assignment of truth values makes all the premises true and the conclusion false.
For example, $q$ follows from $p$ and $p \to q$: of the four rows for $p$ and $q$, only $p = q = 1$ makes both premises true, and that row makes $q$ true.

Exactly: let $\Gamma$ be a set of [[propositional formulas|TT7WT5HPN9]] and $\varphi$ a formula.
Then $\varphi$ is a logical consequence of $\Gamma$, written $\Gamma \models \varphi$, when every truth assignment $v$ with $\bar v(\gamma) = 1$ for all $\gamma \in \Gamma$ also has $\bar v(\varphi) = 1$, where $\bar v$ is the [[truth valuation|H31CS3HK5P]] of $v$.
In first-order logic the definition is the same, with a [[structure|983GZBQYT4]] and an assignment of its elements to the variables in place of a truth assignment.
The [[formal definition|KKNB9JY1YH]] states both cases.

## Motivation

A mathematical argument starts from premises and ends with a conclusion, and we call it valid when the conclusion cannot be false while all the premises are true.
Often this depends only on the form of the sentences.
"If $n$ is divisible by $4$, then $n$ is even; $n$ is divisible by $4$; so $n$ is even" stays valid whatever two statements we put in place of its parts.
The propositional calculus makes "form" exact: replace the parts by variables and check all ways to give them truth values.

Logical consequence is the relation that this check defines.
It is the semantic side of logic, and derivability $\Gamma \vdash \varphi$ in a proof system is the syntactic side.
Every proof system is judged by whether its $\vdash$ captures $\models$, and the [[soundness theorem|XD629S54CS]] and [[completeness theorem|81ZNY1XKYJ]] say that for the propositional calculus it does.

## Notation

We write $\Gamma, \varphi \models \psi$ for $\Gamma \cup \{ \varphi \} \models \psi$, and $\models \varphi$ for $\emptyset \models \varphi$, which says that $\varphi$ is a [[tautology|05006AJ7DZ]].
We write $\Gamma \not\models \varphi$ when the relation fails.
Other names are semantic consequence, entailment, and, in Enderton's book, [[tautological implication|4N2HHE7PC1]].
The same symbol also expresses satisfaction, as in $v \models \varphi$, so look at what stands on its left.
The page on the [[turnstile|2QQMJMS8M5]] compares $\models$, with two bars, to $\vdash$, with one bar; they are easy to confuse in print.

## Remarks

### Valid forms and countermodels

An assignment that makes every formula of $\Gamma$ true and $\varphi$ false is a [[countermodel|FWHBT4HABW]].
So $\Gamma \not\models \varphi$ holds exactly when a countermodel exists, and the usual way to test a consequence is to hunt for one.

Modus ponens, $p, \; p \to q \models q$, is valid, as [[modus ponens as a consequence|H8H9ZYZZEJ]] shows.
Disjunctive syllogism, $p \lor q, \; \neg p \models q$, is valid too, since only $p = 0$, $q = 1$ makes both premises true; see [[disjunctive syllogism|V5H6FW6F9M]].
On the other side, $p \to q, \; q \not\models p$, because $p = 0$, $q = 1$ is a countermodel.
This is the fallacy of [[affirming the consequent|J7KFCFQRBT]], worked out in [[its non-example|ZW5A420AA9]].
In the same way $p \not\models p \land q$, with the countermodel $p = 1$, $q = 0$.

Infinite sets of premises are allowed.
For example, $\{ p_0 \} \cup \{ p_n \to p_{n+1} : n \geq 0 \} \models p_{17}$, because an assignment that makes all premises true has $v(p_0) = 1$, and then $v(p_n) = 1$ for every $n$ by [[induction|0ASJVEFA9J]].

### The rules you can use

Three rules hold for every $\Gamma$, $\Delta$ and $\varphi$, and each follows at once from the definition.
Reflexivity: if $\varphi \in \Gamma$, then $\Gamma \models \varphi$, since an assignment that makes all of $\Gamma$ true makes $\varphi$ true.
Monotonicity: if $\Gamma \subseteq \Gamma'$ and $\Gamma \models \varphi$, then $\Gamma' \models \varphi$, since an assignment that makes $\Gamma'$ true makes $\Gamma$ true.
Cut: if $\Gamma \models \psi$ for each $\psi \in \Delta$ and $\Gamma \cup \Delta \models \varphi$, then $\Gamma \models \varphi$.

Four more facts link consequence to the rest of the calculus.
If no assignment makes all of $\Gamma$ true, then $\Gamma \models \varphi$ for every $\varphi$ (explosion), because there is no row to check.
$\Gamma \models \varphi$ holds exactly when $\Gamma \cup \{ \neg \varphi \}$ is not [[satisfiable|QN7M1JCGT9]].
$\Gamma \models \varphi$ holds exactly when $\Gamma_0 \models \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$, a form of the [[compactness theorem|4X9126SEMM]].
For finite $\Gamma$, a [[truth table|05RSK4Q657]] with $2^k$ rows decides $\Gamma \models \varphi$, where $k$ is the number of variables in $\Gamma \cup \{ \varphi \}$.

### The semantic deduction theorem

The relation $\models$ and the connective $\to$ are linked: for every set $\Gamma$ and all formulas $\varphi$, $\psi$,
$$\Gamma \cup \{ \varphi \} \models \psi \iff \Gamma \models \varphi \to \psi .$$

1. Assume the left side, and let $v$ make all of $\Gamma$ true.
   If $\bar v(\varphi) = 0$, then $\bar v(\varphi \to \psi) = 1$ by the table of [[implication|0NMG7W7Q11]].
   If $\bar v(\varphi) = 1$, then $v$ makes $\Gamma \cup \{ \varphi \}$ true, so $\bar v(\psi) = 1$, and again $\bar v(\varphi \to \psi) = 1$.
2. Assume the right side, and let $v$ make all of $\Gamma \cup \{ \varphi \}$ true.
   Then $\bar v(\varphi \to \psi) = 1$ and $\bar v(\varphi) = 1$, and the only row of the table of $\to$ with these values has $\bar v(\psi) = 1$.

Used $n$ times, the theorem says that $\varphi_1, \ldots, \varphi_n \models \psi$ exactly when $\varphi_1 \to (\varphi_2 \to \cdots (\varphi_n \to \psi) \cdots)$ is a tautology.
The [[deduction theorem|9X08XK5RV2]] is the same statement for $\vdash$.

### Watch out

$\Gamma \models \varphi$ says nothing about whether the premises are actually true.
"If $2 > 3$ then $5 > 7$; $2 > 3$; so $5 > 7$" is valid, with false premises and a false conclusion.

Do not confuse $\models$ with $\to$.
The formula $\varphi \to \psi$ is an object of the language, while $\varphi \models \psi$ is a claim about formulas; the deduction theorem links them, but they are different things.

Explosion surprises readers who expect the premises to be about the conclusion.
$p \land \neg p \models q$ holds, because no row makes $p \land \neg p$ true, so no row can be a countermodel.

### History

Bernard Bolzano, in his Wissenschaftslehre of 1837, called a proposition deducible from another when every replacement of certain parts that makes the first true also makes the second true.
Alfred Tarski gave the modern definition, in terms of all interpretations of the non-logical parts, in his paper "On the concept of logical consequence" of 1936.
For the propositional calculus, the interpretations are the truth assignments.

### Try it

Does $p \to q \models \neg q \to \neg p$ hold?
Yes: a countermodel would need $\neg q = 1$ and $\neg p = 0$, so $q = 0$ and $p = 1$, and then $p \to q = 0$.

Does $p \lor q \models p$ hold?
No: $p = 0$, $q = 1$ makes the premise true and the conclusion false.

## Explanations

### L1 human

A conclusion follows logically from some premises when there is no way to make all the premises true and the conclusion false.
Take the premises "it rains or it snows" and "it does not rain".
The conclusion "it snows" follows: the only way to make both premises true is no rain and snow.
We can check this by listing the four cases of "rains" and "snows" being true or false.
When some case makes the premises true and the conclusion false, that case is a counterexample, and the conclusion does not follow.

### L2 human

We decide whether $p \to q, \; q \to r \models p \to r$, by hunting for a countermodel.
The conclusion $p \to r$ is false only when $p = 1$ and $r = 0$.
With $p = 1$, the premise $p \to q$ is true only when $q = 1$.
With $q = 1$ and $r = 0$, the premise $q \to r$ is
$$1 \to 0 = 0,$$
so it is false.
Every attempt fails, so the consequence holds, and by the semantic deduction theorem $(p \to q) \to ((q \to r) \to (p \to r))$ is a tautology.

The hunt must range over all variables in the premises and the conclusion together.
For $p \models q$, the countermodel $p = 1$, $q = 0$ needs a value for $q$, which the premise never mentions.

### L3 human

Reflexivity, monotonicity and cut make $\models$ a consequence relation in the sense of Tarski, and compactness makes it finitary.
Each logic defines its own consequence relation by its class of interpretations: structures for [[predicate logic|086QKPF0A6]], Kripke models for modal and intuitionistic logic, and truth-value algebras for [[many-valued logic|66NMTCQNQV]].
A propositional consequence stays a consequence in first-order logic after we substitute first-order formulas for the variables, but the converse fails, as the Socrates syllogism shows.
In algebraic terms, $\Gamma \models \varphi$ says that $\varphi$ lies in the filter generated by $\Gamma$ in the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]], a [[Boolean algebra|0XADJKM699]].
Non-monotonic logics, studied in artificial intelligence, drop monotonicity on purpose, so that a new premise can withdraw a conclusion.

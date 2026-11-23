---
tag: Z2WRGJDRQT
kind: concept
name: Probability logic
aliases: [probability-logic, probabilistic-logic]
msc: ["03B48"]
topics: [WZP584JQ06]
audience: research
uses: [09K9MWD2QQ, 05006AJ7DZ, 0DAX8PMAJ4, P7E926JK13, 8DH4QM6AX8]
sources:
  - url: https://plato.stanford.edu/entries/logic-probability/
    locator: 1. Combining Logic and Probability Theory; 2.1 Probabilistic Semantics; 2.2 Adams' Probability Logic; 2.3 Further Generalizations; 3.2 Sums and Products of Probability Terms
  - url: https://en.wikipedia.org/wiki/Probabilistic_logic
    locator: lead section
---

## Summary

Toss two fair coins, and let $p$ say "the first coin shows heads", so $P(p) = \tfrac12$.
If $q$ says "the second coin shows heads", then $P(p \land q) = \tfrac14$.
If $q$ is $p$ itself, then $P(p \land q) = \tfrac12$, and if $q$ says "the first coin shows tails", then $P(p \land q) = 0$.
The same inputs $\tfrac12$ and $\tfrac12$ give three different outputs, so probability is not a truth value.

*Probability logic* studies probability functions on the formulas of a logical language, and the inferences that they support.
For the language $\mathcal{L}$ of [[propositional logic|09K9MWD2QQ]], a *probability function* is a map $P \colon \mathcal{L} \to \mathbb{R}$ with three properties.
First, $P(\varphi) \ge 0$ for every $\varphi$.
Second, $P(\varphi) = 1$ for every [[tautology|05006AJ7DZ]] $\varphi$.
Third, $P(\varphi \lor \psi) = P(\varphi) + P(\psi)$ whenever $\neg(\varphi \land \psi)$ is a tautology.

Some probability logics keep the classical language and ask how probability passes from premises to conclusion.
Others add probability terms to the language, as in the formula $a_1 P(\varphi_1) + \dots + a_n P(\varphi_n) \ge b$.

## Motivation

A valid argument can have uncertain premises.
From "if it rains tomorrow, I get wet" and "it rains tomorrow", it follows that "I get wet".
But each premise may be only probable, and deductive validity says nothing about the probability of the conclusion.
Probability logic computes, from the probabilities of the premises, the best possible bounds for the probability of the conclusion.
Probabilities are not truth values of a matrix, so this question needs its own logic; see [[probability is not truth-functional|EVW7FAWM68]].

## Notation

$P(\varphi)$ is the probability of the formula $\varphi$.
$U(\varphi) = 1 - P(\varphi)$ is its *uncertainty*, in the terms of Adams.
$\Gamma \models_p \varphi$ means *probabilistic validity*: every probability function that gives each premise in $\Gamma$ the value $1$ gives $\varphi$ the value $1$.
In logics with probability terms, $P(\varphi) \le q$ abbreviates $-P(\varphi) \ge -q$, and $P(\varphi) < q$ abbreviates $\neg (P(\varphi) \ge q)$.

## Remarks

### Probability functions from weights

Each classical valuation $v \colon \mathcal{L} \to \{ 0, 1 \}$ is a probability function, called degenerate.
More generally, put weights on the valuations and add up the weights of the valuations that make $\varphi$ true.
On $p$ and $q$, give $(1,1)$, $(1,0)$, $(0,1)$ and $(0,0)$ the weights $0.4$, $0.1$, $0.3$ and $0.2$.
Then $P(p) = 0.5$, $P(q) = 0.7$ and $P(p \lor q) = 0.4 + 0.1 + 0.3 = 0.8$.

### What is not a probability function

The [[minimum and maximum valuation|9HYWPPKC1C]] with $v(p) = \tfrac12$ gives the tautology $p \lor \neg p$ the value $\tfrac12$, so the second property fails.
A map with $P(p) = P(\neg p) = 0.6$ fails additivity, since $p$ and $\neg p$ exclude each other and $0.6 + 0.6 = 1.2 \ne 1$.
A map with $P(p) = 0.3$ and $P(\neg \neg p) = 0.5$ fails too, because equivalent formulas must get the same probability.

### Basic laws

Every probability function has $0 \le P(\varphi) \le 1$, and $P(\varphi) = P(\psi)$ whenever $\varphi \leftrightarrow \psi$ is a tautology.
The law $P(\neg \varphi) = 1 - P(\varphi)$ holds, since $1 = P(\varphi \lor \neg \varphi) = P(\varphi) + P(\neg \varphi)$.
If $\Gamma \vdash \varphi$ classically and $P(\gamma) = 1$ for all $\gamma \in \Gamma$, then $P(\varphi) = 1$.
In fact $\models_p$ coincides with classical consequence, since the degenerate functions are among the probability functions.

### Bounds on conclusions

For a valid argument with finitely many premises, Adams' theorem bounds the uncertainty: $U(\varphi) \le \sum_{\gamma \in \Gamma} U(\gamma)$.
For [[modus ponens|BJZ2BKEV4F]], from $P(p) = a$ and $P(p \to q) = b$ it follows that $a + b - 1 \le P(q) \le b$, and both bounds are reached.
In general, the best bounds for $P(\varphi)$ from interval bounds on the premises are the optimal values of a [[linear program|VNMXB0J2KA]] in the weights.

### Logics with probability terms

When probability terms enter the language, compactness fails.
The formulas $P(p) > 0$ and $P(p) \le \tfrac1k$ for all $k \ge 1$ are finitely satisfiable but not satisfiable; see [[the non-compactness example|PHAKRZ7F0E]].
So such a logic can have a proof system that is weakly complete, for finite sets of premises, but not strongly complete.

### Watch out

Do not treat probabilities as truth values.
The probability of a conjunction depends on how the events are related, and $P(\varphi \land \psi) = P(\varphi) P(\psi)$ holds only for independent events.
Do not confuse [[fuzzy logic|8DH4QM6AX8]] with probability logic either.
A degree of truth measures how far a vague statement holds, and a probability measures uncertainty about a statement that is either true or false.

### History

Carnap's work of 1950 treated probability as a part of logic, after Boole, De Morgan, Ramsey and de Finetti.
Hailperin, from 1965, and Nilsson, in his 1986 paper "Probabilistic Logic", computed optimal probability bounds by linear programming.
Nilsson's paper led to much work on probabilistic reasoning in artificial intelligence.
Fagin, Halpern and Megiddo in 1990 added linear combinations of probability terms to the language, and gave a sound and weakly complete proof system.

### Try it

With $P(p) = 0.9$ and $P(q) = 0.9$, find the least possible value of $P(p \land q)$.
Adams' bound gives $U(p \land q) \le 0.1 + 0.1 = 0.2$, so $P(p \land q) \ge 0.8$.
The value $0.8$ is reached when the two events of probability $0.1$ where $p$ or $q$ fails are disjoint.

## Explanations

### L1 human

Probability logic attaches a chance between $0$ and $1$ to each statement.
A statement that is always true gets chance $1$, and the chances of two statements that cannot both be true add up.
For example, if "rain" has chance $0.3$, then "no rain" has chance $0.7$.
The logic then asks how sure we can be of a conclusion when we are only partly sure of the premises.
If "rain" has chance $0.9$ and "if rain, then wet" has chance $0.8$, then "wet" has a chance between $0.7$ and $0.8$.

### L2 human

List the valuations of the variables, here $(p, q) \in \{ 0, 1 \}^2$, and give each valuation a weight $x_i \ge 0$, with sum $1$.
The probability of a formula is the sum of the weights of the valuations that make it true.
Each constraint on probabilities is then a linear equation or inequality in the $x_i$.
The best bounds for a conclusion are the minimum and the maximum of a linear function under these constraints.
Watch out: the bounds depend on all the premises together, and not on each premise alone.

### L3 human

A probability function on a classical propositional language is the same thing as a finitely additive probability measure on the Boolean algebra of formulas modulo equivalence.
By Stone's representation theorem, it is a finitely additive measure on the clopen sets of the space of valuations.
So probability logic replaces the two points $\{ 0, 1 \}$ of the valuation space by measures on it.
Logics with probability terms, such as that of Fagin, Halpern and Megiddo, put linear arithmetic over the reals inside the formulas.
Their completeness proofs use the theory of linear inequalities.
Unlike [[fuzzy logic|8DH4QM6AX8]], probability logic is not truth-functional, so the methods of logical matrices do not apply to it.

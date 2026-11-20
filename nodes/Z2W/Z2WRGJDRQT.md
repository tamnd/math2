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

*Probability logic* studies probability functions on the formulas of a logical language, and the inferences that they support.
For the language $\mathcal{L}$ of [[propositional logic|09K9MWD2QQ]], a *probability function* is a map $P \colon \mathcal{L} \to \mathbb{R}$ with three properties.
First, $P(\varphi) \ge 0$ for every $\varphi$.
Second, $P(\varphi) = 1$ for every [[tautology|05006AJ7DZ]] $\varphi$.
Third, $P(\varphi \lor \psi) = P(\varphi) + P(\psi)$ whenever $\neg(\varphi \land \psi)$ is a tautology.
Some probability logics keep the classical language and ask how probability passes from premises to conclusion.
Other probability logics add probability terms to the language, as in the formula $a_1 P(\varphi_1) + \dots + a_n P(\varphi_n) \ge b$.
The idea matters because it gives exact numerical rules for reasoning from uncertain premises.

## Motivation

A valid argument can have uncertain premises.
From "if it rains tomorrow, I get wet" and "it rains tomorrow", it follows that "I get wet".
But each premise may be only probable, and deductive validity says nothing about the probability of the conclusion.
Probability logic answers this question with bounds: from the probabilities of the premises, it computes the best possible bounds for the probability of the conclusion.
Probabilities are not truth values of a matrix, so this question needs its own logic; see [[probability is not truth-functional|EVW7FAWM68]].

## Notation

$P(\varphi)$ is the probability of the formula $\varphi$.
$U(\varphi) = 1 - P(\varphi)$ is its *uncertainty*, in the terms of Adams that SEP uses.
$\Gamma \models_p \varphi$ means *probabilistic validity*: every probability function that gives each premise in $\Gamma$ the value $1$ gives $\varphi$ the value $1$.
In logics with probability terms, $P(\varphi) \le q$ abbreviates $-P(\varphi) \ge -q$, and $P(\varphi) < q$ abbreviates $\neg (P(\varphi) \ge q)$.

## Remarks

### Examples

1. Each classical valuation $v \colon \mathcal{L} \to \set{0, 1}$ is a probability function, since it satisfies the three properties. SEP calls these the degenerate probability functions.
2. On the formulas in $p$ and $q$, give the four valuations of $(p, q)$ the weights $0.4, 0.1, 0.3, 0.2$ for $(1,1), (1,0), (0,1), (0,0)$. The sum of weights of the valuations that make $\varphi$ true is a probability function, with $P(p) = 0.5$, $P(q) = 0.7$ and $P(p \lor q) = 0.8$.
3. [[Probability bounds for modus ponens|BJZ2BKEV4F]]: from $P(p) = a$ and $P(p \to q) = b$ it follows that $a + b - 1 \le P(q) \le b$, and both bounds are reached.
4. [[Finitely satisfiable but not satisfiable|PHAKRZ7F0E]]: the formulas $P(p) > 0$ and $P(p) \le \tfrac{1}{k}$ for all $k \ge 1$ show that probability logic is not compact.
5. [[Probability is not truth-functional|EVW7FAWM68]]: two events of probability $\tfrac12$ can have a conjunction of probability $0$, $\tfrac14$ or $\tfrac12$.

### Non-examples

1. [[The minimum-maximum valuation|9HYWPPKC1C]] with $v(p) = \tfrac12$ gives the tautology $p \lor \neg p$ the value $\tfrac12$, so the second property fails.
2. A map with $P(p) = P(\neg p) = 0.6$ fails additivity. The formulas $p$ and $\neg p$ exclude each other, so $P(p \lor \neg p)$ would be $1.2$, but it must be $1$.
3. A map with $P(p) = 0.3$ and $P(\neg \neg p) = 0.5$ is not a probability function, because equivalent formulas must get the same probability.

### Basic properties

1. $0 \le P(\varphi) \le 1$, and $P(\varphi) = P(\psi)$ whenever $\varphi \leftrightarrow \psi$ is a tautology, as SEP states.
2. $P(\neg \varphi) = 1 - P(\varphi)$. Indeed $\varphi$ and $\neg \varphi$ exclude each other, so $1 = P(\varphi \lor \neg \varphi) = P(\varphi) + P(\neg \varphi)$.
3. If $\Gamma \vdash \varphi$ classically and $P(\gamma) = 1$ for all $\gamma \in \Gamma$, then $P(\varphi) = 1$. SEP states that $\models_p$ is strongly sound and complete for classical propositional logic.
4. For a valid argument with finitely many premises, $U(\varphi) \le \sum_{\gamma \in \Gamma} U(\gamma)$. SEP gives this theorem of Adams and says that Suppes (1966) first proved it.
5. The best lower and upper bounds for $P(\varphi)$, from interval bounds on the premises, are computable from the Boolean structure of the formulas. SEP attributes this result to Hailperin and Nilsson, who used [[linear programming|VNMXB0J2KA]].
6. $P(\varphi \land \psi)$ is not a function of $P(\varphi)$ and $P(\psi)$. So a probability function is not a valuation in any [[logical matrix|P7E926JK13]] on $[0, 1]$.

### History

SEP lists Carnap (1950) among the authors who treated probability as a part of logic, after De Morgan, Boole, Ramsey and de Finetti.
SEP reports that Hailperin, from 1965, and Nilsson, in 1986, computed optimal probability bounds with linear programming.
Nilsson's paper "Probabilistic Logic" (1986) led to much work on probabilistic reasoning in artificial intelligence, as SEP states.
Fagin, Halpern and Megiddo (1990) added linear combinations of probability terms to the language, and gave a sound and weakly complete proof system.

### Common errors

1. Treating probabilities as truth values. The probability of a conjunction depends on how the events are related, and not only on their probabilities.
2. Confusing [[fuzzy logic|8DH4QM6AX8]] with probability logic. A degree of truth measures how far a vague statement holds, and a probability measures uncertainty about a statement that is true or false.
3. Writing $P(\varphi \land \psi) = P(\varphi) P(\psi)$ in general. This holds only for independent events.

## Explanations

### L1 human

Probability logic attaches a chance between $0$ and $1$ to each statement.
A statement that is always true gets chance $1$, and the chances of two statements that can not both be true add up.
For example, if "rain" has chance $0.3$, then "no rain" has chance $0.7$.
The logic then asks how sure we can be of a conclusion when we are only partly sure of the premises.
If "rain" has chance $0.9$ and "if rain, then wet" has chance $0.8$, then "wet" has a chance between $0.7$ and $0.8$.

### L2 human

1. List the valuations of the variables, here $(p, q) \in \set{0, 1}^2$.
2. Give each valuation a weight $x_i \ge 0$, with sum $1$.
3. The probability of a formula is the sum of the weights of the valuations that make it true.
4. Each constraint on probabilities is a linear equation or inequality in the $x_i$.
5. The best bounds for a conclusion are the minimum and the maximum of a linear function under these constraints.

This is the typical use: to find what the premises force on the conclusion.
A trap: the bounds depend on all the premises together, and not on each premise alone.
Two premises with probability $0.9$ each can give a conclusion with probability only $0.8$, by property 4.

### L3 human

A probability function on a classical propositional language is the same thing as a finitely additive probability measure on the Boolean algebra of formulas modulo equivalence.
By the representation theorem of Stone, it is a finitely additive measure on the clopen sets of the space of valuations.
So probability logic replaces the two points $\set{0, 1}$ of the valuation space by measures on it.
Logics with probability terms, such as that of Fagin, Halpern and Megiddo, put linear arithmetic over the reals inside the formulas, and their completeness proofs use the theory of linear inequalities.
Modal probability logics and first-order probability logics extend the same ideas; SEP treats them in its sections 4 and 5.
Unlike [[fuzzy logic|8DH4QM6AX8]], probability logic is not truth-functional, so the methods of logical matrices do not apply to it.

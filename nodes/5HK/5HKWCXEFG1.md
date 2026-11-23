---
tag: 5HKWCXEFG1
kind: concept
name: Justification logic
msc: ["03B45", "03F45"]
topics: [CQM9SRN8PM]
audience: research
uses: [N60RVXSA5W, 09K9MWD2QQ, 6BQ71KQ6QT, 4PZM5GJTR5]
aliases: [logic-of-proofs, lp]
sources:
  - url: https://en.wikipedia.org/wiki/Sergei_N._Artemov
    locator: Research
  - url: https://en.wikipedia.org/wiki/Brouwer%E2%80%93Heyting%E2%80%93Kolmogorov_interpretation
    locator: The interpretation
  - book: isbn:9781108424912
    locator: "Artemov and Fitting, Justification Logic: Reasoning with Reasons"
---

## Summary

Suppose $x$ is a proof of $p$ and $y$ is a proof of $q$.
Then a proof of $p \wedge q$ can be written down: take the tautology $p \to (q \to (p \wedge q))$, with a name $c$ for its one-line proof, and apply it first to $x$ and then to $y$.
Justification logic writes this as $((c \cdot x) \cdot y){:}(p \wedge q)$.
In general $t{:}\varphi$ says "$t$ is a justification, or proof, of $\varphi$", and it replaces the box of modal logic by an explicit reason.

Terms are built from proof variables $x, y, \dots$ and proof constants $a, b, c, \dots$ with the binary operations $\cdot$ (application) and $+$ (sum) and the unary operation $!$ (proof checker).
Artemov's logic of proofs $\mathsf{LP}$ has the axioms of the [[propositional calculus|09K9MWD2QQ]] and the following schemas.
$$s{:}(\varphi \to \psi) \to (t{:}\varphi \to (s \cdot t){:}\psi), \quad s{:}\varphi \to (s + t){:}\varphi, \quad t{:}\varphi \to (s + t){:}\varphi, \quad t{:}\varphi \to \varphi, \quad t{:}\varphi \to {!t}{:}(t{:}\varphi).$$
Its rules are modus ponens and axiom necessitation, which gives $\vdash c{:}A$ for every axiom $A$ and every constant $c$.
The forgetful projection, which replaces each $t{:}\varphi$ by $\square\varphi$, maps $\mathsf{LP}$ onto the [[modal logic S4|N60RVXSA5W]], by the [[realization theorem|BP022FTWCP]].
So $\mathsf{LP}$ gives the box of $\mathsf{S4}$ a reading as provability with explicit proofs, and through $\mathsf{S4}$ a provability semantics for intuitionistic logic.

## Motivation

Gödel read $\square\varphi$ as "$\varphi$ is provable" and embedded intuitionistic logic in $\mathsf{S4}$.
Read $\square$ as "provable in [[Peano arithmetic|HACXBCM7SS]]" and take $\varphi = \bot$.
Then $\square\bot \to \bot$ says that Peano arithmetic is consistent, which it cannot prove, by [[Gödel's second incompleteness theorem|4PZM5GJTR5]].
So $\mathsf{S4}$ is not the logic of formal provability, and that logic is the provability logic $\mathsf{GL}$ instead.

Gödel suggested in the 1930s that explicit proofs would behave better.
"$t$ is a proof of $\varphi$" is a decidable relation, so $t{:}\varphi \to \varphi$ is provable for each fixed $t$ and $\varphi$.
Justification logic carries out this suggestion, since each box becomes a term that records why the formula holds.

## Notation

$t{:}\varphi$ is also written $[t]\varphi$, and it reads "$t$ justifies $\varphi$" or "$t$ is a proof of $\varphi$".
$\mathsf{J}$ is the basic justification logic, with application and sum, $\mathsf{JT}$ adds $t{:}\varphi \to \varphi$, $\mathsf{J4}$ adds $!$, and $\mathsf{LP} = \mathsf{JT4}$.
A constant specification $\mathcal{CS}$ lists the pairs $(c, A)$ for which $c{:}A$ is an axiom, and $\mathsf{LP}$ uses the total one.
$\varphi^\circ$ is the forgetful projection, and $A^r$ is the realization of a modal formula $A$ by a map $r$ from box occurrences to terms.

## Remarks

### Each modal axiom has an explicit form

The axiom $\mathsf{K}$, $\square(p \to q) \to (\square p \to \square q)$, is realized by the application axiom $x{:}(p \to q) \to (y{:}p \to (x \cdot y){:}q)$.
The axiom $\mathsf{4}$, $\square p \to \square\square p$, is realized by the checker axiom $x{:}p \to {!x}{:}(x{:}p)$.
The conjunction in the Summary is worked out in [[internalizing a conjunction|6X2ABCND9X]].
The $\mathsf{S4}$ theorem $\square p \vee \square q \to \square(p \vee q)$ needs the sum, and is realized by $x{:}p \vee y{:}q \to (a \cdot x + b \cdot y){:}(p \vee q)$, as in [[a realization with sum|BK27F356QC]].

### Internalization and lifting

Every theorem has an explicit proof inside the logic.
If $\mathsf{LP} \vdash \varphi$, then $\mathsf{LP} \vdash t{:}\varphi$ for some ground term $t$, built from constants with $\cdot$ and $!$.
More generally, lifting says the following.
If $x_1{:}A_1, \dots, x_n{:}A_n, B_1, \dots, B_m \vdash \varphi$, then $x_1{:}A_1, \dots, x_n{:}A_n, y_1{:}B_1, \dots, y_m{:}B_m \vdash t{:}\varphi$ for a term $t$ in $x_1, \dots, x_n, y_1, \dots, y_m$.
The rule "from $\vdash \varphi$ infer $\vdash x{:}\varphi$" for a proof variable $x$ is not admissible, since $x{:}(p \to p)$ is not a theorem.

### Semantics and arithmetic

The forgetful projection of $\mathsf{LP}$ is exactly $\mathsf{S4}$, by [[the realization theorem|BP022FTWCP]].
$\mathsf{LP}$ is arithmetically complete: it proves exactly the formulas that are provable in Peano arithmetic under every interpretation of proof variables as codes of arithmetical proofs.
$\mathsf{LP}$ is decidable, and it is sound and complete for Fitting models, which are [[Kripke models|6BQ71KQ6QT]] with an evidence function $\mathcal{E}(t, \varphi) \subseteq W$.
The formula $t{:}\varphi \to \square\varphi$ is not a formula of pure $\mathsf{LP}$, whose language has no box, and it belongs to combined logics of proofs and provability.

### Watch out

A term is not a label on a box.
The term records the structure of the reasoning, so $x{:}p \to x{:}(p \wedge p)$ fails, although its projection is an $\mathsf{S4}$ theorem, as [[the failure of this formula|RA808VJGHJ]] shows.
In a realization, one variable must not serve two hypotheses, since a normal realization needs distinct variables for the negative occurrences of the box.
Without the constant specification $c{:}A$ for axioms, internalization fails.

### History

Gödel proposed explicit proofs as the meaning of the box of $\mathsf{S4}$ in a 1938 lecture that was published only much later.
Artemov introduced the logic of proofs in 1995 and proved the realization theorem and arithmetical completeness.
His 2001 paper "Explicit provability and constructive semantics" gave the full account, a provability semantics for $\mathsf{S4}$ and for the Brouwer-Heyting-Kolmogorov reading of intuitionistic logic.
Mkrtychev and then Fitting gave the semantics of evidence models, and the book of Artemov and Fitting (2019) surveys the field.

### Try it

Realize $\square p \to \square(q \to p)$.
Give the hypothesis the variable $x$, and let $c$ justify the axiom $p \to (q \to p)$.
The application axiom and modus ponens give $\mathsf{LP} \vdash x{:}p \to (c \cdot x){:}(q \to p)$.

## Explanations

### L1 human

In ordinary logic we say "this is provable" without saying how.
Justification logic always names a reason: "$t$ is a reason for $p$".
Reasons can be combined.
If $s$ is a reason for "if $p$ then $q$" and $t$ is a reason for $p$, then "$s$ applied to $t$" is a reason for $q$.
For example, a teacher's rule and a measurement together justify a conclusion, and the combined reason names both.

### L2 human

We realize the $\mathsf{S4}$ theorem $\square p \to \square(p \vee q)$ step by step.
Give the negative box a proof variable, so the hypothesis becomes $x{:}p$.
The tautology $p \to (p \vee q)$ is an axiom, so axiom necessitation gives $c{:}(p \to (p \vee q))$.
The application axiom gives $c{:}(p \to (p \vee q)) \to (x{:}p \to (c \cdot x){:}(p \vee q))$.
Modus ponens twice gives $\mathsf{LP} \vdash x{:}p \to (c \cdot x){:}(p \vee q)$.

The typical use of justification logic is to make the reasons in an epistemic or proof-theoretic argument explicit and checkable.
Watch out: the term $c \cdot x$ on the right depends on $x$, and a term without $x$ would not work, since nothing then justifies $p$.

### L3 human

Justification logics exist for many modal logics, such as $\mathsf{K}$, $\mathsf{T}$, $\mathsf{K4}$ and $\mathsf{S5}$ (with a negative checker $?$), each with its own realization theorem.
In epistemic logic, justification terms answer the problem of logical omniscience: an agent knows a consequence only through a term that records the work, and the size of the term measures the effort.
Combined with the Gödel translation, $\mathsf{LP}$ completes the chain from intuitionistic logic through $\mathsf{S4}$ to proofs in arithmetic, which gives the [[Brouwer-Heyting-Kolmogorov interpretation|1VFH9WT1RZ]] a formal provability reading.
Logics that combine proofs with the provability box of [[provability logic|WJK0YA4GP2]] relate explicit and implicit provability in Peano arithmetic.

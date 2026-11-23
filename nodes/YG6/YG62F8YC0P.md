---
tag: YG62F8YC0P
kind: concept
name: Pavelka logic
aliases: [pavelka-logic, rational-pavelka-logic, evaluated-syntax]
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
uses: [NFCEM44XYH, JQ713VVD0G]
sources:
  - url: https://en.wikipedia.org/wiki/Fuzzy_logic
    locator: Propositional fuzzy logics
  - url: https://en.wikipedia.org/wiki/T-norm_fuzzy_logics
    locator: Logical language
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 3. Łukasiewicz logic; 5. Other notable fuzzy logics; Bibliography
  - book: isbn:9780792352389
---

## Summary

Suppose we know "the road is icy" to degree at least $0.7$, and "if the road is icy, the bus is late" to degree at least $0.8$.
How late is the bus, to which degree?
In Łukasiewicz semantics the answer is at least $0.7 \odot 0.8 = \max(0, 0.7 + 0.8 - 1) = 0.5$, and no better bound is safe.
Pavelka logic is the fuzzy logic that reasons with such degrees.

In Hájek's form, *rational Pavelka logic* RPL is [[Łukasiewicz logic|NFCEM44XYH]] with a truth constant $\overline{r}$ for each rational $r \in [0, 1]$, and the statement "$\varphi$ to degree at least $r$" is the formula $\overline{r} \to \varphi$.
Its main theorem, Pavelka-style completeness, says that for every theory $T$ and formula $\varphi$ the best provable degree equals the true degree:
$$\lvert \varphi \rvert_T = \lVert \varphi \rVert_T.$$

## Motivation

Ordinary consequence in fuzzy logic only passes on the value $1$.
But a vague premise is often true only to some degree, and a reasoner wants a degree for the conclusion.
Graded consequence answers this: from premises with degrees, find the best lower bound for the degree of the conclusion.
Truth constants let the logic state such bounds inside its own language, so graded reasoning becomes ordinary proof.

Pavelka's original systems put the degrees into the syntax, as evaluated formulas, and Hájek showed that the constants of RPL do the same job inside Łukasiewicz logic.
The construction depends on the continuity of Łukasiewicz implication, which is why it fits $\mathrm{Ł}_\infty$ so well.

## Notation

A truth constant is written $\overline{r}$, and it has the value $r$ under every evaluation.
The *truth degree* of $\varphi$ in a theory $T$ is $\lVert \varphi \rVert_T = \inf \{e(\varphi) : e \text{ a model of } T\}$.
The *provability degree* is $\lvert \varphi \rvert_T = \sup \{r : T \vdash \overline{r} \to \varphi\}$.
We write $\odot$ for strong conjunction; some books write $\&$ or $\otimes$, and Pavelka's own name for the setting is "evaluated syntax".

## Remarks

### Degrees through a proof

The general rule of [[graded modus ponens|820H41656Q]] reads: from $\overline{r} \to \varphi$ and $\overline{s} \to (\varphi \to \psi)$, derive $\overline{r \odot s} \to \psi$.
With $r = 0.7$ and $s = 0.8$ it gives the degree $0.5$, and the evaluation $e(\varphi) = 0.7$, $e(\psi) = 0.5$ shows that $0.5$ is best:
$$e(\varphi \to \psi) = \min(1, 1 - 0.7 + 0.5) = 0.8.$$
The losses $0.3$ and $0.2$ add up to the loss $0.5$.

### Degrees of laws

In the empty theory, [[excluded middle has truth degree one half|NPTZAWBB8A]].
Its value $\max(x, 1 - x)$ is never below $\tfrac12$ and equals $\tfrac12$ at $x = \tfrac12$.
So $\overline{r} \to (p \lor \neg p)$ is a tautology exactly for $r \le \tfrac12$.
In the theory $\{\overline{0.6} \to p\}$ the models have $x \ge 0.6$, and the degree of $p \lor \neg p$ rises to $0.6$.

### The rules you can use

RPL is Łukasiewicz logic plus the *bookkeeping axioms*, which compute with constants.
They are $(\overline{r} \odot \overline{s}) \leftrightarrow \overline{r \odot s}$ and $(\overline{r} \to \overline{s}) \leftrightarrow \overline{r \Rightarrow s}$, where $r \Rightarrow s = \min(1, 1 - r + s)$.
For example, $\overline{0.7} \odot \overline{0.8} \leftrightarrow \overline{0.5}$ is an axiom.
Rational constants are enough, because the Łukasiewicz operations send rationals to rationals.

### What it is not

[[The minimum rule is unsound|KYG8T7KQQ9]]: from degrees $0.7$ and $0.8$ it claims $0.7$ for $\psi$, but the evaluation above gives $\psi$ only $0.5$.
Any bound above $r \odot s$ fails for the same evaluation, for example the product $0.7 \cdot 0.8 = 0.56$.
And RPL is not a logic of exact values: $\overline{r} \to \varphi$ says that $\varphi$ is at least $r$, not equal to $r$.

### Watch out

The provability degree is a supremum, and no single proof needs to reach it.
Take $T = \{\overline{r} \to p : r \in \mathbb{Q}, r < \tfrac{\sqrt2}{2}\}$.
Every model has $e(p) \ge \tfrac{\sqrt2}{2}$, so the truth degree of $p$ is $\tfrac{\sqrt2}{2}$, an irrational number.
Each proof gives a rational bound below it, and only the supremum of the bounds equals $\tfrac{\sqrt2}{2}$.

### History

Pavelka published his papers "On fuzzy logic" I, II and III in 1979, with graded consequence and a completeness theorem for degrees.
Hájek presented rational Pavelka logic, Łukasiewicz logic with rational truth constants, in his 1998 book on the metamathematics of fuzzy logic.

### Try it

First, from $\overline{0.9} \to \varphi$ and $\overline{0.6} \to (\varphi \to \psi)$, which degree for $\psi$ does graded modus ponens give?
It gives $0.9 \odot 0.6 = \max(0, 0.5) = 0.5$.

Second, what is the truth degree of $p \to p$ in the empty theory?
It is $1$, since $\min(1, 1 - x + x) = 1$ for every $x$.

## Explanations

### L1 human

Pavelka logic attaches a number to each statement: how true we know it to be, at least.
The rules then compute numbers for the conclusions.
If one premise is $0.3$ short of true and the other is $0.2$ short, the conclusion may be $0.5$ short.
The completeness theorem says that the computed numbers are the best possible.

### L2 human

We compute the provability degree of $\psi$ from $T = \{\overline{0.7} \to \varphi, \overline{0.8} \to (\varphi \to \psi)\}$.
Graded modus ponens gives $T \vdash \overline{0.5} \to \psi$, so $\lvert \psi \rvert_T \ge 0.5$.
The evaluation $e(\varphi) = 0.7$, $e(\psi) = 0.5$ is a model of $T$, so $\lVert \psi \rVert_T \le 0.5$.
Soundness gives $\lvert \psi \rvert_T \le \lVert \psi \rVert_T$, so both degrees equal $0.5$.
This is the typical pattern: a derivation for the lower bound and one model for the upper bound.
Watch out: if $r + s \le 1$, the rule gives the degree $0$, which carries no information.

### L3 human

Pavelka-style completeness is a statement about suprema of degrees, and the continuity of Łukasiewicz implication makes such suprema behave well.
Among the logics of continuous t-norms, only the Łukasiewicz t-norm, up to isomorphism, has a continuous residuum, and the Gödel and product implications jump at $x = y$.
Truth constants are also added to other [[fuzzy logics|8DH4QM6AX8]], where they are studied for expressive power rather than for this kind of completeness.
The first-order version of RPL keeps Pavelka-style completeness, while ordinary [[first-order Łukasiewicz logic|VAHH1505Z0]] has no complete recursive axiomatization.

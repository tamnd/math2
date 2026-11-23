---
tag: ZVD982MVST
kind: concept
name: Paris-Wilkie translation
aliases: [paris-wilkie-translation, propositional-translation-of-bounded-arithmetic]
msc: ["03F30", "03F20"]
topics: [RA380RWEC0]
audience: research
uses: [GE43CSZTS9, FYGWNXETVJ, TT7WT5HPN9, 05006AJ7DZ, 1Q046J0AW2]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Correspondence to propositional proof systems
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: lead section
---

## Summary

The Paris-Wilkie translation writes out a bounded statement about an unknown set as one long propositional formula for each size $n$.
For example, "every $u \le 1$ has some $v \le 1$ with $R(u, v)$" becomes the formula below, where $p_{i, j}$ stands for the atom $R(i, j)$.

$$(p_{0,0} \lor p_{0,1}) \land (p_{1,0} \lor p_{1,1})$$

In exact terms, let $\alpha$ be a new unary relation symbol, and let $A$ be a closed [[$\Delta_0$ formula|GE43CSZTS9]] of the language of arithmetic with $\alpha$.
The translation $A^{\mathrm{PW}}$ is the [[propositional formula|TT7WT5HPN9]] defined by recursion on $A$, with one variable $p_i$ for each natural number $i$.
An atom $\alpha(t)$ becomes $p_i$, where $i$ is the value of the closed term $t$.
Every other atom becomes $\top$ or $\bot$, according to its truth value in $\mathbb{N}$, and the connectives $\neg, \land, \lor$ stay as they are.
A bounded quantifier $(\forall x \le t) B(x)$ becomes the conjunction of $B(0)^{\mathrm{PW}}, \dots, B(v)^{\mathrm{PW}}$, where $v$ is the value of $t$, and $(\exists x \le t) B(x)$ becomes the disjunction of the same formulas.

For a fixed formula $A(x)$, the translations $A(n)^{\mathrm{PW}}$ have size polynomial in $n$ and constant depth.
Paris and Wilkie showed that proofs in $\mathsf{I}\Delta_0(\alpha)$ become short proofs in constant-depth Frege systems, so lower bounds in [[proof complexity|1Q046J0AW2]] give independence results for bounded arithmetic.

## Motivation

Unprovability in a weak theory is hard to show directly, because the usual tool, a nonstandard model, has to be built by hand.
Lower bounds on the size of propositional proofs are combinatorial instead, and they can be attacked with counting and random restrictions.
The translation connects the two worlds.

A sentence $\forall x \, A(x)$ with $A$ in $\Delta_0(\alpha)$ speaks about every finite part of every set $\alpha \subseteq \mathbb{N}$.
For a fixed $n$, the truth of $A(n)$ depends on finitely many values of $\alpha$, so $A(n)$ is really a statement of propositional logic.
A proof of $\forall x \, A(x)$ in [[$\mathsf{I}\Delta_0(\alpha)$|FYGWNXETVJ]] is uniform in $n$, and it unfolds into short propositional proofs of all the instances.
The main use is Ajtai's theorem on the pigeonhole principle, which returns in [[pigeonhole principles in bounded arithmetic|NJ18EZ5JBC]] and in the sub-area on propositional proof complexity.

## Notation

We write $A^{\mathrm{PW}}$ for the translation of a closed formula $A$, and $A(n)^{\mathrm{PW}}$ for the translation of the instance at the numeral for $n$.
With a binary relation symbol $R$, an atom $R(t, s)$ becomes a variable $p_{i, j}$, where $i$ and $j$ are the values of $t$ and $s$.
A new function symbol $f$ is handled the same way, with $f(t) = s$ becoming $p_{i, j}$.
The depth of a formula counts the alternations of $\bigwedge$ and $\bigvee$ along a branch, after negations are pushed to the variables.
Books use several symbols for the translation, so check which one a text uses before you compare statements.

## Remarks

### Translating a formula step by step

The atom $\alpha(2 + 3)$ becomes $p_5$, because the closed term $2 + 3$ has the value $5$.
Atoms without $\alpha$ become constants, as in the next case.
The sentence $(\exists y \le 3)(y \cdot y = 4)$ becomes a disjunction over $y = 0, 1, 2, 3$:

$$\bot \lor \bot \lor \top \lor \bot.$$

Only $y = 2$ makes $y \cdot y = 4$ true, so the third disjunct is $\top$.
Check: the result is true, and so is the sentence.
The [[translation of a bounded totality statement|SP43M2PV89]] works through a formula with two quantifiers and $(n + 1)^2$ variables.

### Why the size stays polynomial

Take $A(x) := (\forall u \le x)(\forall v \le x \cdot x)\, \alpha(u + v)$.
At $x = n$ the outer quantifier gives $n + 1$ conjuncts and the inner one gives $n^2 + 1$ each:

$$A(n)^{\mathrm{PW}} = \bigwedge_{i \le n} \bigwedge_{j \le n^2} p_{i + j}.$$

So the formula has $(n + 1)(n^2 + 1)$ occurrences of variables, which is polynomial in $n$.
In general each term of $A(n)$ has a value bounded by a polynomial in $n$, so each quantifier gives polynomial fan-in.
The number of quantifiers and connectives of $A$ is fixed, so the depth is a constant.

### The translation theorem

An assignment to the variables $p_i$ is the same as a set $X \subseteq \mathbb{N}$, restricted to the indices that occur.
By induction on $A$, the formula $A^{\mathrm{PW}}$ is true under this assignment if and only if $A$ is true in $\mathbb{N}$ with $\alpha$ read as $X$.
So if $\forall x \, A(x)$ holds for every interpretation of $\alpha$, then each $A(n)^{\mathrm{PW}}$ is a [[tautology|05006AJ7DZ]].

The theorem of Paris and Wilkie strengthens this from truth to proofs.
If $\mathsf{I}\Delta_0(\alpha) \vdash \forall x \, A(x)$, then the formulas $A(n)^{\mathrm{PW}}$ have [[bounded-depth Frege|41QJ1WEMJ3]] proofs of size polynomial in $n$.
With the axiom $\Omega_1$ added, the same method gives proofs of quasipolynomial size, $2^{(\log n)^{O(1)}}$.
Similar translations exist for Buss's relativized theories $T^i_2(\alpha)$, with quasipolynomial size and a depth that grows with $i$.

Read backwards, the theorem is a method for independence.
If the formulas $A(n)^{\mathrm{PW}}$ have no bounded-depth Frege proofs of polynomial size, then $\mathsf{I}\Delta_0(\alpha)$ does not prove $\forall x \, A(x)$.
The [[pigeonhole principle for a relation|6VHPVJ30KA]] translates to the formulas $\mathrm{PHP}^{n+1}_n$, and [[Ajtai's theorem|Q0ERK64J78]] gives exactly such a lower bound.

### What it does not translate

A formula with an unbounded quantifier, such as $\exists y \, \alpha(y)$, has no translation, because the disjunction would be infinite; the [[unbounded existential formula|FWW3GSKV70]] shows that no finite formula can do the job.
A formula $A(x)$ with a free variable has no translation by itself either.
Only its closed instances $A(n)$ have one, and the object of study is the whole family.

Cook's translation of [[Cook's theory PV|FMM44KFZQT]] is a different map.
It produces formulas of unbounded depth, and it turns proofs into proofs in the [[extended Frege system|5YSE04SHFH]].

### Watch out

Size is measured in the value $n$, not in its length.
The translation of $(\exists y \le n)\, \alpha(y)$ has $n + 1$ disjuncts, and that is exponential in the number of binary digits of $n$.
So "polynomial size" here means polynomial in $n$, which is the right measure because $n$ is the number of variables.

Do not expect a translation of a $\mathsf{PV}$ proof to have constant depth.
Constant depth comes from the bounded quantifiers of $\Delta_0$ formulas, while some polynomial-time functions, such as parity, need circuits of unbounded depth.

Do not apply the theorem to a formula without the symbol $\alpha$.
Then every atom becomes $\top$ or $\bot$, and each translation is a variable-free formula that says nothing about proof length.

### History

Paris and Wilkie introduced the translation in their paper *Counting problems in bounded arithmetic*, published in 1985.
Ajtai proved in 1988 that the formulas $\mathrm{PHP}^{n+1}_n$ have no bounded-depth Frege proofs of polynomial size, and that $\mathsf{I}\Delta_0(R)$ does not prove the pigeonhole principle for a new relation $R$.
The translation shows that the second result follows from the first.

### Try it

1. Translate $(\forall u \le 2)\, \alpha(2 \cdot u)$.
   Answer: $p_0 \land p_2 \land p_4$, since $2 \cdot u$ takes the values $0$, $2$ and $4$.
2. How many variable occurrences does $\big((\exists y \le n)\, \alpha(y)\big)^{\mathrm{PW}}$ have for $n = 1000$?
   Answer: $1001$, one for each $y$ from $0$ to $1000$, although $1000$ has only $10$ binary digits.
3. Translate $(\exists y \le 2)(y + y = 3)$.
   Answer: $\bot \lor \bot \lor \bot$, since no $y \le 2$ has $2y = 3$, and the sentence is false.

## Explanations

### L1 human

A statement about all numbers up to $n$ can be written out in full.
For example, "some number up to $3$ is in the set" becomes "$0$ is in the set, or $1$ is in the set, or $2$ is in the set, or $3$ is in the set".
Each part "$i$ is in the set" is a yes-or-no switch.
The long statement is then a formula of propositional logic with $4$ switches.
Paris and Wilkie showed that a proof of the general statement in a weak system turns into a short proof of each written-out version.

### L2 human

We translate $A(x) := (\exists y \le x)\, \alpha(y + y)$ at $x = 2$.
The instance is $A(2) = (\exists y \le 2)\, \alpha(y + y)$, and the existential quantifier becomes a disjunction over $y = 0, 1, 2$:

$$\alpha(0 + 0)^{\mathrm{PW}} \lor \alpha(1 + 1)^{\mathrm{PW}} \lor \alpha(2 + 2)^{\mathrm{PW}}.$$

The closed terms $0 + 0$, $1 + 1$ and $2 + 2$ have the values $0$, $2$ and $4$, so the translation is the following formula:

$$A(2)^{\mathrm{PW}} = p_0 \lor p_2 \lor p_4.$$

Check: this is true under an assignment exactly when the set contains an even number at most $4$, which is what $A(2)$ says.
For general $n$ the same steps give $p_0 \lor p_2 \lor \dots \lor p_{2n}$, with $n + 1$ disjuncts.
The problem shows the typical use: one reads off the size and depth of the family before one applies a lower bound for bounded-depth proofs.

### L3 human

The translation is a bridge between uniform and non-uniform reasoning, in the same way as constant-depth circuits describe the $\Delta_0$ properties of a finite set.
First-order theories correspond to propositional proof systems: $\mathsf{I}\Delta_0(\alpha)$ to bounded-depth Frege, the relativized theories $T^i_2(\alpha)$ to bounded-depth systems of growing depth, and $\mathsf{PV}$ to extended Frege through Cook's translation.

The main application is to [[pigeonhole principles|NJ18EZ5JBC]].
Ajtai's lower bound gives the independence of the pigeonhole principle for $R$ from $\mathsf{I}\Delta_0(R)$, and the later exponential lower bounds extend this to $T_2(R)$.
For theories without a new symbol the translations are trivial, and the corresponding questions, such as the [[separation problem|PEJQDHHX8E]], remain open.

---
tag: 5K9J8R8SCP
kind: statement
role: theorem
name: Quantified provability logic
aliases: [vardanyans-theorem, predicate-provability-logic]
msc: ["03F45", "03B45", "03D35"]
topics: [3E7M66WW6Q]
audience: research
about: [WJK0YA4GP2, D2H3S12V7X, 7CVJCQKY41]
uses: [WJK0YA4GP2, D2H3S12V7X, HACXBCM7SS, NB2BCZR40F, MFJXPAF0R0, 7CVJCQKY41, JTAH37JTHD, TN9G24VABN]
proofs: [JXRXTHBCCG]
history:
  first_stated: "Vardanyan, 1986"
  notes: "Vardanyan's proof uses ideas of Artemov, who proved in 1985 that the set of sentences true in the standard model under every realization is not arithmetical."
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: History
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
    locator: Examples
---

## Statement

Once quantifiers enter the modal language, the laws of provability in $\mathsf{PA}$ stop being axiomatizable: they form a $\Pi^0_2$-complete set.

Let $L_\square$ be the first-order modal language with countably many predicate symbols of each arity, $\neg$, $\to$, $\forall$ and $\square$, and with no function or constant symbols.
A *realization* $*$ assigns to each $n$-ary predicate symbol $P$ a formula $P^*(x_1, \dots, x_n)$ of the language of arithmetic with free variables among $x_1, \dots, x_n$.
It extends to all formulas of $L_\square$ by the following rules.

1. $(P(y_1, \dots, y_n))^* = P^*(y_1, \dots, y_n)$, with bound variables renamed when needed.
2. $(\neg \varphi)^* = \neg \varphi^*$, $(\varphi \to \psi)^* = \varphi^* \to \psi^*$ and $(\forall y \, \varphi)^* = \forall y \, \varphi^*$.
3. If $\varphi$ has the free variables $x_1, \dots, x_n$, then $(\square \varphi)^* = \mathrm{Prov}_{\mathsf{PA}}(\ulcorner \varphi^*(\dot{x}_1, \dots, \dot{x}_n) \urcorner)$, with the [[provability predicate|NB2BCZR40F]] of [[Peano arithmetic|HACXBCM7SS]].

At $k_1, \dots, k_n$, the dotted term gives the [[Gödel number|MFJXPAF0R0]] of $\varphi^*$ with the numerals of the $k_i$ in place of the $x_i$.
The *quantified provability logic of* $\mathsf{PA}$ is the following set.
$$\mathsf{QPL}(\mathsf{PA}) = \{\varphi : \varphi \text{ is a sentence of } L_\square \text{ and } \mathsf{PA} \vdash \varphi^* \text{ for every realization } * \}.$$

### The theorem and its corollary

**Theorem (Vardanyan, 1986).** The set $\mathsf{QPL}(\mathsf{PA})$ is $\Pi^0_2$-complete.
That is, it is $\Pi^0_2$ in the [[arithmetical hierarchy|7CVJCQKY41]], and every $\Pi^0_2$ subset of $\mathbb{N}$ is [[many-one reducible|JTAH37JTHD]] to it.

**Corollary.** $\mathsf{QPL}(\mathsf{PA})$ is not [[computably enumerable|TN9G24VABN]].
So no recursively axiomatized system, such as quantified $\mathsf{GL}$, has exactly these theorems.

## Remarks

### Why each hypothesis is needed

The quantifiers are what break axiomatizability.
Without $\forall$ the language is propositional modal logic, and by [[Solovay's arithmetical completeness theorem|1ZRWVDYPX0]] the formulas provable under every realization are those of $\mathsf{GL}$, a decidable set.

The theory $\mathsf{PA}$ enters the upper bound only through one property, that its set of theorems is computably enumerable.
The proof of the upper bound works for every theory with this property.

Provability, rather than truth, keeps the set low in the hierarchy.
If "$\mathsf{PA} \vdash \varphi^*$" is replaced by "$\varphi^*$ is true in $\mathbb{N}$", the set is no longer $\Pi^0_2$, and by Artemov's theorem below it is not even arithmetical.

The quantifier over all realizations supplies the outer $\forall$ of $\Pi^0_2$.
For one fixed realization $*$, the set $\{\varphi : \mathsf{PA} \vdash \varphi^*\}$ is computably enumerable, since $\varphi \mapsto \varphi^*$ is computable.

### What it gives you

[[The proof|JXRXTHBCCG]] shows in full that a $\Pi^0_2$-complete set is not $\Sigma^0_1$, and this gives the corollary.
So any recursively axiomatized system of quantified modal logic whose theorems all lie in $\mathsf{QPL}(\mathsf{PA})$ misses some sentence of $\mathsf{QPL}(\mathsf{PA})$.
The contrast with the propositional case is sharp.
Propositional $\mathsf{GL}$ is decidable and is exactly the propositional provability logic of $\mathsf{PA}$, while the quantified version is not even computably enumerable.

### The truth version

Artemov proved in 1985 that the set of sentences $\varphi$ of $L_\square$ such that $\varphi^*$ is true in $\mathbb{N}$ for every realization $*$ is not arithmetical.
So the truth version is much harder than the provability version, which sits at level $\Pi^0_2$.

### The converse

The statement is about one set, so it has no converse in the usual sense.
A related question asks whether every set that is not computably enumerable is $\Pi^0_2$-complete, and the answer is no.
The complement $\overline{K}$ of the halting set is $\Pi^0_1$ and not computably enumerable.
If it were $\Pi^0_2$-complete, every $\Pi^0_2$ set would be many-one reducible to a $\Pi^0_1$ set, and so it would be $\Pi^0_1$ itself.
But [[Post's theorem|NYJX5QXX1T]] shows that the arithmetical hierarchy is proper, so some $\Pi^0_2$ set is not $\Pi^0_1$.

### Generalizations

The upper bound holds for the quantified provability logic of every theory with a computably enumerable set of theorems, with the same proof.
The lower bound uses properties of $\mathsf{PA}$ and of the standard model, and the cited proof is written for $\mathsf{PA}$.

## History

Montagna showed in 1984 that quantified $\mathsf{GL}$ is not arithmetically complete for $\mathsf{PA}$.
Artemov proved in 1985 that the logic of truth under all realizations is not arithmetical.
Vardanyan proved in 1986 that $\mathsf{QPL}(\mathsf{PA})$ is $\Pi^0_2$-complete, with a proof that uses ideas of Artemov.

## Explanations

### L1 human

For statements built from "and", "not" and "it is provable", a finite list of rules, the system $\mathsf{GL}$, captures all general laws of provability.
A computer can even decide, for each such statement, whether it is a general law.
If we also allow "for all $x$" and "there is an $x$", this breaks down.
The general laws of provability then form a set that no finite list of rules can produce.
The set has a precise level of difficulty, of the form "for every choice, there is a proof".

### L2 human

We see why the upper bound has the form "for all, there exists".

1. Take the sentence $\varphi = \forall y \, (\square P(y) \to P(y))$ of $L_\square$.
2. A realization chooses a formula $P^*(x_1)$ of arithmetic, and this choice is one natural number, its Gödel number $c$.
3. For each $c$, a program computes the sentence $\varphi^*$ from $c$.
4. "$\mathsf{PA} \vdash \varphi^*$" means "some number $y$ codes a proof of $\varphi^*$", which a program can check for each $y$.
5. So $\varphi \in \mathsf{QPL}(\mathsf{PA})$ says "for every $c$ there is $y$ such that a computable test holds", which is a $\Pi^0_2$ condition.

In fact this $\varphi$ is not in $\mathsf{QPL}(\mathsf{PA})$.
With $P^*(x_1) := (0 = 1)$, the sentence $\varphi^*$ is equivalent to the consistency of $\mathsf{PA}$, which $\mathsf{PA}$ does not prove by the [[second incompleteness theorem|4PZM5GJTR5]].
The typical use of the theorem is negative: it tells us not to look for a complete axiom system for quantified provability.
The trap is to overstate it.
Being $\Pi^0_2$-complete is more than "not computably enumerable", but it does not make the set non-arithmetical, which is Artemov's result for the truth version.

### L3 human

Vardanyan's theorem places quantified provability logic at the same level as the set $\mathrm{Tot}$ of indices of total computable functions.
The lower bound codes the totality of a program into one sentence, whose modal clauses control how a realization can read its predicate symbols.
The result shows a general pattern in [[quantified modal logic|D2H3S12V7X]]: the first-order versions of well-behaved propositional modal logics can be far from axiomatizable.
Related results concern fragments of the language, other theories, and the logic of truth, which is not arithmetical.

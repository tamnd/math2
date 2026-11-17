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

Let $\alpha$ be a new unary relation symbol, and let $A$ be a closed [[$\Delta_0$ formula|GE43CSZTS9]] of the language of arithmetic with $\alpha$.
The Paris-Wilkie translation $A^{\mathrm{PW}}$ is the [[propositional formula|TT7WT5HPN9]] defined by recursion on $A$, with one propositional variable $p_i$ for each $i \in \N$.
An atom $\alpha(t)$ becomes $p_i$, where $i$ is the value of the closed term $t$.
Every other atom becomes the constant $\top$ or $\bot$, according to its truth value in $\N$.
The connectives $\neg, \land, \lor$ stay as they are.
A bounded quantifier $(\forall x \le t) B(x)$ becomes the conjunction of $B(0)^{\mathrm{PW}}, \dots, B(v)^{\mathrm{PW}}$, where $v$ is the value of $t$, and $(\exists x \le t) B(x)$ becomes the disjunction of the same formulas.
For a formula $A(x)$ with one free variable, the translations $A(n)^{\mathrm{PW}}$ for $n \in \N$ have size polynomial in $n$ and constant depth.
The translation turns proofs in $\mathsf{I}\Delta_0(\alpha)$ into short proofs in constant-depth Frege systems, so lower bounds in [[proof complexity|1Q046J0AW2]] give independence results for bounded arithmetic.

## Motivation

A sentence $\forall x \, A(x)$ with $A$ in $\Delta_0(\alpha)$ speaks about every finite part of every set $\alpha \subseteq \N$.
For a fixed $n$, the truth of $A(n)$ depends only on finitely many values of $\alpha$, so it is a statement of propositional logic.
A proof of $\forall x \, A(x)$ in a weak theory is uniform in $n$, and Paris and Wilkie showed that it unfolds into short propositional proofs of all instances.
So a theory such as [[$\mathsf{I}\Delta_0$|FYGWNXETVJ]] corresponds to a propositional proof system, and an unprovability question becomes a question about the length of propositional proofs.
The same idea gives the correspondence between $T^i_2(\alpha)$ and proofs of depth $i + 1$.

## Notation

- $A^{\mathrm{PW}}$ for the translation of a closed formula $A$, and $A(n)^{\mathrm{PW}}$ for the translation of the instance at the numeral for $n$.
- With a new function symbol $f$, an atom $f(t) = s$ becomes a variable $p_{i, j}$, where $i$ and $j$ are the values of $t$ and $s$.
- With a binary relation symbol $R$, an atom $R(t, s)$ becomes $p_{i, j}$ in the same way.
- The depth of a formula counts the alternations of $\bigwedge$ and $\bigvee$ along a branch, with negations pushed to the variables.

## Remarks

### Examples

- The atom $\alpha(2 + 3)$ translates to $p_5$, since the closed term $2 + 3$ has the value $5$.
- The formula $(\exists y \le 3)(y \cdot y = 4)$ translates to $\bot \lor \bot \lor \top \lor \bot$, since only $y = 2$ makes the atom true. The result is a tautology.
- The formula $(\forall x \le n)(\exists y \le n) R(x, y)$ translates to $\bigwedge_{i \le n} \bigvee_{j \le n} p_{i, j}$; [[this example|SP43M2PV89]] checks each clause of the definition.
- The pigeonhole principle for a relation $R$ translates to the propositional pigeonhole formulas $\mathrm{PHP}^{n+1}_n$; [[this example|6VHPVJ30KA]] gives the computation.

### Non-examples

- A formula with an unbounded quantifier, such as $\exists y \, \alpha(y)$, has no translation: the disjunction would be infinite. [[This non-example|FWW3GSKV70]] gives the details.
- A formula $A(x)$ with a free variable has no translation by itself. Only its closed instances $A(n)$ have one, and $A(x)^{\mathrm{PW}}$ is not defined.
- Cook's translation of $\mathsf{PV}$ is a different translation: it produces formulas of unbounded depth, and proofs in the extended Frege system.

### Basic properties

- An assignment of truth values to the variables $p_i$ is the same as a set $X \subseteq \N$, restricted to the indices used. The formula $A^{\mathrm{PW}}$ is true under this assignment if and only if $A$ is true in $\N$ with $\alpha$ read as $X$. This follows by induction on $A$.
- So if $\forall x \, A(x)$ is true in $\N$ for every interpretation of $\alpha$, then each $A(n)^{\mathrm{PW}}$ is a [[tautology|05006AJ7DZ]].
- For a fixed $A(x)$, the depth of $A(n)^{\mathrm{PW}}$ is bounded by a constant, and its size is bounded by $(n + 2)^c$ for a constant $c$. The values of the terms in $A(n)$ are polynomial in $n$.
- (Paris-Wilkie.) If $\mathsf{I}\Delta_0(\alpha) \vdash \forall x \, A(x)$, then the formulas $A(n)^{\mathrm{PW}}$ have constant-depth Frege proofs of size polynomial in $n$. With the axiom $\Omega_1$ added, the proofs have quasipolynomial size.
- Buss's survey sharpens this for $T^i_2(\alpha)$: theorems that are sequents of $\Sigma^b_i(\alpha)$ and $\Pi^b_i(\alpha)$ formulas translate to proofs of depth $i + 1$, with polylogarithmic fan-in at the bottom level.
- Contrapositive: if the formulas $A(n)^{\mathrm{PW}}$ have no constant-depth Frege proofs of polynomial size, then $\mathsf{I}\Delta_0(\alpha)$ does not prove $\forall x \, A(x)$.

### History

Paris and Wilkie introduced the translation in the early 1980s, in their work on counting in bounded arithmetic.
Their paper *Counting problems in bounded arithmetic* appeared in 1985 in the Springer Lecture Notes in Mathematics, volume 1130.
Ajtai proved in 1988 that the pigeonhole principle for a new relation $R$ is unprovable in bounded arithmetic with $R$.
He also proved that the formulas $\mathrm{PHP}^{n+1}_n$ have no constant-depth Frege proofs of polynomial size, and the translation connects the two results.

### Common errors

- To translate $A(x)$ with $x$ free, or to forget that the size is measured in the value $n$ and not in its length.
- To expect the translation of a $\mathsf{PV}$ proof to have constant depth. Constant depth comes from the bounded quantifiers of $\Delta_0$ formulas, while some polynomial-time functions, such as parity, need circuits of unbounded depth.
- To use the theorem for a formula without the relation symbol $\alpha$. Then every atom is $\top$ or $\bot$, and each translation is a variable-free formula with no interest for proof length.

## Explanations

### L1 human

A statement about all numbers up to $n$ can be written out in full.
For example, "some number up to $3$ is in the set" becomes "$0$ is in the set, or $1$ is in the set, or $2$ is in the set, or $3$ is in the set".
Each part "$i$ is in the set" is a yes-or-no switch.
The long statement is then a formula of propositional logic with $4$ switches.
Paris and Wilkie showed that a proof of the general statement in a weak system turns into a short proof of each written-out version.

### L2 human

We translate $A(x) := (\exists y \le x)\, \alpha(y + y)$ at $x = 2$.

1. The instance is $A(2) = (\exists y \le 2)\, \alpha(y + y)$. The bound $2$ has the value $2$.
2. The existential quantifier becomes a disjunction over $y = 0, 1, 2$: $\alpha(0 + 0)^{\mathrm{PW}} \lor \alpha(1 + 1)^{\mathrm{PW}} \lor \alpha(2 + 2)^{\mathrm{PW}}$.
3. The closed terms $0 + 0$, $1 + 1$ and $2 + 2$ have the values $0$, $2$ and $4$.
4. So $A(2)^{\mathrm{PW}} = p_0 \lor p_2 \lor p_4$.
5. This formula is true under an assignment if and only if the corresponding set contains an even number at most $4$, which is what $A(2)$ says.

The typical use is the contrapositive of the Paris-Wilkie theorem: a proof-length lower bound for the translations shows that a theory does not prove a statement.
A trap is to measure the size in the length of $n$: the translation has about $n$ disjuncts, which is exponential in the number of digits of $n$.

### L3 human

The translation is a bridge between uniform and non-uniform proofs, in the same way as the description of $\Delta_0$ sets by constant-depth circuits.
First-order theories correspond to propositional proof systems: $\mathsf{I}\Delta_0(\alpha)$ to constant-depth Frege, $T^i_2(\alpha)$ to depth $i + 1$ proofs, and $\mathsf{PV}$ to extended Frege through Cook's translation.

The main application is to [[pigeonhole principles|NJ18EZ5JBC]]: Ajtai's theorem gives the independence of the pigeonhole principle for $R$ from $T_2(R)$.
Unprovable weak pigeonhole principles separate some relativized theories, for example $S^2_2(f)$ from $T^2_2(f)$.
The [[separation problem|PEJQDHHX8E]] for the theories without a new symbol is open.
For theories without $\alpha$, the translations are trivial, and the corresponding questions remain open.

---
tag: XAMKAB1BZM
kind: concept
name: ω-rule and infinitary derivations
msc: ["03F05", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
uses: [W72CA3R9MP, AYRZ98Y0NW, 0QFT7Z76N5, K7XDVK5854, 0DQPNJNPYK, 0YSCSX5YZC, KT50SMH3EC, PQG7VAZ1R2, 1QD0KDDGYJ]
sources:
  - url: https://en.wikipedia.org/wiki/Ω-consistent_theory
    locator: ω-logic
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Theories with proof-theoretic ordinal ε0
---

## Summary

In Peano arithmetic, the sentence $\forall x \, (0 + x = x)$ needs an induction.
Yet each instance $0 + 0 = 0$, $0 + 1 = 1$, $0 + 2 = 2$, and so on, is a true equation that a calculation checks.
The ω-rule lets a proof collect all these instances into the universal sentence in one step.
Proofs then become infinite trees, but induction disappears, cut elimination works, and the heights of the trees are ordinals that measure the proofs.

Precisely, the ω-rule is the inference with the infinitely many premises $A(\bar 0), A(\bar 1), A(\bar 2), \ldots$ and the conclusion $\forall x \, A(x)$, where $\bar n$ is the numeral for $n$.
The infinitary system $\mathrm{PA}_\infty$ derives finite sets of closed arithmetic formulas, called sequents.
Its axioms are the sequents that contain a true literal, and its rules are the rules for $\wedge$, $\vee$ and $\exists$, the ω-rule for $\forall$, and cut.
A derivation is a [[well-founded|0DQPNJNPYK]] tree, and its height is an [[ordinal|0YSCSX5YZC]].

## Motivation

In a finite [[sequent calculus|W72CA3R9MP]] for [[Peano arithmetic|0QFT7Z76N5]], the [[induction axioms|1QD0KDDGYJ]] block cut elimination, because a cut against an induction axiom cannot be pushed upward.
Gentzen handled this with a delicate reduction procedure on finite proofs.
The ω-rule removes the problem at the root: each instance of induction becomes derivable, so no induction axioms are left.

The price is that derivations are infinite.
In return, [[cut elimination|AYRZ98Y0NW]] becomes the familiar argument for pure logic, and the ordinal heights take the place of Gentzen's ordinal assignment.
This is how the upper bound $\lvert \mathrm{PA} \rvert \le \varepsilon_0$ is proved in most modern books, and the same plan, with stronger rules, drives the later analyses of impredicative theories.

## Notation

We use the one-sided calculus of Tait.
Formulas are built from literals, $s = t$ and $s \ne t$ for closed terms, by $\wedge$, $\vee$, $\forall$ and $\exists$, and $\neg A$ is defined by De Morgan's laws.
The rank $\operatorname{rk}(A)$ counts nested connectives and quantifiers: literals have rank $0$, and each $\wedge$, $\vee$, $\forall$ or $\exists$ adds $1$.
The rules, for a finite set $\Gamma$ of closed formulas, are these.

1. (Ax) $\Gamma, L$ for a true literal $L$.
2. ($\wedge$) From $\Gamma, A$ and $\Gamma, B$ infer $\Gamma, A \wedge B$.
3. ($\vee$) From $\Gamma, A$ or from $\Gamma, B$ infer $\Gamma, A \vee B$.
4. ($\exists$) From $\Gamma, A(\bar n)$ for one $n$ infer $\Gamma, \exists x \, A(x)$.
5. ($\omega$) From $\Gamma, A(\bar n)$ for every $n$ infer $\Gamma, \forall x \, A(x)$.
6. (Cut) From $\Gamma, C$ and $\Gamma, \neg C$ infer $\Gamma$.

We write $\vdash^\alpha_\rho \Gamma$ if $\Gamma$ has a derivation of height at most $\alpha$ whose cut formulas all have rank below $\rho$, so $\vdash^\alpha_0 \Gamma$ means a cut-free derivation.
Some books call the system $Z_\infty$ or $\mathrm{EA}_\infty$, and some use two-sided sequents.

## Remarks

### Three small derivations

The sentence $\forall x \, (x + 0 = x)$ has a cut-free derivation of height $1$: [[one ω-rule over axioms|A5P0CNY0GF]].
Each instance $0 + \bar n = \bar n$ is a true literal too, so $\forall x \, (0 + x = x)$ also has height $1$, although PA needs induction for it.

Every closed instance of the induction schema has a cut-free derivation of height $\omega + 5$, and the core sequent has height $\omega + 1$: see [[embedding an induction axiom|PJ5X9TN6W4]].
The heights $2n$ of the derivations for each $n$ grow without bound, so the final ω-rule lands at $\omega + 1$.

Every true closed formula $A$ has a cut-free derivation of finite height at most $\operatorname{rk}(A)$.
Choose a true disjunct for $\vee$, a true witness for $\exists$, and all instances for $\forall$, and use induction on the rank.

### What the ω-rule is not

[[Peano arithmetic is not closed under the ω-rule|A0X0W51841]]: PA proves each instance of $\operatorname{Con}(\mathrm{PA})$ but not the sentence itself.
So the ω-rule is a tool for studying PA from outside, not a rule of PA.

The [[infinitary logics|PQG7VAZ1R2]] $L_{\omega_1 \omega}$ are different again.
They allow infinitely long formulas, while the ω-rule keeps formulas finite and makes only the derivations infinite.

### The five facts behind the upper bound

These results are due to Schütte and Tait, and we cite them.

1. Soundness and completeness: $\vdash^\alpha_\rho A$ for some $\alpha$ and $\rho$ exactly when $A$ is [[true in the standard model|K7XDVK5854]].
2. Embedding: if PA proves $A(x_1, \ldots, x_k)$, then there are finite $m$ and $r$ with $\vdash^{\omega + m}_r A(\bar n_1, \ldots, \bar n_k)$ for all numerals.
3. Cut elimination: if $\vdash^\alpha_{\rho + 1} \Gamma$, then $\vdash^{\beta}_\rho \Gamma$ with $\beta = 2^\alpha$, or $\omega^\alpha$ in some books.
4. Iterating item 3 $r$ times on a height $\omega + m$ gives a cut-free height below [[epsilon nought|KT50SMH3EC]].
5. Boundedness: a cut-free derivation of height $\alpha$ of induction along a primitive recursive order $\prec$ bounds the type of $\prec$ by an ordinal computed from $\alpha$, and with item 4 this gives $\lvert \mathrm{PA} \rvert \le \varepsilon_0$.

### Watch out

The height of a derivation is not its size.
A derivation of height $1$, such as the one for $\forall x \, (x + 0 = x)$, has infinitely many leaves.

Cut elimination raises the height, and that growth is where $\varepsilon_0$ comes from.
The embedding gives only $\omega + m$, but removing cuts of rank $r$ costs about $r$ exponentials, so the result is a tower such as $2^{2^{\omega + m}}$.

### History

Hilbert proposed a rule of this kind in 1931.
Schütte used the ω-rule in 1951 to give a new proof of Gentzen's results on Peano arithmetic, with ordinal heights in place of Gentzen's reduction procedure.
The one-sided calculus is due to Tait.

### Try it

What is the height of the cut-free derivation of $\forall x \, \forall y \, (x + y = y + x)$ that the third example gives?
Each instance $\bar m + \bar n = \bar n + \bar m$ is a true literal, so one ω-rule gives each $\forall y$ with height $1$, and a second gives height $2$.

Why can a finite computer not check an ω-derivation?
A single ω-rule has infinitely many premises, so a check would need infinitely many steps.

## Explanations

### L1 human

To prove that a statement holds for every natural number, an ordinary proof gives one finite argument that covers all numbers.
The ω-rule instead allows infinitely many separate arguments, one for $0$, one for $1$, one for $2$, and so on.
With this rule every true statement about numbers can be proved, so it is too strong to use as an everyday rule.
Logicians use it as a tool: they translate ordinary proofs into infinite proofs and then measure the infinite proofs with ordinals.

### L2 human

We follow one PA-proof through the plan.
Suppose that the proof uses one induction axiom and one cut on a formula of rank $r$.
The embedding gives an infinite derivation of the end formula with height $\omega + m$ for some finite $m$ and cut bound $r + 1$:
$$\vdash^{\omega + m}_{r + 1}.$$
Each round of cut elimination lowers the cut bound by one and raises the height by one exponential.
After $r + 1$ rounds the derivation is cut-free, with height
$$2^{2^{\cdot^{\cdot^{2^{\omega + m}}}}} \quad (r + 1 \text{ powers of } 2),$$
which is still below $\varepsilon_0$, because $\varepsilon_0$ is closed under $\alpha \mapsto 2^\alpha$.
The typical use is the upper bound of an ordinal analysis: a finite proof becomes a cut-free derivation of controlled height.
Watch out: cut-free derivations are not small, since each level of cut rank removed costs one exponential.

### L3 human

The ω-rule is the first case of a pattern.
Replace a quantifier by its instances, so that the infinitary system is complete for the intended model, and then control the derivations by ordinal heights.
For impredicative theories this is not enough, because cut elimination would need derivations of uncountable height.
Buchholz's [[Ω-rule|5C4YBXQV15]] and the [[collapsing functions|8S6CT4TMB7]] of the later analyses fill this gap.
The ω-rule also connects to ω-consistency and ω-logic, and to reflection principles, which approximate the rule by finite means.

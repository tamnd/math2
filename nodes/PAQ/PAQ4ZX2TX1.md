---
tag: PAQ4ZX2TX1
kind: definition
name: Natural deduction
msc: ["03F03", "03B10", "03B05"]
topics: [TTCRX3NFNY]
audience: ug2
defines: 6KT3BJZ7D1
uses: [09K9MWD2QQ, QS0XVAN9BG, 086QKPF0A6, HYJ10AF6RT, NCDZ969V7X]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_deduction
  - url: https://en.wikipedia.org/wiki/Natural_deduction
    locator: First and higher-order extensions
  - book: isbn:9781447145578
    locator: Chapter 3
---

## Definition

Natural deduction derives formulas by trees in which each logical symbol has rules to introduce it and rules to eliminate it.

Fix a first-order language with equality.
Its formulas are built from atomic formulas and the constant $\bot$ (falsity) with the [[connectives|QS0XVAN9BG]] $\wedge$, $\vee$, $\to$ and the quantifiers $\forall$, $\exists$.
The negation $\neg \varphi$ abbreviates $\varphi \to \bot$.

A *derivation* is a finite tree of formulas, built by the rules below.
The formulas at the leaves are *assumptions*.
Some rules *discharge* assumptions: they mark leaves with a label, here $u$, written $[\varphi]^u$, and these leaves are then closed.
The other leaves are *open*.
A single formula $\varphi$ is a derivation of $\varphi$ with the open assumption $\varphi$.

The propositional rules are the following.
$$\dfrac{\varphi \qquad \psi}{\varphi \wedge \psi}\,{\wedge}\mathrm{I} \qquad \dfrac{\varphi \wedge \psi}{\varphi}\,{\wedge}\mathrm{E} \qquad \dfrac{\varphi \wedge \psi}{\psi}\,{\wedge}\mathrm{E}$$
$$\dfrac{\varphi}{\varphi \vee \psi}\,{\vee}\mathrm{I} \qquad \dfrac{\psi}{\varphi \vee \psi}\,{\vee}\mathrm{I} \qquad \dfrac{\varphi \vee \psi \qquad \begin{array}{c}[\varphi]^u \\ \vdots \\ \chi\end{array} \qquad \begin{array}{c}[\psi]^v \\ \vdots \\ \chi\end{array}}{\chi}\,{\vee}\mathrm{E}^{u,v}$$
$$\dfrac{\begin{array}{c}[\varphi]^u \\ \vdots \\ \psi\end{array}}{\varphi \to \psi}\,{\to}\mathrm{I}^u \qquad \dfrac{\varphi \qquad \varphi \to \psi}{\psi}\,{\to}\mathrm{E} \qquad \dfrac{\bot}{\varphi}\,{\bot}\mathrm{E} \qquad \dfrac{\begin{array}{c}[\neg \varphi]^u \\ \vdots \\ \bot\end{array}}{\varphi}\,\mathrm{RAA}^u$$

A rule may discharge zero, one or several leaves with the same formula.
The quantifier rules use the [[substitution|NCDZ969V7X]] $\varphi[t/x]$, and in each rule the term or variable must be substitutable for $x$ in $\varphi$.
$$\dfrac{\varphi[y/x]}{\forall x\, \varphi}\,{\forall}\mathrm{I} \qquad \dfrac{\forall x\, \varphi}{\varphi[t/x]}\,{\forall}\mathrm{E} \qquad \dfrac{\varphi[t/x]}{\exists x\, \varphi}\,{\exists}\mathrm{I} \qquad \dfrac{\exists x\, \varphi \qquad \begin{array}{c}[\varphi[y/x]]^u \\ \vdots \\ \chi\end{array}}{\chi}\,{\exists}\mathrm{E}^u$$

The variable $y$ in ${\forall}\mathrm{I}$ and ${\exists}\mathrm{E}$ is the *eigenvariable*, and it satisfies the *eigenvariable condition*:

1. In ${\forall}\mathrm{I}$, $y$ is not free in $\forall x\, \varphi$, and $y$ is not free in any open assumption of the derivation of $\varphi[y/x]$.
2. In ${\exists}\mathrm{E}$, $y$ is not free in $\exists x\, \varphi$, not free in $\chi$, and not free in any open assumption of the derivation of $\chi$ other than the discharged leaves $\varphi[y/x]$.

The rules for equality are ${=}\mathrm{I}$, which has no premises and concludes $t = t$, and ${=}\mathrm{E}$, which concludes $\varphi[t/x]$ from $s = t$ and $\varphi[s/x]$.
For a set $\Gamma$ of formulas, $\Gamma \vdash_{\mathsf{ND}} \varphi$ means that some derivation has the root $\varphi$ and all its open assumptions in $\Gamma$.

## Notation

The rule names follow Prawitz: I for introduction, E for elimination, and RAA for reductio ad absurdum, the classical rule.
Some books write ${\to}\mathrm{I}$ as ${\supset}\mathrm{I}$, and ${\bot}\mathrm{E}$ as "ex falso quodlibet" or ${\bot}_i$.
Other books take $\neg$ as primitive, with rules ${\neg}\mathrm{I}$ and ${\neg}\mathrm{E}$ that behave as ${\to}\mathrm{I}$ and ${\to}\mathrm{E}$ for $\varphi \to \bot$.
The same rules written as numbered lines with boxes for subproofs give [[Fitch-style natural deduction|2B6XC7XJA8]].

## Remarks

### Why the eigenvariable condition

Condition 1 is what makes "let $y$ be arbitrary" honest.
Here is a wrong "proof" of $\exists x\, P(x) \to \forall x\, P(x)$ that breaks it, written as a list of the tree's nodes.

1. $[\exists x\, P(x)]^1$, an assumption with label 1.
2. $[P(y)]^2$, an assumption with label 2.
3. $\forall x\, P(x)$, claimed by ${\forall}\mathrm{I}$ from line 2.
4. $\forall x\, P(x)$, by ${\exists}\mathrm{E}^2$ from lines 1 and 3, with eigenvariable $y$.
5. $\exists x\, P(x) \to \forall x\, P(x)$, by ${\to}\mathrm{I}^1$.

Line 4 is a correct use of ${\exists}\mathrm{E}$: $y$ is not free in $\exists x\, P(x)$, in $\forall x\, P(x)$ or in any other open assumption.
Line 3 is the wrong step, because the assumption $P(y)$ is still open there and contains $y$.
Check: in the structure $\{0, 1\}$ with $P$ true of $0$ only, $\exists x\, P(x)$ is true and $\forall x\, P(x)$ is false, so no correct derivation can reach line 5.

### The three parts of condition 2

Each clause of condition 2 blocks a different false conclusion.
If $y$ could be free in $\chi$, the witness name would leave its box; [[a wrong existential elimination|51AN89Q48G]] uses this to derive $\exists x\, P(x) \to \forall y\, P(y)$.
If $y$ could be free in another open assumption, the witness would be identified with an object we already know about.
If $y$ could be free in $\exists x\, \varphi$, then from $\exists x\, (x < y)$ the leaf $y < y$ would give $\exists z\, (z < z)$.
In $\mathbb{N}$ with $y = 1$ the premise is true and the conclusion is false.

A correct use looks like this.
From $\exists x\, (P(x) \wedge Q(x))$ and the leaf $[P(y) \wedge Q(y)]^1$, the rules ${\wedge}\mathrm{E}$ and ${\exists}\mathrm{I}$ give $\exists x\, P(x)$, which does not contain $y$, and ${\exists}\mathrm{E}^1$ concludes $\exists x\, P(x)$.

### Variants of the rules

Van Dalen writes ${\forall}\mathrm{I}$ with the same variable: from $\varphi$ infer $\forall x\, \varphi$, if $x$ is not free in any open assumption.
This form is equivalent to ours, because bound variables can be renamed.
Some books use fresh constants, often called parameters, in place of eigenvariables, and the condition then says that the constant does not occur in the conclusion or in the open assumptions.

Without RAA the rules give natural deduction for [[intuitionistic logic|Q11N8X99FK]], called NJ.
With RAA they give classical natural deduction, called NK.
RAA can be replaced by the law of excluded middle $\varphi \vee \neg \varphi$ as an axiom, or by double negation elimination, from $\neg \neg \varphi$ infer $\varphi$.
The rules without quantifiers, terms and equality are natural deduction for the [[propositional calculus|09K9MWD2QQ]], and the [[rules for equality|Y90Z13AXY8]] derive symmetry and transitivity of $=$ from ${=}\mathrm{I}$ and ${=}\mathrm{E}$.
The worked derivations of [[natural deduction|6KT3BJZ7D1]] put these rules to use.

## Explanations

### L1 human

Natural deduction writes down the rules that people use in a careful argument.
For each logical word there is one rule to prove a statement with it and one rule to use such a statement.
For example, to prove "$A$ and $B$" we prove $A$ and we prove $B$; from "$A$ and $B$" we may use $A$.
For "every" the rule says: prove the claim for an object about which nothing is assumed, and then it holds for every object.
For "some" the rule says: give the object a new name, and argue with that name, but do not let the name appear in the conclusion.

### L2 human

We derive $\forall x\, \neg \neg P(x)$ from the open assumption $\forall x\, P(x)$.

1. $\forall x\, P(x)$ is the open assumption.
2. $P(y)$ follows by ${\forall}\mathrm{E}$ from line 1, with $t = y$.
3. $[\neg P(y)]^1$ is a new assumption, that is, $P(y) \to \bot$.
4. $\bot$ follows by ${\to}\mathrm{E}$ from lines 2 and 3.
5. $\neg \neg P(y)$ follows by ${\to}\mathrm{I}^1$, which discharges line 3.
6. $\forall x\, \neg \neg P(x)$ follows by ${\forall}\mathrm{I}$ from line 5.
   The variable $y$ is not free in $\forall x\, \neg \neg P(x)$ or in the open assumption $\forall x\, P(x)$.

The typical use of the rules is backward: the main symbol of the goal suggests an introduction rule, and the assumptions suggest elimination rules.
Watch out: at line 6 the assumption $\neg P(y)$ is already closed, so it does not block ${\forall}\mathrm{I}$; before line 5 it would.

### L3 human

The rules come in pairs, and each elimination rule undoes its introduction rule.
Introducing a symbol and then eliminating it at once is a detour, and a derivation without detours is normal.
Prawitz proved that every derivation can be normalized, and normal derivations have the subformula property; this is the counterpart of cut elimination in the [[sequent calculus|W72CA3R9MP]].
The ${\to}$ fragment of NJ, with derivations read as terms, is the simply typed lambda calculus, as in the [[Curry-Howard correspondence|A77FER1Q5H]].

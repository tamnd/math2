---
tag: XADWEW9TNP
kind: definition
name: Algebraizable logic
msc: ["03G27"]
topics: [QYA4H5Y7VR]
audience: research
defines: CESWST3NWA
uses: [J78Y1M4GND, NCDZ969V7X, WRXEKT4NQS]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_algebraic_logic
  - book: isbn:9781848902077
---

## Definition

Fix a propositional language $\mathcal{L}$, and let $\mathrm{Fm}$ be the algebra of $\mathcal{L}$-formulas over a countable set of variables.
A *logic* is a [[consequence relation|J78Y1M4GND]] $\vdash$ on $\mathrm{Fm}$ that is structural: $\Gamma \vdash \varphi$ implies $\sigma[\Gamma] \vdash \sigma(\varphi)$ for every [[substitution|NCDZ969V7X]] $\sigma$.

For a class $K$ of $\mathcal{L}$-algebras, write $\Theta \models_K \varepsilon \approx \delta$ if for every $A \in K$ and every homomorphism $h : \mathrm{Fm} \to A$ with $h(\alpha) = h(\beta)$ for all $\alpha \approx \beta$ in $\Theta$, also $h(\varepsilon) = h(\delta)$.

A logic $\vdash$ is *algebraizable* if there are a class $K$ of $\mathcal{L}$-algebras, a set $E(x)$ of equations in one variable and a set $\Delta(x, y)$ of formulas in two variables such that, for all $\Gamma \cup \set{\varphi} \subseteq \mathrm{Fm}$:

1. (A1) $\Gamma \vdash \varphi$ iff $E[\Gamma] \models_K E(\varphi)$;
2. (A2) $x \approx y \models_K E[\Delta(x, y)]$ and $E[\Delta(x, y)] \models_K x \approx y$.

Here $E[\Gamma]$ is the set of equations $\varepsilon(\gamma) \approx \delta(\gamma)$ for $\gamma \in \Gamma$ and $\varepsilon(x) \approx \delta(x)$ in $E$.
Then $K$ is an *equivalent algebraic semantics* of $\vdash$, with *defining equations* $E$ and *equivalence formulas* $\Delta$.

## Notation

$\vdash$ is *finitely algebraizable* if $\Delta$ can be taken finite; it is *BP-algebraizable* if, in addition, $\vdash$ is finitary.
When $K$ can be taken to be a [[quasivariety|WRXEKT4NQS]], it is called the equivalent quasivariety semantics.
Often $E(x) = \set{x \approx 1}$ and $\Delta(x, y) = \set{x \to y, y \to x}$.

## Remarks

1. Condition (A1) alone says that $K$ is an algebraic semantics with defining equations $E$; (A2) adds that every equation can be translated back into formulas without loss.
2. (A1) and (A2) give the reverse translations: $\Psi \models_K \varepsilon \approx \delta$ iff $\Delta[\Psi] \vdash \Delta(\varepsilon, \delta)$, and $x \dashv\vdash \Delta[E(x)]$, where $\Delta[\Psi]$ is the union of the sets $\Delta(\alpha, \beta)$ for $\alpha \approx \beta$ in $\Psi$.
Both follow by applying (A2) to each equation and then (A1).
3. Classical logic is algebraizable with $K$ the Boolean algebras, $E(x) = \set{x \approx x \to x}$ and $\Delta(x, y) = \set{x \leftrightarrow y}$; see [[this example|X3EQTPS85Z]].
4. The conjunction and disjunction fragment of classical logic is not algebraizable; see [[this non-example|N1FSY99EQ8]].
5. A logic with no theorems is never algebraizable. By (A2) and (A1), each formula in $\Delta(x, x)$ is a theorem; and if $\Delta$ is empty, (A2) makes $K$ satisfy $x \approx y$, so by (A1) every formula is a theorem.

## Explanations

### L1 human

A logic is algebraizable if its rules of inference and the equations of some class of algebras say the same thing.
There is a translation of formulas into equations, and a translation of equations back into formulas, and each undoes the other up to equivalence.

### L2 human

1. In classical logic, translate the formula $p \to q$ into the equation $p \to q \approx 1$, that is, $p \le q$.
2. Translate an equation $s \approx t$ into the formula $s \leftrightarrow t$.
3. Translating $p$ to $p \approx 1$ and then back gives $p \leftrightarrow 1$, which is equivalent to $p$.
4. Translating $s \approx t$ to $s \leftrightarrow t$ and then to $(s \leftrightarrow t) \approx 1$ gives an equation equivalent to $s \approx t$ in every Boolean algebra.

The typical use: once both translations are found, every result about the algebras transfers to the logic.
The trap: a translation of formulas into equations alone is not enough; the translation back must also work.

---
tag: X3EQTPS85Z
kind: example
name: Classical propositional logic is algebraizable
msc: ["03G27", "03G05"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [CESWST3NWA]
uses: [XADWEW9TNP, 09K9MWD2QQ, 0XADJKM699]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_algebraic_logic
  - book: isbn:9781848902077
---

## Example

Let $\vdash$ be [[classical propositional logic|09K9MWD2QQ]] in the connectives $\land, \lor, \lnot, \to$, and let $K$ be the class of [[Boolean algebras|0XADJKM699]], with $a \to b = \lnot a \lor b$.
Put $E(x) = \set{x \approx x \to x}$ and $\Delta(x, y) = \set{x \leftrightarrow y}$.
In a Boolean algebra $a \to a = 1$, so $E(\varphi)$ says that $\varphi$ takes the value $1$.
We check [[the definition|XADWEW9TNP]].

1. (A1), soundness. Every axiom takes the value $1$ under every homomorphism into a Boolean algebra, and modus ponens preserves the value $1$, since $a = 1$ and $\lnot a \lor b = 1$ give $b = 1$. So $\Gamma \vdash \varphi$ implies $E[\Gamma] \models_K E(\varphi)$.
2. (A1), completeness. If $\Gamma \nvdash \varphi$, there is a valuation into the two-element Boolean algebra that sends all of $\Gamma$ to $1$ and $\varphi$ to $0$. So $E[\Gamma] \not\models_K E(\varphi)$.
3. (A2). In a Boolean algebra, $a \leftrightarrow b = 1$ iff $a \le b$ and $b \le a$ iff $a = b$. So $x \approx y$ and $x \leftrightarrow y \approx (x \leftrightarrow y) \to (x \leftrightarrow y)$ hold under the same homomorphisms.

So classical logic is [[algebraizable|CESWST3NWA]], with the Boolean algebras as equivalent algebraic semantics.

## Remarks

1. If the language has a constant $\top$, one can take $E(x) = \set{x \approx \top}$ instead; the choice of $E$ is unique only up to $\models_K$-equivalence.
2. $\Delta(x, y) = \set{x \to y, y \to x}$ works as well, by the same computation.
3. The theory of a set $\Gamma$ corresponds to the congruence $\set{(\varphi, \psi) : \Gamma \vdash \varphi \leftrightarrow \psi}$, and the quotient is the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of $\Gamma$.
4. Step 2 is the strong completeness theorem for classical logic, in the form with premises.

## Explanations

### L1 human

Classical logic and Boolean algebras say the same thing in two languages.
A formula follows from premises exactly when it equals $1$ in every Boolean algebra in which the premises equal $1$.

### L2 human

1. Take $\Gamma = \set{p, p \to q}$ and $\varphi = q$.
2. The translation asks: if $p = 1$ and $\lnot p \lor q = 1$, is $q = 1$?
3. Yes: $\lnot p = 0$, so $q = 1$.
4. And the equation $p \approx q$ translates back to $p \leftrightarrow q$, from which $p \vdash q$ and $q \vdash p$ follow.

The typical use: this is the model case, and the definition of algebraizability is read off from it.
The trap: the translation with premises needs the strong completeness theorem, not only completeness for theorems.

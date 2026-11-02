---
tag: ET1HPME8VV
kind: definition
name: Hilbert system
msc: [03B05, 03F03]
defines: 1MGMQX43B8
uses: [09K9MWD2QQ, 0NMG7W7Q11, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_system
---

## Definition

Consider formulas of [[propositional logic|09K9MWD2QQ]] built from variables with [[negation|029JBBF693]] $\neg$ and [[implication|0NMG7W7Q11]] $\to$.
The standard *Hilbert system* for this language has the following axioms, for all formulas $\varphi$, $\psi$, $\chi$:

1. $\varphi \to (\psi \to \varphi)$;
2. $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$;
3. $(\neg \varphi \to \neg \psi) \to (\psi \to \varphi)$.

Its only rule of inference is modus ponens: from $\varphi$ and $\varphi \to \psi$, infer $\psi$.
Let $\Gamma$ be a set of formulas.
A *derivation* of $\varphi$ from $\Gamma$ is a finite sequence of formulas that ends with $\varphi$.
Each formula in it is an axiom, a member of $\Gamma$, or follows from two earlier formulas by modus ponens.
One writes $\Gamma \vdash \varphi$ when such a derivation exists.

## Remarks

Here is a derivation of $\varphi \to \varphi$ from no hypotheses.

1. $(\varphi \to ((\varphi \to \varphi) \to \varphi)) \to ((\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi))$, axiom 2.
2. $\varphi \to ((\varphi \to \varphi) \to \varphi)$, axiom 1.
3. $(\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)$, modus ponens from lines 2 and 1.
4. $\varphi \to (\varphi \to \varphi)$, axiom 1.
5. $\varphi \to \varphi$, modus ponens from lines 4 and 3.

The sequence $\varphi, \; \varphi \to \psi$ is not a derivation of $\varphi \to \psi$ from no hypotheses: its first line is neither an axiom nor obtained by a rule.
More generally, a *Hilbert system* is any proof system of this shape: axiom schemas, few rules, and proofs as lists.
For [[predicate logic|086QKPF0A6]] one adds axioms for the quantifiers and the rule of generalization.

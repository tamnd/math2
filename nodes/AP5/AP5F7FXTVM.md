---
tag: AP5F7FXTVM
kind: concept
name: Finitary formal system
msc: ["03B22", "03F03"]
topics: [H8QZY0RZXZ]
audience: ug2
uses: [439M8B4DY2]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section F
    note: adopted
    mention: wikipedia://en/76765067#0XYB
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Formal_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Infinitary_logic
    locator: lead section
inventory: [WT89R0X3F7]
---

## Summary

A finitary formal system is one in which every proof is a finite object that a machine can check in finite time.
Consider the rule of arithmetic "from $\varphi(0), \varphi(1), \varphi(2), \dots$ infer $\forall x\, \varphi(x)$".
It is a good rule, since its conclusion is true whenever all its premises are, but a derivation that uses it is infinitely long, and no one can check it line by line.

Precisely, a [[formal system|439M8B4DY2]] is finitary when every formula is a finite string over its alphabet, every rule of inference has finitely many premises, and every derivation is a finite sequence of formulas.
In addition, it must be decidable whether a string is a formula, whether a formula is an axiom, and whether a step is an instance of a rule.
Unless we say otherwise, every formal system in mathematical logic is finitary.

## Motivation

Hilbert asked for proofs that can be checked by finite means, with no appeal to completed infinite totalities.
A derivation in a finitary system is such a proof.
Systems with infinitely long formulas or with rules of infinitely many premises are still useful, for example in proof theory, where the infinite rule above makes cut elimination for arithmetic possible.
But their derivations are infinite objects, so they answer a different question from the one Hilbert asked.

## Notation

There is no special symbol.
Some authors say "effective formal system" or "recursively axiomatized system" for the same idea, stressing the decidability conditions.

## Remarks

### Examples and non-examples

Hilbert systems, natural deduction and sequent calculi for propositional and first-order logic are finitary.
Peano arithmetic and Zermelo-Fraenkel set theory are finitary as well, although each has infinitely many axioms given by schemas, because a program can recognize an instance of a schema.

Arithmetic with the $\omega$-rule above is not finitary, because one rule has infinitely many premises.
The [[infinitary logic|PQG7VAZ1R2]] $L_{\omega_1 \omega}$ is not finitary either, because it allows the conjunction of countably many formulas, so a formula can be an infinite object.
[[True arithmetic taken as a set of axioms|9BW1F5B5GA]] has finite formulas and finite rules, but it fails the decidability condition on axioms.

### What finitariness gives

In a finitary system we can list all finite sequences of formulas and check each one, so the set of theorems is [[computably enumerable|TN9G24VABN]].
A derivation from hypotheses uses only finitely many of them, so $\Gamma \vdash \varphi$ implies $\Gamma_0 \vdash \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$.
This makes derivability a finitary [[consequence relation|J78Y1M4GND]], and it is the syntactic source of the compactness theorem.

### Watch out

"Finitary" does not mean "finitely many axioms".
Peano arithmetic has infinitely many induction axioms and is finitary, while a system with one infinitely long axiom is not.

### History

The demand for finitary methods comes from Hilbert's program of the 1920s, which asked for consistency proofs that use only finite, checkable reasoning about derivations.

## Explanations

### L1 human

A finitary formal system is a game of symbols in which every move and every proof is finite.
Each statement is a finite row of symbols, and each proof is a finite list of statements.
So a computer can check any proof in a finite time.
A rule such as "if the claim holds for 0, for 1, for 2, and so on forever, then it holds for all numbers" is not allowed, because no one can finish reading its premises.

### L2 human

Why is the set of theorems of a finitary system computably enumerable?
Order all finite strings over the alphabet by length, and within each length in dictionary order.
A finite sequence of formulas can be coded as one string with a separator symbol, so we can run through all candidate derivations in this order.
For each candidate, the decidability conditions let a program check every line, and when the check succeeds it prints the last line.
Every theorem is printed at some stage, and nothing else is.
Watch out: this procedure lists the theorems but does not decide them, because a formula that is not a theorem is never rejected.

### L3 human

Finitariness is what links formal systems to computability.
The theorems of a finitary system form a computably enumerable set, and conversely every computably enumerable set of strings is the set of theorems of some finitary system, by the construction in [[formal system|439M8B4DY2]].
Infinitary systems, such as arithmetic with the $\omega$-rule, return in [[ordinal analysis|XTTKZTYDSD]], where derivations are well-founded infinite trees and their heights measure the strength of a theory.

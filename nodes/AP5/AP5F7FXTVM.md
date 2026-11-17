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

A finitary formal system is a [[formal system|439M8B4DY2]] in which every formula is a finite string over its alphabet.
Every rule of inference has finitely many premises, and every derivation is a finite sequence of formulas.
In addition, it must be decidable whether a string is a formula, whether a formula is an axiom and whether a step is an instance of a rule.
On these pages "formal system" means a finitary formal system unless the contrary is said, and the main page for the idea is the one linked above.
Finitariness matters because it makes derivations checkable by a finite mechanical procedure, which is the point of formalization.

## Motivation

Hilbert asked for proofs that can be checked by finite means, without any appeal to infinite totalities.
A derivation in a finitary system is such a proof: a finite object that a machine can check line by line.
Systems with infinitely long formulas or rules with infinitely many premises are useful in logic, but their derivations are infinite objects and cannot be checked in this way.

## Notation

There is no special notation.
Some authors say "effective formal system" or "recursively axiomatized system" for the same idea, stressing the decidability conditions.

## Remarks

### Examples

- Hilbert systems, natural deduction and sequent calculi for propositional and first-order logic are finitary.
- Peano arithmetic and Zermelo-Fraenkel set theory, with their axiom schemas, are finitary formal systems.

### Non-examples

- Arithmetic with the $\omega$-rule, "from $\varphi(0), \varphi(1), \varphi(2), \dots$ infer $\forall x\, \varphi(x)$", is not finitary: the rule has infinitely many premises.
- The [[infinitary logic|PQG7VAZ1R2]] $L_{\omega_1 \omega}$ is not finitary: it allows conjunctions of countably many formulas, so formulas are infinite objects.

### Basic properties

- In a finitary system the set of theorems is computably enumerable, since derivations can be listed and checked one by one.
- Derivability in a finitary system is a finitary consequence relation: a derivation uses only finitely many hypotheses.

### History

The demand for finitary methods goes back to Hilbert's program of the 1920s.

### Common errors

- Thinking that "finitary" means that the system has finitely many axioms. Peano arithmetic has infinitely many axioms, given by a schema, and it is finitary.

## Explanations

### L1 human

A finitary formal system is a game of symbols in which every move and every proof is finite.
Each statement is a finite row of symbols, and each proof is a finite list of statements.
So a computer can check any proof in a finite time.

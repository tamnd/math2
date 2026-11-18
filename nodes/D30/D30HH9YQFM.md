---
tag: D30HH9YQFM
kind: example
name: A self-referential definition p ↔ ¬p is not an extension axiom
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
not_instance_of:
  - target: 5YSE04SHFH
    note: the defined variable p occurs in its defining formula ¬p, so the line is not an extension axiom, and admitting it would make the system unsound
uses: [5YSE04SHFH, J2BAR09TPF]
sources:
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: Extended Frege system
---

## Example

Suppose that a proof may use the line $p \leftrightarrow \neg p$ as an extension axiom.
Then it can prove a formula that is not a tautology.

1. $p \leftrightarrow \neg p$, the alleged extension axiom.
2. The formula $(p \leftrightarrow \neg p) \to r$ is a tautology, since its premise is false under every assignment. A fixed [[Frege system|J2BAR09TPF]] proves it.
3. $r$, by modus ponens from lines 1 and 2.

The variable $r$ is not a tautology.
So the line is not allowed: in an [[extension axiom|5YSE04SHFH]] $q \leftrightarrow \varphi$, the variable $q$ may not occur in $\varphi$.

A second condition fails in the same way.
Let $\tau$ be the variable $q$.

4. $q \leftrightarrow (r \lor \neg r)$, with $q$ new in the proof but occurring in $\tau$.
5. From line 4 and a proof of $r \lor \neg r$, Frege rules derive $q$.

The variable $q$ is not a tautology, so the extension variable must not occur in the final formula.

## Remarks

The soundness proof of extended Frege gives each extension variable the value of its definition.
For $p \leftrightarrow \neg p$ no value works, since $p$ and $\neg p$ always differ.
For line 4, the value of $q$ is forced to be $1$, but the final formula $q$ must be true for both values of $q$.

## Explanations

### L1 human

A definition of a word must not use the word itself.
"Let $p$ mean not $p$" defines nothing, because no value of $p$ fits.
A proof that accepts such a definition can prove anything.

### L2 human

We test the three conditions of an extension axiom on line 1.

1. The variable $p$ must not occur in the defining formula. It occurs in $\neg p$, so this condition fails.
2. The variable $p$ must not occur in earlier lines. Line 1 is the first line, so this condition holds.
3. The variable $p$ must not occur in the final formula $r$. This condition holds.

One failed condition is enough to reject the line.
The typical use of the example is to show why each condition is in the definition.

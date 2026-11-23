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
Then it proves a formula that is not a tautology, in three lines.

1. $p \leftrightarrow \neg p$, the would-be extension axiom.
2. $(p \leftrightarrow \neg p) \to r$.
   This is a tautology, since its premise is false under every assignment, so a fixed [[Frege system|J2BAR09TPF]] proves it.
3. $r$, by modus ponens from lines 1 and 2.

The variable $r$ is not a tautology, so the line must be forbidden.
That is why an [[extension axiom|5YSE04SHFH]] $q \leftrightarrow \varphi$ requires that $q$ not occur in $\varphi$.

A second condition fails in the same way.
Let the formula to be proved be the single variable $q$.

1. $q \leftrightarrow (r \lor \neg r)$, where $q$ is new in the proof but occurs in the final formula.
2. From line 1 and a Frege proof of $r \lor \neg r$, the Frege rules derive $q$.

The variable $q$ is not a tautology either, so the extension variable must not occur in the final formula.

## Remarks

The soundness proof of extended Frege gives each extension variable the value of its definition.
For $p \leftrightarrow \neg p$ no value works, because $p$ and $\neg p$ always differ, and so line 1 is false under every assignment.
For $q \leftrightarrow (r \lor \neg r)$ the value of $q$ is forced to be $1$, but the final formula $q$ must be true for both values of $q$.

What if we rename and write $s \leftrightarrow \neg p$ with a new variable $s$?
Then $s$ does not occur in $\neg p$, and if $s$ is not in earlier lines or in the final formula, the line is a legal extension axiom.
The definition is fine, because it names $\neg p$ without referring to itself.

## Explanations

### L1 human

A definition of a word must not use the word itself.
"Let $p$ mean not $p$" defines nothing, because no value of $p$ fits.
A proof that accepts such a definition can prove anything.

### L2 human

We test the three conditions of an extension axiom on the line $p \leftrightarrow \neg p$, in a proof of $r$.

1. The variable $p$ must not occur in the defining formula, but it occurs in $\neg p$, so this condition fails.
2. The variable $p$ must not occur in earlier lines, and line 1 is the first line, so this condition holds.
3. The variable $p$ must not occur in the final formula $r$, and it does not, so this condition holds.

One failed condition is enough to reject the line.
Watch out: the conditions are checked separately, and passing two of them does not make the line safe.

---
tag: SD7R5BDA6N
kind: example
name: A Hilbert system proof that every formula implies itself
msc: ["03B05", "03F03"]
topics: [PM1AYWABA7]
audience: ug1
instance_of: [0Y0MQYST0M]
uses: [0Y0MQYST0M, 1MGMQX43B8]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Example

"If it rains, then it rains" looks too plain to need a proof, but in a system with one rule it takes five lines.
Consider a [[Hilbert system|1MGMQX43B8]] for propositional logic whose only rule is [[modus ponens|0Y0MQYST0M]] and whose axioms include all instances of the two schemas
$$\text{(A1)}\quad \varphi \to (\psi \to \varphi), \qquad \text{(A2)}\quad (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi)).$$
We derive $p \to p$, for a propositional variable $p$, with two uses of modus ponens.

1. $(p \to ((p \to p) \to p)) \to ((p \to (p \to p)) \to (p \to p))$, by (A2) with $\varphi = p$, $\psi = p \to p$ and $\chi = p$.
2. $p \to ((p \to p) \to p)$, by (A1) with $\varphi = p$ and $\psi = p \to p$.
3. $(p \to (p \to p)) \to (p \to p)$, by modus ponens on lines 2 and 1.
   Line 2 is the antecedent of line 1.
4. $p \to (p \to p)$, by (A1) with $\varphi = p$ and $\psi = p$.
5. $p \to p$, by modus ponens on lines 4 and 3.
   Line 4 is the antecedent of line 3.

Each line is an axiom or follows from two earlier lines by modus ponens, so the list is a derivation of $p \to p$.

## Remarks

### What the example shows

Modus ponens does all the inference in a Hilbert system, and the axioms supply the implications to which it is applied.
The same five lines with any formula $\varphi$ in place of $p$ derive $\varphi \to \varphi$, so $\varphi \to \varphi$ is a theorem schema.
With the [[deduction theorem|9X08XK5RV2]] the derivation is immediate, since from the hypothesis $p$ we derive $p$ in one line.
The proof of the deduction theorem uses exactly this five-line derivation as a lemma.
Both axiom schemas hold intuitionistically, so the derivation is valid in intuitionistic logic too.

### Check line 3

Line 1 has the form $X \to Y$ with $X = p \to ((p \to p) \to p)$ and $Y = (p \to (p \to p)) \to (p \to p)$.
Line 2 is exactly $X$, so modus ponens gives $Y$, which is line 3.

### Watch out

Each use of modus ponens needs the antecedent to match symbol for symbol.
At line 3 the formula $p \to (p \to p)$ would not do, because the antecedent of line 1 is $p \to ((p \to p) \to p)$.

### Try it

Which instance of (A1) gives $q \to (p \to q)$?
Take $\varphi = q$ and $\psi = p$.

## Explanations

### L1 human

A Hilbert system is a game with a few starting sentences and one move.
The move is modus ponens: from "A" and "if A then B", write down "B".
Even the sentence "if $p$, then $p$" needs a short game: two starting sentences, one move, a third starting sentence, and a second move.

### L2 human

Matching formulas is the only skill that a Hilbert proof needs, so check each step by naming the parts.
In line 1, call the antecedent $X$ and the consequent $Y$, then confirm that line 2 is $X$ letter for letter.
Such derivations build up derived rules, such as [[hypothetical syllogism|7MT8CPCEM4]], which then shorten later proofs.

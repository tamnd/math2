---
tag: M6ZAJFQ7E2
kind: example
name: A derivation of the transitivity law in L with the deduction theorem
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
illustrates: [1MGMQX43B8, 9X08XK5RV2]
uses: [1MGMQX43B8, 9X08XK5RV2, 0Y0MQYST0M, 7MT8CPCEM4]
sources:
  - url: https://en.wikipedia.org/wiki/Deduction_theorem
    locator: Examples of deduction
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Example

With the deduction theorem, a law that takes many lines from the axioms takes three short steps.
Let $p$, $q$ and $r$ be propositional variables.
We show that the following formula is a theorem of the [[Hilbert system|1MGMQX43B8]] L:
$$(p \to q) \to ((q \to r) \to (p \to r)).$$
This formula is the law of [[hypothetical syllogism|7MT8CPCEM4]], written as one implication.
Let $\Gamma = \{ p \to q, \ q \to r, \ p \}$.

1. The following list is a derivation from $\Gamma$:
   $$\begin{array}{rll} 1. & p & \text{hypothesis} \\ 2. & p \to q & \text{hypothesis} \\ 3. & q & \text{MP, lines 1 and 2} \\ 4. & q \to r & \text{hypothesis} \\ 5. & r & \text{MP, lines 3 and 4} \end{array}$$
   So $\Gamma \vdash r$, where MP is [[modus ponens|0Y0MQYST0M]].
2. The [[deduction theorem|9X08XK5RV2]], with the hypothesis $p$ removed, gives $\{ p \to q, \ q \to r \} \vdash p \to r$.
3. The deduction theorem, with $q \to r$ removed, gives $\{ p \to q \} \vdash (q \to r) \to (p \to r)$.
4. The deduction theorem, with $p \to q$ removed, gives $\vdash (p \to q) \to ((q \to r) \to (p \to r))$.

## Remarks

### The pattern

The example shows the standard method in L.
Assume the antecedents, derive the consequent with modus ponens, and remove the hypotheses with the deduction theorem, the last antecedent first.
The same steps work with formulas $\varphi$, $\psi$, $\chi$ in place of $p$, $q$, $r$.
They give $\vdash (\varphi \to \psi) \to ((\psi \to \chi) \to (\varphi \to \chi))$.

### The same step without the deduction theorem

The deduction theorem only shortens the writing, since its proof turns each use into an explicit derivation.
For step 2, here is a derivation of $p \to r$ from $\{ p \to q, \ q \to r \}$ with axioms and MP only:
$$\begin{array}{rll} 1. & q \to r & \text{hypothesis} \\ 2. & (q \to r) \to (p \to (q \to r)) & \text{A1 with } \varphi := q \to r,\ \psi := p \\ 3. & p \to (q \to r) & \text{MP, lines 1 and 2} \\ 4. & (p \to (q \to r)) \to ((p \to q) \to (p \to r)) & \text{A2 with } \varphi := p,\ \psi := q,\ \chi := r \\ 5. & (p \to q) \to (p \to r) & \text{MP, lines 3 and 4} \\ 6. & p \to q & \text{hypothesis} \\ 7. & p \to r & \text{MP, lines 6 and 5} \end{array}$$
Check: line 4 is "line 3 $\to$ line 5", and line 5 is "line 6 $\to$ line 7".

### What changes with the order

If we remove $p \to q$ before $q \to r$ in steps 3 and 4, the result is $\vdash (q \to r) \to ((p \to q) \to (p \to r))$.
This formula is also a theorem of L.
The same law is an axiom in some other Hilbert systems, for example in the Bernays-Tarski system for the [[implicational propositional calculus|ZMVBAY7ZZD]].

### Watch out

The hypothesis removed first becomes the innermost antecedent.
If we remove $p \to q$ first in step 2, the deduction theorem gives $\{ q \to r, \ p \} \vdash (p \to q) \to r$, not $p \to r$.
Remove the hypotheses in the reverse order of the antecedents of the target formula.

### Try it

Show $\vdash p \to ((p \to q) \to q)$.
Answer: from $\{ p, \ p \to q \}$, MP gives $q$; remove $p \to q$, then $p$, with the deduction theorem.

## Explanations

### L1 human

The law says: if $p$ gives $q$, and $q$ gives $r$, then $p$ gives $r$.
In words: if rain makes the street wet, and a wet street makes it slippery, then rain makes it slippery.
A proof of this law in L from the axioms alone is long.
With the deduction theorem, we assume the three parts, use modus ponens twice, and then turn the assumptions back into "if ... then" parts.

### L2 human

We use the same pattern for $\vdash (p \to (q \to r)) \to (q \to (p \to r))$, the exchange of antecedents.
Let $\Delta = \{ p \to (q \to r), \ q, \ p \}$.

1. From $p$ and $p \to (q \to r)$, modus ponens gives $q \to r$.
2. From $q$ and $q \to r$, modus ponens gives $r$.
   So $\Delta \vdash r$.
3. We remove $p$, then $q$, then $p \to (q \to r)$ with the deduction theorem, and get the theorem.

The typical use of this method is to prove the laws of implication in L in a few lines.
The order of removal again decides the shape: removing $p \to (q \to r)$ first gives a different formula.

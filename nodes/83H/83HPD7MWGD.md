---
tag: 83HPD7MWGD
kind: example
name: Displaying a substructure in a display calculus
msc: ["03F05", "03B45"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [2Q62W689SC]
uses: [1X7D5CBXB7]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Structures and connectives
---

## Example

We work in the calculus $\mathrm{DK_t}$ of the [[definition of display calculus|1X7D5CBXB7]], with the following sequent:
$$p \circ (q \circ {*}r) \vdash s.$$
We display the variable $r$, and then the variable $p$.

### Finding the side of $r$

1. The whole antecedent $p \circ (q \circ {*}r)$ is an antecedent part.
2. So $q \circ {*}r$ is an antecedent part, by the rule for $\circ$.
3. So ${*}r$ is an antecedent part, by the rule for $\circ$ again.
4. So $r$ is a succedent part, because ${*}$ changes the side.

The display theorem therefore promises a sequent of the form $W \vdash r$.

### Applying the postulates

5. D1 in the form $X \circ Y \vdash Z \iff Y \vdash {*}X \circ Z$, with $X = p$, $Y = q \circ {*}r$ and $Z = s$, gives $q \circ {*}r \vdash {*}p \circ s$.
6. D1 in the same form, with $X = q$, $Y = {*}r$ and $Z = {*}p \circ s$, gives ${*}r \vdash {*}q \circ ({*}p \circ s)$.
7. D3 in the form $X \vdash Y \iff {*}Y \vdash {*}X$ gives ${*}({*}q \circ ({*}p \circ s)) \vdash {*}{*}r$.
8. D3 in the form $X \vdash {*}{*}Y \iff X \vdash Y$ gives ${*}({*}q \circ ({*}p \circ s)) \vdash r$, which displays $r$ as the whole succedent.

### Checking the meaning

9. The first sequent reads $(p \wedge (q \wedge \neg r)) \to s$.
10. In step 8, the antecedent reads $\neg(\neg q \vee (\neg p \vee s))$, which is equivalent to $q \wedge p \wedge \neg s$.
11. So step 8 reads $(p \wedge q \wedge \neg s) \to r$.
12. Both formulas are false exactly when $p$ and $q$ are true and $r$ and $s$ are false, so they are equivalent.

To display $p$ instead, one step is enough.

13. D1 in the form $X \circ Y \vdash Z \iff X \vdash {*}Y \circ Z$, with $X = p$ and $Y = q \circ {*}r$, gives $p \vdash {*}(q \circ {*}r) \circ s$.

## Remarks

The example shows that the cost of a display is set by the path to the target.
Each structural connective on the path to $r$ costs postulate steps: one for $\circ$ or ${\bullet}$, and two for ${*}$.
Every display postulate is invertible, so reading steps 5 to 8 from bottom to top recovers the first sequent.

What changes when a modal structure is on the path?
The connective ${\bullet}$ works in the same way.
In ${\bullet}(p \circ q) \vdash r$, D4 gives $p \circ q \vdash {\bullet}r$, and D1 gives $q \vdash {*}p \circ {\bullet}r$.
The last sequent reads $q \to (\neg p \vee \Box r)$, and the first reads $\blacklozenge(p \wedge q) \to r$.
In any Kripke model, one is true at every world exactly when the other is, because $\blacklozenge$ and $\Box$ are adjoint.

## Explanations

### L1 human

The sequent says: "$p$, $q$ and not $r$ together give $s$".
We want a form of the same claim in which $r$ stands alone on the right.
We move $p$ to the right, where it becomes "not $p$", and then move $q$ in the same way.
Finally we move the whole remaining right side to the left, and $r$ comes out alone on the right.
The result says: "$p$, $q$ and not $s$ together give $r$", which is the same claim.

### L2 human

The method has two phases.
First, find the side of the target: follow the path from the top and switch sides at each ${*}$.
Second, peel off one structural connective at a time with its postulate: D1 or D2 for $\circ$, D3 for ${*}$ and D4 for ${\bullet}$.
The typical use is before a logical rule, since a rule such as ${\neg}$L needs its formula to stand alone in the antecedent.
Watch out: $r$ is a succedent part, so no sequence of postulates produces a sequent $r \vdash W$.

---
tag: 2RRB1KHNHR
kind: example
name: A Fitch proof with a reused boxed constant
msc: ["03F03", "03B10"]
topics: [TTCRX3NFNY]
audience: ug1
not_instance_of:
  - target: 2B6XC7XJA8
    note: the second box reuses the constant c, which occurs outside it, so the list breaks the condition of existential elimination
uses: [2B6XC7XJA8, 983GZBQYT4, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/Fitch_notation
    locator: Structure
---

## Example

The following list claims to prove $\exists x\, (P(x) \wedge Q(x))$ from $\exists x\, P(x) \wedge \exists x\, Q(x)$.
```text
 1 │ ∃x P(x) ∧ ∃x Q(x)
   ├─────────────────
 2 │ ∃x P(x)                  ∧ Elim: 1
 3 │ ∃x Q(x)                  ∧ Elim: 1
 4 │ │ [c] P(c)
   │ ├─────────
 5 │ │ │ [c] Q(c)
   │ │ ├─────────
 6 │ │ │ P(c) ∧ Q(c)          ∧ Intro: 4, 5
 7 │ │ │ ∃x (P(x) ∧ Q(x))     ∃ Intro: 6
 8 │ │ ∃x (P(x) ∧ Q(x))       ∃ Elim: 3, 5-7
 9 │ ∃x (P(x) ∧ Q(x))         ∃ Elim: 2, 4-8
```
We check that the list is not a proof, and that no proof exists.

1. The rule ${\exists}$ Elim in [[Fitch-style natural deduction|2B6XC7XJA8]] requires that the boxed constant does not occur outside the box that it starts.
2. The box of lines 5 to 7 starts with $\boxed{c}$, and $c$ occurs in line 4, outside this box.
3. So line 8 breaks the condition of ${\exists}$ Elim, and the list is not a proof. Lines 2 to 4, 6, 7 and 9 are correct steps.
4. Let $\mathcal{M}$ be the [[structure|983GZBQYT4]] with domain $\{0, 1\}$, where $P$ holds of $0$ only and $Q$ holds of $1$ only.
5. $\mathcal{M} \models \exists x\, P(x)$ with witness $0$, and $\mathcal{M} \models \exists x\, Q(x)$ with witness $1$. So the premise holds in $\mathcal{M}$.
6. No element has both $P$ and $Q$, so $\mathcal{M} \not\models \exists x\, (P(x) \wedge Q(x))$.
7. By [[soundness|4A84VHDTHV]], no correct proof of the conclusion from the premise exists.

## Remarks

The error identifies the witness for $P$ with the witness for $Q$.
With a new constant $d$ in line 5, line 6 would give $P(c) \wedge Q(d)$, and ${\exists}$ Intro would not reach $\exists x\, (P(x) \wedge Q(x))$.
In a structure with one element the premise does imply the conclusion, so the countermodel needs two elements.
A proof checker for Fitch proofs rejects line 8 for this reason.

## Explanations

### L1 human

Suppose that someone in the class plays the piano and someone plays the violin.
We call the pianist $c$.
The faulty proof then calls the violinist $c$ too, as if the two were the same person.
So it concludes that someone plays both instruments, which does not follow.

### L2 human

To check the boxed constant of a box, follow two steps.

1. Find the constant $c$ in the first line of the box.
2. Search all lines outside this box, including the enclosing boxes, for $c$.

If $c$ appears outside the box, the step that closes the box is wrong.
Here step 2 finds $c$ in line 4.
A trap is to search only the main proof and not the enclosing box.

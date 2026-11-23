---
tag: C4S1DYMAQP
kind: example
name: An unfocused proof in linear logic
msc: ["03F52", "03F05"]
topics: [R10RMQCJQX]
audience: grad
not_instance_of:
  - target: AMMKNENT3R
    note: the proof applies the positive rule for tensor while the negative formula b^⊥ par ⊥ is still unprocessed, so it does not respect the inversion phase
uses: [AMMKNENT3R, H408H4WHBA]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_logic
    locator: Sequent calculus presentation
---

## Example

In one-sided MALL, a fragment of [[linear logic|H408H4WHBA]], consider the following proof of $\vdash a \otimes b, a^{\perp}, b^{\perp} \mathbin{\wp} \bot$.

1. $\vdash a, a^{\perp}$ is an initial sequent.
2. $\vdash b, b^{\perp}$ is an initial sequent.
3. Rule ${\bot}$ on step 2 gives $\vdash b, b^{\perp}, \bot$.
4. Rule ${\mathbin{\wp}}$ on step 3 gives $\vdash b, b^{\perp} \mathbin{\wp} \bot$.
5. Rule ${\otimes}$ on steps 1 and 4 gives $\vdash a \otimes b, a^{\perp}, b^{\perp} \mathbin{\wp} \bot$.

This is a correct MALL proof.
We check that it is not a focused proof in the sense of [[focusing|AMMKNENT3R]], with atoms $a, b$ positive.

6. The end sequent contains the negative formula $b^{\perp} \mathbin{\wp} \bot$.
7. In a focused proof, the inversion phase must decompose every negative formula other than a negated atom before any Decide step.
8. So a focused proof cannot apply a positive rule to $a \otimes b$ while $b^{\perp} \mathbin{\wp} \bot$ is still present.
9. Step 5 applies the positive rule ${\otimes}$ in exactly that situation, so the proof is not focused.
10. Also, the right premise of step 5 continues with ${\mathbin{\wp}}$ and ${\bot}$ on $b^{\perp} \mathbin{\wp} \bot$, instead of continuing the focus on the subformula $b$.

The focused proof of the same sequent is as follows.

11. Start from $\vdash \cdot \Uparrow a \otimes b, a^{\perp}, b^{\perp} \mathbin{\wp} \bot$. Store $a \otimes b$ and $a^{\perp}$.
12. Rule $[\mathbin{\wp}]$ gives $\vdash a \otimes b, a^{\perp} \Uparrow b^{\perp}, \bot$. Store $b^{\perp}$.
13. Rule $[\bot]$ gives $\vdash a \otimes b, a^{\perp}, b^{\perp} \Uparrow \cdot$.
14. Decide on $a \otimes b$, and split the context as $a^{\perp}$ and $b^{\perp}$ in $[\otimes]$.
15. The premises $\vdash a^{\perp} \Downarrow a$ and $\vdash b^{\perp} \Downarrow b$ are instances of $[\mathrm{init}]$.

## Remarks

The condition that fails is the order of phases: negative rules first, then one focus at a time.
The unfocused proof and the focused proof differ only by the order of rules.
Moving ${\otimes}$ above ${\mathbin{\wp}}$ and ${\bot}$, away from the end sequent, is a permutation of independent rules, because ${\otimes}$ does not act on $b^{\perp} \mathbin{\wp} \bot$.
Such permutations are the core of the proof of Andreoli's theorem: every MALL proof can be rearranged into a focused one.

## Explanations

### L1 human

This proof is correct, but it does its steps in an order that focusing does not allow.
It makes a real choice, how to split the formulas for $a \otimes b$, before it has done the safe unpacking of $b^{\perp} \mathbin{\wp} \bot$.
A focused proof always does the safe unpacking first.
The same steps in a different order give a focused proof.

### L2 human

To test whether a proof is focused, read it from the end sequent upward.

1. While a negative formula other than a negated atom is present, the next rule must be a negative rule or a Store step.
2. After a decision, the rules must stay on the focused formula and its positive subformulas.
3. Here the first rule from the bottom is ${\otimes}$ while $b^{\perp} \mathbin{\wp} \bot$ is present, so test 1 fails.

The permutation lemmas in the proof of Andreoli's theorem do exactly what steps 11 to 15 do by hand: they move negative rules below positive ones.
Watch out: an unfocused proof is not a wrong proof.
It is a valid MALL proof, only not in the focused normal form.

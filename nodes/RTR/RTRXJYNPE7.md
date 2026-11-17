---
tag: RTRXJYNPE7
kind: example
name: An additive focused proof
msc: ["03F52", "03F05"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [AMMKNENT3R]
uses: [AMMKNENT3R, H408H4WHBA]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_logic
    locator: Sequent calculus presentation
---

## Example

We use the focused system for MALL from the page on [[focusing|AMMKNENT3R]], with atoms $a, b$ positive.
We find a focused proof of
$$\vdash a^{\perp} \mathbin{\&} b^{\perp}, \ b \oplus a ,$$
which is the one-sided form of $a \oplus b \vdash b \oplus a$ in [[linear logic|H408H4WHBA]], since $(a \oplus b)^{\perp} = a^{\perp} \mathbin{\&} b^{\perp}$.
The focused goal is $\vdash \cdot \Uparrow a^{\perp} \mathbin{\&} b^{\perp}, b \oplus a$.

1. The first formula of the list has main connective $\mathbin{\&}$. Rule $[\mathbin{\&}]$ gives two premises: $\vdash \cdot \Uparrow a^{\perp}, b \oplus a$ and $\vdash \cdot \Uparrow b^{\perp}, b \oplus a$.

Left branch.

2. Store $a^{\perp}$, then store $b \oplus a$, which is positive. This gives $\vdash a^{\perp}, b \oplus a \Uparrow \cdot$.
3. Decide on $b \oplus a$, the only positive formula. This gives $\vdash a^{\perp} \Downarrow b \oplus a$.
4. Rule $[\oplus_2]$ keeps the second disjunct and gives $\vdash a^{\perp} \Downarrow a$.
5. This is an instance of $[\mathrm{init}]$.

Right branch.

6. Store $b^{\perp}$ and $b \oplus a$. This gives $\vdash b^{\perp}, b \oplus a \Uparrow \cdot$.
7. Decide on $b \oplus a$. This gives $\vdash b^{\perp} \Downarrow b \oplus a$.
8. Rule $[\oplus_1]$ keeps the first disjunct and gives $\vdash b^{\perp} \Downarrow b$.
9. This is an instance of $[\mathrm{init}]$.

We check that the other choices fail.

10. In the left branch, $[\oplus_1]$ gives $\vdash a^{\perp} \Downarrow b$. The atom $b$ is positive, so Release does not apply, and $[\mathrm{init}]$ needs the context $b^{\perp}$. No rule applies.
11. In the right branch, $[\oplus_2]$ gives $\vdash b^{\perp} \Downarrow a$, which fails for the same reason.

## Remarks

The additive rule $[\mathbin{\&}]$ copies the context into both branches, unlike $[\otimes]$, which splits it.
The two branches make different choices in $[\oplus_i]$, and the choice is made after the inversion phase has created the branches.
In an unfocused MALL proof one could apply ${\oplus}$ first, but then one branch of ${\mathbin{\&}}$ would fail.
Focusing forbids that order, because ${\oplus}$ is positive and the negative formula $a^{\perp} \mathbin{\&} b^{\perp}$ must be inverted first.

## Explanations

### L1 human

The goal says: if we have "$a$ or $b$", where we do not choose which one, then we have "$b$ or $a$".
The search first splits into two cases, one where we have $a$ and one where we have $b$.
In the first case it proves "$b$ or $a$" by choosing $a$, and in the second case by choosing $b$.
The case split comes first, and the choice comes after it.

### L2 human

The proof has three phases in each branch.

1. Inversion: $[\mathbin{\&}]$ splits the goal into two branches, and Store empties the list.
2. Decision: focus on $b \oplus a$.
3. Focus: choose the disjunct that matches the stored atom, and close with $[\mathrm{init}]$.

The typical use of this example is to show that inversion before choice avoids a wrong commitment.
A trap is to choose the disjunct of $b \oplus a$ before the case split; no single choice works in both branches.

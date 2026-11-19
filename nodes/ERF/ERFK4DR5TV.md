---
tag: ERFK4DR5TV
kind: example
name: A double negation shift in KC
msc: ["03B55"]
topics: [38EQ20GR7M]
audience: research
instance_of: [H9Z8BWRN69]
uses: [CX032ACTMZ, 5GTQ69W47T, 480TCT5CJ9, 9X08XK5RV2]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Syntactics
---

## Example

We show that $\mathsf{KC} \vdash \neg \neg (p \vee q) \to \neg \neg p \vee \neg \neg q$, and that $\mathsf{IPC}$ does not prove it.

1. Assume $\neg \neg (p \vee q)$. Take the instance $\neg p \vee \neg \neg p$ of [[weak excluded middle|CX032ACTMZ]].
2. Case $\neg \neg p$: then $\neg \neg p \vee \neg \neg q$ at once.
3. Case $\neg p$: assume $\neg q$. From $p \vee q$ we get $\bot$ in both cases, so $\neg (p \vee q)$.
4. With $\neg \neg (p \vee q)$ this gives $\bot$. So $\neg \neg q$ by the [[deduction theorem|9X08XK5RV2]], and $\neg \neg p \vee \neg \neg q$.
5. Disjunction elimination and the deduction theorem give the formula in $\mathsf{KC}$.
6. For $\mathsf{IPC}$, take the fork with root $r$ and leaves $a, b$, and put $V(p) = \set{a}$, $V(q) = \set{b}$.
7. Every world sees $a$ or $b$, where $p \vee q$ holds. So $r \Vdash \neg \neg (p \vee q)$.
8. $b \Vdash \neg p$, since $b$ is maximal and $b \nVdash p$. So $r \nVdash \neg \neg p$. Symmetrically, $a \Vdash \neg q$ and $r \nVdash \neg \neg q$.
9. So the implication fails at $r$, and [[Kripke soundness|480TCT5CJ9]] gives $\mathsf{IPC} \nvdash \neg \neg (p \vee q) \to \neg \neg p \vee \neg \neg q$.

## Remarks

Over $\mathsf{IPC}$ the formula is in fact equivalent to weak excluded middle: the instance $q := \neg p$ gives $\neg \neg (p \vee \neg p) \to \neg \neg p \vee \neg \neg \neg p$.
Its premise is a theorem of $\mathsf{IPC}$, and $\neg \neg \neg p$ is equivalent to $\neg p$.
So the formula is one more axiom for $\mathsf{KC}$, as listed by Wikipedia.

## Explanations

### L1 human

"It is not impossible that $p$ or $q$" does not, intuitionistically, give "$p$ is not impossible" or "$q$ is not impossible".
In $\mathsf{KC}$ it does, because we may first decide whether $p$ is impossible.
If it is, then $q$ can not be impossible.

### L2 human

1. Split on $\neg p \vee \neg \neg p$.
2. In the hard case, combine $\neg p$, $\neg q$ and $\neg \neg (p \vee q)$ into a contradiction.

The typical use is to recognize consequences of $\mathsf{KC}$ that look different from its axiom.
A trap: the formula is a shift of double negation over disjunction, which $\mathsf{IPC}$ proves only for conjunction.

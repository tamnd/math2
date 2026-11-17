---
tag: AFGABSCBPK
kind: example
name: The box is definable from interpretability
msc: ["03F45", "03F25"]
topics: [3E7M66WW6Q]
audience: research
instance_of: [BGKZTSQN3W]
uses: [BGKZTSQN3W, G989VP2NGP, 05006AJ7DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretability_logic
    locator: Logic ILM
---

## Example

We show that the logic $\mathsf{IL}$ of [[interpretability logic|BGKZTSQN3W]] proves
$$\square p \leftrightarrow (\neg p \rhd \bot).$$
Recall that $\lozenge \varphi$ abbreviates $\neg \square \neg \varphi$, and that $\mathsf{IL}$ contains the axiom K, $\square(\varphi \to \psi) \to (\square \varphi \to \square \psi)$, and the rule of [[necessitation|G989VP2NGP]].

The direction from left to right uses J1.

1. The formula $p \to (\neg p \to \bot)$ is a [[tautology|05006AJ7DZ]], so it is an axiom.
2. Necessitation gives $\square(p \to (\neg p \to \bot))$.
3. Axiom K and modus ponens give $\square p \to \square(\neg p \to \bot)$.
4. Axiom J1 with $\neg p$ for $p$ and $\bot$ for $q$ is $\square(\neg p \to \bot) \to \neg p \rhd \bot$.
5. Steps 3 and 4 and the tautology $(a \to b) \to ((b \to c) \to (a \to c))$ give $\square p \to (\neg p \rhd \bot)$.

The direction from right to left uses J4 and $\vdash \square \top$, where $\top$ is $\neg \bot$.

6. Axiom J4 with $\neg p$ for $p$ and $\bot$ for $q$ is $(\neg p \rhd \bot) \to (\lozenge \neg p \to \lozenge \bot)$.
7. The formula $\neg \bot$ is a tautology, and necessitation gives $\square \neg \bot$.
8. The tautology $a \to \neg \neg a$ and step 7 give $\neg \neg \square \neg \bot$, which is $\neg \lozenge \bot$.
9. From steps 6 and 8, the tautology $(a \to (b \to c)) \to (\neg c \to (a \to \neg b))$ gives $(\neg p \rhd \bot) \to \neg \lozenge \neg p$.
10. By definition, $\neg \lozenge \neg p$ is $\neg \neg \square \neg \neg p$, and the tautology $\neg \neg a \to a$ gives $\neg \lozenge \neg p \to \square \neg \neg p$.
11. The tautology $\neg \neg p \to p$, necessitation and K give $\square \neg \neg p \to \square p$.
12. Chaining steps 9, 10 and 11 gives $(\neg p \rhd \bot) \to \square p$.

Steps 5 and 12 together give $\mathsf{IL} \vdash \square p \leftrightarrow (\neg p \rhd \bot)$.
So in $\mathsf{IL}$ the operator $\square$ is definable from $\rhd$.

## Remarks

The arithmetical reading is the following.
For a sentence $A$ and a theory $T$ such as $\mathsf{PA}$, "$T$ proves $A$" is equivalent to "$T + \neg A$ interprets $T + \bot$".
Both sides say that $T + \neg A$ is inconsistent.

Because of the equivalence, one can take $\rhd$ as the only modal operator and define $\square \varphi$ as $\neg \varphi \rhd \bot$.
The proof used only J1, J4 and the rules of $\mathsf{GL}$, so the equivalence holds in every extension of $\mathsf{IL}$, such as $\mathsf{ILM}$ and $\mathsf{ILP}$.
With $p$ replaced by $\neg p$, the equivalence becomes $\square \neg p \leftrightarrow (\neg \neg p \rhd \bot)$, and so $\mathsf{IL} \vdash \lozenge p \leftrightarrow \neg(p \rhd \bot)$ after one more step with $\neg \neg p \rhd \bot \leftrightarrow p \rhd \bot$.
That last step follows from J1 and J2, because $\square(p \to \neg \neg p)$ and $\square(\neg \neg p \to p)$ give $p \rhd \neg \neg p$ and $\neg \neg p \rhd p$.

## Explanations

### L1 human

The formula says: "the theory proves $p$" means the same as "the theory with not-$p$ added can imitate a contradiction".
If adding not-$p$ makes the theory contradict itself, then $p$ must be provable.
And a contradictory theory can imitate everything, including a contradiction.
So provability can be expressed through interpretability.

### L2 human

The derivation above is the worked example.
The typical use is to read every $\square$ in a formula of $\mathsf{IL}$ as a special case of $\rhd$; for example, J4 at $q = \bot$ gives the left-to-right part of the formula for $\lozenge$.
A trap: the equivalence needs $\neg p$ on the left of $\rhd$, not $p$; the formula $\square p \leftrightarrow (p \rhd \bot)$ is not a theorem of $\mathsf{IL}$, since $p \rhd \bot$ is equivalent to $\square \neg p$.

---
tag: 1ENA02ZNAH
kind: example
name: The fork countermodel to weak excluded middle
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: grad
instance_of: [35VKJY77TY]
uses: [5GTQ69W47T, 480TCT5CJ9, CX032ACTMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Semantics of intuitionistic logic
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Semantics
---

## Example

The *fork* is the frame $W = \set{r, a, b}$ with $r \leq a$, $r \leq b$, and $a$, $b$ incomparable.
Let $V(p) = \set{a}$ and $V(q) = \set{b}$; both are up-sets.

1. $[\![p]\!] = \set{a}$ and $[\![q]\!] = \set{b}$.
2. $[\![\neg p]\!]$ is the set of worlds with no later world in $\set{a}$. Since $r \leq a$, it is $\set{b}$.
3. $[\![\neg\neg p]\!]$ is the set of worlds with no later world in $\set{b}$. Since $r \leq b$, it is $\set{a}$.
4. So $r$ forces neither $\neg p$ nor $\neg\neg p$, and $r \nVdash \neg p \vee \neg\neg p$. The [[weak excluded middle|CX032ACTMZ]] fails at $r$.
5. $[\![p \wedge q]\!] = \emptyset$, so every world forces $\neg(p \wedge q)$.
6. $[\![\neg q]\!] = \set{a}$, by the argument of step 2. So $r$ forces neither $\neg p$ nor $\neg q$.
7. So the De Morgan law $\neg(p \wedge q) \to \neg p \vee \neg q$ fails at $r$.
8. By [[soundness|480TCT5CJ9]], neither formula is a theorem of $\mathsf{IPC}$.

## Remarks

The fork is the smallest frame that is not directed: $a$ and $b$ have no common upper bound.
A frame validates $\neg p \vee \neg\neg p$ exactly when it is directed, so every chain and every frame with a top element validates it.
Adding a top world $t$ above $a$ and $b$, with $p$ and $q$ true at $t$, makes both formulas true at $r$.
With three maximal worlds above a root, the fork also refutes the Kreisel-Putnam axiom.

## Explanations

### L1 human

Picture a choice in the future: tomorrow the world goes left or right.
On the left, $p$ becomes known; on the right, $p$ becomes refuted for good.
Today we can not say "$p$ is refuted", because the left branch is still open.
We also can not say "$p$ can never be refuted", because the right branch is open too.

### L2 human

1. At $a$: the only later world is $a$, which forces $p$. So $a \Vdash \neg\neg p$.
2. At $b$: the only later world is $b$, which does not force $p$. So $b \Vdash \neg p$.
3. At $r$: the later world $a$ forces $p$, so $r \nVdash \neg p$.
4. At $r$: the later world $b$ forces $\neg p$, so $r \nVdash \neg\neg p$.

The typical use of the fork is to separate $\mathsf{IPC}$ from the logic $\mathsf{KC}$ of weak excluded middle.
A trap: the two-point chain does not refute $\neg p \vee \neg\neg p$, so a chain is never enough here.

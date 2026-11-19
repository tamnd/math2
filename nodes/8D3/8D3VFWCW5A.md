---
tag: 8D3VFWCW5A
kind: example
name: KC is a proper extension of KP
msc: ["03B55"]
topics: [38EQ20GR7M]
audience: research
not_instance_of:
  - target: 669Y0EGM3N
    note: KC contains KP but proves weak excluded middle, which KP does not prove, so KC is not Kreisel-Putnam logic
uses: [28FPR0F5WK, 6Z9TQZFKQV, 480TCT5CJ9, CX032ACTMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Syntactics, Properties
---

## Example

We show that $\neg p \vee \neg \neg p \notin \mathsf{KP}$, so $\mathsf{KP} \subsetneq \mathsf{KC}$.

1. The fork, with root $r$ and leaves $a, b$, is the Medvedev frame $M(\set{1, 2})$: $r = \set{1, 2}$, $a = \set{1}$, $b = \set{2}$.
2. By [[the Medvedev frame example|28FPR0F5WK]], the fork validates every theorem of $\mathsf{KP}$.
3. Put $V(p) = \set{a}$. Then $r \nVdash \neg p$, since $a \Vdash p$.
4. $b$ is maximal and $b \nVdash p$, so $b \Vdash \neg p$ and $r \nVdash \neg \neg p$.
5. So the fork refutes $\neg p \vee \neg \neg p$, and this formula is not in $\mathsf{KP}$, by [[Kripke soundness|480TCT5CJ9]].
6. With [[the frames with a top|6Z9TQZFKQV]], this gives $\mathsf{KP} \subsetneq \mathsf{KC}$.

## Remarks

There is also a shorter argument from the disjunction property of $\mathsf{KP}$, which we only cite.
If $\neg p \vee \neg \neg p \in \mathsf{KP}$, then $\neg p \in \mathsf{KP}$ or $\neg \neg p \in \mathsf{KP}$, and neither is a classical tautology.
The semantic argument above avoids the cited theorem.

## Explanations

### L1 human

The fork has two possible futures that never meet.
It satisfies the Kreisel-Putnam principle, but not the weak excluded middle.
So the two logics differ, and the logic with the weak excluded middle is the stronger one.

### L2 human

1. Find a frame of the smaller logic that refutes an axiom of the larger one.
2. Medvedev frames are convenient frames of $\mathsf{KP}$.

The typical use is to place $\mathsf{KP}$ in the lattice of intermediate logics.
A trap: a logic with the disjunction property can never prove $\neg p \vee \neg \neg p$, so $\mathsf{KC}$ lacks that property.

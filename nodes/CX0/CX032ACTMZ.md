---
tag: CX032ACTMZ
kind: statement
role: theorem
name: Law of the weak excluded middle
aliases: [weak-excluded-middle, weak-law-of-the-excluded-middle]
msc: ["03B05", "03B55"]
topics: [38EQ20GR7M]
audience: research
uses: [H9Z8BWRN69, 5GTQ69W47T, 480TCT5CJ9, 09PKJKA6J0]
about: [H9Z8BWRN69]
proofs: [PFRT3T5ZQ1]
sources:
  - wikipedia: en:17637@r1370685960
    locator: Law of excluded middle, section Analogous laws > Law of the weak excluded middle
    note: adopted
    mention: wikipedia://en/17637#AS5S
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Syntactics
  - url: https://eprints.illc.uva.nl/id/document/492
    locator: Section 3.3
inventory: [1BQ7ACFGDN]
---

## Statement

The *law of the weak excluded middle* is the formula $\neg p \vee \neg \neg p$.
Adding it to intuitionistic logic gives [[the logic KC|H9Z8BWRN69]], also called De Morgan logic: $\mathsf{KC} = \mathsf{IPC} + \neg p \vee \neg \neg p$.
A Kripke frame is *confluent* if $w \leq u$ and $w \leq v$ imply that $u \leq x$ and $v \leq x$ for some $x$.

**Theorem.**

1. $\mathsf{IPC} \nvdash \neg p \vee \neg \neg p$.
2. Over $\mathsf{IPC}$, the schemas $\neg \varphi \vee \neg \neg \varphi$ and $\neg (\varphi \wedge \psi) \to \neg \varphi \vee \neg \psi$ derive each other. So $\mathsf{KC} = \mathsf{IPC} + \neg (p \wedge q) \to \neg p \vee \neg q$.
3. $\neg p \vee \neg \neg p$ is valid on a frame $F$ iff $F$ is confluent. A rooted frame is confluent iff it is directed.
4. $\mathsf{KC} \vdash \varphi$ iff $\varphi$ is valid on every finite rooted frame with a greatest element. A non-theorem fails on such a frame with at most $2^n$ worlds, where $n$ is the number of subformulas of $\varphi$.

The formula in item 2 is one direction of a [[De Morgan law|09PKJKA6J0]]; $\mathsf{IPC}$ proves the converse direction, but not this one.
The proof is in [[the proof by confluent canonical models|PFRT3T5ZQ1]].

## Remarks

### Why each hypothesis is needed

1. Confluence can not be dropped: the fork has no common upper bound for its two leaves, and it refutes the law; see [[the fork countermodel|1ENA02ZNAH]].
2. In item 4, finiteness matters for the form of the frames. The infinite frame $(\mathbb{N}, \leq)$ is directed and validates the law, but it has no greatest element; see [[the natural numbers as a frame of KC|HBN6HZYJP3]].
3. Item 2 holds for the schemas, not for single instances with fixed variables. The instance $\neg (p \wedge \neg p) \to \neg p \vee \neg \neg p$ of the De Morgan law gives the weak excluded middle for $p$.

### Consequences

1. $\mathsf{KC}$ is decidable, by the bound in item 4.
2. $\mathsf{KC} \subseteq \mathsf{LC}$, since linear frames are confluent; see [[weak excluded middle in LC|F448T49KSX]].
3. $\mathsf{KC}$ proves $\neg \neg (p \vee q) \to \neg \neg p \vee \neg \neg q$; see [[the derivation|ERFK4DR5TV]].
4. $\mathsf{KC}$ does not have the disjunction property, since it proves $\neg p \vee \neg \neg p$ and neither disjunct.

### Converse

Items 2, 3 and 4 are equivalences.
Item 1 has no converse to state; the classical counterpart is that $\mathsf{CPC} \vdash \neg p \vee \neg \neg p$.

### Generalizations

1. The weak excluded middle is equivalent over $\mathsf{IPC}$ to $(p \to q) \vee (\neg p \to \neg q)$.
2. [[Jankov's theorem on KC|DEKDMG563N]]: $\mathsf{KC}$ is the largest intermediate logic with the same negation-free theorems as $\mathsf{IPC}$.
3. In a Heyting algebra, the law says that the pseudocomplement satisfies the Stone identity $\neg a \vee \neg \neg a = 1$.

## History

Jankov studied the logic $\mathsf{KC}$ in 1968, and it is often named after him.
The completeness for finite frames with a greatest element is a standard result of Kripke semantics.

## Explanations

### L1 human

The weak excluded middle says: either $p$ is impossible, or it is impossible that $p$ is impossible.
It does not decide $p$ itself.
It holds when all lines of research about $p$ meet again in a common later state.
On a branching future, where $p$ becomes known on one branch and refuted on another, it fails.

### L2 human

1. To check the law on a finite rooted frame, check whether it has a greatest element.
2. If it does, the law holds, since every world sees the top, which settles $p$.
3. To use the law in a proof, split into the case $\neg p$ and the case $\neg \neg p$.

The typical use is as the axiom of $\mathsf{KC}$, and as a test for the directedness of a frame.
A trap: the law does not give $p \vee \neg p$, and $\mathsf{KC}$ is a proper sublogic of $\mathsf{CPC}$.

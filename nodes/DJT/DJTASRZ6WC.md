---
tag: DJTASRZ6WC
kind: example
name: A reflexive symmetric frame on which axiom 4 fails
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [2QPT4KCM0Q]
uses: [2QPT4KCM0Q, FDFQFWPM4X, 0X8NMST0J2, 061J5VGSPT, 0GJZW9JFZQ, E87G6ZTMTN, VC3A2VWXND]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Take the path with three worlds, where each world sees itself and its neighbors:
$$W = \set{1, 2, 3}, \quad R = \set{(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2)}.$$
The successor sets are $R[1] = \set{1, 2}$, $R[2] = \set{1, 2, 3}$ and $R[3] = \set{2, 3}$.

1. $R$ is [[reflexive|0X8NMST0J2]] and [[symmetric|061J5VGSPT]], by the list of pairs.
2. So the frame validates the [[Brouwerian modal logic|2QPT4KCM0Q]] $\mathsf{B} = \mathsf{KTB}$, by [[common modal axiom schemata|FDFQFWPM4X]] and [[soundness|E87G6ZTMTN]].
3. $R$ is not [[transitive|0GJZW9JFZQ]]: $1 R 2$ and $2 R 3$ hold, and $1 R 3$ fails.
4. Take $V(p) = \set{1, 2}$. Then $\square p$ is true at $1$, since $R[1] = \set{1, 2}$.
5. $\square p$ is false at $2$, since $3 \in R[2]$ lacks $p$.
6. $\square\square p$ is false at $1$, since $2 \in R[1]$ makes $\square p$ false. So $\mathrm{4}$ fails at $1$, and $\mathsf{B} \nvdash \mathrm{4}$.
7. Take $V(p) = \set{1}$. Then $\lozenge p$ is true at $2$, since $1 \in R[2]$.
8. $\lozenge p$ is false at $3$, since $R[3] = \set{2, 3}$ contains no $p$-world.
9. $\square\lozenge p$ is false at $2$, since $3 \in R[2]$. So $\mathrm{5}$ fails at $2$.
10. The [[modal logic S5|VC3A2VWXND]] proves $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$, so $\mathsf{B} \subsetneq \mathsf{S5}$.

## Remarks

The example shows that symmetry and reflexivity do not give transitivity, so $\mathsf{B}$ is strictly weaker than $\mathsf{S5}$.
The relation "is at distance at most 1 on a path" is the standard source of such frames.
Examples are the similarity of colors or of lengths.
A world can see a world at distance 1, but not one at distance 2, so the relation is not transitive.
If we add the pairs $(1, 3)$ and $(3, 1)$, the relation becomes $W \times W$, and neither valuation refutes $\mathrm{4}$ or $\mathrm{5}$ any more.
If we drop the world $3$, the remaining frame on $\set{1, 2}$ is universal.
So a frame of $\mathsf{B}$ that refutes $\mathrm{4}$ needs at least three worlds.

## Explanations

### L1 human

Line up three cups of tea, each a little hotter than the one before.
A person cannot feel the difference between two neighbor cups, but can feel the difference between the first and the last.
"Cannot feel a difference" is reflexive and symmetric.
It is not transitive.
Cup 1 feels like cup 2, and cup 2 feels like cup 3, but cup 1 does not feel like cup 3.
This is exactly the frame above.

### L2 human

1. Check $\mathrm{B}$, $p \to \square\lozenge p$, at $1$ with $V(p) = \set{1}$.
2. $p$ is true at $1$.
3. Each successor of $1$, namely $1$ and $2$, sees $1$, so $\lozenge p$ is true at $1$ and at $2$.
4. So $\square\lozenge p$ is true at $1$, as symmetry predicts: every successor of $1$ sees $1$ back.

The typical use of this frame is as the small witness for $\mathsf{B} \subsetneq \mathsf{S5}$ and for $\mathsf{S4} \not\subseteq \mathsf{B}$.
A trap: $\mathsf{B}$ and $\mathsf{S4}$ are incomparable, so "weaker than $\mathsf{S5}$" does not mean "contained in $\mathsf{S4}$".

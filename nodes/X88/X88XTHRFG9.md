---
tag: X88XTHRFG9
kind: example
name: Axiom B fails on a reflexive frame that is not symmetric
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
not_instance_of:
  - target: 2QPT4KCM0Q
    note: the frame is reflexive but not symmetric, so it is not a frame of KTB
uses: [2QPT4KCM0Q, FDFQFWPM4X, 0X8NMST0J2, 061J5VGSPT, 0VABYWJWH9, E87G6ZTMTN, N60RVXSA5W]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Take the frame
$$W = \set{1, 2}, \quad R = \set{(1, 1), (2, 2), (1, 2)}, \quad V(p) = \set{1}.$$
We show that axiom $\mathrm{B}$, $p \to \square\lozenge p$, fails at $1$, so the frame is not a frame of the [[Brouwerian modal logic|2QPT4KCM0Q]].

1. $R$ is [[reflexive|0X8NMST0J2]]: $(1, 1)$ and $(2, 2)$ are in $R$.
2. $R$ is transitive: the only pair between different worlds is $(1, 2)$, and $2$ sees only $2$.
3. So $R$ is a [[preorder|0VABYWJWH9]], and the frame validates $\mathsf{T}$ and the [[modal logic S4|N60RVXSA5W]], by [[common modal axiom schemata|FDFQFWPM4X]] and [[soundness|E87G6ZTMTN]].
4. $R$ is not [[symmetric|061J5VGSPT]]: $1 R 2$ holds, and $2 R 1$ fails.
5. $p$ is true at $1$, since $1 \in V(p)$.
6. $\lozenge p$ is false at $2$, since $2$ sees only $2$, and $p$ is false at $2$.
7. $\square\lozenge p$ is false at $1$, since the successor $2$ makes $\lozenge p$ false.
8. So $\mathrm{B}$ fails at $1$, and $\mathsf{T} \nvdash \mathrm{B}$ and $\mathsf{S4} \nvdash \mathrm{B}$.

## Remarks

The example shows that the frame condition of $\mathrm{B}$ is symmetry, and reflexivity does not replace it.
The countermodel uses the valuation $V(p) = \set{1}$, the standard choice for $\mathrm{B}$: it makes $p$ true at $w$ with the smallest truth set.
Then $\square\lozenge p$ at $w$ asks that every successor of $w$ sees $w$ back, which is symmetry at $w$.
If we add the pair $(2, 1)$, the relation becomes $W \times W$, and $\lozenge p$ becomes true at $2$.
Together with [[a reflexive symmetric frame on which axiom 4 fails|DJTASRZ6WC]], the example shows that $\mathsf{B}$ and $\mathsf{S4}$ are incomparable.
The same frame also refutes $\mathrm{5}$ at $1$, since $\lozenge p$ is true at $1$ and $\square\lozenge p$ is false at $1$.

## Explanations

### L1 human

Picture two rooms, where room 1 has a door into room 2, but room 2 has no door back.
Each room can also see itself.
A lamp is on in room 1 only.
From room 1, the rule B claims that every room one can enter still has a view of a lit room.
Room 2 sees only itself, and it is dark, so the rule fails.

### L2 human

1. Take any world $w$ of any frame, and put $V(p) = \set{w}$.
2. $p$ is true at $w$.
3. $\square\lozenge p$ is true at $w$ exactly when every successor $v$ of $w$ sees a $p$-world, that is, sees $w$.
4. So $\mathrm{B}$ holds at $w$ under this valuation exactly when $w R v$ implies $v R w$.

The typical use of this frame is as the standard two-world witness that $\mathsf{S4}$ does not contain $\mathsf{B}$.
A trap: a frame of $\mathsf{T}$ that refutes $\mathrm{B}$ must have an arrow without a return arrow, so a frame with only loops never works.

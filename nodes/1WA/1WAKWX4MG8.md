---
tag: 1WAKWX4MG8
kind: example
name: The logic of frames of depth at most two
msc: ["03B55"]
topics: [38EQ20GR7M]
audience: research
instance_of: [H5NSKEP3P2]
uses: [H5NSKEP3P2, 5GTQ69W47T]
sources:
  - url: https://eprints.illc.uva.nl/id/document/492
    locator: Section 5.4, Theorem 109
---

## Example

Let $\mathrm{bd}_2 = p_2 \vee (p_2 \to p_1 \vee \neg p_1)$, and let $\mathsf{BD}_2 = \mathsf{IPC} + \mathrm{bd}_2$.
A frame has *depth at most $2$* if it has no chain $a < b < c$.
We show that $\mathsf{BD}_2$ is a proper [[intermediate logic|H5NSKEP3P2]], and that $\mathrm{bd}_2$ is valid on every frame of depth at most $2$.

1. $\mathrm{bd}_2$ is a classical tautology: if $p_2$ is false, the first disjunct fails but the second holds. So $\mathsf{BD}_2 \subseteq \mathsf{CPC}$.
2. Let $F$ have depth at most $2$, let $w$ be a world in a [[Kripke model|5GTQ69W47T]] on $F$, and suppose $w \nVdash p_2$.
3. Let $u \geq w$ with $u \Vdash p_2$. Then $u \neq w$, so $w < u$.
4. If $u < x$ for some $x$, then $w < u < x$ is a chain of length three. So $u$ is maximal.
5. At a maximal world, $u \Vdash \neg p_1$ iff $u \nVdash p_1$. So $u \Vdash p_1 \vee \neg p_1$.
6. Hence $w \Vdash p_2 \to p_1 \vee \neg p_1$, and $w \Vdash \mathrm{bd}_2$.
7. On the chain $a < b < c$, let $p_1$ hold only at $c$, and $p_2$ hold at $b$ and $c$.
8. Then $a \nVdash p_2$. Also $b \Vdash p_2$, $b \nVdash p_1$, and $b \nVdash \neg p_1$, since $c \Vdash p_1$.
9. So $a \nVdash p_2 \to p_1 \vee \neg p_1$, and $a \nVdash \mathrm{bd}_2$. By soundness, $\mathrm{bd}_2 \notin \mathsf{IPC}$, and $\mathsf{BD}_2 \neq \mathsf{IPC}$.
10. $\mathsf{BD}_2 \neq \mathsf{CPC}$, since the two-element chain has depth $2$ and refutes $p \vee \neg p$ at its root.

## Remarks

The formulas $\mathrm{bd}_1 = p_1 \vee \neg p_1$ and $\mathrm{bd}_{n+1} = p_{n+1} \vee (p_{n+1} \to \mathrm{bd}_n)$ define the logics $\mathsf{BD}_n$.
The same argument shows that $\mathrm{bd}_n$ is valid on every frame of depth at most $n$, and it fails on the chain with $n+1$ worlds.
So $\mathsf{BD}_1 = \mathsf{CPC} \supsetneq \mathsf{BD}_2 \supsetneq \mathsf{BD}_3 \supsetneq \dots$ is an infinite descending chain of intermediate logics.

## Explanations

### L1 human

A frame of depth two has only two stages: an early stage and final stages.
At a final stage every question is settled, so excluded middle holds there.
The formula $\mathrm{bd}_2$ says: either $p_2$ holds now, or as soon as $p_2$ holds, we are at a final stage.

### L2 human

1. To test $\mathrm{bd}_2$ on a frame, look for a chain of three worlds.
2. If there is none, $\mathrm{bd}_2$ is valid.
3. If there is one, make $p_2$ true from the middle world on, and $p_1$ true only at the top.

The typical use is to axiomatize the logics of bounded depth.
A trap: the formula uses two variables, and the two-world chain does not refute it.

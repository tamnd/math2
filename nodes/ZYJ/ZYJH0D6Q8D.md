---
tag: ZYJH0D6Q8D
kind: example
name: A one-world birelational frame with a reflexive relation
msc: ["03B45", "03B20"]
topics: [38EQ20GR7M]
audience: research
instance_of: [J57YRDWX3G]
uses: [J57YRDWX3G, 0QV2JS9RJ3]
sources:
  - url: https://arxiv.org/abs/2309.00532
    locator: Definition 16
---

## Example

Let $W = \set{w}$, let $\le$ be $\set{(w, w)}$, and let $R = \set{(w, w)}$.
We check that $(W, \le, R)$ is a birelational frame for [[intuitionistic modal logic|J57YRDWX3G]], and that it validates $\square p \to p$.

1. The relation $\le$ is a [[partial order|0QV2JS9RJ3]]. Its only pair is $(w, w)$, so it is reflexive, antisymmetric and transitive.
2. Condition F1 holds. The only instance is $w \le w$ and $w R w$, and $v' = w$ satisfies $w \le w$ and $w R w$.
3. Condition F2 holds. The only instance is $w R w$ and $w \le w$, and $w' = w$ satisfies $w \le w$ and $w R w$.
4. The up-sets of $(W, \le)$ are $\emptyset$ and $\set{w}$. So a valuation makes each variable true or false at $w$.
5. The only world above $w$ is $w$, and the only $R$-successor of $w$ is $w$. So $w \Vdash \square A$ iff $w \Vdash A$, and $w \Vdash \lozenge A$ iff $w \Vdash A$.
6. Suppose $w \Vdash \square p$. Taking $w' = w$ and $v = w$ in the clause for $\square$ gives $w \Vdash p$.
7. The only world $w' \ge w$ is $w$ itself, so step 6 gives $w \Vdash \square p \to p$ for every valuation.
8. In the same way, $w \Vdash p$ gives $w \Vdash \lozenge p$, because $w R w$. So $p \to \lozenge p$ is also valid.

## Remarks

The example shows that a reflexive relation $R$ validates $\square p \to p$ and $p \to \lozenge p$, as in classical modal logic.
With one world, the order $\le$ adds nothing, so the frame also validates $p \vee \neg p$, and $\square$ and $\lozenge$ both act as the identity.
Add a world $u$ with $w \le u$, and let $R = \set{(w, w), (u, u)}$.
F1 holds with $v' = u$, and F2 holds with $w' = u$, so the new frame is again birelational.
With $V(p) = \set{u}$, the world $w$ forces neither $p$ nor $\neg p$, while $\square p \to p$ is still valid.
If $R$ is made empty instead, then $\square \bot$ becomes valid and $\square p \to p$ fails at $w$ when $p$ is false there.

## Explanations

### L1 human

Imagine a world that can only see itself.
"Necessarily it rains" means "it rains in every world that I can see", and here that is only this world.
So if it is necessarily raining, then it is raining.
With only one world, nothing changes over time, so every statement is either true or false here.

### L2 human

1. Take $V(p) = \set{w}$. Then $w \Vdash p$, and by step 5, $w \Vdash \square p$ and $w \Vdash \lozenge p$.
2. Take $V(p) = \emptyset$. Then $w \not\Vdash p$, and $w \not\Vdash \square p$, because $w R w$ and $w \not\Vdash p$.
3. In both cases $\square p \to p$ holds at $w$.

The typical use of one-world frames is to check that an axiom of $\mathsf{IK}$ or $\mathsf{IS4}$ reduces to a classical tautology.
A trap: validity on this frame says nothing about intuitionistic validity, because the frame also validates the law of excluded middle.

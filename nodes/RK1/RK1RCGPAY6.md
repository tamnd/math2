---
tag: RK1RCGPAY6
kind: example
name: The pure formula i → ¬◇i defines irreflexive frames
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [NVPQ9W9DED]
uses: [NVPQ9W9DED, 0X8NMST0J2]
sources:
  - url: https://en.wikipedia.org/wiki/Hybrid_logic
    locator: lead section
---

## Example

In [[hybrid logic|NVPQ9W9DED]], let $\chi$ be the pure formula $i \to \neg \lozenge i$.
We show that for every frame $\mathfrak{F} = (W, R)$, $\chi$ is valid on $\mathfrak{F}$ if and only if $R$ is irreflexive, that is, $w R w$ for no $w$.
Here "valid on $\mathfrak{F}$" means true at every world of every hybrid model $(W, R, V)$.

1. Assume $R$ is irreflexive. Fix a hybrid valuation $V$ and a world $w$ with $\mathfrak{M}, w \models i$.
2. Then $V(i) = \{w\}$, by the truth clause for nominals.
3. If $\mathfrak{M}, w \models \lozenge i$, then $w R u$ for some $u$ with $\mathfrak{M}, u \models i$. By step 2, $u = w$, so $w R w$.
4. This contradicts irreflexivity. So $\mathfrak{M}, w \models \neg \lozenge i$, and $\chi$ holds at $w$.
5. At a world where $i$ is false, $\chi$ holds because its antecedent is false. So $\chi$ is valid on $\mathfrak{F}$.
6. Conversely, assume $w R w$ for some $w$. Choose a hybrid valuation with $V(i) = \{w\}$.
7. Then $\mathfrak{M}, w \models i$, and $w R w$ gives $\mathfrak{M}, w \models \lozenge i$.
8. So $\chi$ fails at $w$, and $\chi$ is not valid on $\mathfrak{F}$.

## Remarks

The example shows the main use of nominals in correspondence: a world can be pointed at, so a condition on one world becomes a formula.
No formula of basic modal logic defines [[reflexivity|0X8NMST0J2]] in the negative form "no world sees itself".
The reason is that frame validity of modal formulas is preserved under bounded morphic images, and the irreflexive frame $(\mathbb{N}, S)$ with $S = \{(n, n + 1)\}$ maps onto a reflexive point, see [[the successor chain maps onto a reflexive point|T3YJ84YDV4]].
If we drop the condition that $V(i)$ has one element, step 2 fails, and so does the equivalence.
Because $\chi$ is pure, the completeness theorem for pure axioms gives a complete axiom system for the irreflexive frames: $\mathcal{H}(@)$ plus $\chi$.

## Explanations

### L1 human

The name $i$ belongs to exactly one world.
The formula says "if I am the world called $i$, then I cannot see a world called $i$".
Since only I am called $i$, this says "I cannot see myself".
So the formula holds everywhere exactly when no world can see itself.

### L2 human

We check $\chi$ on the frame $W = \{0, 1\}$, $R = \{(0, 1), (1, 0)\}$, which is irreflexive.

1. Take $V(i) = \{0\}$. At $0$, the only successor is $1$, and $i$ is false at $1$. So $\lozenge i$ is false at $0$, and $\chi$ holds.
2. At $1$, $i$ is false, so $\chi$ holds.
3. Take $V(i) = \{1\}$. The same check with $0$ and $1$ swapped shows that $\chi$ holds at both worlds.
4. These are all hybrid valuations of $i$, so $\chi$ is valid on this frame.

The typical use of this argument is to read off a frame condition from a pure formula by naming the world the condition talks about.
A trap: $\chi$ can be true in one model on a reflexive frame, since $i$ may name a world that does not see itself.

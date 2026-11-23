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
We show that $\chi$ is valid on a frame $\mathfrak{F} = (W, R)$ exactly when $R$ is irreflexive, that is, when $w R w$ holds for no $w$.
Here "valid on $\mathfrak{F}$" means true at every world of every hybrid model $(W, R, V)$ on that frame.

1. Assume that $R$ is irreflexive, fix a hybrid valuation $V$, and fix a world $w$.
2. If $i$ is false at $w$, then $\chi$ holds at $w$ because its antecedent is false.
3. If $i$ is true at $w$, then $V(i) = \{w\}$, by the truth clause for nominals.
4. Suppose $\lozenge i$ were true at $w$.
   Then $w R u$ for some $u$ where $i$ holds, and step 3 gives $u = w$, so $w R w$, against irreflexivity.
   So $\neg \lozenge i$ holds at $w$, and so does $\chi$.
5. By steps 2 to 4, $\chi$ is valid on $\mathfrak{F}$.
6. Conversely, assume that $w R w$ for some $w$, and choose a hybrid valuation with $V(i) = \{w\}$.
   Then $i$ holds at $w$, and $w R w$ gives $\lozenge i$ at $w$, so $\chi$ fails at $w$.

## Remarks

The example shows the main use of nominals in correspondence: a world can be pointed at, so a condition on one world becomes a formula.
Irreflexivity is the failure of [[reflexivity|0X8NMST0J2]] at every world, and no formula of basic modal logic defines it.
Modal validity is preserved under bounded morphic images, and the irreflexive frame $(\mathbb{N}, S)$ with $S = \{(n, n + 1)\}$ maps onto a reflexive point, as [[the successor chain maps onto a reflexive point|T3YJ84YDV4]] shows.

Everything rests on the uniqueness of the world named $i$.
If $V(i)$ may have two elements, step 3 fails, and so does the equivalence.
Because $\chi$ is pure, the completeness theorem for pure axioms applies, and $\mathcal{H}(@)$ plus $\chi$ is a complete axiom system for the irreflexive frames.

## Explanations

### L1 human

The name $i$ belongs to exactly one world.
The formula says "if I am the world called $i$, then I cannot see a world called $i$".
Since only I am called $i$, this says "I cannot see myself".
So the formula holds everywhere exactly when no world can see itself.

### L2 human

We check $\chi$ on the irreflexive frame $W = \{0, 1\}$ with $R = \{(0, 1), (1, 0)\}$.
A hybrid valuation must name either $0$ or $1$ by $i$, so there are two cases.
With $V(i) = \{0\}$, the only successor of $0$ is $1$, where $i$ is false, so $\lozenge i$ fails at $0$ and $\chi$ holds there.
At $1$ the nominal is false, so $\chi$ holds there too.
With $V(i) = \{1\}$ the same check, with $0$ and $1$ swapped, gives $\chi$ at both worlds.
So $\chi$ is valid on the frame.
The typical use of this argument is to read off a frame condition from a pure formula by naming the world that the condition talks about.
Watch out: on a reflexive frame $\chi$ can still be true in one model, when $i$ names a world that does not see itself.

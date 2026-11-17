---
tag: JEA1527ZRE
kind: example
name: A bimodal frame that is not a GLP frame
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
not_instance_of:
  - target: 3EDRQJJHMT
    note: "Each relation is a GL frame and the relations decrease, but the axiom <0>p -> [1]<0>p fails, since R_1 is not empty."
uses: [3EDRQJJHMT, QQ6PZFGGB3, NGHWZ9Y7ZV, 0GJZW9JFZQ, 0DQPNJNPYK]
sources:
  - url: https://en.wikipedia.org/wiki/Japaridze%27s_polymodal_logic
    locator: Other semantics
---

## Example

A frame for the language of [[GLP|3EDRQJJHMT]] is a set $W$ with relations $R_0, R_1, \dots$, where $[n]$ is evaluated along $R_n$ as in [[Kripke semantics|NGHWZ9Y7ZV]].
A natural guess is that $\mathsf{GLP}$ is valid on a frame when each $R_n$ is a frame of $\mathsf{GL}$ and $R_{n+1} \subseteq R_n$.
This guess is false.

1. Let $W = \set{a, b}$, $R_0 = R_1 = \set{(a, b)}$, and $R_n = \emptyset$ for $n \geq 2$. Each $R_n$ is transitive and conversely well-founded, so it validates the $\mathsf{GL}$ axioms for $[n]$ by [[Löb's axiom in provability logic|QQ6PZFGGB3]]. The inclusions $R_{n+1} \subseteq R_n$ make $[m] \varphi \to [n] \varphi$ valid for $m \leq n$.
2. Let $p$ be true at $b$ only. Then $a \models \langle 0 \rangle p$, since $a R_0 b$.
3. The world $b$ has no $R_0$-successor, so $b \not\models \langle 0 \rangle p$. Since $a R_1 b$, $a \not\models [1] \langle 0 \rangle p$.
4. So the axiom $\langle 0 \rangle p \to [1] \langle 0 \rangle p$ fails at $a$, and the frame is not a frame of $\mathsf{GLP}$.

## Remarks

The failure is general: every frame that validates $\mathsf{GLP}$ has $R_1 = \emptyset$.

1. If $[0] p \to [1] p$ is valid, then $R_1 \subseteq R_0$. Otherwise take $x R_1 y$ without $x R_0 y$, and let $p$ be true exactly at the $R_0$-successors of $x$; then $x \models [0] p$ and $x \not\models [1] p$.
2. If $\langle 0 \rangle p \to [1] \langle 0 \rangle p$ is valid, then $x R_1 y$ and $x R_0 z$ imply $y R_0 z$. Otherwise let $p$ be true at $z$ only; then $x \models \langle 0 \rangle p$, $y \not\models \langle 0 \rangle p$, and $x \not\models [1] \langle 0 \rangle p$.
3. Löb's axiom for $[0]$ makes $R_0$ irreflexive, by part 3 of [[Löb's axiom in provability logic|QQ6PZFGGB3]].
4. Let $x R_1 y$. By item 1, $x R_0 y$. Item 2 with $z = y$ gives $y R_0 y$, against item 3. So $R_1 = \emptyset$.

Hence $[1] \bot$ is valid on every frame of $\mathsf{GLP}$, while $\mathsf{GLP} \nvdash [1] \bot$ by arithmetical soundness, and no class of Kripke frames characterizes $\mathsf{GLP}$.

## Explanations

### L1 human

For ordinary provability logic, pictures of points and arrows describe the logic exactly.
For $\mathsf{GLP}$, with one arrow kind for each box, this fails: the axioms force the arrows for $[1]$ to be absent.
Then every picture makes "$[1]$ proves a contradiction" true, but the logic does not prove it.

### L2 human

The typical use of this counterexample is to explain why $\mathsf{GLP}$ needs other semantics, such as topological models or special models where the axiom holds only for the formulas that matter.
A trap: the frame in steps 1 to 4 satisfies the frame conditions for the $\mathsf{GL}$ axioms and for monotonicity; only the last axiom of $\mathsf{GLP}$ fails, and that is enough.

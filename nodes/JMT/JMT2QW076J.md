---
tag: JMT2QW076J
kind: example
name: A frame without condition F1 breaks persistence of diamond
msc: ["03B45", "03B20"]
topics: [38EQ20GR7M]
audience: research
not_instance_of:
  - target: J57YRDWX3G
    note: condition F1 fails, so the formula diamond p is not persistent and an intuitionistic axiom fails
uses: [J57YRDWX3G, 0QV2JS9RJ3]
sources:
  - url: https://arxiv.org/abs/2309.00532
    locator: Definition 16
---

## Example

Let $W = \set{w, u, v}$, with the [[partial order|0QV2JS9RJ3]] whose only pair of distinct worlds is $w \le u$.
Let $R = \set{(w, v)}$, $V(p) = \set{v}$ and $V(q) = \set{u}$.
We show that $(W, \le, R)$ is not a birelational frame of [[intuitionistic modal logic|J57YRDWX3G]], and that the forcing clauses then give wrong results.

1. The relation $\le$ is a partial order: its pairs are $(w, w)$, $(u, u)$, $(v, v)$ and $(w, u)$.
2. $V(p)$ and $V(q)$ are up-sets: the only world above $v$ is $v$, and the only world above $u$ is $u$.
3. F2 holds. The only instance is $w R v$ with $v \le v$, and $w' = w$ satisfies $w \le w$ and $w R v$.
4. F1 fails. We have $w \le u$ and $w R v$, but $u$ has no $R$-successor at all.
5. $w \Vdash \lozenge p$, because $w R v$ and $v \Vdash p$.
6. $u \not\Vdash \lozenge p$, because $u$ has no $R$-successor. With $w \le u$, persistence fails for $\lozenge p$.
7. $u \Vdash q$ and $u \not\Vdash \lozenge p$, so $w \not\Vdash q \to \lozenge p$, since $w \le u$.
8. With step 5, $w \not\Vdash \lozenge p \to (q \to \lozenge p)$. This is an instance of the intuitionistic axiom $A \to (B \to A)$.

## Remarks

The example shows why F1 is part of the definition: it is exactly what makes $\lozenge A$ persistent.
Without persistence, the clause for $\to$ no longer validates intuitionistic logic, as step 8 shows.
The formula $\square p$ stays persistent on this frame, because its clause already quantifies over all later worlds.
If we add the pair $(u, v)$ to $R$, then F1 holds with $v' = v$, F2 still holds, and $u \Vdash \lozenge p$.
Another repair keeps the frame and changes the clause: $w \Vdash \lozenge A$ iff every $w' \ge w$ has an $R$-successor that forces $A$.
A clause of this form is used in the semantics of constructive $\mathsf{K}$.

## Explanations

### L1 human

Today there is a possible alternative where $p$ holds.
Tomorrow, with more information, that alternative has disappeared.
In intuitionistic logic, what we know today must stay true tomorrow, so this situation is not allowed.
The rule F1 says that every alternative visible today stays visible, in a later form, tomorrow.

### L2 human

1. Check F1 for every pair $w \le w'$ and every $R$-successor of $w$. For $w \le u$ and $w R v$, we need some $v' \ge v$ with $u R v'$.
2. The only $v' \ge v$ is $v$, and $(u, v) \notin R$. So F1 fails.
3. Then the truth of $\lozenge p$ drops from $w$ to $u$, as in steps 5 and 6.
4. The formula $\lozenge p \to (q \to \lozenge p)$ fails at $w$, so this frame is not even a model of intuitionistic propositional logic.

The typical use of this example is to test a proposed frame condition: one checks that every formula stays persistent.
A trap: checking F2 alone is not enough.
F2 is needed for the soundness of the axiom $(\lozenge A \to \square B) \to \square(A \to B)$, and F1 is needed for persistence.

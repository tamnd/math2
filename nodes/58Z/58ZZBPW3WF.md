---
tag: 58ZZBPW3WF
kind: example
name: Evaluating a PDL formula with star and composition
msc: ["03B45", "68Q60"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [VJ78A0Q22R]
uses: [VJ78A0Q22R, 05J9NWX07X]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_logic_(modal_logic)
    locator: Propositional dynamic logic (PDL)
---

## Example

Take the model of [[propositional dynamic logic|VJ78A0Q22R]] with $W = \{0, 1, 2, 3\}$, two atomic programs $a$ and $b$, and the data below.
$$R_a = \{(0, 1), (2, 3)\}, \quad R_b = \{(1, 2), (3, 0)\}, \quad V(p) = \{2\}, \quad V(q) = \{0, 1, 3\}$$
We find the worlds where $\langle (a ; b)^* \rangle p$ and $[a^*] q$ hold, by computing the relations of the programs first.

1. The pair $(w, u)$ is in $R_{a ; b}$ when $w R_a v$ and $v R_b u$ for some $v$.
   The step $0 R_a 1$ continues with $1 R_b 2$, and $2 R_a 3$ continues with $3 R_b 0$.
   There are no other $a$-steps, so $R_{a ; b} = \{(0, 2), (2, 0)\}$.
2. The star is the reflexive [[transitive closure|05J9NWX07X]] of $R_{a ; b}$.
   The composites $(0, 0)$ and $(2, 2)$ of the two pairs are already identity pairs, so $R_{(a ; b)^*} = \{(0, 0), (1, 1), (2, 2), (3, 3), (0, 2), (2, 0)\}$.
3. The formula $\langle (a ; b)^* \rangle p$ holds at $w$ when some $(a ; b)^*$-successor of $w$ is in $V(p) = \{2\}$.
   The pairs that end in $2$ start at $0$ and at $2$, so the formula holds exactly there.
4. Worlds $1$ and $3$ have no $a$-successor, so $R_a$ has no chains of two steps.
   Hence $R_{a^*} = \{(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (2, 3)\}$.
5. The formula $[a^*] q$ holds at $0$, whose $a^*$-successors $0$ and $1$ are $q$-worlds, and at $1$ and at $3$, whose only $a^*$-successors are themselves.
6. It fails at $2$, since $2$ is its own $a^*$-successor and $2 \notin V(q)$.

So the two formulas hold at these sets of worlds:
$$\|\langle (a ; b)^* \rangle p\| = \{0, 2\}, \qquad \|[a^*] q\| = \{0, 1, 3\}.$$
Check: from $0$ the program $a ; b$ runs once, $0 \to 1 \to 2$, and lands on the $p$-world.

## Remarks

The example shows each operation acting on relations: composition joins steps end to end, and the star adds the identity and all finite chains.
It also lets us test a Segerberg axiom, $[a ; b] p \leftrightarrow [a][b] p$, at world $0$.
The only $(a ; b)$-successor of $0$ is $2$, a $p$-world, so the left side holds.
The only $a$-successor of $0$ is $1$, and the only $b$-successor of $1$ is $2$, so the right side holds too.

Small changes show how the answer depends on the data.
If we add the pair $(1, 3)$ to $R_b$, then $R_{a ; b}$ gains $(0, 3)$, and $\langle (a ; b)^* \rangle p$ still holds at $0$ through world $2$.
If instead we move $p$ to world $3$, no $(a ; b)^*$-chain reaches it from another world, and the formula holds only at $3$.

## Explanations

### L1 human

Think of four rooms and two kinds of doors, $a$-doors and $b$-doors.
The program $a ; b$ means "go through an $a$-door, then through a $b$-door".
The program $(a ; b)^*$ means "do that any number of times, perhaps zero".
From room $0$ we can do $a ; b$ once and reach room $2$, where $p$ holds, so $\langle (a ; b)^* \rangle p$ is true at room $0$.

### L2 human

We confirm the value at world $1$ with the star axiom in its diamond form.
$$\langle \alpha^* \rangle \varphi \leftrightarrow \varphi \vee \langle \alpha \rangle \langle \alpha^* \rangle \varphi$$
With $\alpha = a ; b$ and $\varphi = p$, the first disjunct is false at $1$, because $p$ is false there.
The second disjunct needs an $(a ; b)$-step from $1$, and that needs an $a$-step from $1$, of which there are none.
So both disjuncts are false, and $\langle (a ; b)^* \rangle p$ is false at $1$, as step 3 found.
This is the typical use of the star axiom: unfold the star once and look one step ahead.
Watch out: on a cycle such as $0, 2, 0, \dots$ the unfolding refers back to itself, and you must take its least solution, which is what the induction axiom enforces.

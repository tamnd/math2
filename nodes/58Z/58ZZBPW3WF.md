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

Let $\mathfrak{M} = (W, R_a, R_b, V)$ be the model of [[propositional dynamic logic|VJ78A0Q22R]] with $W = \{0, 1, 2, 3\}$ and
$$R_a = \{(0, 1), (2, 3)\}, \quad R_b = \{(1, 2), (3, 0)\}, \quad V(p) = \{2\}, \quad V(q) = \{0, 1, 3\}.$$
We compute the relations of $a ; b$, $(a ; b)^*$ and $a^*$, and the worlds where $\langle (a ; b)^* \rangle p$ and $[a^*] q$ hold.

1. $R_{a ; b}$ contains $(w, u)$ when $w R_a v$ and $v R_b u$ for some $v$. From $0 R_a 1$ and $1 R_b 2$ we get $(0, 2)$. From $2 R_a 3$ and $3 R_b 0$ we get $(2, 0)$. There are no other $a$-steps, so $R_{a ; b} = \{(0, 2), (2, 0)\}$.
2. $R_{(a ; b)^*}$ is the reflexive [[transitive closure|05J9NWX07X]] of $R_{a ; b}$. It contains the four pairs $(w, w)$, the pairs $(0, 2)$ and $(2, 0)$, and their composites $(0, 0)$ and $(2, 2)$, which are already there. So $R_{(a ; b)^*} = \{(0, 0), (1, 1), (2, 2), (3, 3), (0, 2), (2, 0)\}$.
3. $\langle (a ; b)^* \rangle p$ holds at $w$ when some $u$ with $w R_{(a ; b)^*} u$ lies in $V(p) = \{2\}$. The worlds with a pair ending in $2$ are $0$ and $2$. So the formula holds exactly at $0$ and $2$.
4. $R_{a^*}$ is the reflexive transitive closure of $R_a$. The worlds $1$ and $3$ have no $a$-successor, so there are no chains of two $a$-steps, and $R_{a^*} = \{(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (2, 3)\}$.
5. $[a^*] q$ at $0$: the $a^*$-successors are $0$ and $1$, both in $V(q)$. True.
6. $[a^*] q$ at $1$: the only $a^*$-successor is $1 \in V(q)$. True.
7. $[a^*] q$ at $2$: the $a^*$-successors are $2$ and $3$, and $2 \notin V(q)$. False.
8. $[a^*] q$ at $3$: the only $a^*$-successor is $3 \in V(q)$. True.

So $\|\langle (a ; b)^* \rangle p\| = \{0, 2\}$ and $\|[a^*] q\| = \{0, 1, 3\}$.

## Remarks

The example shows how each program operation acts on relations: composition joins steps, and the star adds the identity and all finite chains.
We check one Segerberg axiom here: $[a ; b] p \leftrightarrow [a][b] p$ at $0$.
The only $(a ; b)$-successor of $0$ is $2 \in V(p)$, so the left side holds.
The only $a$-successor of $0$ is $1$, and the only $b$-successor of $1$ is $2 \in V(p)$, so the right side holds.
If we add the pair $(1, 3)$ to $R_b$, then $R_{a ; b}$ gains $(0, 3)$, and $\langle (a ; b)^* \rangle p$ still holds at $0$ through $2$.

## Explanations

### L1 human

Think of four rooms and two kinds of doors, $a$-doors and $b$-doors.
The program $a ; b$ means "go through an $a$-door, then through a $b$-door".
The program $(a ; b)^*$ means "do that any number of times, perhaps zero".
From room $0$ we can do $a ; b$ once and reach room $2$, where $p$ holds, so $\langle (a ; b)^* \rangle p$ is true at room $0$.

### L2 human

We check $\langle (a ; b)^* \rangle p$ at world $1$ with the star axiom $\langle \alpha^* \rangle \varphi \leftrightarrow \varphi \vee \langle \alpha \rangle \langle \alpha^* \rangle \varphi$.

1. $p$ is false at $1$.
2. $\langle a ; b \rangle \psi$ at $1$ needs an $a$-successor of $1$. There is none, so it is false for every $\psi$.
3. By the axiom, $\langle (a ; b)^* \rangle p$ at $1$ is equivalent to "false or false", so it is false.

This agrees with step 3 of the example.
The typical use of the star axiom is to compute a star formula by unfolding it once.
A trap: the unfolding alone does not decide a formula on a cycle; on the cycle $0, 2, 0, \dots$ the least solution is the right one, and the induction axiom gives it.

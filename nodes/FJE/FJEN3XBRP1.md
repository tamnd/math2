---
tag: FJEN3XBRP1
kind: example
name: Since and until on the integers
msc: ["03B44"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [8XB117FKKV]
uses: [8XB117FKKV, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Temporal_logic
    locator: Temporal operators
  - url: https://en.wikipedia.org/wiki/Kamp%27s_theorem
    locator: lead section
---

## Example

Take the [[temporal frame|8XB117FKKV]] $(\mathbb{Z}, <)$ of the [[integers|0C4JS9RF5M]] with this valuation:
$$V(p) = \{1, 2, 3\}, \qquad V(q) = \{-2, 4\}.$$
We use the strict clauses.
The formula $\varphi \, U \, \psi$ is true at $t$ when some $u > t$ has $\psi$ and every $v$ with $t < v < u$ has $\varphi$.
The formula $\varphi \, S \, \psi$ is true at $t$ when some $u < t$ has $\psi$ and every $v$ with $u < v < t$ has $\varphi$.

1. $p \, U \, q$ at $0$: take $u = 4$, where $q$ is true.
   The points strictly between are $1$, $2$ and $3$, and $p$ is true at each, so $p \, U \, q$ is true at $0$.
2. $p \, U \, q$ at $-1$: the only $q$-point after $-1$ is $4$.
   The point $0$ lies between them and has no $p$, so $p \, U \, q$ is false at $-1$.
3. $\neg p \, S \, q$ at $1$: take $u = -2$.
   The points strictly between are $-1$ and $0$, where $p$ is false, so $\neg p \, S \, q$ is true at $1$.
4. $\neg p \, S \, q$ at $2$: the only $q$-point before $2$ is $-2$.
   The point $1$ lies between them with $p$ true, so $\neg p \, S \, q$ is false at $2$.
5. Next as until: $\bot \, U \, p$ at $t$ asks for a $u > t$ with $p$ and no point strictly between.
   In $\mathbb{Z}$ this forces $u = t + 1$, so $\bot \, U \, p$ is true at $0$, $1$ and $2$, and false at $3$, because $p$ fails at $4$.
6. Eventually as until: $\top \, U \, q$ at $t$ asks only for some $u > t$ with $q$.
   So it is true exactly at the points $t < 4$.

## Remarks

Step 5 shows that the operator "next" $X$ is definable from $U$ on discrete time, as $X\varphi = \bot \, U \, \varphi$.
On $(\mathbb{Q}, <)$ the same formula $\bot \, U \, p$ is false at every point under every valuation, because no rational has an immediate successor.
So one formula means "next" on one frame and "false" on another.

The answers depend on the valuation in a local way.
If we change $V(p)$ to $\{0, 1, 2, 3\}$, step 2 changes: now every point between $-1$ and $4$ has $p$, so $p \, U \, q$ becomes true at $-1$.
Step 3 changes the other way: $0$ now lies between $-2$ and $1$ with $p$ true, so $\neg p \, S \, q$ becomes false at $1$.
Steps 1 and 4 keep their answers, and in step 5 the formula $\bot \, U \, p$ becomes true at $-1$ as well.

## Explanations

### L1 human

"It stays sunny until it rains" is true today when rain comes on some later day and every day in between is sunny.
Here rain comes on day 4, and days 1, 2 and 3 are sunny, so the sentence is true on day 0.
On day $-1$ it is false, because day 0 is in between and is not sunny.

### L2 human

A quick way to evaluate is to write the points $-2$ to $4$ in a row with their letters: $-2$ has $q$, then $1$, $2$ and $3$ have $p$, and $4$ has $q$.
For $U$ at $t$, scan to the right until you meet a $q$, and check every point you pass.
For $S$ at $t$, scan to the left in the same way.
The typical use of $U$ is the specification "the request stays pending until it is granted".
Watch out: with the strict clause, $p \, U \, q$ does not need $p$ at the present point, and books with the reflexive clause get different answers.
For example, $p \, U \, q$ is true at $0$ here, although $p$ is false at $0$.

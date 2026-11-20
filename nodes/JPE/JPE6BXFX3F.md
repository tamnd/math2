---
tag: JPE6BXFX3F
kind: example
name: Duplicator wins every finite game on the integers and two copies of the integers
aliases: [ehrenfeucht-fraisse-game-on-z-and-z-plus-z]
msc: ["03C07", "06A05"]
topics: [N64R1MGDBN]
audience: grad
instance_of: [2RE7YAZK8R]
uses: [2RE7YAZK8R, 1DVRN1T2Z0, 0FRXBVVR03, NJY30DQG3H, P3B1V182N4]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrenfeucht%E2%80%93Fra%C3%AFss%C3%A9_game
    locator: Definition
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Example

Let $\mathcal{A} = (\Z, <)$ and $\mathcal{B} = (\Z + \Z, <)$, the [[ordinal sum|NJY30DQG3H]] of two copies of $\Z$.
For points $u \le v$ of one order, let $d(u, v)$ be the number of steps from $u$ to $v$, and $d(u, v) = \infty$ when $u$ and $v$ lie in different copies of $\Z$.
We show that Duplicator wins the [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]] $G_n(\mathcal{A}, \mathcal{B})$ for every $n$.

Duplicator keeps this invariant when $r$ rounds are left: for all chosen $a_i, a_j$ and their partners $b_i, b_j$, $a_i < a_j \iff b_i < b_j$, and $d(a_i, a_j) = d(b_i, b_j)$ or both are at least $2^r$.

1. At the start nothing is chosen, so the invariant holds.
2. Let $r + 1$ rounds be left, and let Spoiler pick a point $a$ in $\mathcal{A}$; the case of $\mathcal{B}$ is the same. If $a$ was chosen before, Duplicator answers its partner. Otherwise let $a_j$ and $a_l$ be the nearest chosen points below and above $a$.
3. If $d(a_j, a) < 2^r$, Duplicator picks $b$ above $b_j$ with $d(b_j, b) = d(a_j, a)$. If $d(a, a_l) < 2^r$, Duplicator picks $b$ below $b_l$ in the same way.
4. In step 3, if $d(a_j, a_l) < 2^{r+1}$, then $d(b_j, b_l) = d(a_j, a_l)$, so the other distance also matches. Otherwise both remaining distances are at least $2^{r+1} - 2^r = 2^r$.
5. If $d(a_j, a) \ge 2^r$ and $d(a, a_l) \ge 2^r$, then $d(a_j, a_l) \ge 2^{r+1}$, so also $d(b_j, b_l) \ge 2^{r+1}$. Duplicator picks $b$ above $b_j$ with $d(b_j, b) = 2^r$, and then $d(b, b_l) \ge 2^r$.
6. If $a$ has no chosen point on one side, Duplicator uses the same rule with that side empty. Both orders have no endpoints, so the required point exists.
7. The distance from $a$ to any other chosen point is $d(a_j, a)$ or $d(a, a_l)$ plus a distance between chosen points, so it also matches or is at least $2^r$ on both sides.
8. When $r = 0$, the invariant gives $a_i < a_j \iff b_i < b_j$, and $a_i = a_j \iff b_i = b_j$, since equal points have distance $0$. So Duplicator wins.

## Remarks

By the [[Ehrenfeucht-Fraïssé theorem|72BMYXGFA8]], $(\Z, <)$ and $(\Z + \Z, <)$ are [[elementarily equivalent|P3B1V182N4]].
They are not partially isomorphic: in the infinite game Spoiler can first pick one point in each copy, and then more points than fit between their partners; see [[this non-example|4TAA50T7QB]].
The same strategy shows that $\Z$ is elementarily equivalent to $\Z \cdot I$ for any nonempty linear order $I$, the sum of copies of $\Z$ indexed by $I$.

## Explanations

### L1 human

Duplicator pretends that two points far apart might as well be infinitely far apart.
With $r$ rounds left, Spoiler can only measure distances up to about $2^r$, by halving the gap again and again.
So Duplicator copies short distances exactly and answers long ones with long ones.

### L2 human

We play $G_3$.

1. Round 1: Spoiler picks $(0, 0)$ in the first copy of $\mathcal{B}$. Duplicator answers $0 \in \Z$. Now $2$ rounds are left.
2. Round 2: Spoiler picks $(1, 0)$, in the second copy, at distance $\infty$ from $(0, 0)$. Here $r + 1 = 2$, so $r = 1$, and $\infty \ge 2^1$.
3. By step 5 Duplicator answers $2 \in \Z$, at distance $2^1$ from $0$. Both distances are at least $2$, so the invariant holds with $1$ round left.
4. Round 3: Spoiler picks $1 \in \Z$, between $0$ and $2$. Duplicator answers $(0, 1)$, which lies between $(0, 0)$ and $(1, 0)$, and wins.

A trap is to answer the far point $(1, 0)$ with $1 \in \Z$: then with one more round Spoiler picks a point between $(0, 0)$ and $(1, 0)$, and there is no integer between $0$ and $1$.

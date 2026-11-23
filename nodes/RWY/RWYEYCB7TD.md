---
tag: RWYEYCB7TD
kind: example
name: The Magari algebra of a finite strict partial order
msc: ["03G25", "03F45"]
topics: [3E7M66WW6Q]
audience: research
instance_of: [YTA4C8QCB0]
uses: [PHWAN904PT, 00E0YZCERH, 60FNZ35H6R, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_algebra
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: Examples
---

## Example

Take $W = \{0, 1, 2\}$ with $i R j$ exactly when $i < j$, and box a set $X \subseteq W$ by keeping the points whose successors all lie in $X$.
Then $R[0] = \{1, 2\}$, $R[1] = \{2\}$ and $R[2] = \emptyset$.
So $0 \in \square X$ when $\{1, 2\} \subseteq X$, $1 \in \square X$ when $2 \in X$, and $2 \in \square X$ always.
The table lists, for each $X$, the sets $\square X$, $\square X \to X = (W \setminus \square X) \cup X$ and $\square(\square X \to X)$.

| $X$ | $\square X$ | $\square X \to X$ | $\square(\square X \to X)$ |
|---|---|---|---|
| $\emptyset$ | $\{2\}$ | $\{0, 1\}$ | $\{2\}$ |
| $\{0\}$ | $\{2\}$ | $\{0, 1\}$ | $\{2\}$ |
| $\{1\}$ | $\{2\}$ | $\{0, 1\}$ | $\{2\}$ |
| $\{2\}$ | $\{1, 2\}$ | $\{0, 2\}$ | $\{1, 2\}$ |
| $\{0, 1\}$ | $\{2\}$ | $\{0, 1\}$ | $\{2\}$ |
| $\{0, 2\}$ | $\{1, 2\}$ | $\{0, 2\}$ | $\{1, 2\}$ |
| $\{1, 2\}$ | $W$ | $\{1, 2\}$ | $W$ |
| $W$ | $W$ | $W$ | $W$ |

In each row the last column equals the second, which is the Löb law for this chain.
The same holds for every finite strict partial order, and the steps below prove it.

### The general case

Let $W$ be a finite set and $R$ a [[strict partial order|60FNZ35H6R]] on $W$, so $R$ is irreflexive and transitive.
Let $B = \mathcal{P}(W)$ be the [[power set|00E0YZCERH]] algebra, with $\cap$, $\cup$, complement $W \setminus X$, $0 = \emptyset$ and $1 = W$.
Write $R[w] = \{v \in W : wRv\}$ and define the box as follows.
$$\square X = \{w \in W : R[w] \subseteq X\}.$$
We check the three properties of the [[definition of a Magari algebra|PHWAN904PT]].

1. Property 1: every $R[w]$ is a subset of $W$, so $\square W = W$.
2. Property 2: $R[w] \subseteq X \cap Y$ holds exactly when $R[w] \subseteq X$ and $R[w] \subseteq Y$.
   So $w \in \square(X \cap Y)$ exactly when $w \in \square X \cap \square Y$.
3. Property 3: by Lemma 2 of the definition it suffices to show $\square(\square X \to X) \subseteq \square X$.
   Steps 4 to 9 prove this inclusion.
4. Take $w \in \square(\square X \to X)$ and suppose, for a contradiction, that $w \notin \square X$.
   Then the set $S = \{v \in R[w] : v \notin X\}$ is not empty.
5. The set $S$ has an element $v_0$ with no $u \in S$ such that $v_0 R u$.
   Otherwise we could choose $v_0 R v_1 R v_2 R \cdots$ in $S$, and transitivity with irreflexivity would make these elements distinct, which is impossible in a finite set.
6. Since $w R v_0$ and $w \in \square(\square X \to X)$, we get $v_0 \in (W \setminus \square X) \cup X$.
7. Since $v_0 \notin X$, step 6 gives $v_0 \notin \square X$, so there is $u$ with $v_0 R u$ and $u \notin X$.
8. Transitivity gives $w R u$, so $u \in S$, and $v_0 R u$ contradicts the choice of $v_0$ in step 5.
9. So $w \in \square X$, and $\square(\square X \to X) \subseteq \square X$.

So $(\mathcal{P}(W), \square)$ is a [[Magari algebra|YTA4C8QCB0]].

## Remarks

### Kripke semantics in algebraic form

The example is the algebraic side of the [[Kripke semantics|NGHWZ9Y7ZV]] of $\mathsf{GL}$.
If $X$ is the set of worlds where $\varphi$ holds, then $\square X$ is the set of worlds where $\square \varphi$ holds.
So a modal formula is true at every world of every model on $(W, R)$ exactly when it takes the value $W$ under every assignment.

### Iterating the box

The chain shows that $\square$ is not idempotent, since $\square \emptyset = \{2\}$ but $\square \square \emptyset = \square \{2\} = \{1, 2\}$.
It also shows $\square x \not\le x$, since $\square \emptyset = \{2\} \not\subseteq \emptyset$.
The iterates $\emptyset$, $\square \emptyset$, $\square^2 \emptyset$, $\square^3 \emptyset$ are $\emptyset$, $\{2\}$, $\{1, 2\}$ and $W$.
In general $\square^n \emptyset$ is the set of points from which every $R$-path has fewer than $n$ steps.

### What each condition on the order does

Finiteness of $W$ is used only in step 5.
For infinite $W$, step 5 needs $R$ to be conversely well-founded, and with that condition the same proof works.
For $W = \mathbb{N}$ with $<$, which is not conversely well-founded, the Löb law fails at $X = \emptyset$; see the [[concept page|YTA4C8QCB0]].

Irreflexivity is needed as well.
Suppose $w R w$ and put $X = W \setminus \{w\}$.
Then $w \notin \square X$, because $w R w$ and $w \notin X$.
So $\square X \to X$ contains $w$ and all of $X$, which means $\square X \to X = W$ and $\square(\square X \to X) = W$.
This set contains $w$ while $\square X$ does not, so the Löb law fails.
The one-point case is [[the identity operator|F3YQMQHKYR]].

## Explanations

### L1 human

Take three rooms in a row, numbered $0$, $1$ and $2$, where one can look only forward.
From $0$ one sees $1$ and $2$, from $1$ one sees $2$, and from $2$ one sees nothing.
Paint some rooms red.
"Box red" holds in a room when every room it sees is red.
Room $2$ sees nothing, so "box red" always holds there.
The table checks Löb's rule for all eight ways to paint the rooms.

### L2 human

We compute the row of the table for $X = \{2\}$.

1. $0 \in \square X$ needs $\{1, 2\} \subseteq \{2\}$, which is false.
2. $1 \in \square X$ needs $\{2\} \subseteq \{2\}$, which is true.
3. $2 \in \square X$ holds, since $R[2] = \emptyset$.
   So $\square X = \{1, 2\}$.
4. $W \setminus \square X = \{0\}$, so $\square X \to X = \{0\} \cup \{2\} = \{0, 2\}$.
5. For $\square\{0, 2\}$, point $0$ needs $1 \in \{0, 2\}$, which is false, point $1$ needs $2 \in \{0, 2\}$, which is true, and point $2$ always qualifies.
   So $\square \{0, 2\} = \{1, 2\}$.
6. Steps 3 and 5 give $\square(\square X \to X) = \{1, 2\} = \square X$.

The typical use is to show that a formula is not a theorem of $\mathsf{GL}$: give the variables subsets of $W$ and compute.
The trap is to think that $w \in \square X$ needs $w \in X$.
The set $\square X$ depends on the successors of $w$ only, as $2 \in \square \emptyset$ shows.

---
tag: XQ8W9DEBD2
kind: example
name: Harrop's procedure finds an S4 countermodel to the McKinsey formula
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [3NT8RCA6HE]
uses: [3NT8RCA6HE, VSYQ1AZ9G7, XNPJK6B921, N60RVXSA5W, E87G6ZTMTN, NGHWZ9Y7ZV, 0X8NMST0J2, 0GJZW9JFZQ]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_model_property
    locator: lead section
  - url: https://en.wikipedia.org/wiki/S4_(modal_logic)
    locator: lead section
---

## Example

Let $\mathrm{M}$ be the McKinsey formula $\square\lozenge p \to \lozenge\square p$.
We run the search of [[Harrop's theorem|VSYQ1AZ9G7]] for a finite frame of [[S4|N60RVXSA5W]], also written $\mathsf{KT4}$, that refutes $\mathrm{M}$.
The frames of $\mathsf{S4}$ are the preorders, the [[reflexive|0X8NMST0J2]] and [[transitive|0GJZW9JFZQ]] frames.
We list them by size, up to isomorphism, and check every valuation of $p$.

### Size 1

The only preorder is one reflexive point $w$.
Its only successor is $w$ itself, so $\lozenge p$ and $\square p$ both have the truth value of $p$ at $w$.
So $\square\lozenge p$ and $\lozenge\square p$ both have the value of $p$, and $\mathrm{M}$ is true at $w$ for both valuations.

### Size 2

There are three preorders on $\{ a, b \}$ up to isomorphism: two separate reflexive points, the chain $a \le b$, and the cluster in which each point sees both.

With two separate points, each point sees only itself, so the size 1 argument applies at each point, and $\mathrm{M}$ is true everywhere.

In the chain, $a$ sees $a$ and $b$, and $b$ sees only $b$.
At $b$ the size 1 argument applies again, so $\mathrm{M}$ is true at $b$.
At $a$, $\square\lozenge p$ needs $\lozenge p$ at $b$, which means $p$ at $b$.
If $p$ is true at $b$, then $\square p$ is true at $b$, so $\lozenge\square p$ is true at $a$.
So in the chain, whenever the antecedent holds at $a$ the consequent holds too, and $\mathrm{M}$ is valid on the chain.

In the cluster, take $V(p) = \{ a \}$.
Each point sees $a$, where $p$ is true, so $\lozenge p$ is true at $a$ and at $b$, and $\square\lozenge p$ is true at $a$.
Each point sees $b$, where $p$ is false, so $\square p$ is false at $a$ and at $b$, and $\lozenge\square p$ is false at $a$.
So $\mathrm{M}$ fails at $a$.

### The answer

The cluster is a preorder, so it validates $\mathsf{S4}$, and by [[soundness|E87G6ZTMTN]] $\mathsf{S4} \nvdash \mathrm{M}$.

## Remarks

### Why the search had to end

The search stops at size 2, and the size 1 case shows that no smaller countermodel exists.
With $\lozenge$ counted as primitive, the subformulas of $\mathrm{M}$ are $p$, $\lozenge p$, $\square p$, $\square\lozenge p$, $\lozenge\square p$ and $\mathrm{M}$, six in all.
The [[finite model property theorem|XNPJK6B921]] bounds the search by $2^6 = 64$ worlds, so it was certain to end.
The other half of Harrop's procedure lists the proofs of $\mathsf{S4}$, and it never finds a proof of $\mathrm{M}$.

### What the cluster shows

Adding $\mathrm{M}$ to $\mathsf{S4}$ gives the logic $\mathsf{S4.1}$, and the cluster shows that this extension is proper.
Every $\mathsf{S5}$ frame is a union of clusters, and the cluster is itself an $\mathsf{S5}$ frame, so it also shows $\mathsf{S5} \nvdash \mathrm{M}$.

### Watch out

A countermodel on a frame that is not a preorder, such as a single irreflexive point, proves nothing about $\mathsf{S4}$.
The search must stay inside the frame class of the logic.

## Explanations

### L1 human

The procedure looks for a small picture where the formula is false.
It tries every picture with one world, then every picture with two worlds.
With one world, nothing can go wrong.
With two worlds that see each other, and with $p$ true at only one of them, the formula fails.
So the formula is not a law of $\mathsf{S4}$.

### L2 human

Read $\square\lozenge p$ as "from every reachable world, $p$ is still reachable" and $\lozenge\square p$ as "some reachable world has $p$ at every world it reaches".
In the cluster with $p$ at $a$ only, every world can reach $a$, so the first statement holds.
No world has $p$ at all its successors, because every world reaches $b$, so the second statement fails.
The typical use of the example is to see that the finite model property turns non-provability into a finite search.

### L3 human

Over $\mathsf{K}$, the [[McKinsey formula|4N4ZNWZRE2]] defines no first-order class of frames, so the search above cannot be replaced by a check of one first-order condition.
Harrop's method gives decidability, but the naive search through all frames below the bound is very slow.
The [[complexity theorem|1P2B0C7CQ4]] gives the optimal PSPACE bound for $\mathsf{S4}$.

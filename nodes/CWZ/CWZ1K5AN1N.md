---
tag: CWZ1K5AN1N
kind: example
name: Alexandrov spaces give Kripke semantics
msc: ["03B45", "54A05"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [HWJXMBNHQ0]
uses: [HWJXMBNHQ0, ATP1JK3V27, 0VABYWJWH9, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: Topological semantics
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Semantics of intuitionistic logic
---

## Example

Let $(W, \leq)$ be a [[preorder|0VABYWJWH9]].
Call $U \subseteq W$ an up-set when $u \in U$ and $u \leq v$ imply $v \in U$, and let $\tau$ be the family of up-sets.
This is the [[Alexandrov topology|ATP1JK3V27]] of the preorder.
We show that truth in the space $(W, \tau)$, as in [[topological semantics|HWJXMBNHQ0]], is the same as truth in the Kripke frame $(W, \leq)$.

1. The family $\tau$ is a topology.
   Unions and intersections of up-sets, even infinite ones, are up-sets, and so are $\emptyset$ and $W$.
2. For $w \in W$, the set ${\uparrow} w = \{ v : w \leq v \}$ is an up-set by transitivity, and it contains $w$ by reflexivity.
   Every up-set that contains $w$ contains ${\uparrow} w$.
3. So ${\uparrow} w$ is the smallest open set that contains $w$, and $w \in \mathrm{Int}\, A$ exactly when ${\uparrow} w \subseteq A$.
4. In [[Kripke semantics|NGHWZ9Y7ZV]], $\square \varphi$ holds at $w$ exactly when every $v \geq w$ satisfies $\varphi$, that is, when ${\uparrow} w \subseteq V(\varphi)$.
5. By induction on $\varphi$, the topological and the Kripke truth sets agree for every valuation.
   The Boolean cases are the same in both semantics, and the case of $\square$ is steps 3 and 4.
6. So a formula is valid in the space $(W, \tau)$ exactly when it is valid on the frame $(W, \leq)$.

For a concrete case, take $W = \{0, 1\}$ with $0 \leq 1$, so the open sets are $\emptyset$, $\{1\}$ and $W$.
With $V(p) = \{1\}$, both semantics give these truth sets:
$$V(\square p) = \{1\}, \qquad V(\lozenge p) = W.$$
Check: the closed sets are $W$, $\{0\}$ and $\emptyset$, and the smallest closed set that contains $\{1\}$ is $W$.

## Remarks

Kripke semantics for $\mathsf{S4}$ is the special case of topological semantics for Alexandrov spaces.
Since $\mathsf{S4}$ is complete for finite preorders, it is also complete for finite topological spaces.
Every finite space is an Alexandrov space, because it has only finitely many open sets and so is closed under all intersections of them.
So finite spaces and finite preorders give the same semantics.

A space that is not Alexandrov behaves differently.
In $\mathbb{R}$ the intersection of all neighborhoods of a point is the point itself, which is not open, so no point has a smallest neighborhood, and no frame gives the same truth sets.
The same correspondence turns intuitionistic Kripke models into open-set models, with up-sets as propositions.

## Explanations

### L1 human

In a preorder, each point has a set of points "above" it.
Declare a set open when it contains, with each point, everything above that point.
Then "true near $w$" means "true everywhere above $w$", which is how Kripke semantics reads "necessarily".

### L2 human

We compute one box in both semantics on the chain $0 \leq 1 \leq 2$.
The open sets are the up-sets $\emptyset$, $\{2\}$, $\{1, 2\}$ and $\{0, 1, 2\}$.
Let $V(p) = \{0, 2\}$.
The largest open subset of $\{0, 2\}$ is $\{2\}$, so topologically $V(\square p) = \{2\}$.
In the frame, $0 \leq 1$ and $1 \leq 1$ with $1 \notin V(p)$, so $\square p$ fails at $0$ and at $1$ and holds at $2$.
The two answers agree, as the example predicts.
The typical use of the correspondence is to move results about preorders to spaces, and back for finite spaces.
Watch out: here the box looks upward, so the open sets are up-sets; some books use down-sets with the converse order.

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

Let $(W, \leq)$ be a [[preorder|0VABYWJWH9]], and let $\tau$ be the family of up-sets: sets $U$ with $u \in U$ and $u \leq v$ implying $v \in U$.
This is the [[Alexandrov topology|ATP1JK3V27]] of the preorder.
We show that topological truth in $(W, \tau)$ is the same as Kripke truth in the frame $(W, \leq)$, as in [[topological semantics|HWJXMBNHQ0]].

1. $\tau$ is a topology. Unions and intersections of up-sets, even infinite ones, are up-sets, and $\emptyset$ and $W$ are up-sets.
2. For $w \in W$, the set ${\uparrow} w = \set{v : w \leq v}$ is an up-set by transitivity, and it contains $w$ by reflexivity. Every up-set that contains $w$ contains ${\uparrow} w$.
3. So ${\uparrow} w$ is the smallest open set that contains $w$. Hence $w \in \mathrm{Int}\, A$ if and only if ${\uparrow} w \subseteq A$.
4. In Kripke semantics, $w \models \square \varphi$ if and only if every $v \geq w$ satisfies $\varphi$, that is, ${\uparrow} w \subseteq V(\varphi)$.
5. By induction on $\varphi$, the topological and the Kripke truth sets agree for every valuation. The Boolean cases are the same, and the $\square$ case is steps 3 and 4.
6. So a formula is valid in the space $(W, \tau)$ if and only if it is valid on the Kripke frame $(W, \leq)$.

For a concrete case, take $W = \set{0, 1}$ with $0 \leq 1$.
The open sets are $\emptyset$, $\set{1}$ and $W$.
With $V(p) = \set{1}$, both semantics give $V(\square p) = \set{1}$ and $V(\lozenge p) = W$.

## Remarks

The example shows that Kripke semantics for $\mathsf{S4}$ is the special case of topological semantics for Alexandrov spaces.
Since $\mathsf{S4}$ is complete for finite preorders, it follows that $\mathsf{S4}$ is complete for finite topological spaces.
Every finite space is an Alexandrov space, since there are finitely many open sets; so finite spaces and finite preorders give the same semantics.
For a space that is not Alexandrov, such as $\R$, the intersection of all neighbourhoods of a point is the point itself, and there is no frame that gives the same truth sets.
The same correspondence interprets intuitionistic Kripke models as open-set models, with up-sets as propositions.

## Explanations

### L1 human

In a preorder, each point has a set of points "above" it.
Declare a set open when it contains, with each point, everything above that point.
Then "true near $w$" means "true everywhere above $w$", which is how Kripke semantics reads "necessarily".

### L2 human

1. Take the three-point chain $0 \leq 1 \leq 2$. The open sets are $\emptyset$, $\set{2}$, $\set{1, 2}$ and $\set{0, 1, 2}$.
2. Let $V(p) = \set{0, 2}$. The largest open subset of $\set{0, 2}$ is $\set{2}$.
3. So $V(\square p) = \set{2}$ topologically. In the Kripke frame, $0 \leq 1$ and $1 \notin V(p)$, so $\square p$ fails at $0$ and at $1$ and holds at $2$.

The typical use of the example is to move results about preorders to spaces, and back for finite spaces.
A trap: the Alexandrov topology uses up-sets for "$\square$ looks upward"; some texts use down-sets with the converse order.

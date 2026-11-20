---
tag: J3X26BSQEY
kind: example
name: The evaluation map from a vector space to its double dual is canonical
msc: ["00A35", "15A04"]
topics: [Z2WNQ1DNTX, 9K7FFF26QR]
audience: ug2
instance_of: [F8WNADZFMM]
uses: [F8WNADZFMM, 0ZJM9D7NPS, 07JBSZE0V4, 0ZD2CF6ZS0, 0KCQ9Y3QKA]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Injection into the double-dual
  - url: https://en.wikipedia.org/wiki/Natural_transformation
    locator: Double dual of a vector space
---

## Example

Let $V = \mathbb{R}^2$, and let $V^*$ be its [[dual space|07JBSZE0V4]], the space of linear maps $V \to \mathbb{R}$.
Each $f \in V^*$ has the form $f(x, y) = ax + by$ for real numbers $a$ and $b$.
The evaluation map $\operatorname{ev} \colon V \to V^{**}$ is defined by $\operatorname{ev}(v)(f) = f(v)$.
We check that $\operatorname{ev}$ is an isomorphism, and that it is [[canonical|F8WNADZFMM]]: it does not depend on a choice of basis.

1. For a fixed $v$, the map $f \mapsto f(v)$ is linear, because $(f + g)(v) = f(v) + g(v)$ and $(cf)(v) = c f(v)$ by the definition of the operations on $V^*$. So $\operatorname{ev}(v) \in V^{**}$.
2. The map $\operatorname{ev}$ is linear, because $f(v + w) = f(v) + f(w)$ and $f(cv) = c f(v)$ for each linear $f$.
3. The map $\operatorname{ev}$ is injective. If $\operatorname{ev}(x, y) = 0$, then $f(x, y) = 0$ for every $f$. With $f(x, y) = x$ we get $x = 0$, and with $f(x, y) = y$ we get $y = 0$.
4. The spaces $V$ and $V^{**}$ both have dimension $2$. An injective linear map between spaces of the same finite dimension is an isomorphism, so $\operatorname{ev}$ is an isomorphism.
5. The definition $\operatorname{ev}(v)(f) = f(v)$ names only $v$ and $f$. No basis, no coordinate and no inner product appears in it.
6. We compare with a basis description. Let $b_1 = (1, 0)$ and $b_2 = (1, 1)$. Their [[dual basis|0ZD2CF6ZS0]] is $b_1^*(x, y) = x - y$ and $b_2^*(x, y) = y$, since $b_1^*(b_1) = 1$, $b_1^*(b_2) = 0$, $b_2^*(b_1) = 0$ and $b_2^*(b_2) = 1$.
7. The basis $b_1^*, b_2^*$ of $V^*$ has a dual basis $b_1^{**}, b_2^{**}$ of $V^{**}$. We have $\operatorname{ev}(b_1)(b_1^*) = b_1^*(b_1) = 1$ and $\operatorname{ev}(b_1)(b_2^*) = b_2^*(b_1) = 0$, so $\operatorname{ev}(b_1) = b_1^{**}$. In the same way, $\operatorname{ev}(b_2) = b_2^{**}$.
8. The computation of step 7 works for every basis $b_1, \ldots, b_n$ of every finite-dimensional space: $\operatorname{ev}(b_i)(b_j^*) = b_j^*(b_i)$, which is $1$ for $i = j$ and $0$ otherwise. So the rule "send $b_i$ to $b_i^{**}$" gives the same map $\operatorname{ev}$ for each choice of basis.

## Remarks

The example shows the test for a canonical map: a description by a basis is allowed, but the result must be the same for every basis.
The rule "send $b_i$ to $b_i^*$" fails this test, as the [[non-example of a basis isomorphism to the dual|A3CP855PNV]] shows.
For an infinite-dimensional space, steps 1, 2, 3 and 5 still hold, so $\operatorname{ev}$ is still canonical and injective.
Step 4 fails there, and $\operatorname{ev}$ is not surjective, as the page on the [[double dual|0ZJM9D7NPS]] says.
The evaluation map also commutes with every isomorphism $\varphi \colon V \to W$; the computation is in the basic properties of the page on [[canonical maps|F8WNADZFMM]].

## Explanations

### L1 human

A vector $v$ can act on a rule $f$ in a direct way: it feeds itself into the rule and returns the value $f(v)$.
This turns each vector into a machine that eats rules and returns numbers.
To build this machine, nobody has to choose axes or units.
For example, the vector $(1, 2)$ turns the rule $f(x, y) = 3x - y$ into the number $3 - 2 = 1$, and every person gets the same answer.
That is why mathematicians call the map canonical.

### L2 human

We compute $\operatorname{ev}(1, 2)$ in two bases and get the same result.

1. In the standard basis $e_1 = (1, 0)$, $e_2 = (0, 1)$, the dual basis is $e_1^*(x, y) = x$ and $e_2^*(x, y) = y$. So $\operatorname{ev}(1, 2)$ takes the value $1$ on $e_1^*$ and $2$ on $e_2^*$, and $\operatorname{ev}(1, 2) = e_1^{**} + 2e_2^{**}$.
2. In the basis $b_1 = (1, 0)$, $b_2 = (1, 1)$, we have $(1, 2) = -b_1 + 2b_2$. By step 7, $\operatorname{ev}(1, 2) = -b_1^{**} + 2b_2^{**}$.
3. We check that the two answers agree on $f(x, y) = 3x - y$. Write $f = 3e_1^* - e_2^*$, so the first answer gives $3 \cdot 1 - 2 = 1$. Also $f = 3b_1^* + 2b_2^*$, because $3(x - y) + 2y = 3x - y$; so the second answer gives $-3 + 4 = 1$.
4. Both give $f(1, 2) = 1$, as the definition $\operatorname{ev}(v)(f) = f(v)$ says.

The typical use is the identification of $V^{**}$ with $V$ in finite dimension, for example to say that the dual of the dual basis is the original basis.
A trap: the isomorphism $V \to V^{**}$ is canonical, but the isomorphisms $V \to V^*$ and $V^* \to V^{**}$ are not, although all three spaces have the same dimension.

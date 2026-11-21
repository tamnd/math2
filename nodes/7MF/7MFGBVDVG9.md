---
tag: 7MFGBVDVG9
kind: statement
role: theorem
name: Omitting types theorem
msc: ["03C07", "03C15"]
topics: [Z772KEC9BY]
audience: grad
uses: [9V71Q3SD1G, VA7AK1R5AN, ~ecb9582c, ~13f847af, 92SWXST1ZM, MVCH6N9SNW, 01TQB88H4C]
about: [9V71Q3SD1G, ~ecb9582c]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Omitting types theorem
  - book: isbn:9780387987606
    locator: Chapter 4
  - book: isbn:9780521587136
---

## Statement

Let $L$ be a [[countable|01TQB88H4C]] signature and let $T$ be a satisfiable $L$-[[theory|92SWXST1ZM]].
For each $k \in \N$ let $p_k(x_1, \dots, x_{n_k})$ be an $n_k$-[[type|9V71Q3SD1G]] of $T$ that is not [[isolated|~ecb9582c]].
So no $L$-formula $\varphi(\bar{x})$ with $T \cup \set{\varphi}$ satisfiable has $T \models \forall \bar{x} \, (\varphi \to \psi)$ for all $\psi \in p_k$.
Then $T$ has a countable [[model|MVCH6N9SNW]] that omits every $p_k$.

## Remarks

Two proofs are given: a [[Henkin construction|~77fed017]] and a [[Baire category argument|~fdd9ca8f]].

### Why each hypothesis is needed

- Non-isolation: if $T$ is complete and $\varphi$ isolates $p$, then $T \models \exists \bar{x} \, \varphi$, and a witness of $\varphi$ realizes $p$ in every model.
- Countable language: let $L$ have constants $c_\alpha$ for $\alpha < \omega_1$ and $d_k$ for $k \in \N$, let $T$ say that the $c_\alpha$ are pairwise different, and let $p(x) = \set{x \ne d_k : k \in \N}$.
- In this example $p$ is not isolated: if $\varphi(x)$ holds at $e$ in a model of $T$, reinterpret a constant $d_k$ that is not in $\varphi$ as $e$. Still every model of $T$ is uncountable, so it has an element outside the countable set of the $d_k$, and no model omits $p$.
- Countably many types: for the theory of infinitely many independent unary predicates $P_i$, no complete $1$-type over $\emptyset$ is isolated, and each element of a model realizes one of them. So the $2^{\aleph_0}$ non-isolated types cannot all be omitted together.

### Consequences

- A countable complete theory whose isolated types are dense in each $S_n(T)$ has a countable model that realizes only isolated types, an atomic model, which is a [[prime model|S8W40PYNHX]].
- If a countable complete theory has a non-isolated type, then it has a countable model that omits it and one that realizes it, so it is not [[$\aleph_0$-categorical|A22K1X8GKD]]; this is one direction of the [[Ryll-Nardzewski theorem|1513J40TKA]].
- The [[type of an infinite natural number|~a176ff80]] is not isolated, and the standard model is a countable model that omits it.

### Converse

For a complete $T$ the converse holds: if some model omits $p$, then $p$ is not isolated, since isolated types are realized in every model.
For a theory that is not complete the converse fails: in the theory of fields, $x \cdot x = 1 + 1$ isolates a type, and the field $\Q$ omits it.

### Generalizations

The theorem holds for countable fragments of the infinitary logic $L_{\omega_1 \omega}$; see [[infinitary logics|VBYC17XY83]].
Omitting a type in an uncountable model needs other methods, and in general it fails.

## Explanations

### L1 human

A type is a wish list of properties for an element.
Some wish lists are forced: a single consistent property already implies the whole list.
For a complete theory, every model then has an element that meets the whole list.
The theorem says that, in a countable language, every list that is not forced in this way can be avoided by some countable model, and even countably many lists at once.

### L2 human

We apply the theorem to $T = \operatorname{Th}(\Q, <)$ with new constants $c_q$ for the rationals, and to the type $p(x) = \set{c_q < x : q < \sqrt{2}} \cup \set{x < c_q : q > \sqrt{2}}$.

1. The language is countable, since $\Q$ is countable.
2. A consistent formula $\varphi(x)$ defines a finite union of points and intervals with rational endpoints, by quantifier elimination.
3. Such a set contains a rational number, which does not realize $p$, so $\varphi$ does not isolate $p$.
4. The theorem gives a countable model that omits $p$; here $(\Q, <)$ with its own constants is such a model.

The typical use is to build countable models with prescribed properties, as for atomic models.
The trap is to apply the theorem to an isolated type of an incomplete theory and expect it to be realized in every model.

### L3 human

The Baire category proof shows the general shape of the theorem.
The models of $T$ built from constants form a compact space, the models that realize a non-isolated type form a meager set, and a generic model avoids countably many meager sets.
This is the model-theoretic form of forcing, and the same argument builds generic structures in many areas.
The theorem is the companion of the [[realizing types theorem|~17fa6973]]: compactness produces models that realize types, and this theorem produces models that omit them.
It is the main tool of the study of countable models and of [[Vaught's conjecture|YVBHE2SEE6]].

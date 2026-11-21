---
tag: ~fdd9ca8f
kind: proof
name: Baire category proof of the omitting types theorem
msc: ["03C07", "03C15", "54E52"]
topics: [Z772KEC9BY]
audience: grad
proves: 7MFGBVDVG9
uses: [~ecb9582c, ~319ab8e1, 0A7KGAYHGV, 0TVJZYB6SH, 0S1FJ8VEX9, 60SA99BER7, 1NR3HAWG9D]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Omitting types theorem
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Proof

The types $p_k(x_1, \dots, x_{n_k})$ for $k \in \N$ are non-isolated types of the satisfiable $L$-theory $T$, and $L$ is countable.

### The space

1. Let $C = \set{c_0, c_1, \dots}$ be new constants and $L^* = L \cup C$, a countable language.
2. Let $X$ be the set of complete satisfiable sets of $L^*$-sentences that contain $T$. For an $L^*$-sentence $\theta$ put $[\theta] = \set{T' \in X : \theta \in T'}$.
3. With the sets $[\theta]$ as a basis, $X$ is a closed subspace of the [[Stone space|~319ab8e1]] of complete $L^*$-theories, so $X$ is [[compact|0TVJZYB6SH]] and [[Hausdorff|0S1FJ8VEX9]].
4. The space $X$ is nonempty: expand a model of $T$ by any values of the constants, and take its complete $L^*$-theory.
5. A basic set $[\theta]$ is nonempty exactly when $T \cup \set{\theta}$ is satisfiable.
6. By the [[Baire category theorem|0A7KGAYHGV]] for compact Hausdorff spaces, the intersection of countably many dense open subsets of $X$ is dense, and so nonempty.

### Witness sets are dense

7. For an $L^*$-formula $\chi(v)$ with one free variable, let $U_\chi = [\neg \exists v \, \chi] \cup \bigcup_{c \in C} [\chi(c)]$. It is open as a union of basic sets.
8. Let $[\theta]$ be nonempty. If $T \cup \set{\theta, \neg \exists v \, \chi}$ is satisfiable, then $[\theta]$ meets $U_\chi$.
9. Otherwise $T \cup \set{\theta} \models \exists v \, \chi$. Choose $c \in C$ not in $\theta$ or $\chi$, and reinterpret $c$ as a witness in a model of $T \cup \set{\theta}$.
10. So $T \cup \set{\theta, \chi(c)}$ is satisfiable, and $[\theta] \cap [\chi(c)]$ is nonempty. So $U_\chi$ is dense.

### Omission sets are dense

11. For $k \in \N$ and $\bar{d} \in C^{n_k}$, let $V_{k, \bar{d}} = \bigcup_{\psi \in p_k} [\neg \psi(\bar{d})]$. It is open.
12. Let $[\theta]$ be nonempty, and write $\bar{d} = (d_1, \dots, d_n)$. Let $\varepsilon(\bar{x})$ say $x_a = x_b$ whenever $d_a = d_b$.
13. Replace in $\theta$ each $d_a$ by $x_a$ for the least such $a$, and the other constants of $C$ by new variables $\bar{y}$, to get $\theta'(\bar{x}, \bar{y})$.
14. The $L$-formula $\varphi(\bar{x}) = \varepsilon(\bar{x}) \wedge \exists \bar{y} \, \theta'(\bar{x}, \bar{y})$ holds at the values of $\bar{d}$ in a model of $T \cup \set{\theta}$, so it is consistent with $T$.
15. Since $p_k$ is not [[isolated|~ecb9582c]], some $\psi \in p_k$ and some tuple $\bar{a}$ in a model of $T$ satisfy $\varphi(\bar{a}) \wedge \neg \psi(\bar{a})$.
16. Interpret $d_a$ as $a_a$ and the other constants of $\theta$ as a witness for $\bar{y}$. This model satisfies $T \cup \set{\theta, \neg \psi(\bar{d})}$, so $V_{k, \bar{d}}$ meets $[\theta]$ and is dense.

### The generic model

17. There are countably many sets $U_\chi$ and $V_{k, \bar{d}}$, so by step 6 some $T' \in X$ lies in all of them.
18. Let $\mathcal{N}^*$ be a model of $T'$, and let $M = \set{c^{\mathcal{N}^*} : c \in C}$. Since $T'$ is complete, $T'$ is the set of $L^*$-sentences true in $\mathcal{N}^*$.
19. If $\mathcal{N}^* \models \exists v \, \chi(v)$ for an $L^*$-formula $\chi$, then $T' \in U_\chi$ gives $\chi(c) \in T'$ for some $c \in C$. So a witness lies in $M$.
20. Taking $\chi$ of the form $v = t$ for closed $L^*$-terms $t$ shows that $M$ contains the constants and is closed under the functions. By the [[Tarski-Vaught test|60SA99BER7]], $M$ is the domain of an elementary substructure $\mathcal{M}^* \preceq \mathcal{N}^*$, and it is countable.
21. Each $n_k$-tuple of $\mathcal{M}^*$ is the value of some $\bar{d} \in C^{n_k}$. Since $T' \in V_{k, \bar{d}}$, some $\neg \psi(\bar{d})$ with $\psi \in p_k$ is in $T'$.
22. So the tuple fails $\psi$ in $\mathcal{N}^*$, and in $\mathcal{M}^*$ by elementarity.
23. The $L$-reduct of $\mathcal{M}^*$ is a countable model of $T$ that omits every $p_k$.

This proves the [[omitting types theorem|7MFGBVDVG9]].

## Idea

A complete $L^*$-theory that contains $T$ describes a structure named by constants.
The theories whose constants form an elementary substructure, and whose tuples omit the types, are the points of countably many dense open sets.
Non-isolation is exactly what makes the omission sets dense.
The Baire category theorem then gives a point in all of them.

## Variants

The [[Henkin proof|~77fed017]] builds the same point step by step: each stage of the construction shrinks a basic open set into one of the dense open sets.
The same scheme proves that a generic model omits each non-isolated type, and it is a simple case of forcing in model theory.

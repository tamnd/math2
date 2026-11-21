---
tag: N82JBAR3CB
kind: proof
name: Henkin proof of the omitting types theorem
msc: ["03C07", "03C15"]
topics: [Z772KEC9BY]
audience: grad
proves: 7MFGBVDVG9
uses: [A0VNTN725W, RY8KRKR097, 1NR3HAWG9D, 60SA99BER7, 01TQB88H4C]
methods: [01XM7JEKHY, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Omitting types theorem
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Proof

We follow the [[Henkin construction|RY8KRKR097]] and add one kind of step that omits the types.
The types $p_k(x_1, \dots, x_{n_k})$ for $k \in \N$ are non-isolated types of the satisfiable $L$-theory $T$, and $L$ is countable.

### Setup

1. Let $C = \set{c_0, c_1, \dots}$ be new constants and $L^* = L \cup C$. The set of $L^*$-sentences is countable, so list it as $\theta_0, \theta_1, \dots$.
2. The pairs $(k, \bar{d})$ with $k \in \N$ and $\bar{d} \in C^{n_k}$ form a countable set. List them as $(k_0, \bar{d}_0), (k_1, \bar{d}_1), \dots$.
3. We build finite sets $F_0 \subseteq F_1 \subseteq \dots$ of $L^*$-sentences with $F_0 = \emptyset$ and each $T \cup F_s$ satisfiable.

### The construction

4. Stage $3j$: if $T \cup F_s \cup \set{\theta_j}$ is satisfiable, add $\theta_j$; otherwise add $\neg \theta_j$. In the second case every model of $T \cup F_s$ satisfies $\neg \theta_j$, so satisfiability is kept.
5. Stage $3j + 1$: if $\theta_j$ was added and has the form $\exists v \, \chi(v)$, add $\chi(c)$ for a constant $c \in C$ that does not occur in $F_s$ or in $\theta_j$.
6. This keeps satisfiability: in a model of $T \cup F_s \cup \set{\exists v \, \chi}$, reinterpret $c$ as a witness of $\chi$. The constant $c$ does not occur in the other sentences.
7. Stage $3j + 2$: let $p = p_{k_j}$, $\bar{d} = \bar{d}_j = (d_1, \dots, d_n)$, and let $\sigma$ be the conjunction of $F_s$.
8. Let $\varepsilon(\bar{x})$ be the conjunction of $x_a = x_b$ over all $a, b$ with $d_a = d_b$. Let $\bar{e}$ list the constants of $C$ in $\sigma$ that are not in $\bar{d}$.
9. Let $\sigma'(\bar{x}, \bar{y})$ be $\sigma$ with each $d_a$ replaced by $x_a$ for the least such $a$, and $\bar{e}$ replaced by new variables $\bar{y}$. Put $\varphi(\bar{x}) = \varepsilon(\bar{x}) \wedge \exists \bar{y} \, \sigma'(\bar{x}, \bar{y})$, an $L$-formula.
10. In a model of $T \cup F_s$ the tuple of values of $\bar{d}$ satisfies $\varphi$, so $T \cup \set{\varphi}$ is satisfiable.
11. Since $p$ is not isolated, some $\psi \in p$ has $T \not\models \forall \bar{x} \, (\varphi \to \psi)$. So a model $\mathcal{N}$ of $T$ has a tuple $\bar{a}$ with $\varphi(\bar{a}) \wedge \neg \psi(\bar{a})$.
12. Interpret $d_a$ as $a_a$, which is well defined because $\varepsilon(\bar{a})$ holds, and interpret $\bar{e}$ as a witness $\bar{b}$ of $\exists \bar{y} \, \sigma'(\bar{a}, \bar{y})$.
13. This expansion satisfies $T \cup F_s \cup \set{\neg \psi(\bar{d})}$. Add $\neg \psi(\bar{d})$.

### The model

14. Let $T^* = T \cup \bigcup_s F_s$. Each finite part lies in some satisfiable $T \cup F_s$, so $T^*$ has a model $\mathcal{N}^*$ by the [[compactness theorem|1NR3HAWG9D]].
15. For every $j$, stage $3j$ put $\theta_j$ or $\neg \theta_j$ into $T^*$, so $T^*$ is complete, and $T^*$ is the set of $L^*$-sentences true in $\mathcal{N}^*$.
16. Let $M = \set{c^{\mathcal{N}^*} : c \in C}$. Suppose $\mathcal{N}^* \models \exists v \, \chi(v, \bar{m})$ with $\bar{m} = \bar{c}^{\mathcal{N}^*}$ in $M$.
17. The sentence $\exists v \, \chi(v, \bar{c})$ is some $\theta_j$, and it is in $T^*$ by step 15. Stage $3j + 1$ added $\chi(c, \bar{c})$, so a witness lies in $M$.
18. Taking $\chi$ of the form $v = t(\bar{c})$ for terms $t$ shows that $M$ contains the constants of $L$ and is closed under the functions.
19. By the [[Tarski-Vaught test|60SA99BER7]], $M$ is the domain of an elementary substructure $\mathcal{M}^* \preceq \mathcal{N}^*$. It is [[countable|01TQB88H4C]], since $C$ is countable.

### The model omits the types

20. Let $\bar{a}$ be an $n_k$-tuple of $\mathcal{M}^*$. Each $a_i$ is the value of some constant, so $\bar{a} = \bar{d}^{\mathcal{N}^*}$ for some $\bar{d} \in C^{n_k}$.
21. The pair $(k, \bar{d})$ is $(k_j, \bar{d}_j)$ for some $j$, and stage $3j + 2$ added $\neg \psi(\bar{d})$ for some $\psi \in p_k$.
22. So $\mathcal{N}^* \models \neg \psi(\bar{a})$, and $\mathcal{M}^* \models \neg \psi(\bar{a})$ since $\mathcal{M}^* \preceq \mathcal{N}^*$. So $\bar{a}$ does not realize $p_k$.
23. The $L$-reduct $\mathcal{M}$ of $\mathcal{M}^*$ satisfies $T \subseteq T^*$, and the formulas of $p_k$ are $L$-formulas, so $\mathcal{M}$ omits every $p_k$.

So $T$ has a countable model that omits every $p_k$, which proves the [[omitting types theorem|7MFGBVDVG9]].

## Idea

The model is built from new constants, as in the proof of the completeness theorem.
There are countably many tasks: decide each sentence, give each existential sentence a witness, and stop each tuple of constants from realizing each type.
A tuple $\bar{d}$ could only be forced to realize $p$ by the finite information built so far, and that information is one $L$-formula $\varphi$, which does not isolate $p$.
So some formula of $p$ can still be denied at $\bar{d}$.

## Variants

The [[Baire category proof|PYAR8R8AQR]] shows that the complete theories that meet all tasks form a comeager set in a compact space.
For a single type the construction needs one omission task for each tuple, and the countable list of tasks is the reason why the language must be countable.

---
tag: BKSPVH8B35
kind: proof
name: Proof of Vaught's two-cardinal theorem
msc: ["03C55", "03C50"]
topics: [W9CHA4PD9H]
audience: grad
proves: XT227BYP7B
uses: [484M0TZ1S7, 1NR3HAWG9D, NHCRZ74JHH, 4NJS7W57VK, 8WZF9SBP39, 9V71Q3SD1G, EY20BF96SJ, Z92S2GVCX9, 0ZHQMQ2C1N]
methods: [01XM7JEKHY, 0ZHQMQ2C1N]
sources:
  - book: isbn:9780387987606
  - book: isbn:9780486488219
    locator: Chapter 7
---

## Proof

Let $\mathcal{M}$ be a $(\kappa, \lambda)$-model of $T$ with $\kappa > \lambda \ge \aleph_0$.
"Homogeneous" means $\aleph_0$-homogeneous in the sense of [[homogeneous models|4NJS7W57VK]].

### Step 1: a Vaughtian pair

1. The signature $L$ is countable and $\lambda \ge \aleph_0$. By the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]], some $\mathcal{N} \preceq \mathcal{M}$ has $P^{\mathcal{M}} \subseteq N$ and $\abs{N} = \lambda$.
2. Then $P^{\mathcal{N}} = P^{\mathcal{M}} \cap N = P^{\mathcal{M}}$, and this set is infinite since $\lambda \ge \aleph_0$.
3. As $\abs{N} = \lambda < \kappa = \abs{M}$, $\mathcal{N} \ne \mathcal{M}$. So $(\mathcal{M}, \mathcal{N})$ is a Vaughtian pair.

### Step 2: the theory of pairs

Let $L_U = L \cup \set{U}$ with a new unary symbol $U$.
A pair $\mathcal{N} \subseteq \mathcal{M}$ gives the [[expansion|EY20BF96SJ]] $(\mathcal{M}, N)$ of $\mathcal{M}$ with $U$ interpreted as $N$.
Let $T_U$ be the set of these $L_U$-sentences:

- the axioms of $T$, and "$U$ is nonempty and closed under the function symbols and contains the constants of $L$";
- for each $L$-formula $\varphi(\bar{x})$: for all $\bar{x}$ in $U$, $\varphi(\bar{x}) \leftrightarrow \varphi^U(\bar{x})$, where $\varphi^U$ relativizes the quantifiers to $U$;
- $\exists x \, \neg U(x)$, the sentence $\forall x \, (P(x) \to U(x))$, and "$P$ has at least $n$ elements" for each $n$.

The models of $T_U$ are the Vaughtian pairs $(\mathcal{M}, N)$: the first two groups say that $U$ is an [[elementary substructure|8WZF9SBP39]] that is a model of $T$.
By step 1, $T_U$ has a model, and by downward Löwenheim-Skolem in the countable $L_U$, it has a countable model.

### Step 3: one stage of the chain

Let $(\mathcal{M}_k, N_k)$ be a countable model of $T_U$.
We build a countable $L_U$-elementary extension $(\mathcal{M}_{k+1}, N_{k+1})$ that realizes these types.

1. For each tuple $\bar{b}$ of $M_k$: the set $\set{U(x_l)}_l \cup \operatorname{tp}^{\mathcal{M}_k}(\bar{b})$, in variables $\bar{x}$. A finite part says $\exists \bar{x} \, \varphi(\bar{x})$ in $\mathcal{M}_k$, so in $\mathcal{N}_k \preceq \mathcal{M}_k$, so with $\bar{x}$ in $U$.
2. For tuples $\bar{a}, \bar{b}$ of $M_k$ with the same $L$-type, and $c \in M_k$: the set $\set{\varphi(\bar{b}, x) : \mathcal{M}_k \models \varphi(\bar{a}, c)}$. A finite part is $\varphi(\bar{b}, x)$ with $\mathcal{M}_k \models \exists x \, \varphi(\bar{a}, x)$, so $\exists x \, \varphi(\bar{b}, x)$ holds.
3. For $\bar{a}, \bar{b}, c$ in $N_k$ with $\operatorname{tp}(\bar{a}) = \operatorname{tp}(\bar{b})$: the set $\set{U(x)} \cup \set{\varphi(\bar{b}, x) : \mathcal{M}_k \models \varphi(\bar{a}, c)}$. As in item 2 a witness exists in $\mathcal{N}_k$.

There are countably many such sets, each with its own new constants.
With the elementary diagram of $(\mathcal{M}_k, N_k)$, they are finitely satisfiable, by items 1 to 3.
The [[compactness theorem|1NR3HAWG9D]] and downward Löwenheim-Skolem give the countable extension.

### Step 4: a homogeneous countable pair

1. Start with a countable model $(\mathcal{M}_0, N_0)$ of $T_U$ from step 2, and apply step 3 for each $k \in \N$.
2. Let $\mathcal{M} = \bigcup_k \mathcal{M}_k$ and $N = \bigcup_k N_k$. By the [[elementary chain theorem|NHCRZ74JHH]] in $L_U$, $(\mathcal{M}, N) \models T_U$, so it is a countable Vaughtian pair.
3. Every finite tuple of $M$ lies in some $M_k$. Item 1 of step 3 at stage $k$ shows that every [[type|9V71Q3SD1G]] realized in $\mathcal{M}$ is realized in $\mathcal{N}$.
4. Every type realized in $\mathcal{N}$ is realized in $\mathcal{M}$, since $\mathcal{N} \preceq \mathcal{M}$.
5. Items 2 and 3 of step 3 at stage $k$ make $\mathcal{M}$ and $\mathcal{N}$ homogeneous, since types in $\mathcal{M}_k$, in $\mathcal{N}_k$ and in $\mathcal{M}$ agree by elementarity.
6. The models $\mathcal{N}$ and $\mathcal{M}$ are countable, homogeneous, elementarily equivalent, and realize the same types. By the [[homogeneous model|4NJS7W57VK]] page, they are isomorphic.

### Step 5: the chain of length $\omega_1$

We build countable homogeneous models $\mathcal{M}^\alpha$, for $\alpha < \omega_1$, with $\mathcal{M}^\alpha \preceq \mathcal{M}^\beta$ and $P^{\mathcal{M}^\alpha} = P^{\mathcal{N}}$ for $\alpha < \beta$, by [[transfinite induction|0ZHQMQ2C1N]].
Each $\mathcal{M}^\alpha$ realizes the same types as $\mathcal{N}$.

1. Start: $\mathcal{M}^0 = \mathcal{N}$.
2. Successor: by step 4 item 6 there is an isomorphism $g \colon \mathcal{N} \to \mathcal{M}^\alpha$. Extend $g$ to a bijection from $M$ onto a set $M^{\alpha + 1} \supseteq M^\alpha$, with new elements for $M \setminus N$, and copy the structure of $\mathcal{M}$.
3. Then $(\mathcal{M}^{\alpha+1}, M^\alpha) \cong (\mathcal{M}, N)$. So $\mathcal{M}^\alpha \preceq \mathcal{M}^{\alpha+1}$, $\mathcal{M}^\alpha \ne \mathcal{M}^{\alpha+1}$, and $P^{\mathcal{M}^{\alpha+1}} = g(P^{\mathcal{N}}) = P^{\mathcal{M}^\alpha}$.
4. The model $\mathcal{M}^{\alpha+1}$ is isomorphic to $\mathcal{M}$, so it is countable, homogeneous, and realizes the same types as $\mathcal{N}$.
5. Limit $\delta$: $\mathcal{M}^\delta = \bigcup_{\alpha < \delta} \mathcal{M}^\alpha$. It is countable, as $\delta$ is countable, and $\mathcal{M}^\alpha \preceq \mathcal{M}^\delta$ by the elementary chain theorem.
6. $P^{\mathcal{M}^\delta} = \bigcup_\alpha P^{\mathcal{M}^\alpha} = P^{\mathcal{N}}$. Each finite tuple and each instance of homogeneity lies in some $\mathcal{M}^\alpha$, so $\mathcal{M}^\delta$ is homogeneous and realizes the same types as $\mathcal{N}$.

### Step 6: the conclusion

Let $\mathcal{M}^{\omega_1} = \bigcup_{\alpha < \omega_1} \mathcal{M}^\alpha$.
It is an elementary extension of $\mathcal{N}$, by the elementary chain theorem, so it is a model of $T$.
The chain is strictly increasing of length $\omega_1$ and each member is countable, so $\abs{M^{\omega_1}} = \aleph_1$.
Its set $P^{\mathcal{M}^{\omega_1}} = P^{\mathcal{N}}$ is countable and infinite.
So $\mathcal{M}^{\omega_1}$ is an $(\aleph_1, \aleph_0)$-model of $T$.

## Idea

A model where $P$ is smaller than the model gives a pair of models with the same $P$.
The pair can be made countable, and then so homogeneous that the small model is isomorphic to the large one.
Then the step from the small model to the large one can be repeated $\omega_1$ times without changing $P$.

## Variants

In a two-sorted language one can treat $P$ as a sort, and the same proof works.
For $\omega$-stable theories, a Vaughtian pair gives $(\kappa, \aleph_0)$-models for every uncountable $\kappa$, with prime models over sets in place of homogeneous models.

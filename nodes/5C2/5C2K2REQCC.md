---
tag: 5C2K2REQCC
kind: proof
name: Outline proof of Chang's two-cardinal theorem
msc: ["03C55", "03C50"]
topics: [W9CHA4PD9H]
audience: research
proves: 4STP69KESQ
uses: [XT227BYP7B, BKSPVH8B35, GSQ833HAZT, RMTZ5J64FX, DZ65A6X12W, NHCRZ74JHH, 13ZV2F8JAR, BAWHE1W6MH, 0ZHQMQ2C1N]
methods: [01XM7JEKHY, 0ZHQMQ2C1N]
sources:
  - book: isbn:9780486488219
    locator: Chapter 7
  - book: isbn:9780387987606
---

## Proof

This is an outline: steps 1 to 6 and 8 are complete, and step 7 cites the literature for the limit stages of small [[cofinality|BAWHE1W6MH]].
Let $\mathcal{M}_1$ be an $(\aleph_1, \aleph_0)$-model of $T$, and let $\kappa^{<\kappa} = \kappa$.
For $\kappa = \aleph_0$ there is nothing to prove, so let $\kappa$ be uncountable.

### Step 1: a complete theory of pairs

1. Step 1 of [[the proof of Vaught's theorem|BKSPVH8B35]], with $\lambda = \aleph_0$, gives a Vaughtian pair: $\mathcal{N} \preceq \mathcal{M}$ with $\mathcal{N} \ne \mathcal{M}$, $P^{\mathcal{N}} = P^{\mathcal{M}}$, and $P^{\mathcal{M}}$ infinite.
2. Let $T'$ be the complete $L_U$-theory of the expansion $(\mathcal{M}, N)$, with $U$ interpreted as $N$. Its models are again Vaughtian pairs, as in step 2 of that proof.

### Step 2: a saturated pair

1. The signature $L_U$ is countable, $\kappa$ is uncountable and $\kappa^{<\kappa} = \kappa$.
2. By the [[existence of saturated models|GSQ833HAZT]], $T'$ has a [[saturated|RMTZ5J64FX]] model $(\mathcal{A}, B)$ of size $\kappa$.
3. Then $\mathcal{B} \preceq \mathcal{A}$, $\mathcal{B} \ne \mathcal{A}$ and $P^{\mathcal{B}} = P^{\mathcal{A}}$, where $\mathcal{B}$ is the $L$-structure on $B$.

### Step 3: both parts are saturated

1. Let $X \subseteq A$ with $\abs{X} < \kappa$, and let $p(x)$ be an $L$-type over $X$ in $\mathcal{A}$. It is also an $L_U$-type, so the saturation of the pair realizes it. So $\mathcal{A}$ is saturated.
2. Let $X \subseteq B$ with $\abs{X} < \kappa$, and let $p(x)$ be an $L$-type over $X$ in $\mathcal{B}$. Each finite part of $p$ is satisfied in $\mathcal{B}$, so $\set{U(x)} \cup p$ is an $L_U$-type of the pair.
3. The saturation of the pair realizes $\set{U(x)} \cup p$ by an element of $B$. This element realizes $p$ in $\mathcal{B}$, as $\mathcal{B} \preceq \mathcal{A}$. So $\mathcal{B}$ is saturated.
4. The type $\set{P(x)} \cup \set{x \ne c : c \in X}$ is realized for each $X$ with $\abs{X} < \kappa$, since $P$ is infinite. So $\abs{P^{\mathcal{A}}} = \kappa$, and also $\abs{B} = \kappa$.

### Step 4: the two parts are isomorphic

The structures $\mathcal{A}$ and $\mathcal{B}$ are saturated of size $\kappa$, and $\mathcal{B} \preceq \mathcal{A}$ gives $\mathcal{A} \equiv \mathcal{B}$.
By the [[uniqueness of saturated models|DZ65A6X12W]], $\mathcal{A} \cong \mathcal{B}$.

### Step 5: the plan of the chain

We build an elementary chain $(\mathcal{A}^\alpha)_{\alpha < \kappa^+}$ of saturated models of $T$ of size $\kappa$, by [[transfinite induction|0ZHQMQ2C1N]].
It has $\mathcal{A}^\alpha \ne \mathcal{A}^{\alpha+1}$ and $P^{\mathcal{A}^\alpha} = P^{\mathcal{B}}$ for all $\alpha$.
We start with $\mathcal{A}^0 = \mathcal{B}$.

### Step 6: successors and limits of cofinality $\kappa$

1. Successor: step 4 and uniqueness give an isomorphism $g \colon \mathcal{B} \to \mathcal{A}^\alpha$, since both are saturated of size $\kappa$ and elementarily equivalent to $\mathcal{B}$.
2. Extend $g$ to a bijection from $A$ onto a set $A^{\alpha+1} \supseteq A^\alpha$, and copy the structure of $\mathcal{A}$. Then $(\mathcal{A}^{\alpha+1}, A^\alpha) \cong (\mathcal{A}, B)$, which gives the required properties.
3. Limit $\delta$ with $\operatorname{cf}(\delta) = \kappa$: let $\mathcal{A}^\delta$ be the union. It is an elementary extension of each $\mathcal{A}^\alpha$ by the [[elementary chain theorem|NHCRZ74JHH]], and it has size $\kappa$.
4. A set $X$ with $\abs{X} < \kappa$ lies in one $\mathcal{A}^\alpha$, because $\kappa$ is [[regular|13ZV2F8JAR]]. A type over $X$ is realized in $\mathcal{A}^\alpha$, so $\mathcal{A}^\delta$ is saturated.

### Step 7: limits of small cofinality (cited)

At a limit $\delta$ with $\operatorname{cf}(\delta) < \kappa$, the union of the chain is a model of size $\kappa$ with the same $P$, but it need not be saturated.
A set $X$ of size $\operatorname{cf}(\delta)$ can meet every stage, and a type over $X$ need not be realized.
To continue, the proof needs a saturated model of size $\kappa$ at stage $\delta$ that is an elementary extension of the union with the same $P$.
The published proofs handle this point with an additional argument, which we do not reproduce; see Chang and Keisler, Chapter 7.

### Step 8: the conclusion

Let $\mathcal{A}^{\kappa^+} = \bigcup_{\alpha < \kappa^+} \mathcal{A}^\alpha$.
It is a model of $T$ by the elementary chain theorem.
The chain is strictly increasing of length $\kappa^+$ and each member has size $\kappa$, so $\abs{A^{\kappa^+}} = \kappa^+$.
Its set $P^{\mathcal{A}^{\kappa^+}} = P^{\mathcal{B}}$ has size $\kappa$, by step 3.
So $\mathcal{A}^{\kappa^+}$ is a $(\kappa^+, \kappa)$-model of $T$.

## Idea

The proof follows Vaught's proof one cardinal higher.
Saturated models of size $\kappa$ replace countable homogeneous models: they exist when $\kappa^{<\kappa} = \kappa$, and two of them of the same theory are isomorphic.
A Vaughtian pair of saturated models then repeats along a chain of length $\kappa^+$ with a fixed set $P$ of size $\kappa$.
The only delicate points are the limit stages of small cofinality, where saturation is not kept by unions.

## Variants

The countable case $\kappa = \aleph_0$ is Vaught's proof itself, with countable homogeneous models in place of saturated ones.
Under the axiom of constructibility, Jensen proved cardinal transfer theorems with morasses, by a different construction.

---
tag: JNXY3WRYFY
kind: statement
role: theorem
name: Svenonius's theorem
aliases: [svenonius-theorem, svenonius-definability-theorem]
msc: ["03C40"]
topics: [JYJHB4YBAH]
audience: research
about: [CY1TXHF6KQ]
uses: [CY1TXHF6KQ, DSQ17TNW1C, EY20BF96SJ, 92SWXST1ZM, 655K8Y7VS8, 8WZF9SBP39, RJBDSA2ETP]
history:
  first_stated: "1959"
sources:
  - book: isbn:9780521587136
---

## Statement

Let $L \subseteq L^+$ be signatures, let $T$ be an $L^+$-[[theory|92SWXST1ZM]], and let $\varphi(x_1, \dots, x_n)$ be an $L^+$-formula.
For a model $\mathcal{A}$ of $T$, write $\mathcal{A} | L$ for its [[reduct|EY20BF96SJ]] to $L$.

1. The following are equivalent.
   - (a) There are $L$-formulas $\psi_1(\bar x), \dots, \psi_k(\bar x)$ with $T \models \bigvee_{i = 1}^{k} \forall \bar x \, (\varphi(\bar x) \leftrightarrow \psi_i(\bar x))$.
   - (b) For every model $\mathcal{A}$ of $T$, every [[automorphism|DSQ17TNW1C]] of $\mathcal{A} | L$ maps $\varphi(\mathcal{A})$ onto itself.
   - (c) Condition (b) holds for the models of $T$ of cardinality at most $\lvert L^+ \rvert + \aleph_0$.
2. If $T$ is [[complete|655K8Y7VS8]], one can take $k = 1$ in (a), so (b) holds if and only if $\varphi$ is $T$-equivalent to an $L$-formula.
3. In particular, let $\mathcal{M}$ be an $L^+$-structure. Then $\varphi(\mathcal{M})$ is [[definable|CY1TXHF6KQ]] in $\mathcal{M} | L$ by an $L$-formula without parameters if and only if, for every [[elementary extension|8WZF9SBP39]] $\mathcal{N}$ of $\mathcal{M}$, every automorphism of $\mathcal{N} | L$ maps $\varphi(\mathcal{N})$ onto itself.

## Remarks

### Why each hypothesis is needed

- Elementary extensions in part 3. In $(\mathbb{N}, <)$ every set is invariant, since the identity is the only automorphism, but the set $E$ of even numbers is not definable from $<$. In an elementary extension $\mathbb{N} + \mathbb{Z}$ of $(\mathbb{N}, <, E)$, shifting the copy of $\mathbb{Z}$ by one place is an automorphism of the order that moves $E$.
- Finitely many formulas in (a). With $L = \emptyset$, $L^+ = \set{P}$ and $T = \set{\forall x \, P(x) \vee \forall x \, \neg P(x)}$, every automorphism preserves $P$, but no single formula defines $P$, since models with the same domain can disagree on $P$. Here $k = 2$ with $\psi_1 = (x = x)$ and $\psi_2 = \neg(x = x)$.

### Consequences

- A set that some automorphism of $\mathcal{M} | L$ moves is not $L$-definable in $\mathcal{M}$; this is the easy direction, used throughout model theory.
- If $T$ implicitly defines a relation symbol $P$ in the sense of the [[Beth definability theorem|RJBDSA2ETP]], then (b) holds for $\varphi = P(\bar x)$. Transporting $\mathcal{A}$ along an automorphism $\alpha$ of $\mathcal{A} | L$ gives a model of $T$ with the same reduct to $L$ and with $\alpha(P^{\mathcal{A}})$ in place of $P^{\mathcal{A}}$, so $\alpha(P^{\mathcal{A}}) = P^{\mathcal{A}}$.

### Converse

Each part is an equivalence; the directions from definability to invariance are immediate, since automorphisms preserve every set defined by an $L$-formula.

### Generalizations

- The [[Chang-Makkai theorem|MFR9Z5PPH4]] replaces "invariant under all automorphisms" by "few images under automorphisms", in a saturated model, and gets definability with parameters.
- If $T$ is complete and $\mathcal{A}$ is a [[saturated model|RMTZ5J64FX]] of $T$, condition (b) for this one model already gives (a), because tuples with the same $L$-type are then moved onto each other by automorphisms of $\mathcal{A} | L$. This is the form used in a [[monster model|EYTTQZ0E1S]]; part 3 avoids saturated models, whose existence may need extra set theory.

## History

Lars Svenonius published the theorem in 1959.
Its proof by an elementary chain, used [[here|PYR2H4K836]], needs no set-theoretic assumptions.

## Explanations

### L1 human

If a property can be written as a formula, then every symmetry of the structure respects it.
Svenonius's theorem gives the converse, with one change: you must also look at the larger structures that look exactly like the original one.
If the property is respected by every symmetry of all of these, then it can be written as a formula.

### L2 human

We test part 3 on $(\mathbb{Z}, <)$ with $E$ the set of even integers.

1. The map $x \mapsto x + 1$ is an automorphism of $(\mathbb{Z}, <)$.
2. It sends $E$ to the set of odd integers, so it does not map $E$ onto itself.
3. Already $\mathcal{N} = \mathcal{M}$ is an elementary extension, so part 3 says that $E$ is not definable in $(\mathbb{Z}, <)$.

A trap is to apply the test only to $\mathcal{M}$ itself when $\mathcal{M}$ has few automorphisms, as $(\mathbb{N}, <)$ does; there the elementary extensions do the work.

### L3 human

The theorem is the automorphism form of the [[Beth definability theorem|RJBDSA2ETP]]: Beth compares two expansions of one $L$-structure, Svenonius compares $\varphi(\mathcal{A})$ with its images under automorphisms.
It underlies the Galois-theoretic view of definability in stability theory, where definable and algebraic closures are read off from automorphism groups of a monster model.

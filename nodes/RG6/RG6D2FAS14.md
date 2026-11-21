---
tag: RG6D2FAS14
kind: statement
role: theorem
name: Existence of indiscernibles
aliases: [existence-of-indiscernible-sequences, ehrenfeucht-mostowski-existence-theorem]
msc: ["03C30", "03C50", "05D10"]
topics: [W9CHA4PD9H]
audience: grad
about: [6EG0ZK1YBX]
uses: [4016QKAHFB, 92SWXST1ZM, 1NR3HAWG9D, YSZ82MRXT8, S1BHE358VX, ZC4BHVHWE9, Z92S2GVCX9, 0FRXBVVR03]
history:
  notes: "Ehrenfeucht and Mostowski proved the existence of indiscernible sequences in 1956 with Ramsey's theorem; the method with the Erdős-Rado theorem is due to Morley."
sources:
  - url: https://en.wikipedia.org/wiki/Indiscernibles
    locator: lead section
  - book: isbn:9780387987606
    locator: Chapter 5
  - book: isbn:9780486488219
    locator: Chapter 3
  - book: isbn:9780486488219
    locator: Chapter 7
---

## Statement

Let $L$ be a signature and let $T$ be an $L$-[[theory|92SWXST1ZM]].
Indiscernible means [[order-indiscernible over the empty set|4016QKAHFB]].

1. (Ramsey form.) Let $\mathcal{M} \models T$ and let $(b_n)_{n \in \N}$ be an injective sequence in $M$. Let $(I, <)$ be an infinite [[linear order|0FRXBVVR03]]. Then some $\mathcal{N} \equiv \mathcal{M}$ has an injective indiscernible sequence $(a_i)_{i \in I}$ such that every formula true at all increasing tuples of $(b_n)$ is true at all increasing tuples of $(a_i)$.
2. In particular, if $T$ has an infinite model, then for every infinite linear order $I$ some model of $T$ has an injective indiscernible sequence indexed by $I$.
3. (Morley form.) Let $L$ be countable, and let the families $X_\alpha$ and $\Psi_k$ satisfy the conditions (a) and (b) below. Then the conclusion (c) holds.

The conditions of part 3 are the following.

- (a) For each $\alpha < \omega_1$, $\mathcal{M}_\alpha \models T$ and $X_\alpha \subseteq M_\alpha$ is a linearly ordered subset with $\abs{X_\alpha} \ge \beth_\alpha$.
- (b) For each $k \in \N$, $\Psi_k = \set{\psi_{k,j}(x_1, \dots, x_{n_k}) : j \in \N}$ is a set of $L$-formulas. For all $k$ and $\alpha$, every increasing $n_k$-tuple of $X_\alpha$ satisfies some $\psi_{k,j}$.
- (c) For each infinite linear order $I$, some $\mathcal{N} \models T$ has an injective indiscernible sequence $(a_i)_{i \in I}$ with this property. For each $k$ there is one $j$ such that $\psi_{k,j}$ holds at all increasing $n_k$-tuples of $(a_i)$.

Here $\beth_\alpha$ is the [[beth number|ZC4BHVHWE9]] and $\omega_1$ is the [[first uncountable ordinal|Z92S2GVCX9]].
The proof is in [[the proof of the existence of indiscernibles|TMWDJVRV3Z]].

## Remarks

### Why each hypothesis is needed

- Infinite models in part 2: a theory whose models all have $5$ elements has no injective sequence with $6$ members, so no injective indiscernible sequence indexed by an infinite order.
- Passing to another model $\mathcal{N}$ in part 1: in $(\N, <)$ no infinite injective sequence is indiscernible, since each $n$ is definable; see [[this non-example|1T221XPKPJ]].
- Countable $L$ in part 3: the proof decides the countably many formulas of $L$ one at a time, in $\omega$ steps. For an uncountable signature the method needs sizes $\beth_\alpha$ for a longer sequence of ordinals $\alpha$.
- All $\alpha < \omega_1$ in part 3: for each $\beta < \omega_1$ there is an infinitary sentence with a model of size $\beth_\beta$ and no larger model; see [[this example|CGEPN90SDZ]]. As a countable theory with types to omit, it meets the hypothesis for $\alpha \le \beta$. The conclusion fails for it, since it would give models of every size.

### Consequences

- Every theory with infinite models has, for each infinite linear order $I$, a model with an injective indiscernible sequence indexed by $I$, and so a model with many automorphisms; see [[Ehrenfeucht-Mostowski models|TSGB29FJM0]].
- Part 3 with $\Psi_{(p, t)} = \set{\neg \sigma(t(\bar{x})) : \sigma \in p}$, for Skolem terms $t$ and a type $p$ to be omitted, gives the bound for the [[Hanf number|A9XBRF3A7Z]] of omitting types.
- Indiscernible sequences exist in the monster model of every complete theory with infinite models, with any given index order.

### Converse

The converse of part 2 holds: an injective sequence indexed by an infinite order makes the model infinite.
The converse of part 3 holds.
By compactness, the sequence $(a_i)$ stretches to a sequence indexed by an order of size $\beth_\alpha$, in some model of $T$, with the same type.
This stretched sequence is a set $X_\alpha$ of size $\beth_\alpha$ on which each $\Psi_k$ is satisfied.

### Generalizations

A version of the Ramsey form holds for suitable ordered index structures whose finite substructures form a [[Ramsey class|8XS8FCTF8T]], and it gives [[generalized indiscernibles|RQS808ZC8T]].
The same proofs give indiscernible sequences over a set $A$ of parameters, by adding constants for $A$ to $L$.

## History

Ehrenfeucht and Mostowski proved part 1 in 1956, with Ramsey's theorem, to build models with many automorphisms.
The method of part 3, with the Erdős-Rado theorem in place of Ramsey's theorem, is due to Morley, who used it to compute the Hanf number for omitting types.

## Explanations

### L1 human

Ramsey's theorem says that in any coloring of pairs of a large enough set, some big part has all pairs of one color.
Here the colors are the answers to questions in the language of the structure.
Take, for example, the yes or no question "is the first element smaller than the second?".
Ramsey's theorem gives a big part on which the answers agree, and a limit argument turns this into an infinite sequence on which all answers agree.

### L2 human

We find an indiscernible sequence of length $3$ for one formula, from $b_n = n$ in $(\Z, <)$, with $\varphi(x_1, x_2) := \exists y \, (x_1 < y < x_2)$.

1. Color the pair $\set{m < n}$ red if $\varphi(m, n)$ holds and blue otherwise. Then $\set{m < n}$ is blue exactly when $n = m + 1$.
2. The set $H = \set{0, 2, 4}$ has only red pairs, so it is homogeneous for $\varphi$.
3. The tuples $(0, 2)$, $(0, 4)$ and $(2, 4)$ all satisfy $\varphi$, so the sequence $0, 2, 4$ is indiscernible for $\varphi$.

The typical use is to start with any infinite set, extract a homogeneous part for finitely many formulas, and finish with compactness.
The trap is to expect the sequence inside the given model: compactness places it in an elementary extension, or in another model of the same theory.

### L3 human

The theorem is the model-theoretic face of partition calculus: finite Ramsey theory gives indiscernibles of every order type by compactness, and the Erdős-Rado theorem gives indiscernibles that keep a property of every member of a family of large models.
The second kind is what the omission of types needs, because omitting a type is not expressed by one first-order sentence.
The general principle is the modeling property of an index structure: indiscernibles indexed by $I$ exist with the local properties of any $I$-indexed family when the age of $I$ is a Ramsey class.
These results lead to [[Ehrenfeucht-Mostowski models|TSGB29FJM0]], to the [[Hanf number|A9XBRF3A7Z]] of infinitary logic, and to the two-cardinal theorems of [[Vaught|XT227BYP7B]] and [[Chang|4STP69KESQ]].

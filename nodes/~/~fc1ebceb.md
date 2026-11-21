---
tag: ~fc1ebceb
kind: example
name: The intersection of a chain of refining equivalence relations
aliases: [intersection-of-refining-equivalence-relations, eliminable-bounded-hyperimaginary]
msc: ["03C45"]
topics: [SZRM3N6BXW]
audience: research
instance_of: [~edde366e]
uses: [~bba20a81, 0G8VEZ3WTK, 1NR3HAWG9D, EYTTQZ0E1S, DSQ17TNW1C]
sources:
  - book: isbn:9780521119559
---

## Example

Let $L = \set{E_n : n \in \mathbb{N}}$ with each $E_n$ binary.
Let $T_0$ say that each $E_n$ is an [[equivalence relation|0G8VEZ3WTK]], that $E_0$ has one class, and that each $E_n$-class is the union of exactly two $E_{n+1}$-classes.
Let $T$ be any completion of $T_0$, with [[monster model|EYTTQZ0E1S]] $\mathbb{M}$, and let $E_\infty = \bigcap_n E_n$.
We show that the classes of $E_\infty$ are bounded [[hyperimaginaries|~bba20a81]] that are eliminable, and that $E_\infty$ is not definable.

1. Type-definable. $E_\infty$ is defined by the partial type $\set{E_n(x, y) : n \in \mathbb{N}}$ over $\emptyset$. An intersection of equivalence relations is an equivalence relation.
2. Chain. Each $E_{n+1}$ refines $E_n$, since each $E_n$-class is a union of $E_{n+1}$-classes. So $E_0 \supseteq E_1 \supseteq \cdots$.
3. Bounded. By induction, $E_n$ has exactly $2^n$ classes. The class $a / E_\infty$ is determined by the sequence $(a / E_n)_n$, and there are at most $2^{\aleph_0}$ such sequences. So $E_\infty$ has fewer than $|\mathbb{M}|$ classes.
4. Not definable. Suppose $\varphi(x, y)$ defines $E_\infty$. Then $\set{E_n(x, y) : n \in \mathbb{N}} \cup \set{\neg \varphi(x, y)}$ is not realized in the saturated $\mathbb{M}$, so it is inconsistent. By [[compactness|1NR3HAWG9D]] and step 2, $E_N(x, y) \to \varphi(x, y)$ for some $N$.
5. Then $E_N \subseteq E_\infty \subseteq E_{N+1}$. But each $E_N$-class contains two $E_{N+1}$-classes, so $E_{N+1} \neq E_N$, a contradiction.
6. Eliminable. Let $e = a / E_\infty$ and $d = (a / E_n)_n$. An [[automorphism|DSQ17TNW1C]] $\sigma$ fixes $d$ exactly when $E_n(\sigma a, a)$ for every $n$. That is the condition $E_\infty(\sigma a, a)$, which says that $\sigma$ fixes $e$.
7. So $e$ and $d$ have the same stabilizer, and they are interdefinable. Each $a / E_n$ is an imaginary, so $e$ is eliminable.

## Remarks

The same argument applies to any decreasing chain of $\emptyset$-definable equivalence relations that is not eventually constant.
The intersection is type-definable and not definable, and its classes are eliminable.
Boundedness uses that each $E_n$ has finitely many classes.
If some $E_n$ has infinitely many classes, it has $|\mathbb{M}|$ classes by saturation, and so does the intersection.
In a stable theory, every $\emptyset$-type-definable equivalence relation is an intersection of $\emptyset$-definable ones, so intersections are the general case there.

## Explanations

### L1 human

Sort people into two halves, then split each half in two, and keep going forever.
Two people are in the same final group when they stay together at every step.
No single step describes the final groups, since each step is still too coarse.
But each final group is named by the list of halves it passes through, one per step.

### L2 human

We compute in one model of $T_0$.

1. Let $M = \set{0, 1}^{\mathbb{N}} \times \mathbb{N}$, with $E_n((s, k), (t, l))$ when $s$ and $t$ agree on their first $n$ entries.
2. $E_0$ holds everywhere, and an $E_n$-class, given by a word of length $n$, splits by the next entry into two $E_{n+1}$-classes.
3. Take $s$ and $t$ that first differ at entry $5$, counting from $0$. Then $E_5((s, 0), (t, 0))$ holds and $E_6$ fails.
4. $E_\infty$ holds when $s = t$, so the class of $(s, k)$ is $\set{s} \times \mathbb{N}$.

The typical use is as the simplest bounded hyperimaginary that is not an imaginary of a single definable relation.
A trap is to think that steps 4 and 5 need a particular model: the argument works in any completion.

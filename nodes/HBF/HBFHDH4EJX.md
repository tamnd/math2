---
tag: HBFHDH4EJX
kind: statement
role: theorem
name: Urysohn metrization theorem
msc: ["54E35"]
uses: [0CQHFPGJ45, 03PPNCM9GG, 03HMJASQBQ, 0S1FJ8VEX9, 091GJ3FYD7]
about: [091GJ3FYD7]
sources:
  - url: https://en.wikipedia.org/wiki/Metrizable_space
---

## Statement

Let $X$ be a [[topological space|0CQHFPGJ45]].
Assume that $X$ is [[second-countable|03PPNCM9GG]], [[regular|03HMJASQBQ]] and [[Hausdorff|0S1FJ8VEX9]].
Then $X$ is [[metrizable|091GJ3FYD7]]: there is a metric on $X$ whose open sets are exactly the open sets of $X$.

## Remarks

A second-countable regular space is normal, so [[Urysohn's lemma|01EY3VR7ZD]] applies to it.
With a countable base one picks countably many continuous functions $f_n \colon X \to [0, 1]$ that separate points from closed sets.
The map $x \mapsto (f_n(x))_n$ is then an embedding of $X$ into the [[Hilbert cube|JKMMJ8RFC6]] $[0,1]^{\N}$, which is metrizable.
For example, every subspace of $\R^n$ satisfies the hypotheses, and so does every compact Hausdorff space with a countable base.
Second countability cannot be dropped: the [[Sorgenfrey line|Y4T3GVK8GV]] is regular and Hausdorff but not metrizable.
Regularity cannot be dropped either: there are second-countable Hausdorff spaces that are not regular, and a metrizable space is always regular.
The converse holds only in part: a metrizable space is regular and Hausdorff, and it is second-countable exactly when it is separable.

## Explanations

### L1 human

A metric is a way to measure distances, and many spaces are given only by their open sets.
The theorem says when distances can be put back in.
It is enough that the space has a countable family of basic open sets and that points and closed sets can be kept apart by open sets.
So a large class of spaces that look abstract can be treated as metric spaces.

### L2 human

The theorem is the first answer to the metrization problem: which topological spaces come from a metric.
The proof is an embedding into the Hilbert cube, a standard method that also shows each such space is a subspace of one fixed compact metric space.
It characterizes separable metrizable spaces as the second-countable regular Hausdorff spaces.
The [[Nagata–Smirnov metrization theorem|KB11T6389G]] and the [[Bing metrization theorem|RGCZ2P9QRM]] remove the countability condition and give a full characterization.

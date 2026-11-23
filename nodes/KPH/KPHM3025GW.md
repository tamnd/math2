---
tag: KPHM3025GW
kind: definition
name: WWKL0
aliases: [weak-weak-konigs-lemma-system]
msc: ["03B30", "03F35", "03D32"]
topics: [BY8AAFN7C5]
audience: research
defines: BJQ77Y2QFX
uses: [XQENB067R3, DC60FYCSPM, 7W9EG02T79, W9VYJRBF9N]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Additional systems
  - url: https://en.wikipedia.org/wiki/K%C5%91nig%27s_lemma
    locator: Computability aspects
---

## Definition

A computable binary tree can keep half of all strings at every length and still have no computable path, and $\mathsf{WWKL}_0$ is the system that adds paths through such trees.
We work in the language of [[second-order arithmetic|DC60FYCSPM]].
Let $2^{<\mathbb{N}}$ be the set of finite binary strings, coded by natural numbers.
Write $\lvert \sigma \rvert$ for the length of $\sigma$, and $\tau \preceq \sigma$ when $\tau$ is an initial segment of $\sigma$.

1. A *tree* is a set $T \subseteq 2^{<\mathbb{N}}$ such that $\sigma \in T$ and $\tau \preceq \sigma$ imply $\tau \in T$.
2. For a tree $T$ and $n \in \mathbb{N}$, let $T_n = \{\sigma \in T : \lvert \sigma \rvert = n\}$.
   This is a finite set, and $\mathsf{RCA}_0$ proves that its number of elements $\lvert T_n \rvert$ exists.
3. A tree $T$ has *positive measure* if there is a rational number $q > 0$ such that $\lvert T_n \rvert / 2^n \ge q$ for all $n$.
4. A *path* of $T$ is a function $f \colon \mathbb{N} \to \{0, 1\}$ such that the string $f \upharpoonright n = \langle f(0), \dots, f(n-1) \rangle$ is in $T$ for every $n$.
5. *Weak weak König's lemma*, $\mathrm{WWKL}$, is the sentence: every tree of positive measure has a path.
6. $\mathsf{WWKL}_0$ is the system $\mathsf{RCA}_0 + \mathrm{WWKL}$.
   Its axioms are the basic axioms of arithmetic, induction for $\Sigma^0_1$ formulas, comprehension for $\Delta^0_1$ formulas, and $\mathrm{WWKL}$.

## Notation

The name "weak weak König's lemma" goes back to Yu and Simpson in 1990.
Some texts call a tree of positive measure a *fat* tree, and some write $\mathrm{WWKL}$ for the whole system.
The subscript $0$ in $\mathsf{WWKL}_0$ means, as for [[RCA0|XQENB067R3]], that induction is restricted to $\Sigma^0_1$ formulas.
In an $\omega$-model $(\mathbb{N}, \mathcal{S})$, a tree of positive measure is a tree $T \in \mathcal{S}$ whose set of paths has positive measure in [[Cantor space|W9VYJRBF9N]].

## Remarks

### Why the rational bound

Each string of $T_{n+1}$ has its initial segment of length $n$ in $T_n$, and each string of $T_n$ has at most two extensions of length $n + 1$.
So $\lvert T_{n+1} \rvert \le 2 \lvert T_n \rvert$, and the ratio $\lvert T_n \rvert / 2^n$ is non-increasing in $n$.
Its limit is the measure of the set of paths of $T$.
$\mathsf{RCA}_0$ does not prove that this limit exists as a real number, because a computable non-increasing sequence of rationals can converge to a noncomputable real.
The rational bound $q$ in clause 3 says "the limit is positive" without using the limit.
Since the ratio is non-increasing, it is enough to ask for $\lvert T_n \rvert / 2^n \ge q$ for infinitely many $n$.

### Place among the subsystems

A tree of positive measure has $\lvert T_n \rvert \ge q 2^n > 0$ for every $n$, so it is infinite.
So [[weak König's lemma|7W9EG02T79]] gives it a path, and $\mathsf{WKL}_0$ proves $\mathrm{WWKL}$.
Yu and Simpson showed that $\mathsf{WWKL}_0$ is strictly weaker than $\mathsf{WKL}_0$.
$\mathsf{RCA}_0$ does not prove $\mathrm{WWKL}$, by the [[computable tree with no computable path|7KNY1EMB1G]].
The concept [[weak weak König's lemma|BJQ77Y2QFX]] gives the equivalents in measure theory and the link with randomness.

### Watch out

The hypothesis is about every level, not about the limit, and not about a single level.
A tree that keeps $3$ of the $4$ strings of length $2$ and then only the strings $0^n$ has ratio $2^{-n}$ eventually, so it does not have positive measure.
Clause 3 with "$\lvert T_n \rvert > 0$ for all $n$" in place of the bound $q$ would turn $\mathrm{WWKL}$ into weak König's lemma.

## Explanations

### L1 human

A binary tree is a family of finite strings of $0$ and $1$, closed under cutting off the end of a string.
At each length $n$ there are $2^n$ strings, and the tree keeps some of them.
The tree has positive measure if it always keeps at least a fixed fraction, such as one half, at every length.
The axiom $\mathrm{WWKL}$ says that such a tree has an infinite branch.
For example, the tree of strings that do not start with $1, 1$ keeps $3$ of the $4$ strings of length $2$, and the branch $0, 0, 0, \dots$ runs through it.

### L2 human

Let $T$ be the set of strings $\sigma$ that do not have $\sigma(0) = \sigma(1) = 1$, and do not have $\sigma(2) = \sigma(3) = 1$, wherever these positions exist.

1. For $n \le 1$ no condition applies, so the ratio is $1$.
2. For $n = 2$ and $n = 3$ only the first condition applies, and it removes one quarter of the strings, so the ratio is $\tfrac{3}{4}$.
3. For $n \ge 4$ the two conditions concern disjoint positions, so the ratio is $\tfrac{3}{4} \cdot \tfrac{3}{4} = \tfrac{9}{16}$.

Check: at $n = 4$ there are $16$ strings, $3$ choices for the first two bits and $3$ for the next two, so $\lvert T_4 \rvert = 9$.
So $q = \tfrac{9}{16}$ works, and $T$ has positive measure.
The typical use of $\mathrm{WWKL}$: a theorem of measure theory says that some set of positive measure is not empty, and the proof codes that set as the set of paths of a tree.
The trap: it is not enough that each $\lvert T_n \rvert$ is positive; the fraction must stay above one fixed $q$.

### L3 human

In topological terms, $\mathrm{WKL}$ says that a closed subset of Cantor space coded by an infinite tree is not empty, and $\mathrm{WWKL}$ says the same only for closed sets of positive measure.
So $\mathrm{WKL}$ is about compactness and $\mathrm{WWKL}$ is about measure.
The computability-theoretic content is randomness.
The $\omega$-models of $\mathsf{WWKL}_0$ are the Turing ideals that contain, for each $X$, a set that is [[Martin-Löf random|X5KD3X3VJ3]] relative to $X$.
The bridge is Kučera's lemma: a set that is random relative to the tree has a tail that is a path of the tree.
In constructive mathematics, forms of the fan theorem play the part that $\mathrm{WKL}$ plays here, a topic of [[constructive reverse mathematics|3XFMHSCVYZ]].

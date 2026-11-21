---
tag: QDJHX2YABM
kind: example
name: Finite sets are not pseudo-elementary
aliases: [finite-sets-not-pc-class, finiteness-not-pseudo-elementary]
msc: ["03C52"]
topics: [JYJHB4YBAH]
audience: grad
not_instance_of:
  - target: YEC1Q3A490
    note: "Any theory whose models have finite reducts of every size has a model with an infinite reduct, by compactness."
uses: [YEC1Q3A490, 1NR3HAWG9D, 92SWXST1ZM, EY20BF96SJ]
sources:
  - book: isbn:9780521587136
---

## Example

Let $L = \emptyset$, so that $L$-structures are nonempty sets, and let $\mathcal{K}$ be the class of finite sets.
Then $\mathcal{K}$ is not a [[pseudo-elementary class|YEC1Q3A490]], even in the $\mathrm{PC}_\Delta$ sense.

1. Suppose $L^+$ is a signature and $T$ is an $L^+$-[[theory|92SWXST1ZM]] such that $\mathcal{K}$ is the class of [[reducts|EY20BF96SJ]] to $L$ of the models of $T$.
2. For each $n \ge 1$, the $n$-element set lies in $\mathcal{K}$, so it expands to a model of $T$ with exactly $n$ elements.
3. So each finite subset of $T \cup \set{\exists^{\ge n} x \, (x = x) : n \ge 1}$ has a model.
4. By [[compactness|1NR3HAWG9D]], the whole set has a model $\mathcal{B}$.
5. Then $\mathcal{B} \models T$, and its reduct to $L$ is infinite, so it is not in $\mathcal{K}$, a contradiction.

## Remarks

The argument only uses that $\mathcal{K}$ contains arbitrarily large finite structures and no infinite one.
So no pseudo-elementary class of structures in any signature consists of finite structures of unbounded size.
In finite model theory, where only finite structures are considered, this obstruction disappears, and [[Fagin's theorem|BG8Q0BYSQ3]] describes the classes that are $\mathrm{PC}$ relative to finite structures.

## Explanations

### L1 human

"The set is finite" cannot be expressed by any list of rules, even with hidden extra structure.
Rules that allow sets of every finite size are forced, by compactness, to allow an infinite set as well.

### L2 human

Try to define finiteness on a set $A$ by adding a linear order $<$ with a least and a greatest element in which every element except the greatest has an immediate successor.
Every finite set has such an order, but so does $\omega + \omega^*$, the natural numbers followed by a reversed copy of them.
A trap is to think that the successor condition forces the order to be finite: it only controls each step, and first-order axioms cannot forbid infinitely many steps.

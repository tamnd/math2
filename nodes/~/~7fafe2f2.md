---
tag: ~7fafe2f2
kind: definition
name: Pseudo-elementary class
aliases: [pseudo-elementary-class-definition, basic-pseudo-elementary-class]
msc: ["03C52"]
topics: [JYJHB4YBAH]
audience: grad
defines: ~d3135277
uses: [WDVVEYD6AT, 983GZBQYT4, EY20BF96SJ, DKFGQTRYZE, 92SWXST1ZM, MVCH6N9SNW]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoelementary_class
    locator: Definition
  - book: isbn:9780521587136
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]], and let $\mathcal{K}$ be a class of [[$L$-structures|983GZBQYT4]].

1. $\mathcal{K}$ is a *basic pseudo-elementary class*, or $\mathrm{PC}$ class, if there are a signature $L^+ \supseteq L$ and an $L^+$-[[sentence|DKFGQTRYZE]] $\sigma$ such that $\mathcal{K}$ is the class of [[reducts|EY20BF96SJ]] $\mathcal{B} | L$ of the [[models|MVCH6N9SNW]] $\mathcal{B}$ of $\sigma$.
2. $\mathcal{K}$ is a *pseudo-elementary class*, or $\mathrm{PC}_\Delta$ class, if there are a signature $L^+ \supseteq L$ and an $L^+$-[[theory|92SWXST1ZM]] $T$ such that $\mathcal{K}$ is the class of reducts $\mathcal{B} | L$ of the models $\mathcal{B}$ of $T$.

Equivalently, an $L$-structure $\mathcal{A}$ lies in $\mathcal{K}$ exactly when $\mathcal{A}$ has an expansion to $L^+$ that satisfies $\sigma$, or $T$.

## Notation

$\mathrm{PC}(L)$ and $\mathrm{PC}_\Delta(L)$ denote the collections of such classes.
One writes $\mathcal{K} = \operatorname{Mod}(\sigma) | L$ or $\mathcal{K} = \operatorname{Mod}(T) | L$.

## Remarks

- Every basic elementary class is $\mathrm{PC}$, and every elementary class is $\mathrm{PC}_\Delta$, with $L^+ = L$.
- Every $\mathrm{PC}$ class is $\mathrm{PC}_\Delta$, and both kinds of class are closed under isomorphism.
- The symbols of $L^+ \setminus L$ may be renamed freely, so one can assume that the new symbols of two given classes are disjoint.

## Explanations

### L1 human

A pseudo-elementary class is a family of structures that can be described by rules, if you are allowed to add some hidden extra structure to describe them and then forget it.

### L2 human

We check that the class of infinite sets is $\mathrm{PC}$, with $L = \emptyset$.

1. Let $L^+ = \set{f}$ with $f$ unary, and let $\sigma$ say that $f$ is injective and some element is not a value of $f$.
2. If $(A, f) \models \sigma$, then $a, f(a), f(f(a)), \ldots$, for $a$ outside the image of $f$, are pairwise distinct, so $A$ is infinite.
3. If $A$ is infinite, it contains distinct elements $a_0, a_1, \ldots$; let $f(a_n) = a_{n+1}$ and $f(x) = x$ elsewhere. Then $(A, f) \models \sigma$.

The trap is in step 3: the map must stay injective, which is why it fixes the elements outside the sequence.

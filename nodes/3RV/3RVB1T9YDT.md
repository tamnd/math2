---
tag: 3RVB1T9YDT
kind: statement
role: theorem
name: Extended Goodstein's theorem
msc: ["03F30", "03F15"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [XQMNJF241J, 0YSCSX5YZC, 6GD30FGYDZ, KT50SMH3EC, MPSCREYC3M]
about: [XQMNJF241J, KT50SMH3EC]
history:
  first_stated: "1944"
  notes: "The extended form with an arbitrary nondecreasing sequence of bases is the form studied in Goodstein's 1944 paper, as reported in the Wikipedia article."
sources:
  - wikipedia: en:150062@r1368439001
    locator: Goodstein's theorem, section Proof of Goodstein's theorem > Extended Goodstein's theorem
    note: adopted
    mention: wikipedia://en/150062#Z2SW
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/Goodstein's_theorem
    locator: Extended Goodstein's theorem
inventory: [KS3YDTBRHQ]
---

## Statement

For integers $2 \le b \le c$ and $n \in \N$, let $B_{b,c}(n)$ be the number that we get when we replace every $b$ in the hereditary base-$b$ notation of $n$ by $c$.
The hereditary notation is defined on the page [[Goodstein's theorem|XQMNJF241J]], and $B_{b,c}(0) = 0$.
Let $b_1, b_2, b_3, \dots$ be a nondecreasing sequence of integers with $b_1 \ge 2$.
The *extended Goodstein sequence* of $m \in \N$ for these bases is defined by $E_1 = m$ and $E_{k+1} = B_{b_k, b_{k+1}}(E_k) - 1$ as long as $E_k > 0$.

**Theorem.**

1. For every $m \in \N$ and every nondecreasing sequence of bases with $b_1 \ge 2$, there is a $k$ with $E_k = 0$.
2. For the bases $b_k = k + 1$ the sequence is the Goodstein sequence, so [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$ does not prove part 1 even for this one sequence of bases.
3. For every fixed primitive recursive sequence of bases, part 1 is provable in $\mathsf{PA}$ plus transfinite induction up to [[epsilon nought|KT50SMH3EC]].

The [[proof|~5684585f]] is the proof of Goodstein's theorem with one lemma made general.

## Remarks

### Why each hypothesis is needed

- The bases must not decrease. For $b_1 = 3$ and $b_2 = 2$ the number $2$ is a digit of base $3$ but not of base $2$, so $B_{3,2}(2)$ has no meaning as a base-$2$ notation.
- The condition $b_1 \ge 2$ is needed because base $1$ has no positional notation with digits $0 < c < 1$.
- The notation must be hereditary for the ordinal argument to reach $\varepsilon_0$. With plain base-$b$ notation the ordinals stay below $\omega^\omega$, and the weak sequences terminate by a proof in $\mathsf{PA}$.
- Part 1 quantifies over arbitrary sequences of bases. This is not a sentence of first-order arithmetic, so only versions for definable sequences of bases can be compared with $\mathsf{PA}$.

### Consequences

- A faster growth of the bases does not prevent termination. For example the bases $b_k = 2k$ or $b_k = 2^k$ also give sequences that reach $0$.
- If $b_{k+1} = b_k$, the step is a subtraction of $1$ only. So long constant stretches of bases are allowed.

### Converse

The theorem has no hypothesis on $m$, so the converse question does not arise for $m$.
For the bases, the hypothesis is sufficient but not necessary.
The proof works whenever every digit, at every level of the hereditary notation of $E_k$, is below $b_{k+1}$.
A nondecreasing sequence of bases is the simplest condition that gives this for every $m$.

### Generalizations

The [[Kirby-Paris hydra|~360e5faf]] gives the same freedom: every choice of the numbers of new heads leads to the death of the hydra.

### Examples

Let $b_1 = 2$, $b_2 = 4$, $b_3 = 6$, and so on, with $m = 3$.
Then $E_1 = 2 + 1$ becomes $4 + 1 - 1 = 4$, and $E_2 = 4 = 4^1$ becomes $E_3 = 6 - 1 = 5$.
Then $E_4 = 4$, and the sequence reaches $E_8 = 0$.
Let a step change base $4$ into base $9$ with $E_k = 3 \cdot 4^{4^4} + 4$.
The ordinal is $3 \omega^{\omega^\omega} + \omega$, and $E_{k+1} = 3 \cdot 9^{9^9} + 8$ has the smaller ordinal $3 \omega^{\omega^\omega} + 8$.

## History

The Wikipedia article on Goodstein's theorem reports that Goodstein's 1944 paper studied this extended form.
It also reports that Goodstein related the extended form to transfinite induction below $\varepsilon_0$.

## Explanations

### L1 human

In Goodstein's game the base goes up by one at each step: $2$, $3$, $4$, and so on.
In the extended game the base can jump, for example from $4$ to $9$, or it can stay the same.
After each change of base we still subtract $1$.
Even if the base jumps very fast, the numbers come back to $0$ in the end.

### L2 human

A worked check with bases $2, 4, 6, 8, \dots$ and $m = 3$.

1. $E_1 = 3 = 2^1 + 1$ in base $2$, with ordinal $\omega + 1$.
2. Replace $2$ by $4$: $4^1 + 1 = 5$, and subtract $1$: $E_2 = 4$.
3. In base $4$, $E_2 = 4^1$, with ordinal $\omega$.
4. Replace $4$ by $6$ and subtract $1$: $E_3 = 5$. This is a digit in base $6$, with ordinal $5$.
5. The digits stay the same under each later base change, so $E_4 = 4$, $E_5 = 3$, $E_6 = 2$, $E_7 = 1$, $E_8 = 0$.

The ordinals $\omega + 1 > \omega > 5 > 4 > \cdots > 0$ decrease, as in the proof.
The trap: a faster growth of the bases makes the numbers larger at first, but it does not change the ordinal at the moment of the base change.

### L3 human

The extended theorem shows that the ordinal of the sequence depends only on the shape of the hereditary notation and not on the base.
Every descending sequence of ordinals below $\varepsilon_0$ that is primitive recursive can be slowed down to such a sequence, so the extended theorem is a form of the well-foundedness of $\varepsilon_0$.
This is the link between Goodstein's theorem and [[Gentzen's consistency proof|QPV0HNP22S]], which needs well-foundedness only for primitive recursive descending sequences.

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

The extended theorem says that Goodstein sequences still reach $0$ when the base jumps by any amount at each step, or stays the same, as long as it never goes down.

For integers $2 \le b \le c$ and $n \in \mathbb{N}$, let $B_{b,c}(n)$ be the number that we get when we replace every $b$ in the hereditary base-$b$ notation of $n$ by $c$.
The hereditary notation is defined in [[Goodstein's theorem|XQMNJF241J]], and $B_{b,c}(0) = 0$.
Let $b_1, b_2, b_3, \dots$ be a nondecreasing sequence of integers with $b_1 \ge 2$.
The *extended Goodstein sequence* of $m \in \mathbb{N}$ for these bases is defined by $E_1 = m$ and $E_{k+1} = B_{b_k, b_{k+1}}(E_k) - 1$ as long as $E_k > 0$.

**Theorem.**

1. For every $m \in \mathbb{N}$ and every nondecreasing sequence of bases with $b_1 \ge 2$, there is a $k$ with $E_k = 0$.
2. For the bases $b_k = k + 1$ the sequence is the Goodstein sequence, so [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$ does not prove part 1 even for this one sequence of bases.
3. For every fixed primitive recursive sequence of bases, part 1 is provable in $\mathsf{PA}$ plus transfinite induction up to [[epsilon nought|KT50SMH3EC]].

The [[proof|XJEMYS8MH6]] is the proof of Goodstein's theorem with one lemma made general.

## Remarks

### Bases that jump

Take the bases $2, 4, 6, 8, \dots$ and start at $m = 3$.
In base $2$ we have $E_1 = 2^1 + 1$.
Replace $2$ by $4$ and subtract $1$:
$$E_2 = (4^1 + 1) - 1 = 4 = 4^1.$$
Replace $4$ by $6$ and subtract $1$:
$$E_3 = 6^1 - 1 = 5.$$
Now $5$ is a single digit in base $6$, and it stays a digit in every larger base.
So $E_4 = 4$, $E_5 = 3$, $E_6 = 2$, $E_7 = 1$ and $E_8 = 0$.
The ordinals of the terms are $\omega + 1, \omega, 5, 4, 3, 2, 1, 0$, and they go down at every step.

A large jump works in the same way.
Let one step change base $4$ into base $9$, with $E_k = 3 \cdot 4^{4^4} + 4$.
In hereditary base $4$ this is $4^{4^4} \cdot 3 + 4^1$, with ordinal $\omega^{\omega^\omega} \cdot 3 + \omega$.
The step gives
$$E_{k+1} = 3 \cdot 9^{9^9} + 9 - 1 = 3 \cdot 9^{9^9} + 8,$$
with the smaller ordinal $\omega^{\omega^\omega} \cdot 3 + 8$.
The number grew enormously, but the ordinal went down.

### Why each hypothesis is needed

The bases must not decrease.
For $b_1 = 3$ and $b_2 = 2$, the number $2$ is a digit of base $3$ but not of base $2$, so $B_{3,2}(2)$ is not a base-$2$ notation at all.

The condition $b_1 \ge 2$ is needed because base $1$ has no positional notation with digits $0 < c < 1$.

The notation must be hereditary for the ordinal argument to reach $\varepsilon_0$.
With plain base-$b$ notation the ordinals stay below $\omega^\omega$, and $\mathsf{PA}$ proves that these weak sequences terminate.

Part 1 quantifies over arbitrary sequences of bases, which is not a sentence of first-order arithmetic.
So only versions for definable sequences of bases, as in parts 2 and 3, can be compared with $\mathsf{PA}$.

### What it gives you

Faster bases do not prevent termination.
The bases $b_k = 2k$ or $b_k = 2^k$ also give sequences that reach $0$.
If $b_{k+1} = b_k$, the step is only a subtraction of $1$, so long constant stretches of bases are allowed too.

### The converse

The theorem has no hypothesis on $m$, so the converse question concerns the bases only.
There the hypothesis is sufficient but not necessary.
The proof works whenever every digit, at every level of the hereditary notation of $E_k$, is below $b_{k+1}$.
A nondecreasing sequence of bases is the simplest condition that gives this for every $m$.

### Watch out

A faster growth of the bases makes the numbers larger at first, and it is tempting to think that it makes the sequence longer in ordinal terms too.
It does not: the ordinal at the moment of the base change stays the same.
In the example with bases $2, 4, 6, \dots$ the sequence of $3$ ends at step $8$, and with bases $2, 3, 4, \dots$ it ends at step $6$.
What changes is how many single subtractions the last digit needs, not whether the sequence ends.

### Try it

Run the sequence of $m = 2$ with the bases $2, 5, 5, 5, \dots$.
The answer is $E_1 = 2^1$, then $E_2 = 5 - 1 = 4$, then $E_3 = 3$, $E_4 = 2$, $E_5 = 1$ and $E_6 = 0$.

## History

The extended form, with an arbitrary nondecreasing sequence of bases, is the form that Goodstein studied in his paper of 1944.
In that paper he proved it equivalent to the restricted ordinal theorem, a form of transfinite induction below $\varepsilon_0$.

## Explanations

### L1 human

In Goodstein's game the base goes up by one at each step: $2$, $3$, $4$, and so on.
In the extended game the base can jump, for example from $4$ to $9$, or it can stay the same.
After each change of base we still subtract $1$.
Even if the base jumps very fast, the numbers come back to $0$ in the end.

### L2 human

We check the ordinal argument on the bases $2, 4, 6, \dots$ and $m = 3$.
The term $E_1 = 2^1 + 1$ has ordinal $\omega + 1$.
After the change to base $4$ and the subtraction, $E_2 = 4^1$ has ordinal $\omega$.
After the change to base $6$, $E_3 = 5$ is a digit with ordinal $5$.
From then on each later base change leaves the digit alone, and the ordinals run $4, 3, 2, 1, 0$.
So the chain
$$\omega + 1 > \omega > 5 > 4 > 3 > 2 > 1 > 0$$
goes down at each step, as the proof predicts.
The example shows the point of the theorem: the ordinal depends on the shape of the notation and not on the base.

### L3 human

The extended theorem shows that the ordinal of a term depends only on the shape of its hereditary notation.
So it is a form of the well-foundedness of $\varepsilon_0$ for descending sequences that come from base changes.
This links Goodstein's theorem with [[Gentzen's consistency proof|QPV0HNP22S]], which needs the well-foundedness of $\varepsilon_0$ only for primitive recursive descending sequences.
The [[Kirby-Paris hydra|C028FF4TWM]] shows the same freedom in a game: every choice of the opponent still leads to the death of the hydra.

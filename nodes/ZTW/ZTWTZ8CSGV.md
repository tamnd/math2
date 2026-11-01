---
tag: ZTWTZ8CSGV
kind: statement
role: theorem
name: Hindman's theorem
msc: [05D10, 11B75]
uses: [G5TWXV565S]
about: [G5TWXV565S]
sources:
  - url: https://en.wikipedia.org/wiki/IP_set
---

## Statement

For a set $S$ of positive integers, let $\mathrm{FS}(S)$ be the set of all sums $\sum_{s \in F} s$ where $F$ is a nonempty finite subset of $S$.
Let the positive integers be coloured with finitely many colours.
Then there is an infinite set $S$ of positive integers such that all elements of $\mathrm{FS}(S)$ have the same colour.

## Remarks

A short proof uses the Stone–Čech compactification $\beta\N$, which is a semigroup under an extension of addition.
It finds an idempotent ultrafilter $p$, that is, $p + p = p$.
The colour class that belongs to $p$ then contains $\mathrm{FS}(S)$, where the elements of $S$ are chosen one by one inside sets that belong to $p$.
A set that contains $\mathrm{FS}(S)$ for some infinite $S$ is called an IP set; the theorem says that in every finite colouring some colour class is an IP set.
Taking two elements $x < y$ of $S$, the numbers $x$, $y$ and $x + y$ have the same colour, which gives [[Schur's theorem|V6XJQXZ7E8]].
The sums must use distinct elements.
With repeats allowed, the sums would include both $x$ and $2x$.
Colour $n$ by the parity of the exponent of $2$ in $n$; then $x$ and $2x$ always get different colours.

## Explanations

### L1 human

Colour the positive integers with a few colours.
Hindman's theorem says you can find infinitely many numbers such that every sum of finitely many different ones among them has the same colour.
So one colour contains a whole infinite family closed under such sums.

### L2 human

Hindman's theorem is an infinite, additive analogue of [[Ramsey's theorem|00TQV3F5S4]] and strengthens Schur's theorem.
Its ultrafilter proof was a starting point of the use of the algebra of $\beta\N$ in [[Ramsey theory|G5TWXV565S]].
IP sets also play a role in topological dynamics and ergodic theory, where recurrence along IP sets is studied.

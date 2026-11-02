---
tag: QNGGCTXK9S
kind: statement
role: theorem
name: Whipple's transformation
msc: [33C20]
uses: [VDBAW9PN88, YZHM3HSM0F]
about: [VDBAW9PN88]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_hypergeometric_function
---

## Statement

Let $n$ be a nonnegative integer and let $a, b, c, d, e$ be complex numbers.
Assume that none of $\frac{a}{2}, 1 + a - b, 1 + a - c, 1 + a - d, 1 + a - e, 1 + a + n$ and $d + e - a - n$ lies in $\set{0, -1, \dots, 1 - n}$.
Write $(x)_k = x (x + 1) \cdots (x + k - 1)$ for the [[Pochhammer symbol|YZHM3HSM0F]].
Then the terminating [[generalized hypergeometric series|VDBAW9PN88]] satisfy
$${}_7F_6\left( \begin{matrix} a,\ 1 + \frac{a}{2},\ b,\ c,\ d,\ e,\ -n \\ \frac{a}{2},\ 1 + a - b,\ 1 + a - c,\ 1 + a - d,\ 1 + a - e,\ 1 + a + n \end{matrix} ; 1 \right)$$
$$= \frac{(1 + a)_n\, (1 + a - d - e)_n}{(1 + a - d)_n\, (1 + a - e)_n}\; {}_4F_3\left( \begin{matrix} -n,\ d,\ e,\ 1 + a - b - c \\ 1 + a - b,\ 1 + a - c,\ d + e - a - n \end{matrix} ; 1 \right).$$

## Remarks

The left side is a very well-poised ${}_7F_6$: each upper parameter plus the matching lower parameter gives $1 + a$.
The ${}_4F_3$ on the right is balanced: its lower parameters sum to $1$ more than its upper parameters.
So the transformation trades well-poised structure for balanced structure, and the number of free parameters stays the same.
A standard proof uses the Pfaff–Saalschütz summation together with an exchange of the order of summation.
For $n = 0$ both sides equal $1$.
If moreover $1 + 2a = b + c + d + e - n$, then $d + e - a - n = 1 + a - b - c$, the ${}_4F_3$ reduces to a balanced ${}_3F_2$, and the Pfaff–Saalschütz theorem sums it; this proves Dougall's formula.

## Explanations

### L1 human

Whipple's transformation rewrites one long finite hypergeometric sum as a shorter one with a simple factor in front.
The two sums look very different, but they have the same value.
Identities of this kind let one move a hard sum into a form where a known summation formula applies.

### L2 human

The theorem connects the two main families of hypergeometric series at $1$: the well-poised ones and the balanced ones.
Combined with the Pfaff–Saalschütz theorem it gives Dougall's ${}_7F_6$ summation.
Its $q$-analogue is Watson's transformation between a very well-poised ${}_8\phi_7$ and a balanced ${}_4\phi_3$.
The name Whipple is attached to several other transformations of ${}_3F_2$ and ${}_7F_6$ series as well.

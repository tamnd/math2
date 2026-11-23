---
tag: ARGGZ9N2SV
kind: example
name: Darapti and existential import
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
instance_of: [1TD6HRM5NG, S4BTTGFR6J]
uses: [1TD6HRM5NG, S4BTTGFR6J, MZBNX2T6Q6, 0KCT6DPXJK, 0ECVK59Y03]
sources:
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Square_of_opposition
    locator: lead section
---

## Example

Darapti is the syllogism of mood AAI in the third figure: all $M$ are $P$, all $M$ are $S$, so some $S$ are $P$.
We check its mood and figure, prove it when $M$ is not empty, and show that it fails when $M$ is empty.

1. The premises are A propositions and the conclusion is an I proposition, so the [[mood|1TD6HRM5NG]] is AAI.
2. The middle term $M$ is the subject of both premises, which is the scheme of the [[third figure|S4BTTGFR6J]].
3. Suppose $M$ is not empty and choose $m$ in $M$.
   By the major premise $m$ is in $P$, and by the minor premise $m$ is in $S$, so some $S$ are $P$.
4. For a failure, let $M$ be the even primes greater than $2$, $P$ the odd numbers and $S$ the even numbers.
5. The only even prime is $2$, so $M$ is [[empty|0ECVK59Y03]].
   In the modern reading "all $M$ are $P$" and "all $M$ are $S$" are both true, because no element of $M$ can fail them.
6. The conclusion "some even numbers are odd" is false.
7. So in the modern reading the premises can be true and the conclusion false, and Darapti is valid only under the assumption that $M$ is not empty.
8. A [[Venn diagram|0KCT6DPXJK]] shows the same.
   "All $M$ are $P$" shades $SM\bar P$ and $\bar S M \bar P$, "all $M$ are $S$" shades $\bar S M P$ and $\bar S M \bar P$, and no premise puts a cross in $SMP$ or $S\bar M P$.
9. Add "some object is in $M$", and the cross must go into the only unshaded part of $M$, which is $SMP$, so the conclusion is shown.

## Remarks

Darapti is one of the $9$ moods that are valid in the traditional reading and invalid in the modern one.
It is not a weakened mood: AAA-3 is invalid, so Darapti has no universal counterpart.
Its name gives its reduction: the p says to convert the minor premise by limitation, "all $M$ are $S$" to "some $S$ are $M$", and then Darii gives the conclusion.
That conversion is the step that needs $M$ to be non-empty, just as subalternation does on the [[square of opposition|VYNBSVZ2TH]].

With a non-empty middle term the form works.
Take $M$ the even primes, $P$ the numbers less than $3$ and $S$ the positive numbers: both premises hold because the only element of $M$ is $2$, and Darapti gives "some positive numbers are less than $3$", which is true.

## Explanations

### L1 human

Darapti says: if all unicorns are white, and all unicorns are horses, then some horses are white.
If unicorns existed, a unicorn would be a white horse, so some horse would be white.
But unicorns do not exist, and then "all unicorns are white" is true in modern logic only because there is nothing to check.
The two premises would then be true even if no horse were white.
So the argument works only when we know that the middle group is not empty.

### L2 human

We test Darapti on a mathematical example where the middle term is empty.

1. Let $M$ be the real numbers $x$ with $x^2 = -1$, $P$ the positive real numbers and $S$ the negative real numbers.
2. No real number has square $-1$, because $x^2 \geq 0$ for every real $x$, so $M$ is empty.
3. "All real $x$ with $x^2 = -1$ are positive" and "all real $x$ with $x^2 = -1$ are negative" are both true in the modern reading.
4. The conclusion "some negative real numbers are positive" is false.

This is why modern logic drops Darapti from the list of valid forms.
The trap is to think that the premises contradict each other: they are both true about nothing, and that is consistent.

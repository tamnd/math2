---
tag: HBTQ8ZVSG6
kind: example
name: The dual weak pigeonhole principle for a polynomial-time function
msc: ["03F30", "68Q15"]
topics: [RA380RWEC0]
audience: research
instance_of: [65K2S22DGZ]
uses: [65K2S22DGZ, FMM44KFZQT, 0HGVCWQGY3]
sources:
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: lead section
---

## Example

Nine letters cannot reach twelve mailboxes so that every mailbox gets a letter.
The dual weak pigeonhole principle says this for maps that a fast program computes.
For a function $f$, the principle $\mathrm{dWPHP}(f)$ is the universal closure of this formula:

$$x > 0 \to \exists v < x(\lvert y \rvert + 1) \; \forall u < x \lvert y \rvert \; f(u) \ne v.$$

It says that $f$ does not map the interval $[0, x \lvert y \rvert)$ onto the larger interval $[0, x(\lvert y \rvert + 1))$.
The schema $\mathrm{dWPHP}(\mathsf{PV})$ has one such axiom for each function symbol $f$ of [[PV|FMM44KFZQT]], and it is the axiom of [[approximate counting|65K2S22DGZ]].
We check one instance in the standard numbers, and then the principle in general.

1. Take $x = 3$ and $y = 5$.
   Then $\lvert y \rvert = 3$, since $5 = 101_2$, so the domain is $[0, 9)$ and the target is $[0, 12)$.
2. Take $f(u) = u + 3$.
   Its values on the domain are $3, 4, \dots, 11$.
3. The number $v = 0$ is below $12$, and $f(u) = u + 3 \ge 3$ for every $u$.
   So $v = 0$ is a witness, and this instance holds.
4. For any $f$, the image of $[0, x \lvert y \rvert)$ has at most $x \lvert y \rvert$ elements.
   The target has $x(\lvert y \rvert + 1) = x \lvert y \rvert + x$ elements, which is more, since $x > 0$.
5. So some $v$ in the target is not a value of $f$, by the finite [[pigeonhole principle|0HGVCWQGY3]].
   Hence $\mathrm{dWPHP}(f)$ is true in the standard numbers for every $f$.

## Remarks

The example shows that $\mathrm{dWPHP}(f)$ is a true and elementary statement.
Its content lies in which theory proves it.
The ratio of the two sizes is $1 + 1/\lvert y \rvert$, so the target is only slightly larger than the domain.
With $y = 1$ the ratio is $2$, and over $S^1_2$ the schema is equivalent to the forms with ratio $2$ or with domain $x$ and target $x^2$.

A witness $v$ is easy to find for $f(u) = u + 3$, but not in general.
For a generic polynomial-time $f$, no polynomial-time algorithm is known that finds a point outside the image.
This is why $\mathrm{dWPHP}(\mathsf{PV})$ is not known to be provable in $\mathsf{PV}_1$ or in $S^1_2$, while $T^2_2$ proves it.

The gap in the sizes cannot be removed.
If the target $x(\lvert y \rvert + 1)$ is replaced by $x \lvert y \rvert$, the statement becomes false for the identity function, which maps the domain onto itself.

## Explanations

### L1 human

Nine letters cannot reach twelve mailboxes so that every mailbox gets a letter.
At least three mailboxes stay empty.
The dual weak pigeonhole principle says this for maps given by fast programs.
Finding an empty mailbox can be hard, even when we know that one exists.

### L2 human

We test the principle for the doubling map with $x = 2$ and $y = 7$.
Since $7 = 111_2$, we have $\lvert 7 \rvert = 3$, so the domain is $[0, 6)$ and the target is $[0, 8)$.
Let $f(u) = 2u$, and list its values on the domain:

$$f(0), \dots, f(5) = 0, 2, 4, 6, 8, 10.$$

The values below $8$ are $0, 2, 4, 6$, so $1$, $3$, $5$ and $7$ are not hit, and $v = 1$ is a witness.

The typical use is as an axiom: one adds $\mathrm{dWPHP}(\mathsf{PV})$ to $\mathsf{PV}_1$ and derives counting facts from it.
Watch out: the values of $f$ need not lie in the target.
Values outside $[0, x(\lvert y \rvert + 1))$, such as $8$ and $10$ here, are allowed, and they simply do not help to cover the target.

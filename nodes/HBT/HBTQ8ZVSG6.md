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

For a function $f$, the dual weak pigeonhole principle $\mathrm{dWPHP}(f)$ is the universal closure of
$$x > 0 \to \exists v < x(\abs y + 1) \; \forall u < x \abs y \; f(u) \ne v.$$
It says that $f$ does not map the interval $[0, x \abs y)$ onto the larger interval $[0, x(\abs y + 1))$.
The schema $\mathrm{dWPHP}(\mathsf{PV})$ has one such axiom for each function symbol $f$ of [[PV|FMM44KFZQT]], and it is the axiom of [[approximate counting|65K2S22DGZ]].
We check one instance in $\N$, and then the principle in general.

1. Take $x = 3$ and $y = 5$. Then $\abs y = 3$, the domain is $[0, 9)$ and the target is $[0, 12)$.
2. Take $f(u) = u + 3$. Its values on $[0, 9)$ are $3, 4, \dots, 11$.
3. The number $v = 0$ satisfies $v < 12$, and $f(u) \ne 0$ for all $u < 9$. So this instance holds with the witness $v = 0$.
4. For any $f$, the image of $[0, x \abs y)$ has at most $x \abs y$ elements. The target has $x(\abs y + 1) > x \abs y$ elements, since $x > 0$.
5. So some $v$ in the target is not a value of $f$, by the finite [[pigeonhole principle|0HGVCWQGY3]]. Hence $\mathrm{dWPHP}(f)$ is true in $\N$ for every $f$.
6. The ratio of the two sizes is $1 + 1/\abs y$, so the target is only slightly larger than the domain. Over $S^1_2$ the schema is equivalent to the schema with domain $x$ and target $x^2$.

## Remarks

The example shows that $\mathrm{dWPHP}(f)$ is a true and elementary statement; its content lies in the theory that proves it.
A witness $v$ cannot in general be found in polynomial time from $x$ and $y$: for a generic $f$, finding a point outside the image is a search problem that a polynomial-time algorithm is not known to solve.
So $\mathrm{dWPHP}(\mathsf{PV})$ is not known to be provable in $\mathsf{PV}_1$ or $S^1_2$, while $T^2_2$ proves it.
If the target $x(\abs y + 1)$ is replaced by $x \abs y$, the statement becomes false for the identity function.

## Explanations

### L1 human

Nine letters cannot reach twelve mailboxes so that every mailbox gets a letter.
At least three mailboxes stay empty.
The dual weak pigeonhole principle says this for maps given by fast programs.
Finding an empty mailbox can be hard, even if one knows that it exists.

### L2 human

We test the principle for the doubling map with $x = 2$ and $y = 7$.

1. $\abs 7 = 3$, so the domain is $[0, 6)$ and the target is $[0, 8)$.
2. Let $f(u) = 2u$. The values on the domain are $0, 2, 4, 6, 8, 10$.
3. The values below $8$ are $0, 2, 4, 6$, so $v = 1$, $3$, $5$ and $7$ are not hit.
4. So $v = 1$ is a witness, and the instance of $\mathrm{dWPHP}(f)$ holds.

The typical use is as an axiom: one adds $\mathrm{dWPHP}(\mathsf{PV})$ to $\mathsf{PV}_1$ and derives counting facts from it.
A trap is to require the values of $f$ to lie in the target: values outside $[0, x(\abs y + 1))$, such as $8$ and $10$ here, are allowed and simply do not help.

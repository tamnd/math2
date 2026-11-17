---
tag: 6QWGVWWVGC
kind: example
name: Testing the claim that each group of order 4 is cyclic
msc: ["00A35", "20K01"]
topics: [N4P3E53HM0]
audience: ug1
instance_of: [F3NNR77WKP]
uses: [F3NNR77WKP, 0ED72CTBNP, 03VFZ2WETT, 0PMRQJVTME, 0KVGH0J5B3, 0WE2NHZJ7B]
sources:
  - url: https://en.wikipedia.org/wiki/Klein_four-group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Counterexample
    locator: lead section
---

## Example

The claim is: "each group with $4$ elements is [[cyclic|0KVGH0J5B3]]".
A group of order $4$ is cyclic exactly when it has an element of [[order|0WE2NHZJ7B]] $4$, because such an element generates all $4$ elements.
We test the claim on two groups of order $4$.

The first test object is the group $\mathbb{Z}/4\mathbb{Z} = \{0, 1, 2, 3\}$ of the [[integers modulo 4|03VFZ2WETT]] with addition.

1. The element $0$ is the identity, so it has order $1$.
2. The multiples of $1$ are $1, 2, 3, 0$. The first return to $0$ is at the fourth step, so $1$ has order $4$.
3. The multiples of $2$ are $2, 0$. So $2$ has order $2$.
4. The multiples of $3$ are $3, 2, 1, 0$. So $3$ has order $4$.
5. The element $1$ has order $4$, so $\mathbb{Z}/4\mathbb{Z}$ is cyclic. This example agrees with the claim.

The second test object is the [[Klein four-group|0PMRQJVTME]] $V = \{e, a, b, c\}$, where $e$ is the identity, $a^2 = b^2 = c^2 = e$, and the product of two distinct elements of $\{a, b, c\}$ is the third one.

6. The element $e$ has order $1$.
7. The elements $a$, $b$ and $c$ are not $e$, and their squares are $e$. So each of them has order $2$.
8. No element of $V$ has order $4$, so $V$ is not cyclic.
9. The group $V$ has order $4$, so it is a [[counterexample|0ED72CTBNP]] to the claim. The claim is false.

## Remarks

The example shows the two roles of test examples.
A confirming example, here $\mathbb{Z}/4\mathbb{Z}$, only shows that the claim has a chance to be true.
A single counterexample, here $V$, settles the question.
The first group that comes to mind for a given order is often the cyclic group, so a test only on that group would have missed the failure.

If we replace $4$ by a prime number $p$, the claim becomes true: [[each group of prime order is cyclic|05MM4EK4SA]], by Lagrange's theorem.
If we replace $4$ by $6$, the claim fails again, and the counterexample is the [[symmetric group|0515A6D2Y1]] $S_3$.
So the order $4$ is the smallest order at which the claim fails.

## Explanations

### L1 human

Somebody claims that each group with four elements works like counting around a clock with four hours.
On the four-hour clock, stepping by $1$ hour visits all four positions before it returns to the start.
The Klein four-group is a different group with four elements.
In it, each step other than "stay" returns to the start after two moves.
So no single step visits all four elements, and the claim is false.

### L2 human

We check the multiplication rule $ab = c$ of $V$ on a model.

1. Take the four pairs $(0, 0)$, $(1, 0)$, $(0, 1)$, $(1, 1)$, with addition modulo $2$ in each coordinate.
2. Put $e = (0, 0)$, $a = (1, 0)$, $b = (0, 1)$, $c = (1, 1)$.
3. Then $a + b = (1, 1) = c$, and $a + a = (2, 0) = (0, 0) = e$, because $2 \equiv 0 \pmod 2$.
4. Each element added to itself gives $(0, 0)$, so each element other than $e$ has order $2$.

The typical use of such a test is to probe a claim before an attempt to prove it.
A trap is to test the claim only on $\mathbb{Z}/4\mathbb{Z}$, which is the most familiar group of order $4$.
That group has extra structure, a generator, and that structure is exactly what the claim asserts.

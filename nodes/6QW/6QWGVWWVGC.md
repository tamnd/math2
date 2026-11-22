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

The claim under test is "every group with $4$ elements is [[cyclic|0KVGH0J5B3]]".
A group with $4$ elements is cyclic exactly when it has an element of [[order|0WE2NHZJ7B]] $4$, because the powers of such an element are $4$ different elements, so they fill the group.
We test the claim on two groups with $4$ elements, first the familiar one and then a less familiar one.

The first test object is $\mathbb{Z}/4\mathbb{Z} = \{0, 1, 2, 3\}$, the [[integers modulo 4|03VFZ2WETT]] with addition.

1. The element $0$ is the identity, so it has order $1$.
2. The multiples of $1$ are $1, 2, 3, 0$, and the first return to $0$ is at the fourth step, so $1$ has order $4$.
3. The multiples of $2$ are $2, 0$, so $2$ has order $2$.
4. The multiples of $3$ are $3, 2, 1, 0$, so $3$ has order $4$.
5. The element $1$ has order $4$, so $\mathbb{Z}/4\mathbb{Z}$ is cyclic, and this group agrees with the claim.

The second test object is the [[Klein four-group|0PMRQJVTME]] $V = \{e, a, b, c\}$.
Here $e$ is the identity, $a^2 = b^2 = c^2 = e$, and the product of two different elements of $\{a, b, c\}$ is the third one.

6. The element $e$ has order $1$.
7. Each of $a$, $b$ and $c$ is not $e$, and its square is $e$, so each has order $2$.
8. No element of $V$ has order $4$, so $V$ is not cyclic.
9. The group $V$ has $4$ elements and is not cyclic, so it is a [[counterexample|0ED72CTBNP]], and the claim is false.

## Remarks

The two tests play different roles.
The confirming test on $\mathbb{Z}/4\mathbb{Z}$ only shows that the claim had a chance.
The single failing test on $V$ settles the question for good.
The cyclic group is the first group of each order that comes to mind, so a test on that group alone would have missed the failure.

What happens when the number $4$ changes?
For a prime $p$ in place of $4$, the claim becomes true, because [[every group of prime order is cyclic|05MM4EK4SA]] by Lagrange's theorem.
For $6$ in place of $4$, it fails again, and the [[symmetric group|0515A6D2Y1]] $S_3$ is a counterexample.
For $1$, $2$ and $3$ every group is cyclic, so $4$ is the smallest order at which the claim fails.

## Explanations

### L1 human

Somebody claims that every group with four elements works like a clock with four hours.
On that clock, stepping forward one hour at a time visits all four positions before it returns to the start.
The Klein four-group is a different group with four elements.
In it, every step other than "stay" returns to the start after two moves.
So no single step visits all four elements, and the claim is false.

### L2 human

The rules of $V$ can look made up, so we build a model of $V$ where every rule can be checked.
Take the four pairs $(0, 0)$, $(1, 0)$, $(0, 1)$ and $(1, 1)$, and add them entry by entry modulo $2$.
Name them $e = (0, 0)$, $a = (1, 0)$, $b = (0, 1)$ and $c = (1, 1)$.
Then
$$a + b = (1, 1) = c, \qquad a + a = (2, 0) = (0, 0) = e,$$
because $2 \equiv 0 \pmod 2$.
Check: each pair added to itself has even entries, so it gives $(0, 0)$, and each element other than $e$ has order $2$.
This kind of test is how you probe a claim before you try to prove it.
Watch out: a test only on $\mathbb{Z}/4\mathbb{Z}$ uses a group whose extra structure, a generator, is exactly what the claim asserts.

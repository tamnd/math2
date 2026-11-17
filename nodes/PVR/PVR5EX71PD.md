---
tag: PVR5EX71PD
kind: example
name: Doubling on the integers is not an isomorphism
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0JYTG5K9Y4]
not_instance_of:
  - target: 08MG7H8JW5
    note: the image is the even integers, so the map is not onto
illustrates: [0N2P0XRTDF]
uses: [0C4JS9RF5M, 08MG7H8JW5, 09NWETVTNY, 01RVCMSN5N, 0N2P0XRTDF]
sources:
  - url: https://en.wikipedia.org/wiki/Group_isomorphism
    locator: Definition and notation
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Types
---

## Example

Let $G = (\mathbb{Z}, +)$ be the [[integers|0C4JS9RF5M]] under addition.
Define $d \colon G \to G$ by $d(u) = 2u$.

1. The map is a homomorphism: $d(u + v) = 2u + 2v = d(u) + d(v)$.
2. If $2u = 0$, then $u = 0$. So the kernel is $\{0\}$.
3. By [[injectivity and the kernel|0N2P0XRTDF]], $d$ is [[injective|09NWETVTNY]].
4. The image of $d$ is $2\mathbb{Z}$, the set of even integers.
5. The integer $1$ is odd, so it is not in the image. So $d$ is not [[surjective|01RVCMSN5N]].
6. So $d$ is not an [[isomorphism|08MG7H8JW5]] from $\mathbb{Z}$ to $\mathbb{Z}$.

## Remarks

The example shows that an injective homomorphism from a group to itself need not be surjective.
For finite groups this cannot happen, because an injective map from a finite set to itself is a bijection.
The map $d$ is an isomorphism from $\mathbb{Z}$ onto its image $2\mathbb{Z}$, so $\mathbb{Z}$ is isomorphic to a proper subgroup of itself.
For an integer $c$, the map $u \mapsto cu$ is an isomorphism of $\mathbb{Z}$ when $c = \pm 1$, is trivial when $c = 0$, and is injective but not surjective when $|c| \ge 2$.
On $(\mathbb{Q}, +)$, doubling is an isomorphism, with inverse $x \mapsto x/2$.
On $\mathbb{Z}/n\mathbb{Z}$, doubling is an isomorphism exactly when $n$ is odd.

## Explanations

### L1 human

Doubling sends each whole number to an even number.
No two numbers have the same double, so no information is lost.
But the odd numbers are never reached.
So doubling is a faithful copy of the integers inside the even numbers, and not a renaming of all the integers.

### L2 human

We compare doubling on $\mathbb{Z}$ with doubling on $\mathbb{Z}/5\mathbb{Z}$.

1. On $\mathbb{Z}/5\mathbb{Z}$, the values of $x \mapsto 2x$ are $0, 2, 4, 1, 3$ for $x = 0, 1, 2, 3, 4$.
2. All five classes appear, so doubling on $\mathbb{Z}/5\mathbb{Z}$ is a bijection and an isomorphism.
3. On $\mathbb{Z}$, the value $1$ never appears, because $2u = 1$ has no integer solution.

The typical use is a warning about infinite groups.
A count of elements cannot replace the check of surjectivity for them.
The trap is to stop after step 3 of the example: a trivial kernel gives injectivity, but it says nothing about surjectivity.

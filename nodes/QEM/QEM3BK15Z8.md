---
tag: QEM3BK15Z8
kind: example
name: A subgroup of order two in S3 is not a kernel
msc: ["20B30"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0X1JXT47GA]
not_instance_of:
  - target: 0W88CEGQP1
    note: kernels are normal, and this subgroup is not normal in S3
illustrates: [0C9ZKYSPYR]
uses: [0515A6D2Y1, 0X1JXT47GA, 0W88CEGQP1, 0C9ZKYSPYR]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Kernel_(algebra)
    locator: Group homomorphisms
---

## Example

In the [[symmetric group|0515A6D2Y1]] $S_3$, let $H = \{e, (1\,2)\}$.
Compose permutations from right to left: $\sigma\tau$ means first $\tau$, then $\sigma$.
We claim that $H$ is not the [[kernel|0W88CEGQP1]] of any homomorphism with domain $S_3$.

1. $H$ is a [[subgroup|0X1JXT47GA]], because $(1\,2)(1\,2) = e$.
2. Conjugate $(1\,2)$ by $g = (1\,3)$, with $g^{-1} = (1\,3)$. A check of each point gives $(1\,3)(1\,2)(1\,3) = (2\,3)$.
3. The element $(2\,3)$ is not in $H$. So $H$ is not normal in $S_3$ ([[a subgroup of order two in S3 is not normal|XD0WBC1MWB]]).
4. Suppose that $H = \ker \varphi$ for a homomorphism $\varphi \colon S_3 \to K$. Then $\varphi((2\,3)) = \varphi(g)\varphi((1\,2))\varphi(g)^{-1} = \varphi(g)\varphi(g)^{-1} = e_K$.
5. So $(2\,3) \in \ker \varphi = H$, and this contradicts step 3.

So $H$ is not a kernel, in agreement with [[kernels are normal|0C9ZKYSPYR]].

## Remarks

The example shows that "subgroup" and "kernel" are different conditions.
The subgroup $H$ is still the image of a homomorphism: the inclusion $H \to S_3$ has image $H$.
So images need not be normal, but kernels must be normal.
The subgroup $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$ of $S_3$ is a kernel: it is the kernel of the sign ([[the alternating group as a kernel|TJ6EBSS3S7]]).
In an abelian group each subgroup $N$ is normal, so each subgroup is the kernel of the quotient map onto the quotient by $N$.

## Explanations

### L1 human

A kernel is the set of elements that a homomorphism sends to the identity.
If a homomorphism ignores the swap of $1$ and $2$, then it also ignores each relabelled version of that swap.
Relabelling $1$ and $3$ turns the swap of $1$ and $2$ into the swap of $3$ and $2$.
So a kernel that contains $(1\,2)$ also contains $(2\,3)$, and the set $\{e, (1\,2)\}$ is too small to be a kernel.

### L2 human

We find the smallest kernel that contains $(1\,2)$.

1. Each kernel is normal, so it contains all conjugates of $(1\,2)$.
2. The conjugates of $(1\,2)$ in $S_3$ are $(1\,2)$, $(1\,3)$ and $(2\,3)$.
3. A subgroup that contains two different transpositions contains their product, a $3$-cycle. Its order is divisible by $2$ and $3$, so it is $S_3$ by [[Lagrange's theorem|3C53TD]].
4. So the only kernel that contains $(1\,2)$ is $S_3$, the kernel of the trivial homomorphism.

The typical use is a quick test: a subgroup that is not closed under conjugation is not a kernel.
The trap is the image: the same subgroup is an image, so the test does not apply to images.

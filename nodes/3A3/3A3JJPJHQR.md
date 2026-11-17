---
tag: 3A3JJPJHQR
kind: example
name: A translation of the integers is not a homomorphism
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
not_instance_of:
  - target: 0JYTG5K9Y4
    note: it sends the identity 0 to 1
uses: [0C4JS9RF5M, 0JYTG5K9Y4, 08FKQD7NJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Properties
---

## Example

Let $G = (\mathbb{Z}, +)$ be the [[integers|0C4JS9RF5M]] under addition.
Define $t \colon G \to G$ by $t(u) = u + 1$.

1. A [[homomorphism|0JYTG5K9Y4]] sends the identity to the identity ([[the preservation lemma|08FKQD7NJ3]]). But $t(0) = 1$, and the identity of $G$ is $0$.
2. A direct check gives the same answer: $t(0 + 0) = 1$, but $t(0) + t(0) = 2$.
3. In fact the condition fails for all $a, b$. We have $t(a + b) = a + b + 1$ and $t(a) + t(b) = a + b + 2$.
4. The map $t$ is a bijection, with inverse $u \mapsto u - 1$.

So $t$ is a bijection of $G$ that is not a homomorphism.

## Remarks

The example shows that a bijection between groups need not be an isomorphism.
For an integer $c$, the translation $u \mapsto u + c$ is a homomorphism only when $c = 0$, because it must send $0$ to $0$.
The multiplication $u \mapsto cu$ is a homomorphism for each integer $c$, because $c(a + b) = ca + cb$.
A map $u \mapsto cu + d$ is a homomorphism exactly when $d = 0$.
The translations are still useful in group theory: they are the permutations of $\mathbb{Z}$ by which $\mathbb{Z}$ acts on itself.

## Explanations

### L1 human

Moving every number one step to the right looks like a harmless map.
But a homomorphism of the integers under addition must send $0$ to $0$.
This map sends $0$ to $1$, so it breaks the rule.
A shift of the whole number line is not a map that respects addition.

### L2 human

We test $t(u) = u + 1$ on the pair $a = 3$ and $b = 4$.

1. $t(3 + 4) = t(7) = 8$.
2. $t(3) + t(4) = 4 + 5 = 9$.
3. The two results differ by $1$, and this happens for each pair.

The typical use of this example is as a quick test.
Before a long check of the product rule, look at the image of the identity.
The trap is to think that a bijection of $\mathbb{Z}$ must be an isomorphism because both sides are the same group.

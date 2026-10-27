---
tag: 0N2P0XRTDF
kind: statement
role: proposition
name: A homomorphism is injective iff its kernel is trivial
msc: [20A05]
about: [0JYTG5K9Y4, 0W88CEGQP1]
uses: [0Z424HK8CQ, 08FKQD7NJ3]
formal:
  - system: lean4
    library: mathlib
    decl: MonoidHom.ker_eq_bot_iff
    match: stronger
    adapter: Math2.Match.injective_iff_ker
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(algebra)
    locator: Group homomorphisms
---

## Statement

Let $G$ and $H$ be [[groups|G5S1M9]], let $e_G$ be the identity element of $G$, and let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]].
Then $\varphi$ is injective if and only if $\ker \varphi = \{e_G\}$.

## Remarks

If $\varphi(a) = \varphi(b)$, then $\varphi(a^{-1}b) = e_H$, so $a^{-1}b \in \ker \varphi$.
More generally, $\varphi(a) = \varphi(b)$ exactly when $a$ and $b$ lie in the same coset of $\ker \varphi$.

## Explanations

### L1 human

To check that a homomorphism is injective, you only need to check one fibre: the elements that go to the identity.
If only the identity goes to the identity, then no two elements can go to the same place.
This is much easier than comparing all pairs of elements.

### L2 agent

For a map of sets, injectivity needs a check on each pair of points. For a homomorphism, it is enough to look at one fibre, the kernel.

The proof uses the group structure to move any pair to the identity:

1. If $\varphi$ is injective, then only $e$ maps to $e$, because $\varphi(e) = e$.
2. Conversely, suppose that $\ker \varphi = \{e\}$ and $\varphi(a) = \varphi(b)$.
3. Then $\varphi(a^{-1}b) = \varphi(a)^{-1}\varphi(b) = e$.
4. Thus $a^{-1}b = e$, and $a = b$.

A worked example with $\varphi : \mathbb{Z} \to \mathbb{Z}$, $\varphi(n) = 3n$:

1. The map is a homomorphism, because $3(m + n) = 3m + 3n$.
2. If $3n = 0$, then $n = 0$. Thus the kernel is $\{0\}$.
3. By the result, $\varphi$ is injective. There is no need to compare pairs.

A non-example is reduction modulo $3$, $\mathbb{Z} \to \mathbb{Z}/3\mathbb{Z}$. Its kernel is $3\mathbb{Z}$, which is not trivial. Thus the map is not injective: for example, $0$ and $3$ have the same image.

More generally, $\varphi(a) = \varphi(b)$ exactly when $a^{-1}b \in \ker\varphi$, that is, when $a$ and $b$ are in the same coset of the kernel. Thus each fibre of $\varphi$ is a coset of the kernel, or it is empty.

A common error is to use the test for a map that is not a homomorphism. The map $x \mapsto x^2$ on $\mathbb{R}$ sends only $0$ to $0$, but it is not injective.

---
tag: C0TE34BHYQ
kind: example
name: The rational and real orders are partially isomorphic but not isomorphic
aliases: [rational-and-real-orders-are-partially-isomorphic]
msc: ["03C07", "03C75", "06A05"]
topics: [N64R1MGDBN]
audience: grad
instance_of: [EWB8KXZMCV]
not_instance_of:
  - target: 6F2DB4HTJR
    note: the extension properties hold, but the real line cannot be listed as b_0, b_1, ..., so the zig-zag construction cannot reach every real
uses: [EWB8KXZMCV, 6F2DB4HTJR, K4D3S1MBZH, 01TQB88H4C, PZMGQMDN25, TZZVG88865]
sources:
  - url: https://en.wikipedia.org/wiki/Back-and-forth_method
    locator: Application to densely ordered sets
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Example

Let $\mathcal{A} = (\Q, <)$ and $\mathcal{B} = (\R, <)$.
Let $I$ be the set of all order-preserving maps $p$ from a finite subset of $\Q$ into $\R$.
We check that $I$ is a [[back-and-forth system|EWB8KXZMCV]] and that $\mathcal{A}$ and $\mathcal{B}$ are not [[isomorphic|PZMGQMDN25]].

1. $I$ is not empty: it contains the empty map.
2. Each $p \in I$ is a partial isomorphism. It is injective because it is strictly increasing, and $x < y$ if and only if $p(x) < p(y)$, since both orders are linear.
3. Forth: let $p$ map $a_1 < \dots < a_k$ to $b_1 < \dots < b_k$, and let $a \in \Q$. The real line is [[dense|K4D3S1MBZH]] and has no endpoints, so there is a real $b$ in the same gap of $b_1, \dots, b_k$ as $a$ is in $a_1, \dots, a_k$. If $a = a_i$, take $b = b_i$. Then $p \cup \set{(a, b)} \in I$.
4. Back: for a real $b$, the same argument in $\Q$, which is also dense without endpoints, gives a rational $a$ in the matching gap.
5. So $\mathcal{A} \cong_p \mathcal{B}$.
6. An isomorphism is a bijection, $\Q$ is [[countable|01TQB88H4C]] and $\R$ is not. So $\mathcal{A} \not\cong \mathcal{B}$.

## Remarks

The example shows that a back-and-forth system does not give an isomorphism by itself.
The [[back-and-forth method|6F2DB4HTJR]] uses the system along two lists $a_0, a_1, \dots$ and $b_0, b_1, \dots$, and after countably many steps the range of the union is countable.
So the zig-zag construction reaches only countably many reals, and $\R$ has uncountably many.
By [[Karp's theorem|KAWWZ2DF0G]], $(\Q, <)$ and $(\R, <)$ satisfy the same sentences of $L_{\infty\omega}$, the logic with conjunctions of any size and finite blocks of quantifiers.
So no sentence of $L_{\infty\omega}$ expresses the completeness of the real order.
In particular they are [[elementarily equivalent|TZZVG88865]].

If $\R$ is replaced by a countable dense order without endpoints, such as the dyadic rationals, the same system gives an isomorphism by the method.
If $\R$ is replaced by $(\Z, <)$, the forth property fails at step 3, since $\Z$ is not dense.

## Explanations

### L1 human

The fractions and the real numbers look the same in every finite piece: between two points there is always a third, and there is no first or last point.
So any finite matching of fractions with real numbers that keeps the order can be extended by one more point, in either direction.
Still, the two lines cannot be matched completely, because there are more real numbers than fractions.
Local sameness of this kind is called partial isomorphism.

### L2 human

We extend $p = \set{(0, 0), (1, \sqrt{2})}$ by one forth step and one back step.

1. Forth with $a = \frac12$: it lies between $0$ and $1$, so we need $b$ with $0 < b < \sqrt{2}$. Take $b = 1$.
2. Now $p = \set{(0, 0), (\frac12, 1), (1, \sqrt{2})}$.
3. Back with $b = \pi$: it lies above $\sqrt{2}$, the largest image, so we need a rational $a > 1$. Take $a = 2$.
4. Now $p = \set{(0, 0), (\frac12, 1), (1, \sqrt{2}), (2, \pi)}$, which is order-preserving.

The typical use of this example is to separate partial isomorphism from isomorphism.
A trap is to think that potential isomorphism is a weak notion; it implies agreement on all infinitary sentences of $L_{\infty\omega}$.

---
tag: AY1QQFQZ41
kind: example
name: The rational order is an elementary substructure of the real order
msc: ["03C07"]
topics: [2RE7GWWXM5]
audience: ug2
instance_of: [CGH8C8EA9N, 8WZF9SBP39]
illustrates: [60SA99BER7]
uses: [60SA99BER7, 8WZF9SBP39, NDTJ2E895C, XY6CJMDY5M]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Tarski–Vaught test
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Example

Let $L = \set{<}$, and consider the structures $(\Q, <)$ and $(\R, <)$ with the usual orders.
We check that $(\Q, <) \preceq (\R, <)$, so that the inclusion map is an [[elementary embedding|CGH8C8EA9N]].

1. $(\Q, <)$ is a substructure of $(\R, <)$, because the order of $\Q$ is the restriction of the order of $\R$.
2. By the [[Tarski-Vaught test|60SA99BER7]], it is enough to show the following. If $\varphi(x_1, \dots, x_n, y)$ is a formula, $a_1, \dots, a_n \in \Q$, $b \in \R$ and $\R \models \varphi(\bar a, b)$, then $\R \models \varphi(\bar a, q)$ for some $q \in \Q$.
3. If $b \in \Q$, take $q = b$. Otherwise $b$ differs from each $a_i$.
4. Let $u$ be the largest $a_i$ below $b$, or $u = b - 1$ if there is none. Let $v$ be the smallest $a_i$ above $b$, or $v = b + 1$ if there is none. Then $u < b < v$, and no $a_i$ lies strictly between $u$ and $v$.
5. The rationals are dense in $\R$, so there is $q \in \Q$ with $u < q < v$.
6. Define $\sigma$ on $(-\infty, b]$. If some $a_i$ lies below $b$, let $\sigma$ be the identity on $(-\infty, u]$ and the increasing affine map of $[u, b]$ onto $[u, q]$. If not, let $\sigma(x) = x + (q - b)$.
7. Define $\sigma$ on $[b, \infty)$ in the same way, with $v$ in place of $u$. Both definitions give $\sigma(b) = q$.
8. Each piece is increasing and the pieces fit together, so $\sigma$ is an order-preserving bijection, that is, an [[automorphism|XY6CJMDY5M]] of $(\R, <)$. Each $a_i$ satisfies $a_i \le u$ or $a_i \ge v$, so $\sigma$ fixes it.
9. Automorphisms [[preserve the truth of formulas|NDTJ2E895C]], so $\R \models \varphi(\sigma(\bar a), \sigma(b))$, that is, $\R \models \varphi(\bar a, q)$.
10. So the condition of step 2 holds, and $(\Q, <) \preceq (\R, <)$.

## Remarks

The example shows the standard way to use the Tarski-Vaught test: an automorphism of the large structure that fixes the parameters moves a witness into the small structure.
The proof used only that $\Q$ is dense in $\R$, so every dense subset $D \subseteq \R$ gives $(D, <) \preceq (\R, <)$, for example the dyadic rationals $\Z[1/2]$.
The integers are not dense in $\R$, and indeed $(\Z, <)$ is not even [[elementarily equivalent|P3B1V182N4]] to $(\R, <)$.
If we add the field operations, the inclusion $\Q \subseteq \R$ is no longer elementary: the formula $\exists y \, (y \cdot y = 1 + 1)$ is true in $\R$ and false in $\Q$.
So elementarity depends on the signature, and richer signatures give fewer automorphisms.

## Explanations

### L1 human

Take the fractions and the real numbers, and look only at the order "less than".
Any question about the order that mentions some fractions gets the same answer in both sets.
For example, "is there a number between $0$ and $1$ that is bigger than $\tfrac12$" is answered yes in both, by $\tfrac34$.
The reason is that the real line can be stretched, without changing the order, so that any real number lands on a fraction while the named fractions stay where they are.

### L2 human

We run the proof for the formula $\varphi(x, y) = x < y$ with the parameter $a = 0$ and the witness $b = \sqrt{2}$.

1. $\R \models 0 < \sqrt{2}$, and $\sqrt{2} \notin \Q$.
2. The largest parameter below $b$ is $u = 0$, and no parameter lies above $b$, so $v = \sqrt{2} + 1$.
3. Choose $q = 1$, which is rational and satisfies $0 < 1 < \sqrt{2} + 1$.
4. The map $\sigma$ fixes all $x \le 0$, maps $[0, \sqrt{2}]$ onto $[0, 1]$ by $x \mapsto x/\sqrt{2}$, and shifts $x \ge \sqrt{2}$ by $1 - \sqrt{2}$.
5. Then $\sigma(0) = 0$ and $\sigma(\sqrt{2}) = 1$, and $\R \models 0 < 1$, as the proof predicts.

The typical use of this pattern is to show that a dense or homogeneous part of a structure is an elementary substructure.
A trap is to apply the same argument to the field $\R$: the field has no automorphism other than the identity, so no witness can be moved.

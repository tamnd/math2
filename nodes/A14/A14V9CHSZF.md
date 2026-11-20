---
tag: A14V9CHSZF
kind: example
name: Every countable linear order embeds into the rational order
aliases: [countable-linear-orders-embed-into-the-rationals]
msc: ["06A05", "03C15"]
topics: [N64R1MGDBN]
audience: ug2
instance_of: [6F2DB4HTJR]
uses: [6F2DB4HTJR, 0FRXBVVR03, K4D3S1MBZH, 01TQB88H4C, SCRB74SWQN]
sources:
  - url: https://en.wikipedia.org/wiki/Back-and-forth_method
    locator: Application to densely ordered sets
  - book: isbn:9780387987606
---

## Example

Let $(A, <)$ be a countable [[linear order|0FRXBVVR03]], finite or infinite, and list its elements as $a_0, a_1, a_2, \dots$.
We build an order-preserving injective map $f \colon A \to \Q$ by the forth half of the [[back-and-forth method|6F2DB4HTJR]].

1. Put $f(a_0) = 0$.
2. Suppose $f$ is defined on $a_0, \dots, a_{n-1}$ and preserves the order. Let $c_1 < \dots < c_{n}$ be these elements in the order of $A$, with images $f(c_1) < \dots < f(c_n)$.
3. The new element $a_n$ lies in one gap: below $c_1$, between some $c_i$ and $c_{i+1}$, or above $c_n$.
4. Choose $f(a_n)$ in the same gap of the images: below $f(c_1)$, strictly between $f(c_i)$ and $f(c_{i+1})$, or above $f(c_n)$. Such a rational exists, because $\Q$ is [[dense|K4D3S1MBZH]] and has no endpoints.
5. Then $f$ preserves the order on $a_0, \dots, a_n$, since $f(a_n)$ has the same position relative to the earlier images as $a_n$ has relative to the earlier elements.
6. Every element of $A$ appears in the list, so $f$ is defined on all of $A$. Any two elements appear together at some finite stage, so $f$ is strictly increasing on $A$.

So $f$ is an order [[embedding|SCRB74SWQN]] of $(A, <)$ into $(\Q, <)$.

## Remarks

The example shows when forth alone suffices: we want a map defined on all of $A$, and we do not need it to be onto.
The back steps are not needed, because no element of $\Q$ must be hit.
The image need not be all of $\Q$; for $A = \Z$ the image is a discrete subset.
The target can be any countable dense linear order without endpoints, since the proof uses only density and the lack of endpoints.

Countability of $A$ is needed: $(\R, <)$ does not embed into $(\Q, <)$, since an injective map from $\R$ to $\Q$ does not exist.
Density of the target is needed: $(\Q, <)$ does not embed into $(\Z, <)$, because the images of $0$ and $1$ would have infinitely many integers between them.
So $(\Q, <)$ is a universal countable linear order, and by [[Cantor's isomorphism theorem|ABN5PTXEHY]] it is the only countable dense one without endpoints.

## Explanations

### L1 human

Take any countable list of points in a row, such as $0, 1, 2, \dots$ followed by one extra point at the end.
We can place them all on the number line at fractions, keeping their order.
Each new point goes into the right gap between the fractions used so far.
There is always a free fraction in that gap, because between two fractions there is always another one.

### L2 human

Let $A = \set{0, 1, 2, \dots} \cup \set{\infty}$, with $\infty$ above every number, listed as $\infty, 0, 1, 2, \dots$.

1. Put $f(\infty) = 0$.
2. The element $0$ is below $\infty$, so $f(0)$ must be below $0$. Choose $f(0) = -1$.
3. The element $1$ lies between $0$ and $\infty$, so $f(1)$ lies between $-1$ and $0$. Choose $f(1) = -\frac12$.
4. In general $n$ lies between $n - 1$ and $\infty$, and we choose $f(n) = -2^{-n}$, between $-2^{-(n-1)}$ and $0$.

The typical use of the forth construction is to embed a countable structure into a rich one, such as a countable saturated or universal structure.
A trap is to put $f(n)$ greedily at $f(n - 1) + 1$: then $f(1) = 0 = f(\infty)$, and step 4 shows that the gap must be respected.

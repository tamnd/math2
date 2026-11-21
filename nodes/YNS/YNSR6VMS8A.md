---
tag: YNSR6VMS8A
kind: example
name: The integer order is homogeneous but not saturated
msc: ["03C50", "06A05"]
topics: [Z772KEC9BY]
audience: grad
instance_of: [4NJS7W57VK]
not_instance_of:
  - target: RMTZ5J64FX
    note: "the order of the integers omits the type of an element at infinite distance from 0"
  - target: F30ZVR4AD5
    note: "two copies of the integers, one after the other, do not embed elementarily into the integers"
  - target: EPNZKJQHWJ
    note: "the translation by 1 is an automorphism of the integer order that is not the identity"
uses: [4NJS7W57VK, RMTZ5J64FX, F30ZVR4AD5, EPNZKJQHWJ, XTNYY0WRQ5, DSQ17TNW1C, CGH8C8EA9N]
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
    locator: lead section
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Example

Let $\mathcal{Z} = (\Z, <)$.
For $k \ge 0$ let $\delta_k(x, y)$ be the formula "$x < y$ and exactly $k$ elements lie between $x$ and $y$".

1. Homogeneity: a [[partial elementary map|XTNYY0WRQ5]] $f$ preserves each $\delta_k$, so it preserves distances. On a finite nonempty domain it equals the translation $x \mapsto x + c$ with $c = f(a) - a$ for any $a$ in the domain.
2. The translation is an [[automorphism|DSQ17TNW1C]], so $\mathcal{Z}$ is strongly $\aleph_0$-homogeneous, and [[strongly homogeneous|4NJS7W57VK]] since it is countable.
3. Not saturated: the set $p(x) = \set{0 < x} \cup \set{\neg \delta_k(0, x) : k \ge 0}$ is finitely satisfiable in $\mathcal{Z}$, since a large integer satisfies any finite part of it.
4. Each integer $n > 0$ satisfies $\delta_{n-1}(0, n)$, so no integer realizes $p$. The parameter set $\set{0}$ is finite, so $\mathcal{Z}$ is not $\aleph_0$-[[saturated|RMTZ5J64FX]].
5. Not universal: let $\mathcal{W}$ be the order $\Z \times \set{0, 1}$, with all of $\Z \times \set{0}$ below $\Z \times \set{1}$. It is a discrete order without endpoints, so $\mathcal{W} \equiv \mathcal{Z}$, and it is countable.
6. An [[elementary embedding|CGH8C8EA9N]] $g : \mathcal{W} \to \mathcal{Z}$ would map $a = (0, 0)$ and $b = (0, 1)$ to integers with $g(b) - g(a) = k + 1$ for some $k \ge 0$. Then $\delta_k(g(a), g(b))$ holds, while $\delta_k(a, b)$ fails, since infinitely many elements lie between $a$ and $b$.
7. So $\mathcal{Z}$ is not [[universal|F30ZVR4AD5]].
8. Not rigid: the translation $x \mapsto x + 1$ is an automorphism that moves every element, so $\mathcal{Z}$ is not [[rigid|EPNZKJQHWJ]].

## Remarks

Step 5 uses that the theory of discrete linear orders without endpoints is complete.
The type $p$ in step 3 is computable, so $\mathcal{Z}$ is not recursively saturated either.

## Explanations

### L1 human

The integers with their order look the same from every point, so any finite pattern of integers can be shifted onto any other pattern with the same gaps.
That is homogeneity.
They are not saturated, because there is no integer infinitely far from $0$, although first-order logic cannot rule such an element out.

### L2 human

The test for homogeneity is to find an automorphism for each partial elementary map.

1. The map $\set{2 \mapsto 7, 5 \mapsto 10}$ preserves the distance $3$, so it is a restriction of $x \mapsto x + 5$.
2. The map $\set{2 \mapsto 7, 5 \mapsto 9}$ is order-preserving, but $\delta_2(2, 5)$ holds and $\delta_2(7, 9)$ fails, so it is not partial elementary.

The typical use is as a homogeneous structure that is far from saturated.
The trap is to think that homogeneity forces richness.

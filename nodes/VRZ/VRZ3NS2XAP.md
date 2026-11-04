---
tag: VRZ3NS2XAP
kind: proof
name: Proof of the fixed point congruence for p-group actions
msc: [20D15, 20B05]
proves: 098D2E7DEH
uses: [06DAH3VS6M, 0JM7PA288B, 051VYKA1EX, 084HH1NDCB, 08JF1K4DW1, 00F2JFA41J, 0ZC7FYE0NZ, 0S19CWFZM2]
sources:
  - url: https://en.wikipedia.org/wiki/P-group
    locator: Non-trivial center
---

## Proof

We split $X$ into orbits and reduce their sizes modulo $p$. Let $e$ be the identity of $G$.

1. First, $\abs{G}$ is a power of $p$. Let $q$ be a prime that divides $\abs{G}$. By [[Cauchy's theorem|0JM7PA288B]], some $g \in G$ has order $q$.
2. Since $G$ is a [[$p$-group|06DAH3VS6M]], the order of $g$ is $p^s$ for some $s \geq 0$. So $q = p^s$, and as $q$ is prime, $q = p$.
3. So $p$ is the only prime factor of $\abs{G}$. By the [[fundamental theorem of arithmetic|084HH1NDCB]], $\abs{G} = p^r$ for some $r \geq 0$.
4. Let $d$ be a positive divisor of $p^r$ and $q$ a prime dividing $d$. Then $q \mid p^r$, so $q \mid p$ by [[Euclid's lemma|051VYKA1EX]], and $q = p$. As in step 3, $d$ is a power of $p$.
5. By the [[orbit size formula|0S19CWFZM2]], the size of each [[orbit|00F2JFA41J]] divides $\abs{G} = p^r$. By step 4, each orbit has size $p^j$ for some $j \geq 0$.
6. An orbit $G \cdot x$ has size $1$ if and only if $G \cdot x = \set{x}$, since $x = e \cdot x$ lies in it. This means $g \cdot x = x$ for all $g$, that is, $x$ is a [[fixed point|08JF1K4DW1]].
7. So the orbits of size $1$ are the sets $\set{x}$ with $x \in X^G$. Every other orbit has size $p^j$ with $j \geq 1$, which is divisible by $p$.
8. The [[orbits partition|0ZC7FYE0NZ]] $X$, and $X$ is finite. So $\abs{X}$ is the sum of the orbit sizes, which is $\abs{X^G}$ plus a sum of multiples of $p$.
9. Hence $\abs{X} \equiv \abs{X^G} \pmod p$.

## Idea

The orbits cut $X$ into pieces whose sizes divide the order of the group, which is a power of $p$. Every piece of size more than one is then a multiple of $p$ and disappears modulo $p$. Only the one-point orbits, the fixed points, are left.

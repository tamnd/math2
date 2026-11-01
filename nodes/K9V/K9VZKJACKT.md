---
tag: K9VZKJACKT
kind: definition
name: Combinatorial species
msc: [05A15, 18B99]
defines: 7PEE48WBQF
uses: [0BBTH3YSZA, 0JHXPVFKT0]
sources:
  - url: https://en.wikipedia.org/wiki/Combinatorial_species
---

## Definition

Let $\mathbb{B}$ be the category whose objects are the [[finite sets|0BBTH3YSZA]] and whose morphisms are the bijections.
A *combinatorial species* is a functor $F \colon \mathbb{B} \to \mathbb{B}$.
Thus $F$ assigns:

1. to each finite set $U$ a finite set $F[U]$, whose elements are the *$F$-structures* on $U$;
2. to each bijection $\sigma \colon U \to V$ a bijection $F[\sigma] \colon F[U] \to F[V]$, the *transport* along $\sigma$;
3. in such a way that $F[\id_U] = \id_{F[U]}$ and $F[\tau \circ \sigma] = F[\tau] \circ F[\sigma]$ for bijections $\sigma \colon U \to V$ and $\tau \colon V \to W$.

## Remarks

The *exponential generating function* of $F$ is $F(x) = \sum_{n \ge 0} \abs{F[\set{1, \ldots, n}]}\, \frac{x^n}{n!}$.

Example: the species $L$ of linear orders assigns to $U$ the set of total orders on $U$.
A bijection $\sigma$ transports an order $u_1 < \cdots < u_n$ to $\sigma(u_1) < \cdots < \sigma(u_n)$, and the functor rules hold.
Since $\abs{L[\set{1, \ldots, n}]} = n!$, its generating function is $\frac{1}{1 - x}$.
The species $E$ of sets, with $E[U] = \set{U}$, has generating function $e^x$.

Non-example: let $F[U] = \set{U}$ if $U \subseteq \N$ and $F[U] = \emptyset$ otherwise.
For a bijection $\sigma$ from $\set{1}$ to $\set{a}$ with $a \notin \N$, clause 2 needs a bijection from a one-element set to the empty set, which does not exist.
So $F$ is not a species.

Sum, product, composition and derivative of species correspond to the same operations on exponential generating functions.
Some authors let $F$ take values in the category of finite sets and all functions; this gives the same notion, since a functor sends bijections to bijections.

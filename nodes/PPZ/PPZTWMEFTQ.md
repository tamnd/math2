---
tag: PPZTWMEFTQ
kind: example
name: A monster model of dense linear orders
msc: ["03C50", "06A05", "03E55"]
topics: [Z772KEC9BY]
audience: grad
instance_of: [EYTTQZ0E1S]
uses: [EYTTQZ0E1S, GSQ833HAZT, DZ65A6X12W, 7WH24MZZQ8, 2W4S2H4VYA, 7FDDXV3JK7, NW4DREQ5DQ]
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
    locator: Motivation
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Example

Let $T$ be the theory of [[dense linear orders|2W4S2H4VYA]] without endpoints, and let $\bar{\kappa}$ be an [[inaccessible cardinal|NW4DREQ5DQ]].

1. Since $\bar{\kappa}$ is regular and $2^\mu < \bar{\kappa}$ for $\mu < \bar{\kappa}$, every function from $\mu < \bar{\kappa}$ to $\bar{\kappa}$ is bounded, and $\bar{\kappa}^{<\bar{\kappa}} = \bar{\kappa}$.
2. By [[existence of saturated models|GSQ833HAZT]], part 2, $T$ has a saturated model $\mathbb{D}$ of size $\bar{\kappa}$.
3. By [[uniqueness of saturated models|DZ65A6X12W]], part 1, $\mathbb{D}$ is strongly $\bar{\kappa}$-homogeneous, so it is a [[monster model|EYTTQZ0E1S]].
4. By [[quantifier elimination|7FDDXV3JK7]], a type over a small set $A$ is a point of $A$ or a cut $(X, Y)$ of $A$, with $X < Y$ and $X \cup Y = A$. Saturation says that every cut of every small set is filled.
5. If $b$ and $c$ fill the same cut of $A$, then $A \cup \set{b} \to A \cup \set{c}$, fixing $A$ and sending $b$ to $c$, is order-preserving and so partial elementary. Step 3 extends it to an automorphism, so the cut is one [[orbit|7WH24MZZQ8]] over $A$.

## Remarks

The existence of an inaccessible cardinal is not provable in ZFC.
Without it, a $\kappa$-saturated and strongly $\kappa$-homogeneous dense order for a fixed $\kappa$ serves as the monster model.
Unlike algebraically closed fields, dense linear orders have no saturated model of singular size, by part 5 of the existence theorem, so the size of a saturated monster model must be chosen with care.

## Explanations

### L1 human

The monster dense order is a very long dense line in which every gap that a smaller set of points could describe is filled.
Two points in the same gap of a small set can be exchanged by a symmetry of the whole line that fixes the small set.

### L2 human

We fill the cut of $A = \set{a_n : n \in \N}$ with $a_0 < a_1 < \cdots$ given by $X = A$ and $Y = \emptyset$.

1. The type $\set{a_n < x : n \in \N}$ is finitely satisfiable, since $\mathbb{D}$ has no greatest element.
2. The set $A$ is countable, so it is small, and some $b \in \mathbb{D}$ realizes the type.

The typical use is to find points above or between small sets of points.
The trap is to fill a cut of a set that is not small, such as the cut of $\mathbb{D}$ itself at its top.

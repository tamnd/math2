---
tag: 20QJANNKP7
kind: example
name: Standard examples of categoricity
aliases: [four-categoricity-patterns]
msc: ["03C35"]
topics: [6XEXRME4C1]
audience: grad
instance_of: [1JJCGNX240]
uses: [1JJCGNX240, KFWXHKBHYT, 000AYPA9AJ, 2W4S2H4VYA, RMXR0FEF54, 0SGTMBEWRF, MT8TDVPBXB, 97YPZ0YHEB, 91WRBX69MB, V7N84P60SJ, CAEHMSX9RT]
sources:
  - url: https://en.wikipedia.org/wiki/Categorical_theory
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Omega-categorical_theory
    locator: Examples
  - book: isbn:9780387987606
---

## Example

A complete theory in a countable signature with infinite models falls into one of four patterns.
It is categorical in every infinite cardinal, only in $\aleph_0$, only in the uncountable cardinals, or in none.
The table gives a standard theory for each pattern, and the checks below justify each entry.

| theory | $\aleph_0$-categorical | uncountably categorical |
| --- | --- | --- |
| infinite sets | yes | yes |
| infinite vector spaces over a finite field | yes | yes |
| equivalence relation, infinitely many classes, all of size 2 | yes | yes |
| dense linear orders without endpoints | yes | no |
| random graph | yes | no |
| equivalence relation, exactly two classes, both infinite | yes | no |
| equivalence relation, infinitely many classes, all infinite | yes | no |
| algebraically closed fields of characteristic $p$ | no | yes |
| nonzero vector spaces over $\Q$ | no | yes |
| successor function on $\Z$ | no | yes |
| order of $\Z$ | no | no |

### Rows 1 to 7

Rows 1 to 7 are the $\aleph_0$-categorical rows.

1. [[Infinite sets|KFWXHKBHYT]]. Two sets of the same infinite size are in bijection, and a bijection is an isomorphism in the empty signature.
2. Infinite [[vector spaces|000AYPA9AJ]] over a finite field $F$. A space of infinite dimension $d$ has size $d$, so two spaces of the same infinite size have the same dimension and are isomorphic.
3. An [[equivalence relation|0SGTMBEWRF]] with infinitely many classes, each of size $2$. A model of size $\kappa$ has exactly $\kappa$ classes, so two such models are isomorphic class by class.
4. [[Dense linear orders without endpoints|2W4S2H4VYA]]. Cantor's theorem gives $\aleph_0$-categoricity, and that page builds two non-isomorphic models of each uncountable size.
5. The [[random graph|RMXR0FEF54]]. Countable models satisfy the extension axioms, so back-and-forth gives an isomorphism. Over a countable model $M$, each subset $X \subseteq M$ gives a type "adjacent to exactly the points of $X$", so there are $2^{\aleph_0}$ types over a countable set. A theory categorical in an uncountable cardinal has only countably many such types, by the proof of [[Morley's theorem|V7N84P60SJ]]. So the random graph is not uncountably categorical.
6. Two infinite classes. A countable model has two classes of size $\aleph_0$. In size $\kappa > \aleph_0$, the class sizes $(\kappa, \aleph_0)$ and $(\kappa, \kappa)$ give two non-isomorphic models.
7. Infinitely many infinite classes. A countable model has $\aleph_0$ classes of size $\aleph_0$. In size $\kappa > \aleph_0$, compare $\kappa$ classes of size $\aleph_0$ with one class of size $\kappa$ and $\aleph_0$ classes of size $\aleph_0$.

### Rows 8 to 11

Rows 8 to 11 are not $\aleph_0$-categorical.

8. [[Algebraically closed fields|MT8TDVPBXB]] of characteristic $p$. A model is fixed by its transcendence degree, by [[Steinitz's theorem|CAEHMSX9RT]]. In size $\kappa > \aleph_0$ the degree is $\kappa$, while the countable models have degrees $0, 1, 2, \dots, \aleph_0$.
9. Vector spaces over $\Q$. This is [[this example|97YPZ0YHEB]], with dimension in place of transcendence degree.
10. The successor function $s$ on $\Z$. A model is a disjoint union of copies of $(\Z, s)$, since $s$ is a bijection without cycles. A model of size $\kappa > \aleph_0$ has $\kappa$ copies, while countable models can have $1, 2, \dots$ or $\aleph_0$ copies.
11. The order of $\Z$. This is [[this example|91WRBX69MB]]: there are two non-isomorphic models in every infinite size.

## Remarks

The table shows that all four patterns occur.
By [[Morley's theorem|V7N84P60SJ]], no countable theory is categorical in some uncountable cardinals and not in others, so the four patterns are the only ones.
In the uncountably categorical rows, a model is fixed by one cardinal, a dimension: transcendence degree, linear dimension, or the number of copies of $\Z$.
In the rows that are $\aleph_0$-categorical only, the countable model has a large automorphism group, but there is no dimension that controls the larger models.

## Explanations

### L1 human

Some rules describe one world of each size, and some describe many.
Rules for a plain set describe one world of each size, since only the number of elements matters.
Rules for fields like the complex numbers describe one world of each uncountable size, and many countable ones.
Rules for dense orders like the fractions describe one countable world, and many larger ones.
Rules for the integers in their order describe many worlds of every size.

### L2 human

We check row 6 for $\kappa = \aleph_1$.

1. Let $M$ have one class of size $\aleph_1$ and one of size $\aleph_0$. Let $N$ have two classes of size $\aleph_1$. Both have size $\aleph_1$.
2. An isomorphism maps classes onto classes, and it keeps their sizes.
3. $M$ has a countable class and $N$ has none, so $M \not\cong N$.
4. In the countable case both classes have size $\aleph_0$, so any two countable models are isomorphic.

The typical use is to test a new conjecture about categoricity against each row.
A trap is to think that $\aleph_0$-categoricity says something about uncountable models; rows 4 to 7 show that it does not.

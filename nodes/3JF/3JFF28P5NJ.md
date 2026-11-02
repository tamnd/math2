---
tag: 3JFF28P5NJ
kind: definition
name: Berkovich space
msc: [14G22, 32P05, 12J25]
defines: T284RZ6AGE
uses: [1H5F1BP6XS, 9KYWN94QDN, FP5GVCN8GV, B1TEQ98JZD]
sources:
  - url: https://en.wikipedia.org/wiki/Berkovich_space
---

## Definition

Let $K$ be a field that is complete for a [[non-Archimedean absolute value|1H5F1BP6XS]] $\abs{\cdot}$.
Let $A$ be a commutative [[Banach algebra|9KYWN94QDN]] over $K$ with unit, with norm $\norm{\cdot}$.
A *bounded multiplicative seminorm* on $A$ is a map $x \colon A \to [0, \infty)$, written $f \mapsto \abs{f(x)}$, such that:

1. $\abs{1(x)} = 1$ and $\abs{(f + g)(x)} \le \abs{f(x)} + \abs{g(x)}$ for all $f, g \in A$;
2. $\abs{(fg)(x)} = \abs{f(x)} \, \abs{g(x)}$ for all $f, g \in A$;
3. $\abs{f(x)} \le \norm{f}$ for all $f \in A$.

The *Berkovich spectrum* $\mathcal{M}(A)$ is the set of bounded multiplicative [[seminorms|FP5GVCN8GV]] on $A$.
It carries the weakest topology for which the map $x \mapsto \abs{f(x)}$ is continuous for every $f \in A$.
A $K$-affinoid algebra is a quotient of a [[Tate algebra|B1TEQ98JZD]] or of one of its versions with other radii.
For such $A$, $\mathcal{M}(A)$ is a *$K$-affinoid space*.
A *Berkovich analytic space* over $K$ is a space glued from $K$-affinoid spaces along affinoid domains.

## Remarks

Berkovich proved that $\mathcal{M}(A)$ is a nonempty compact Hausdorff space when $A \ne 0$.

Example: let $A = K\langle T \rangle$ be the Tate algebra of power series $\sum_n a_n T^n$ with $a_n \to 0$, with the Gauss norm $\norm{\sum a_n T^n} = \max_n \abs{a_n}$.
Take $a \in K$ with $\abs{a} \le 1$ and a real number $0 \le r \le 1$.
Expand $f \in A$ as $f = \sum_n c_n (T - a)^n$ and set $\abs{f(\zeta_{a,r})} = \max_n \abs{c_n} r^n$.
This is a point $\zeta_{a,r}$ of $\mathcal{M}(A)$, the point of the disc of centre $a$ and radius $r$.
Clause 3 holds because $\abs{c_n} \le \norm{f}$ when $\abs{a} \le 1$, and clause 2 is a form of Gauss's lemma.
For $a = 0$ and $r = 1$ it is the Gauss norm itself.
For $r = 0$ it is $f \mapsto \abs{f(a)}$, evaluation at $a$, a classical point.

Non-example: the supremum over the two-point set $\set{0, 1}$, namely $f \mapsto \max(\abs{f(0)}, \abs{f(1)})$, satisfies clauses 1 and 3 but not clause 2.
For $f = T$ and $g = T - 1$ both values are $1$, while $fg$ vanishes at both points and has value $0$.

Let $X = \operatorname{Spec} B$ be an affine variety of finite type over $K$.
Its analytification $X^{\mathrm{an}}$ is the set of multiplicative seminorms on $B$ that extend $\abs{\cdot}$ on $K$, with the same kind of topology.

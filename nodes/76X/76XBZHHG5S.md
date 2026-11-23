---
tag: 76XBZHHG5S
kind: example
name: Congruence modulo n is an equivalence relation
msc: ["00A35", "11A07"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [RGNF33GVHX]
uses: [RGNF33GVHX, 0WAY5WX8NY, 0PG2H7WKGG, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Equivalence_relation
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: Congruence
---

## Example

Fix an integer $n \ge 1$.
For integers $a$ and $b$, [[congruence modulo $n$|0WAY5WX8NY]] is the relation
$$a \equiv b \pmod{n} \iff n \mid a - b,$$
where $n \mid m$ means that $m = nk$ for some integer $k$, by the definition of [[divisibility|0PG2H7WKGG]].
We prove that this relation is an [[equivalence relation|0G8VEZ3WTK]] on $\mathbb{Z}$ by the three checks of [[proving a relation is an equivalence relation|RGNF33GVHX]].

1. Reflexivity.
   Let $a \in \mathbb{Z}$.
   Then $a - a = 0 = n \cdot 0$, so $n \mid a - a$ and $a \equiv a \pmod{n}$.
2. Symmetry.
   Let $a \equiv b \pmod{n}$, so $a - b = nk$ for some integer $k$.
   Then $b - a = -(a - b) = n(-k)$ with $-k$ an integer, so $b \equiv a \pmod{n}$.
3. Transitivity.
   Let $a \equiv b$ and $b \equiv c \pmod{n}$, so $a - b = nk$ and $b - c = n\ell$ for some integers $k$ and $\ell$.
4. Add the two equations:
   $$a - c = (a - b) + (b - c) = nk + n\ell = n(k + \ell).$$
5. Since $k + \ell$ is an integer, $n \mid a - c$ and $a \equiv c \pmod{n}$.
   The three properties hold, so congruence modulo $n$ is an equivalence relation.

Check with $n = 7$: $3 \equiv 10$ because $3 - 10 = -7$, and $10 \equiv 24$ because $10 - 24 = -14$.
Step 4 gives $3 - 24 = -7 + (-14) = -21 = 7 \cdot (-3)$, so $3 \equiv 24 \pmod 7$.

## Remarks

Each check uses one property of the set $n\mathbb{Z}$ of multiples of $n$.
It contains $0$, which gives reflexivity; it contains $-m$ whenever it contains $m$, which gives symmetry; and it contains $m + m'$ whenever it contains $m$ and $m'$, which gives transitivity.
So the same proof works for any subgroup $H$ of an abelian group $G$: the relation $a - b \in H$ is an equivalence relation, and its classes are the cosets of $H$.

The function route gives a second proof.
By the [[division algorithm|0CHQKZFK5S]], each integer $a$ has a unique remainder $r(a) \in \{0, 1, \dots, n - 1\}$, and $a \equiv b \pmod n$ holds exactly when $r(a) = r(b)$.
That proof needs this lemma first, so the direct checks are shorter here.
For $n = 1$ all integers are congruent and there is one class, and for $n = 2$ the classes are the even and the odd integers.

## Explanations

### L1 human

Two whole numbers are congruent modulo $7$ when they differ by a multiple of $7$, like $3$ and $10$.
On a clock with $7$ hours, such numbers point to the same hour.
Every number differs from itself by $0$, which is a multiple of $7$.
If $3$ and $10$ differ by a multiple of $7$, so do $10$ and $3$.
If $3$ matches $10$ and $10$ matches $24$, the two differences add, and $3$ and $24$ differ by $21$, again a multiple of $7$.

### L2 human

We use the result to describe the classes modulo $3$.

1. Congruence modulo $3$ is an equivalence relation, so its classes split $\mathbb{Z}$ into disjoint pieces.
2. The class of $0$ is $\{\dots, -3, 0, 3, 6, \dots\}$, the class of $1$ is $\{\dots, -2, 1, 4, 7, \dots\}$, and the class of $2$ is $\{\dots, -1, 2, 5, 8, \dots\}$.
3. Each integer lies in exactly one of these classes, by the division algorithm.
4. The set of the three classes is $\mathbb{Z}/3\mathbb{Z}$, the integers modulo $3$.

This proof is the first step in building modular arithmetic.
Watch out: the proof does not need $n$ to be prime, and it works for every $n \ge 1$.
Only later results, such as division by every non-zero class, need a prime modulus.

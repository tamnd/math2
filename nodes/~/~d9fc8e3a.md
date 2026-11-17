---
tag: ~d9fc8e3a
kind: example
name: Congruence modulo n is an equivalence relation
msc: ["00A35", "11A07"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [~0d0aebf3]
uses: [~0d0aebf3, 0WAY5WX8NY, 0PG2H7WKGG, 0G8VEZ3WTK]
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
We prove that this relation is an [[equivalence relation|0G8VEZ3WTK]] on $\mathbb{Z}$, by the three checks of [[proving a relation is an equivalence relation|~0d0aebf3]].

1. Reflexivity. Let $a \in \mathbb{Z}$. Then $a - a = 0 = n \cdot 0$, so $n \mid a - a$ and $a \equiv a \pmod{n}$.
2. Symmetry. Let $a, b \in \mathbb{Z}$ with $a \equiv b \pmod{n}$. Then $a - b = nk$ for some integer $k$.
3. So $b - a = -(a - b) = n \cdot (-k)$, and $-k$ is an integer. Hence $n \mid b - a$, and $b \equiv a \pmod{n}$.
4. Transitivity. Let $a, b, c \in \mathbb{Z}$ with $a \equiv b \pmod{n}$ and $b \equiv c \pmod{n}$. Then $a - b = nk$ and $b - c = n\ell$ for some integers $k$ and $\ell$.
5. Add the two equations: $a - c = (a - b) + (b - c) = nk + n\ell = n(k + \ell)$, and $k + \ell$ is an integer.
6. So $n \mid a - c$, and $a \equiv c \pmod{n}$.
7. The three properties hold, so congruence modulo $n$ is an equivalence relation on $\mathbb{Z}$.

A check with numbers for $n = 7$: $3 \equiv 10$ because $3 - 10 = -7$, and $10 \equiv 24$ because $10 - 24 = -14$.
Step 5 gives $3 - 24 = -21 = 7 \cdot (-3)$, so $3 \equiv 24 \pmod{7}$.

## Remarks

1. Each check uses one property of the set $n\mathbb{Z}$ of multiples of $n$: it contains $0$ (reflexivity), it contains $-m$ with $m$ (symmetry), and it contains $m + m'$ with $m$ and $m'$ (transitivity).
2. So the same proof works for any subgroup $H$ of an abelian group $G$: the relation $a \sim b \iff a - b \in H$ is an equivalence relation. Its classes are the cosets of $H$.
3. The function route gives a second proof. By the [[division algorithm|0CHQKZFK5S]], each integer $a$ has a unique remainder $r(a) \in \{0, 1, \ldots, n - 1\}$, and $a \equiv b \pmod{n}$ holds if and only if $r(a) = r(b)$.
4. The second proof needs the lemma in Remark 3, so the three direct checks are shorter here.
5. For $n = 1$ every two integers are congruent, so there is one class. For $n = 2$ the two classes are the even and the odd integers.

## Explanations

### L1 human

Two whole numbers are congruent modulo $7$ when they differ by a multiple of $7$, like $3$ and $10$.
On a clock with $7$ hours, such numbers point to the same hour.
Every number differs from itself by $0$, which is a multiple of $7$.
If $3$ and $10$ differ by a multiple of $7$, then so do $10$ and $3$.
If $3$ and $10$ are congruent, and $10$ and $24$ are congruent, then the two differences add up, and $3$ and $24$ differ by $21$, again a multiple of $7$.

### L2 human

We use the result to describe the classes modulo $3$.

1. By the example, congruence modulo $3$ is an equivalence relation, so its classes partition $\mathbb{Z}$.
2. The class of $0$ is $\{\ldots, -3, 0, 3, 6, \ldots\}$, the class of $1$ is $\{\ldots, -2, 1, 4, 7, \ldots\}$, and the class of $2$ is $\{\ldots, -1, 2, 5, 8, \ldots\}$.
3. Each integer lies in exactly one of these classes, by the division algorithm.
4. The set of the three classes is $\mathbb{Z}/3\mathbb{Z}$, the integers modulo $3$.

The typical use of the result is the construction of the integers modulo $n$ and of modular arithmetic.
A trap is to think that the proof needs $n$ to be prime.
It works for each $n \ge 1$.
Only later results, such as division by non-zero classes, need a prime modulus.

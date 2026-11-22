---
tag: Z9Q8PGPQ1Y
kind: example
name: The diagonal set for a map from a three-element set to its power set
msc: ["03E10", "00A35"]
topics: [GB14W4SYPK]
audience: ug1
instance_of: [V2H30SA654]
uses: [V2H30SA654, 00E0YZCERH, 0EPAT51DXQ, 01RVCMSN5N, 0WTEMGYV2C]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor%27s_theorem
    locator: lead section
---

## Example

Let $X = \{1, 2, 3\}$, and let $f \colon X \to \mathcal{P}(X)$ be the [[function|0EPAT51DXQ]] into the [[power set|00E0YZCERH]] with
$$f(1) = \{1, 2\}, \quad f(2) = \emptyset, \quad f(3) = \{1, 3\}.$$
We build the [[diagonal|V2H30SA654]] set $D = \{x \in X : x \notin f(x)\}$ and check that $D$ is not a value of $f$.

1. Test $x = 1$: $1 \in f(1) = \{1, 2\}$, so $1 \notin D$.
2. Test $x = 2$: $2 \notin f(2) = \emptyset$, so $2 \in D$.
3. Test $x = 3$: $3 \in f(3) = \{1, 3\}$, so $3 \notin D$.
4. So $D = \{2\}$.
5. $D \ne f(1)$, because $1 \in f(1)$ and $1 \notin D$.
6. $D \ne f(2)$, because $2 \notin f(2)$ and $2 \in D$.
7. $D \ne f(3)$, because $3 \in f(3)$ and $3 \notin D$.
8. So $D$ is not in the image of $f$, and $f$ is not [[surjective|01RVCMSN5N]].

## Remarks

The diagonal set $D$ disagrees with $f(x)$ at the element $x$ itself, and steps 5 to 7 each use just that one element as the witness.
For a finite set the result also follows by counting: $\mathcal{P}(X)$ has $2^3 = 8$ elements, and the image of $f$ has at most $3$.
The diagonal proof needs no count, so it works for every set, finite or infinite, and gives [[Cantor's theorem|0WTEMGYV2C]].

The set $D$ changes with $f$.
If we change $f(2)$ to $\{2\}$, then $2 \in f(2)$, so $D = \emptyset$, and again $D$ is none of $\{1, 2\}$, $\{2\}$ and $\{1, 3\}$.
If instead $f(3) = \{1, 2\}$, then $3 \notin f(3)$, so $D = \{2, 3\}$, which is also missing from the image.

## Explanations

### L1 human

Three people each make a list of the people in the group whom they like, and a person may list themselves.
Person $1$ lists $1$ and $2$, person $2$ lists nobody, and person $3$ lists $1$ and $3$.
Now form a new list: the people who did not list themselves.
Only person $2$ did not list themselves, so the new list is just person $2$.
This new list differs from each person's list, because it disagrees with person $x$ about person $x$.

### L2 human

We check the construction on a map from $X = \{a, b\}$ to $\mathcal{P}(X)$ with $f(a) = \{b\}$ and $f(b) = \{a, b\}$.
Since $a \notin f(a) = \{b\}$, we get $a \in D$.
Since $b \in f(b) = \{a, b\}$, we get $b \notin D$.
So $D = \{a\}$, which differs from $f(a)$ at the element $a$ and from $f(b)$ at the element $b$.

The typical use is the proof that no set maps onto its power set.
Watch out: compare $D$ with $f(x)$ at the element $x$, since a difference is guaranteed only there.
For instance, $D = \{a\}$ and $f(b) = \{a, b\}$ agree at the element $a$.

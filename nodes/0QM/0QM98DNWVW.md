---
tag: 0QM98DNWVW
kind: statement
role: theorem
name: The Galois group has order at most the degree
msc: [12F10]
uses: [0XVR72M51M, 0NRYPM9Y27]
sources:
  - url: https://en.wikipedia.org/wiki/Galois_group
    locator: Cardinality of the Galois group and the degree of the field extension
  - url: https://en.wikipedia.org/wiki/Galois_extension
    locator: Characterization of Galois extensions
---

## Statement

Let $L/K$ be a [[finite extension|0NRYPM9Y27]].
Then the group $\operatorname{Aut}(L/K)$ of [[automorphisms of $L/K$|0XVR72M51M]] is finite, and
$$|\operatorname{Aut}(L/K)| \le [L : K].$$

## Remarks

For a simple extension $L = K(a)$, an automorphism is determined by $\sigma(a)$, which is a root in $L$ of the minimal polynomial of $a$. There are at most $[L : K]$ such roots.
Equality holds if and only if $L/K$ is a [[Galois extension|0DS2F7GK05]].
For $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$, the inequality is strict: $1 < 3$.

## Explanations

### L1 human

A finite extension has only finitely many symmetries over the base field, and at most as many as its degree.
When there are exactly as many as the degree, the extension is Galois.

---
tag: MJ864PBRRJ
kind: statement
role: theorem
name: Casus irreducibilis
msc: ["12E12", 12F10]
uses: [00X2A9G9W3, V74WMGQQ9D, 07QY5RPFBR]
about: [V74WMGQQ9D]
sources:
  - url: https://en.wikipedia.org/wiki/Casus_irreducibilis
same_as:
  wikidata: Q5050952
  wikipedia: Casus irreducibilis
---

## Statement

Let $K$ be a [[subfield|07QY5RPFBR]] of $\R$, and let $f \in K[x]$ be a cubic polynomial that is [[irreducible|00X2A9G9W3]] over $K$ and has three real roots.
Then no root of $f$ lies in a [[radical extension|V74WMGQQ9D]] $R$ of $K$ with $R \subseteq \R$.

## Remarks

The three roots are distinct, since an irreducible polynomial over a field of characteristic $0$ has no repeated roots.
For the idea of the proof, adjoin first the square root of the discriminant, which is real.
Then over every real field $F$ that contains this square root and over which $f$ is irreducible, adjoining one root of $f$ adjoins all three roots.
Take a real tower of steps adjoining $q$-th roots, $q$ prime, whose last step $E \subseteq E(\alpha)$ with $\alpha^q \in E$ first makes $f$ reducible.
Then $3$ divides $[E(\alpha) : E]$, which is $1$ or $q$, so $q = 3$ and $E(\alpha)/E$ is normal of degree $3$.
Hence $x^3 - \alpha^3$ splits in $E(\alpha)$, so this real field contains a nonreal cube root of unity, which is impossible.
Example: $f = x^3 - 3x + 1$ over $\Q$ is irreducible, since $\pm 1$ are not roots, and its roots $2\cos(2\pi/9)$, $2\cos(4\pi/9)$, $2\cos(8\pi/9)$ are real.
So every expression of these roots by radicals passes through nonreal numbers, as in the [[cubic formula|FB6J5WAT5V]].
Irreducibility is necessary: $x^3 - x = x(x - 1)(x + 1)$ has three real roots, all in $\Q$.

## Explanations

### L1 human

The cubic formula sometimes takes the square root of a negative number even when all three answers are real.
The casus irreducibilis says this detour is unavoidable when the cubic does not factor.
No formula built only from real roots of real numbers can give the roots.

### L2 human

For a real cubic with three distinct real roots, the discriminant is positive, so the square root in the [[cubic formula|FB6J5WAT5V]] is of a negative number.
The theorem shows that the problem is not the formula but the numbers themselves.
The roots can still be written with real numbers using trigonometry, for example as $2\sqrt{-p/3}\cos\theta$ for suitable angles $\theta$ when the cubic is $t^3 + pt + q$.

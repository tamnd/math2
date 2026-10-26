---
tag: 0CHE3J7QMX
kind: counterexample
name: Irreducible elements need not be prime
msc: [13A05]
uses: [052SDEPZH7, 0MNHXBSX3M]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_element
    locator: Example
---

## Counterexample

In the integral domain $\mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$, the element $2$ is [[irreducible|052SDEPZH7]] but not [[prime|0MNHXBSX3M]].
Let $N(a + b\sqrt{-5}) = a^2 + 5b^2$. This norm is multiplicative, and the units are the elements of norm $1$, that is $\pm 1$.
If $2 = x y$ with nonunits $x, y$, then $N(x) N(y) = 4$, so $N(x) = 2$. But $a^2 + 5b^2 = 2$ has no integer solution. So $2$ is irreducible.
The element $2$ divides $(1 + \sqrt{-5})(1 - \sqrt{-5}) = 6$.
It does not divide $1 \pm \sqrt{-5}$, because $(1 \pm \sqrt{-5})/2$ is not in $\mathbb{Z}[\sqrt{-5}]$. So $2$ is not prime.

## Remarks

The same ring shows that factorization is not unique: $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$. See [[$\mathbb{Z}[\sqrt{-5}]$ is not a UFD|0BSJYCG7NM]].
In a [[unique factorization domain|06YMXJMXYS]], every irreducible element is prime.

## Explanations

### L1 human

In the integers, "cannot be factored" and "divides a factor of each product it divides" are the same property.
In $\mathbb{Z}[\sqrt{-5}]$, the number $2$ cannot be factored, but it divides $6 = (1 + \sqrt{-5})(1 - \sqrt{-5})$ and neither factor.
So the two properties are different in general rings.

---
tag: 0DQG39K2NH
kind: statement
role: theorem
name: K[x] is a Euclidean domain
msc: [13F07]
uses: [0GJ2HRG95T, 0MES3KS0ZC, 0DPF6WRZW6, 0B5Z1EC66J]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_domain
    locator: Examples
---

## Statement

Let $K$ be a [[field|0QA8CHH8MG]].
Then the polynomial ring $K[x]$ is a [[Euclidean domain|0GJ2HRG95T]], with the [[degree|0DPF6WRZW6]] as Euclidean function.
That is, for all $f, g \in K[x]$ with $g \neq 0$, there are $q, r \in K[x]$ with $f = q g + r$ and $r = 0$ or $\deg r < \deg g$.

## Remarks

The ring $K[x]$ is an integral domain because $K$ is one. The existence of $q$ and $r$ is the [[division algorithm|0MES3KS0ZC]] over a field.
A consequence is that $K[x]$ is a principal ideal domain and a unique factorization domain.
The ring $\mathbb{Z}[x]$ is not a Euclidean domain, because it is [[not a principal ideal domain|06E3AG9TM2]].

## Explanations

### L1 human

Over a field, you can divide any polynomial by any nonzero polynomial and get a remainder of smaller degree.
This is the same situation as division with remainder for integers.
So all the theory of the Euclidean algorithm works for polynomials over a field.

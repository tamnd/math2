---
tag: 0NN5JEMTVE
kind: example
name: 0.999... equals 1
msc: [11A63]
instance_of: [0VM8B2SB4P]
sources:
  - url: https://en.wikipedia.org/wiki/0.999...
    locator: lead section
  - url: https://en.wikipedia.org/wiki/0.999...
    locator: Infinite series and sequences
same_as:
  wikidata: Q713113
  wikipedia: 0.999...
---

## Example

The [[decimal expansion|06XY4X9430]] $0.999\dots$, with the digit $9$ at every place after the point, represents the real number $1$.
By definition, $0.999\dots = \sum_{k=1}^{\infty} 9 \cdot 10^{-k}$.
This is a geometric series with first term $9/10$ and ratio $1/10$, thus its sum is $\frac{9/10}{1 - 1/10} = 1$.
Thus the number $1$ has two decimal expansions, $1.000\dots$ and $0.999\dots$.

## Remarks

Another proof: the $n$th truncation is $1 - 10^{-n}$. The supremum of these numbers is $1$, by the [[Archimedean property|0A3GWZ86AY]].
The same happens for each number with a finite expansion. For example, $0.25 = 0.24999\dots$.

## Explanations

### L1 human

Many people feel that $0.999\dots$ is a little less than $1$.
But the difference $1 - 0.999\dots$ is smaller than $10^{-n}$ for every $n$.
The only nonnegative real number with this property is $0$.
Another view: $1/3 = 0.333\dots$, and three times this gives $1 = 0.999\dots$.

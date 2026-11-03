---
tag: CD5Y77KGYA
kind: concept
name: Karatsuba algorithm
msc: [68W30, 68W40, 11Y16]
specializes: [G9NFJ55KCX]
sources:
  - url: https://en.wikipedia.org/wiki/Karatsuba_algorithm
same_as:
  wikidata: Q629940
  wikipedia: Karatsuba algorithm
---

## Summary

The Karatsuba algorithm multiplies two $n$-digit integers with $O(n^{\log_2 3})$ digit operations, and $\log_2 3 \approx 1.585$.
It splits each factor into two halves and gets the product from three half-size products instead of the four of the obvious method.
It was the first method to beat the $O(n^2)$ cost of schoolbook multiplication, and it is a standard example of a [[divide-and-conquer algorithm|G9NFJ55KCX]].
The same trick multiplies polynomials.

## Explanations

### L1 human

To multiply $12 \cdot 34$, write them as $1 \cdot 10 + 2$ and $3 \cdot 10 + 4$.
The schoolbook way needs the four products $1 \cdot 3$, $1 \cdot 4$, $2 \cdot 3$ and $2 \cdot 4$.
Karatsuba computes $1 \cdot 3 = 3$, $2 \cdot 4 = 8$ and $(1 + 2)(3 + 4) = 21$, and then the middle part is $21 - 3 - 8 = 10$.
So $12 \cdot 34 = 3 \cdot 100 + 10 \cdot 10 + 8 = 408$, with three multiplications instead of four.
Applied again and again to the halves, the saving grows into a real speed-up for large numbers.

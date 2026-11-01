---
tag: CTXX2CXFRB
kind: definition
name: Natural density
msc: [11B05]
defines: RVG9Z8NYA6
uses: [0MWKJ44V5A, 05M5SWSZZD, 033RZ32T4Q]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_density
---

## Definition

Let $A$ be a set of positive integers.
For each integer $n \ge 1$, let $A(n)$ be the number of elements $a \in A$ with $a \le n$.
If the [[limit|05M5SWSZZD]]
$$d(A) = \lim_{n \to \infty} \frac{A(n)}{n}$$
exists, then $d(A)$ is the *natural density* (or *asymptotic density*) of $A$.
The *upper density* $\overline{d}(A)$ and the *lower density* $\underline{d}(A)$ are the limit superior and the [[limit inferior|033RZ32T4Q]] of $A(n)/n$; they always exist.

## Remarks

The natural density exists if and only if $\overline{d}(A) = \underline{d}(A)$, and then all three numbers are equal.

Example: for the multiples of a positive integer $m$, $A(n) = \floor{n/m}$, and $n/m - 1 < A(n) \le n/m$; so $d(A) = 1/m$.

Non-example: let $A$ be the set of positive integers whose first decimal digit is $1$.
For $n = 2 \cdot 10^k - 1$ one has $A(n) = 1 + 10 + \dots + 10^k = (10^{k+1} - 1)/9$, so $A(n)/n \to 5/9$.
For $n = 10^{k+1} - 1$ the count $A(n)$ is the same, so $A(n)/n \to 1/9$.
Hence the limit does not exist; here $\overline{d}(A) = 5/9$ and $\underline{d}(A) = 1/9$.

If $d(A)$ and $d(B)$ exist and $A \cap B$ is empty, then $d(A \cup B) = d(A) + d(B)$.
Natural density is not the same as [[Schnirelmann density|QHH8RY9XCZ]], which is an infimum over all $n$ and is $0$ for every set not containing $1$.

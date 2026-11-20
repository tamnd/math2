---
tag: WAENF6VDJZ
kind: example
name: A countable nonstandard model of arithmetic is not an ultrapower of the natural numbers
msc: ["03C20", "03C62"]
topics: [HZG1YP26AB]
audience: grad
not_instance_of:
  - target: 5ZVJK0V0GF
    note: "every ultrapower of the standard model over an ultrafilter on the natural numbers is standard or has the size of the continuum"
uses: [5ZVJK0V0GF, E4TD8X2ZRX, 0MWKJ44V5A, 0G0ASKNA6Z, 1QWN5CV4CG]
sources:
  - url: https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic
    locator: lead section
---

## Example

Let $\mathcal{N} = (\N, +, \cdot, 0, 1, <)$, and let $\mathcal{K}$ be a countable [[nonstandard model of arithmetic|1QWN5CV4CG]] with $\mathcal{K} \equiv \mathcal{N}$.
We check that $\mathcal{K}$ is not isomorphic to $\mathcal{N}^{\N} / \mathcal{U}$ for any ultrafilter $\mathcal{U}$ on $\N$.

1. If $\mathcal{U}$ is principal, then $\mathcal{N}^{\N} / \mathcal{U} \cong \mathcal{N}$, which is standard. So $\mathcal{K}$ is not of this form.
2. Let $\mathcal{U}$ be nonprincipal. For an infinite $0$-$1$ sequence $s$, let $f_s(n) = 2^n + \sum_{k < n} s(k) 2^k$, so $f_s(n)$ codes the first $n$ terms of $s$.
3. If $s \neq t$, they differ at some $k$. For every $n > k$, the codes $f_s(n)$ and $f_t(n)$ differ, so $f_s$ and $f_t$ differ on a cofinite set.
4. A nonprincipal $\mathcal{U}$ contains every cofinite set, so $[f_s] \neq [f_t]$.
5. There are $2^{\aleph_0}$ sequences $s$, so the ultrapower has at least $2^{\aleph_0}$ elements; it is uncountable.

## Remarks

The example shows that ultrapowers do not give all elementary extensions: $\mathcal{K}$ is an elementary extension of a copy of $\mathcal{N}$, but not an ultrapower of it.
The [[cardinality|0G0ASKNA6Z]] count of step 5 is exact: $\mathcal{N}^{\N}$ itself has $2^{\aleph_0}$ elements.
Over larger index sets, ultrapowers of $\N$ are not countable and nonstandard either: a countably incomplete ultrafilter gives at least $2^{\aleph_0}$ elements, and a countably complete one gives back $\N$.
Countable nonstandard models come from the compactness theorem together with the downward Löwenheim-Skolem theorem.
By [[Frayne's theorem|QPX9HG9BH4]], $\mathcal{K}$ still embeds elementarily into some ultrapower of $\N$.

## Explanations

### L1 human

An ultrapower of the natural numbers is built from infinite lists of natural numbers.
Different infinite strings of zeros and ones lead to different lists in it, and there are uncountably many such strings.
So a nonprincipal ultrapower of the natural numbers is uncountable.
A countable nonstandard model is too small to be one of them.

### L2 human

We compute the first codes in step 2 for two sequences.

1. For $s = (1, 0, 1, 0, \dots)$: $f_s(0) = 1$, $f_s(1) = 2 + 1 = 3$, $f_s(2) = 4 + 1 = 5$, $f_s(3) = 8 + 1 + 4 = 13$.
2. For $t = (1, 0, 0, 0, \dots)$: $f_t(0) = 1$, $f_t(1) = 3$, $f_t(2) = 5$, $f_t(3) = 9$.
3. The sequences first differ at $k = 2$, and $f_s(n) \neq f_t(n)$ for all $n \ge 3$.
4. The leading term $2^n$ makes $f_s(n)$ determine $n$ and the first $n$ terms of $s$, as the binary digits below the leading digit.

The typical use is to bound the size of ultrapowers from below.
The trap is to expect a countable ultrapower from a countable structure and a countable index set.

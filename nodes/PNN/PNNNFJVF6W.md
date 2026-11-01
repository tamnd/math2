---
tag: PNNNFJVF6W
kind: concept
name: Hardy space
msc: [30H10]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy_space
same_as:
  wikidata: Q1585233
  wikipedia: Hardy space
---

## Summary

Let $0 < p \le \infty$.
The Hardy space $H^p$ of the unit disc is the space of [[holomorphic functions|0NAHXR1FRH]] whose $L^p$ means over the circles $\abs{z} = r$ stay bounded as $r \to 1$.
For $p \ge 1$ it is a [[Banach space|06GZ956657]], and $H^2$ is the Hilbert space of power series $\sum a_n z^n$ with $\sum \abs{a_n}^2 < \infty$.
By [[Fatou's theorem|Q2N917JQ6A]], functions in $H^p$ have boundary values almost everywhere on the circle.
So $H^p$ can be seen as a subspace of $L^p$ of the circle.
Hardy spaces connect complex analysis with Fourier analysis and operator theory, through [[inner functions|NN8XH5RJYB]], [[Blaschke products|9N6R5ADJXT]] and [[Toeplitz operators|GQ0X3R3WM2]].

## Explanations

### L1 human

Take a holomorphic function on the unit disc and look at its size along circles of radius $r$ around $0$.
The function is in a Hardy space if these average sizes stay bounded as the circles approach the rim.
So the function may blow up at some rim points, but not too strongly on average.
For example, $\log(1 - z)$ is unbounded near $z = 1$, yet it lies in $H^2$ because its Taylor coefficients $-1/n$ are square-summable.

---
tag: G9NFJ55KCX
kind: concept
name: Divide-and-conquer algorithm
msc: [68W40, 68W01]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm
same_as:
  wikidata: Q671298
  wikipedia: Divide-and-conquer algorithm
---

## Summary

A divide-and-conquer algorithm splits a problem into smaller subproblems of the same kind, solves them recursively, and combines their solutions.
Its running time satisfies a recurrence, which the [[master theorem|3WNSDAEMQQ]] or the [[Akra–Bazzi method|VZ1J7KM4QS]] often solves.
[[Merge sort|GNGVP9EE8Y]], [[quicksort|Q9B393M2AV]], [[binary search|V67H7YCQ17]], [[Karatsuba multiplication|CD5Y77KGYA]] and the fast Fourier transform are classic examples.

## Explanations

### L1 human

A large job becomes easy if it can be cut into smaller copies of itself.
To find the largest number in a list, find the largest in each half, then keep the larger of the two answers.
Each half is handled the same way, until the pieces have only one element.
The skill lies in cutting so that the pieces are small and putting the answers together is cheap.

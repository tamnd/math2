---
tag: AAYEQE
kind: computation
name: The subgroups of the symmetric group S4
claim: The symmetric group $S_4$ has 30 subgroups. It has 1, 9, 4, 7, 4, 3, 1 and 1 subgroups of the orders 1, 2, 3, 4, 6, 8, 12 and 24, and each of these orders divides 24.
engine:
  image: m2-gap@sha256:1378718f9f1cbc151d7c44f33b246be3069087a55f8bfc44ea4fda4b0350d748
  entry: compute/AAYEQE/main.g
  seed: null
  resources: {cpu: 1, mem: 2G, wall: 10m}
output:
  hash: blake3:1f659e57b810fc209eeca3571bd7939cd6858d6a6eea06e77f448514ae842fd9
  summary: "subgroups of S4: 30. Orders 1, 2, 3, 4, 6, 8, 12 and 24: 1, 9, 4, 7, 4, 3, 1 and 1 subgroups."
certificate:
  kind: witness-table
  artefact: blake3:2357b50189dc3ede995f7fd2f95cece3c9c18015d73b2388e9e69c37eb529b4f
  checker: m2-python@sha256:84f284326896a049f22d31677fe9a7ee8dcc4d37261650c0a4b32e05f5e525f5
  checker_entry: check.py
---

## Description

The program in GAP lists each subgroup of $S_4$, the [[group|G5S1M9]] of the permutations of $\{1, 2, 3, 4\}$. It writes each subgroup with the sorted list of its elements to the certificate, and it prints the number of subgroups of each order.

The checker is a short Python program that does not use GAP. It finds the subgroups of $S_4$ again with its own search. It starts with the trivial subgroup and adds the subgroup that a known subgroup and one more element generate, until it finds no new subgroup. It accepts the certificate only when the lines of the certificate are these subgroups, each one time, and the order of each one divides 24.

## Remarks

The orders divide 24, as [[Lagrange's theorem|3C53TD]] says. The converse of the theorem is not true for each finite group, but it is true for $S_4$: for each divisor $d$ of 24, $S_4$ has a subgroup of order $d$. The alternating group $A_4$ of order 12 has no subgroup of order 6, so the converse is false for $A_4$.

---
tag: ~ff3aaab8
kind: statement
role: theorem
name: De Morgan's laws for sets
msc: ["03E20"]
uses: [~ef45614e, ~bf3fa33b, ~71f1e924, ~53574b2c]
sources:
  - url: https://en.wikipedia.org/wiki/De_Morgan's_laws
    locator: lead section
same_as:
  wikidata: Q173300
  wikipedia: De Morgan's laws
---

## Statement

Let $U$ be a set and let $A$ and $B$ be [[subsets|~a9b9ba7e]] of $U$. Write $X^c = U \setminus X$ for the [[complement|~ef45614e]] of a subset $X$ in $U$.
Then
$$(A \cup B)^{c} = A^{c} \cap B^{c},$$
$$(A \cap B)^{c} = A^{c} \cup B^{c}.$$

## Remarks

The laws come from [[De Morgan's laws|~53574b2c]] of logic, applied to $x \in A$ and $x \in B$.
They hold also for arbitrary families: the complement of $\bigcup_i A_i$ is $\bigcap_i A_i^c$, and the complement of $\bigcap_i A_i$ is $\bigcup_i A_i^c$.
With set differences, $C \setminus (A \cup B) = (C \setminus A) \cap (C \setminus B)$ for each set $C$.

## Explanations

### L1 human

An element is outside $A \cup B$ exactly when it is outside $A$ and outside $B$.
An element is outside $A \cap B$ exactly when it is outside $A$ or outside $B$.
A [[Venn diagram|~164195f9]] with two circles shows both laws.

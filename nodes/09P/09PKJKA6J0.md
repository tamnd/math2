---
tag: 09PKJKA6J0
kind: statement
role: theorem
name: De Morgan's laws
aliases: [de-morgan-laws]
msc: [03B05]
uses: [0XR7A7RSXB, 0M28ASWG8T, 0H5GKDTB01, 06GYGS41JK]
sources:
  - url: https://en.wikipedia.org/wiki/De_Morgan's_laws
    locator: lead section
same_as:
  wikidata: Q173300
  wikipedia: De Morgan's laws
---

## Statement

For all [[propositions|0ZGC7ZESYN]] $p$ and $q$, these two [[logical equivalences|06GYGS41JK]] hold.
$$\neg (p \lor q) \equiv \neg p \land \neg q$$
$$\neg (p \land q) \equiv \neg p \lor \neg q$$

## Remarks

The first law is also valid in intuitionistic logic. In the second law, only the direction from $\neg p \lor \neg q$ to $\neg (p \land q)$ is.
The laws for sets have the same form. See [[De Morgan's laws for sets|0VK0W4D5Y5]].
The [[negation of a universal statement|0P3A06QNDP]] is the analogue for quantifiers.

## Explanations

### L1 human

To negate "and", change it to "or" and negate each part.
"$n$ is not both even and prime" means "$n$ is not even, or $n$ is not prime".
A [[truth table|05RSK4Q657]] with four rows proves each law.

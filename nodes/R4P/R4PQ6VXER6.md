---
tag: R4PQ6VXER6
kind: concept
name: Intersection type
aliases: [comparison-of-languages-with-intersection-types, comparison-of-programming-languages-intersection-types]
sources:
  - wikipedia: en:24140211@r1374885617
    locator: Intersection type
    note: adopted
    mention: wikipedia://en/24140211
    sections: [Summary]
same_as:
  wikidata: Q85769734
  wikipedia: Intersection type
inventory: [3DJY288JJQ]
---

## Summary

In type theory, an **intersection type** can be allocated to values that can be assigned both the type $\sigma$ and the type $\tau$. This value can be given the intersection type $\sigma \cap \tau$ in an intersection type system. Generally, if the ranges of values of two types overlap, then a value belonging to the *intersection* of the two ranges can be assigned the *intersection type* of these two types. Such a value can be safely passed as argument to functions expecting *either* of the two types. For example, in Java the class Boolean implements both the Serializable and the Comparable interfaces. Therefore, an object of type Boolean can be safely passed to functions expecting an argument of type Serializable and to functions expecting an argument of type Comparable.

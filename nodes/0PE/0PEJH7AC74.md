---
tag: 0PEJH7AC74
kind: definition
name: Transitive closure
msc: ["03E20"]
defines: 05J9NWX07X
uses: [08EJC6Q25H, 0CYRECG2YQ]
sources:
  - url: https://en.wikipedia.org/wiki/Transitive_closure
    locator: lead section
inventory: [ESPGMH4G0W]
---

## Definition

Let $R$ be a [[binary relation|08EJC6Q25H]] on a set $A$.
The transitive closure of $R$ is the relation $R^{+}$ on $A$ such that $a \mathrel{R^{+}} b$ when there are $n \ge 1$ and $x_0, \dots, x_n \in A$ with
$$a = x_0 \mathrel{R} x_1 \mathrel{R} x_2 \cdots x_{n-1} \mathrel{R} x_n = b.$$

## Remarks

The relation $R^{+}$ is [[transitive|0CYRECG2YQ]], it contains $R$, and it is a subset of each transitive relation that contains $R$.
It is also the intersection of all transitive relations on $A$ that contain $R$.
Example: the transitive closure of "is a parent of" is "is an ancestor of".

## Explanations

### L1 human

The transitive closure adds all the shortcuts.
In a graph, $a \mathrel{R^{+}} b$ means that there is a path of one or more arrows from $a$ to $b$.

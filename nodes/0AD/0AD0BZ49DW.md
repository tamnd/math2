---
tag: 0AD0BZ49DW
kind: statement
role: proposition
name: Metrizable spaces are normal
msc: ["54E35"]
uses: [0AJ646N339, 09KDHB82SG, 07TXYYVYZR, 0P9DCDES73]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_space
    locator: Examples of normal spaces
---

## Statement

Let $X$ be a [[metrizable space|09KDHB82SG]].
Then $X$ is [[normal|0AJ646N339]].

## Remarks

Proof: choose a metric $d$ for the topology. For disjoint closed sets $A$ and $B$, let $U = \{x : d(x, A) < d(x, B)\}$ and $V = \{x : d(x, B) < d(x, A)\}$. Here $d(x, A)$ is the [[distance to a set|07TXYYVYZR]].
The sets $U$ and $V$ are open, because $x \mapsto d(x, A)$ is continuous. They are disjoint, and $A \subseteq U$ because $d(x, A) = 0 < d(x, B)$ for $x \in A$.
Single points are closed in a metric space. Thus each metrizable space is normal and T1, and also [[Hausdorff|0P9DCDES73]].

## Explanations

### L1 human

In a metric space, you separate two disjoint closed sets by the points that are nearer to one set than to the other.

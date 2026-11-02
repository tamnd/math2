---
tag: 6CXPGB13WD
kind: concept
name: Mapping cone
msc: [18G35, 18G80]
sources:
  - url: https://en.wikipedia.org/wiki/Mapping_cone_(homological_algebra)
same_as:
  wikidata: Q6754178
  wikipedia: Mapping cone (homological algebra)
---

## Summary

The mapping cone of a [[chain map|HTK9WQZJ1G]] $f \colon C_\bullet \to D_\bullet$ is a [[chain complex|WQ82C0M3QB]] $\mathrm{cone}(f)$.
It is built from $D$ and a shifted copy of $C$, with a differential that uses $f$.
It measures the failure of $f$ to be a [[quasi-isomorphism|C9JEC2WQKV]]: $f$ is one exactly when the cone has zero homology.
The cone fits into a short exact sequence of complexes, and in the [[homotopy category|9Y5Y92R4D5]] and the [[derived category|5ST7NVJFSM]] it gives the [[distinguished triangles|ADKK56VZHW]].

## Explanations

### L1 human

The cone glues the source of $f$, moved up one degree, onto the target of $f$.
In topology, the mapping cone of a map of spaces $X \to Y$ is formed by attaching the cone on $X$ to $Y$, and its chains are this algebraic cone.
The homology of the cone sits in a long exact sequence between the homologies of $C$ and $D$, with the maps $H_n(f)$ as connecting maps.
So the cone is acyclic exactly when $f$ induces isomorphisms on homology.
For example, the cone of multiplication by $2$ on $\Z$ in degree $0$ is $0 \to \Z \xrightarrow{2} \Z \to 0$, whose homology $\Z/2\Z$ is the cokernel of $f$.

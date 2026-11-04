---
tag: G1ME5XRPHP
kind: proof
name: Proof that characteristic subgroups are normal
msc: [20F28]
proves: 0SRE7K4E49
uses: [01CS8Q2APC, 0H47DMFN3S, 0HV9Y7WG5R, 01VG2A0BHW, 0D9NDGE9KP, 0CWXCWP0Y0, 0W77CVBCHQ]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_subgroup
    locator: Normal subgroup
---

## Proof

We show that each inner automorphism is an automorphism, and then apply the definition of a characteristic subgroup.

1. Let $G$ be a group with identity $e$, and let $H$ be a [[characteristic subgroup|01CS8Q2APC]] of $G$.
2. For $g \in G$, let $c_g \colon G \to G$, $c_g(x) = gxg^{-1}$, be the [[inner automorphism|0H47DMFN3S]] given by $g$.
3. For $x, y \in G$, $c_g(x) c_g(y) = gxg^{-1}gyg^{-1} = gxyg^{-1} = c_g(xy)$. So $c_g$ is a [[group homomorphism|0HV9Y7WG5R]].
4. For $g, h \in G$, $(gh)(h^{-1}g^{-1}) = e$, so $(gh)^{-1} = h^{-1}g^{-1}$ by the [[uniqueness of inverses|0D9NDGE9KP]]. Hence $c_g(c_h(x)) = (gh)x(gh)^{-1} = c_{gh}(x)$.
5. By step 4, $c_g \circ c_{g^{-1}} = c_{g^{-1}} \circ c_g = c_e$, which is the identity map of $G$. So $c_g$ is [[bijective|01VG2A0BHW]].
6. By steps 3 and 5, $c_g$ is an [[automorphism|0CWXCWP0Y0]] of $G$.
7. Since $H$ is characteristic, $c_g(H) = H$. Let $h \in H$. Then $ghg^{-1} = c_g(h) \in c_g(H) = H$.
8. Step 7 holds for all $g \in G$ and all $h \in H$. So $H$ is a [[normal subgroup|0W77CVBCHQ]] of $G$.

## Idea

Normality asks a subgroup to be fixed by the conjugations, and the characteristic property asks it to be fixed by all automorphisms. The conjugations are automorphisms, so the second condition includes the first.

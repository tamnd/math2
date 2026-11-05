---
tag: GQR6RCE82C
kind: proof
name: Proof of Beilinson's theorem
proves: CQ6AGQWB0Z
sources:
  - wikipedia: en:63070573@r1369241780
    locator: Derived noncommutative algebraic geometry, section Orlov's reconstruction theorem > Sketch of proof
    note: adopted
    mention: wikipedia://en/63070573#L1BC
    sections: [Proof]
---

## Proof

The proof starts out by analyzing two induced Serre functors on $D^b(Y)$ and finding an isomorphism between them. It particular, it shows there is an object $\omega_Y = F(\omega_X)$ which acts like the dualizing sheaf on $Y$. The isomorphism between these two functors gives an isomorphism of the set of underlying points of the derived categories. Then, what needs to be check is an ismorphism $F(\omega_X^{\otimes k}) \cong \omega_Y^{\otimes k}$, for any $k \in \mathbb{N}$, giving an isomorphism of canonical rings

$$A(X) = \bigoplus_{k=0}^\infty H^0(X,\omega_X^{\otimes k}) \cong \bigoplus_{k=0}^\infty H^0(Y,\omega_Y^{\otimes k})$$

If $\omega_Y$ can be shown to be (anti-)ample, then the proj of these rings will give an isomorphism $X \to Y$. All of the details are contained in Dolgachev's notes.

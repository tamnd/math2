---
tag: Y5KAWMJBZH
kind: statement
role: theorem
name: Ribet's theorem for Frey curves
msc: [11D41]
sources:
  - wikipedia: en:19021953@r1375981458
    locator: Fermat's Last Theorem, section Mathematical history > Connection with elliptic curves > Ribet's theorem for Frey curves
    note: adopted
    mention: wikipedia://en/19021953#L0GM
    sections: [Statement]
inventory: [TFSJHGXPS0]
---

## Statement

In 1984, Gerhard Frey noted a link between Fermat's equation and the modularity theorem, then still a conjecture. If Fermat's equation had any solution $(a, b, c)$ for exponent $p > 2$, then it could be shown that the semi-stable elliptic curve (now known as a Frey-Hellegouarch)

$$y^2 = x(x - a^p)(x + b^p)$$

would have such unusual properties that it was unlikely to be modular. This would conflict with the modularity theorem, which asserted that all elliptic curves are modular. As such, Frey observed that a proof of the Taniyama–Shimura–Weil conjecture might also simultaneously prove Fermat's Last Theorem. By contraposition, a *disproof* or refutation of Fermat's Last Theorem would disprove the Taniyama–Shimura–Weil conjecture.

In plain English, Frey had shown that, if this intuition about his equation was correct, then any set of four numbers $(a, b, c, n)$ capable of disproving Fermat's Last Theorem, could also be used to disprove the Taniyama–Shimura–Weil conjecture. Therefore, if the latter were true, the former could not be disproven, and would also have to be true.

Following this strategy, a proof of Fermat's Last Theorem required two steps. First, it was necessary to prove the modularity theorem, or at least to prove it for the types of elliptical curves that included Frey's equation (known as semistable elliptic curves). This was widely believed inaccessible to proof by contemporary mathematicians. Second, it was necessary to show that Frey's intuition was correct: that if an elliptic curve were constructed in this way, using a set of numbers that were a solution of Fermat's equation, the resulting elliptic curve could not be modular. Frey showed that this was *plausible* but did not go as far as giving a full proof. The missing piece (the so-called "epsilon conjecture", now known as Ribet's theorem) was identified by Jean-Pierre Serre who also gave an almost-complete proof and the link suggested by Frey was finally proved in 1986 by Ken Ribet.

Following Frey, Serre and Ribet's work, this was where matters stood:

- The modularity theorem—if proved for semi-stable elliptic curves—would mean that all semistable elliptic curves *must* be modular;
- Ribet's theorem showed that any solution to Fermat's equation for a prime number could be used to create a semistable elliptic curve that *could not* be modular;
- So either no such curve could be created because no solutions existed to Fermat's equation; or the modularity theorem was false.

This meant that a proof of the modularity theorem would automatically prove Fermat's Last Theorem as well.

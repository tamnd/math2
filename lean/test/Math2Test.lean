import Math2
import Math2Test.Cert

/-!
# Golden tests of the m2 attribute

`lake test` builds this file. Each `#guard_msgs` block fails the build when the messages change.
-/

open Math2.Meta

/-- info: true -/
#guard_msgs in
#eval isTag "7K3QX2"

/-- info: true -/
#guard_msgs in
#eval isTag ("~" ++ "3fa94c01")

/-- info: true -/
#guard_msgs in
#eval isTag "7K3QX2ABCE"

/-- info: false -/
#guard_msgs in
#eval isTag "7K3QX2ABCF"

/-- info: false -/
#guard_msgs in
#eval isTag "7K3QX2ABC"

/-- info: false -/
#guard_msgs in
#eval isTag "7K3QXI"

/-- info: false -/
#guard_msgs in
#eval isTag ("~" ++ "3FA94C01")

/-- error: "7K3" is not a tag or a provisional id. -/
#guard_msgs in
@[m2 "7K3"] theorem bad_tag : True := trivial

/-- error: The check character of 7K3QX2ABCF is not correct. Look for a typing error in the tag. -/
#guard_msgs in
@[m2 "7K3QX2ABCF"] theorem bad_check : True := trivial

/-- error: Math2.Match.lagrange is already bound to 3C53TD. -/
#guard_msgs in
attribute [m2 "7K3QX2"] Math2.Match.lagrange

/--
info: [(`Math2.Match.lagrange, "3C53TD"), (`Math2.Match.inv_unique, "0D9NDGE9KP"), (`Math2.Match.cyclic_comm, "04RG02S6BA"),
  (`Math2.Match.orderOf_dvd, "08V7JHS3QZ"), (`Math2.Match.prime_card, "05MM4EK4SA"),
  (`Math2.Match.ker_normal, "0C9ZKYSPYR"), (`Math2.Match.injective_iff_ker, "0N2P0XRTDF"),
  (`Math2.Match.first_iso, "0CXXJNG5B6")]
-/
#guard_msgs in
#eval return (bindings (← Lean.getEnv)).toList.map fun (b : Binding) => (b.decl, b.tag)

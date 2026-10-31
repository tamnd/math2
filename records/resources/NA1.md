---
records:
    - id: NA12MZWC2P
      kind: problem-set
      title: Putnam 1990
      date: "1990"
      expressions:
        - key: e1
          kind: edition
          date: "1990"
          structure: NA12MZWC2P/e1.json
      relations:
        - kind: part_of
          to: TYDZDDC2MA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: putnam
          snapshot: blake3:317d171d8e409d9741a4f33624a74aedbca628bebf057e16b0f4fee2668a9f1f
          native_id: "1990"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---

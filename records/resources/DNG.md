---
records:
    - id: DNG3PTXXM5
      kind: monograph
      title: From Divergent Power Series to Analytic Functions
      creators:
        - name: Werner Balser
          role: author
      date: "1994"
      expressions:
        - key: e1
          kind: edition
          date: "1994"
          ids:
            doi: 10.1007/bfb0073564
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1994"
              ids:
                isbn:
                    - "9783540582687"
                    - "9783540485940"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0073564
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: DNGQ82PS4S
      kind: course
      title: Integral and Vector Calculus
      creators:
        - name: Hari Shankar Mahato
          role: instructor
      ids:
        course: 03w5sq511:111105122
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Kharagpur
              ids:
                nptel: "111105122"
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111105122"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
---

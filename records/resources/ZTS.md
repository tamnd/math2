---
records:
    - id: ZTSZ894TQB
      kind: course
      title: Numerical methods
      creators:
        - name: Ameeya Kumar Nayak
          role: instructor
        - name: Sanjeev Kumar
          role: instructor
      ids:
        course:
            - 00582g326:111107105
            - 00582g326:111107107
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Roorkee
              ids:
                nptel: "111107105"
            - key: m2
              kind: page
              publisher: IIT Roorkee
              ids:
                nptel: "111107107"
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111107105"
          level: manifestation
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111107107"
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
